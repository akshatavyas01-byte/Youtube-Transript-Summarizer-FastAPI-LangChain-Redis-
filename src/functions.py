from src.chains import chunk_summaries,chunk_summary_chain, full_summary_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
import time, re


def normalise_text(doc:list)->str:
    text=("\n\n").join(d.page_content for d in doc)
    text=re.sub("\r\n","\n",text)
    text=re.sub("\n{3,}","\n\n",text)
    text=text.strip()
    return text

def text_chunks(text:str)->list:
    splitter=RecursiveCharacterTextSplitter(
    separators=[r"\[\d{2}\:\d{2}:\d{2}\]","\n\n","\n"],
    chunk_size=800,
    chunk_overlap=300
    )
    textchunks=splitter.split_text(text)
    return textchunks

def chunks_group(chunks:list,chunk_size:int)->list:
    content=[]
    content_text=''
    for i in range(0, chunk_size,4):
        for chunk in chunks[i:i+4]:
            content_text+=chunk
        content.append(content_text)
    return content


def chunked_content(doc:list, chunk_size:int)-> list:
    content=[]
    chunk_text=''
    print("here")
    for i in range(0, chunk_size, 4):
        for d in doc[i:i+4]:
            chunk_text+=(
            d.metadata["start_timestamp"]
            +
            "\n"
            +
            d.page_content
            +
            "\n\n"
            )
    content.append(chunk_text)
    print("done")
    return content

def chunks_summaries(contents:list)->list:
    summaries=[]
    for content in contents:
        time.sleep(5)
        response=chunk_summary_chain.invoke({'content':content})
        summaries.append(response)
    return summaries

def full_summary(summaries:list[chunk_summaries])->dict:
    content=("\n\n").join(
      f"{chunk.summary_timestamp}\n{chunk.summarized_content}"
        for chunk in summaries  
    )
    time.sleep(5)
    response=full_summary_chain.invoke({'content':content})
    return response