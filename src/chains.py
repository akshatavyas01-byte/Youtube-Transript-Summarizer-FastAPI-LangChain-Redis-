from langchain_groq import ChatGroq
from pydantic import SecretStr
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 
import os 
load_dotenv()

api=os.getenv("GROQ_API_KEY")
llm=ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=SecretStr(api) if api else None
)

class chunk_summaries(BaseModel):
    '''Response Pattern for the Chunks'''
    summary_timestamp:str=Field(description="Timestamp of the summary")
    summarized_content:str=Field(description="Detailed Summary of the content")

class fullsummary(BaseModel):
    '''Response Pattern for the whole Youtube Video'''
    video_title:str=Field(description="Title of the video")
    overall_duration:str=Field(description="Durtion of the video")
    one_sentence_summary:str=Field(description="Summarize the video in one sentence")
    overall_summary:str=Field(description="Comprehensive Summary of the video")
    highlight:str=Field(description="Highlight of the video")
    key_takeaway:str|list[str]=Field(description="Key takeways from the video")
    
    
chunk_summary_response=PydanticOutputParser(pydantic_object=chunk_summaries)

full_summary_response=PydanticOutputParser(pydantic_object=fullsummary)

chunk_summary_prompt_template='''
Your a smart summarizer:
Summarize the following Youtube Video content:
{content}

Generate the summary in the following Json format:
{format_instructions}
'''

full_summary_prompt_template='''
Your a smart summarizer:
Summarize the following Youtube Video content:
{content}


Generate the summary in the following Json format:
{format_instructions}
'''

chunk_summary_prompt=PromptTemplate(
    template=chunk_summary_prompt_template,input_variables=["content"],
    partial_variables={"format_instructions":chunk_summary_response.get_format_instructions()}
)

full_summary_prompt=PromptTemplate(
    template=full_summary_prompt_template,input_variables=["content"],
    partial_variables={"format_instructions":full_summary_response.get_format_instructions()}
)

chunk_summary_chain=(
    chunk_summary_prompt
    |llm
    |chunk_summary_response
)

full_summary_chain=(
    full_summary_prompt
    |llm
    |full_summary_response
)


