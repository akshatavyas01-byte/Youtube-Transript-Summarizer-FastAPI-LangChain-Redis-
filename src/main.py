from fastapi import FastAPI, Query,UploadFile, File
import asyncio
import redis
from src.functions import chunked_content, chunks_summaries, full_summary, normalise_text, text_chunks, chunks_group
from typing import Optional
from langchain_community.document_loaders import YoutubeLoader, TextLoader
from langchain_community.document_loaders.youtube import TranscriptFormat
import tempfile
import json

r=redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

app=FastAPI()


pattern=r"(?:https?:\/\/)?(?:www\.|m\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?(?:\S+=\S+&)*v=))([\w-]{11})"
@app.post("/youtube/")
async def trascriptgetter(
    url:Optional[str]=Query(default=None,title="URL",description="Youtube Url", pattern=pattern),
    file:Optional[UploadFile]=File(None)
):  
    if url:
        youtube_url=str(url)
        if r.get(youtube_url):
            response=r.get(youtube_url)
            return {"response":response}
        else:
            loader=YoutubeLoader.from_youtube_url(
            youtube_url,
            add_video_info=False,
            transcript_format=TranscriptFormat.CHUNKS,
            chunk_size_seconds=180)
            try:
                doc= await  asyncio.wait_for(asyncio.to_thread(loader.load), timeout=15)
                chunk_size=len(doc)
                content=chunked_content(doc,chunk_size)
                summaries=chunks_summaries(content)
                response=full_summary(summaries)
                r.setex(youtube_url,120,json.dumps(response.__dict__))
                return {"response":response}
            except  asyncio.TimeoutError:
                print("Time out Error")
                return {"error":"YouTube Error Loding"}
    elif file:
        if file.content_type=="text/plain":
            name=file.filename
            if name:
                if r.get(name):
                    response=r.get(name)
                    return{"response":response}
                else:
                    with tempfile.NamedTemporaryFile(delete=False,suffix=".txt") as temp:
                        content= await file.read()
                        temp.write(content)
                        temp_path=temp.name
                    try:
                        loader=TextLoader(temp_path)
                        doc= await asyncio.wait_for(asyncio.to_thread(loader.load), timeout=30)
                        text=normalise_text(doc)
                        textchunks=text_chunks(text)
                        chunk_size=len(textchunks)
                        grouped_chunks=chunks_group(textchunks,chunk_size)
                        summaries=chunks_summaries(grouped_chunks)
                        response=full_summary(summaries)
                        r.setex(name,120,json.dumps(response.__dict__))
                        return {"response":response}
                    except asyncio.TimeoutError:
                        return {"error":"Txt doc not loaded"}
            else:
                return {"file_content":"ERRROR FOR FILE CONTENT"}
    else:
         return {"error":"No file or url found!!"}
