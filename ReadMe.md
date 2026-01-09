# Youtube Transript Summarizer (FastAPI + LangChain + Redis)

Developed a FastAPI-based YouTube transcript summarization service using LangChain and LLMs, with Redis caching, schema-validated outputs via Pydantic, and optimized response performance.

---

## FESTURES
### 1. App Features:
    - Accepts a YouTube video URL or raw text transcript via a POST API endpoint  
    - Automatically extracts and processes the YouTube transcript  
    - Generates a structured summary of the video content  
    - Returns concise insights including highlights and key takeaways  

### 2. LangChain Concepts:
    - Document loaders
    - Transcript Formatting and chunking
    - Prompt Engineering
    - Output Parsers (Pydantic-based)

### 3. LangChain + GROQ
    -ChatGroq LLM integration

### 4. Asyncio
    - `asyncio.to_thread` to run YouTube transcript loading in a separate thread and keep the event loop responsive  
    - `asyncio.wait_for`to set a timeout for requests and avoid long-running operations.

### 5. Redis 
    - Response caching using `SETEX` with TTL(Time To Live)

### 6. FAST API
    - POST endpoints
    - `UploadFile` handling
    - Optional (typping)
    - Path and Query parameters
    - Auto-generated API documentation (Swagger UI)

### 7. Backend utilites
    - `tempfile` for temporary text storage
    - Pydantic Models for data validation and strutured responses

### 8. Testing
    - POSTMAN
    - Swagger UI

---
## TECHNOLOGIES USED

    Python 3.x
    FastAPI
    Uvicorn  
    Langchain
    Langchain_core
    Langchain-community
    Langchain-Groq
    Typing Extensions
    Redis
    Docker

## FOLDER STRUCTURE

     project/
            |── src/
            |   |── main.py
            |   |── chains.py
            |   |── functions.py
            |
            |── images/
            |
            |── Testing/
            |   |── SetConceptandConventionsSets#1Class11MathsCh.txt
            |   |── url.txt
            |
            |── .env
            |
            |── requirements.txt
            |
            └── ReadMe.md

    
## Installation & Setup for the project

```python
git clone Youtube-Transript-Summarizer-FastAPI-LangChain-Redis-
cd Youtube-Transript-Summarizer

pip install -r requirements.txt

uvicorn src.main:app --reload

```

## Environment Setup
```python

python -m venv venv

venv/Scripts/Activate.ps1

```
## Install Dependencies
```python

pip install -r requirements.txt

```
---
## Environment Variables (.env Setup)
This project requires an API key to access GROQ LLMs.

### 1. Create a .env file in the project root
```python
GROQ_API_KEY=your_api_key_here
```

### 2. Ensure the key loads in your code

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
```
### 3. Install dotenv if not installed
```python
pip install python-dotenv

```
## Redis Setup (Docker)

Start Redis:
```bash
docker compose up -d
```
Verify Redis is running:
```bash
docker ps
```
Test Redis connection:
```bash
docker exec redis redis-cli ping
```
Expected output:
```bash
PONG
```
---
## API Endpoints

| Method | Endpoint | Parameters| Description |
|---|---|---|---|
|POST| `/youtube/`| `Optional`: **Body (form-data):** `file` (TXT) / **Query:** `url`| Upload a transcript text file or the url of the youtube video to get summary of the video.|

---

## Request and Example
### Upload TXT
 - POST(`"/youtube/"`)
    - Body (form-data):
        - `file:` TXT file

### Response
```json
{
  "response": {
    "video_title": "Concept of Sets in Mathematics",
    "overall_duration": "Not specified",
    "one_sentence_summary": "The video explains the concept of sets in mathematics, including examples, notation, and operations on sets.",
    "overall_summary": "A set is a well-defined collection of objects, which can be represented using curly brackets and can have a fixed or infinite number of elements. Examples of sets include players of the Indian cricket team, rivers of India, students of a school, and members of a family. The video also covers concepts such as equality between sets, subsets, proper subsets, supersets, single-turn sets, power sets, and universal sets. Operations on sets, including union, intersection, difference, and complement of a set are also discussed.",
    "highlight": "The video provides examples of sets and explains how to determine whether a particular element belongs to a set.",
    "key_takeaway": [
      "A set is a well-defined collection of objects",
      "Examples of sets include players of the Indian cricket team, rivers of India, students of a school, and members of a family",
      "Operations on sets include union, intersection, difference, and complement of a set"
    ]
  }
}
```      

---
# Demo Images
### 1. Uvicorn:
![alt text](/images/image.png)

### 2. FAST API(SWAGGER DOCS):
![alt text](/images/image1.png)
![alt text](/images/image2.png)

### 3. Swagger UI POST Tryout:
#### URL
![alt text](/images/image3.png)
![alt text](/images/image4.png)
#### TXT File
![alt text](/images/image5.png)
![alt text](/images/image6.png)

### 5. Postman POST request:
#### URL Cache testing
![alt text](/images/image7.png)

#### TXT Cache testing 
![alt text](/images/image8.png)
       
---

## Possible Improvements
- Add persistent caching to reduce repeated LLM calls

- Optimize chunking, token usage, and API efficiency

- Evaluate alternative LLMs for higher accuracy
---
## License
This project is licensed under the MIT License.

---
## Author
**Akshata Vyas**  
GitHub: [akshatavyas01-byte](https://github.com/akshatavyas01-byte)
