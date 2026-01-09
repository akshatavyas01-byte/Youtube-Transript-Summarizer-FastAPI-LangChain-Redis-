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
            |
            |── .env
            |
            |── requirements.txt
            |
            └── ReadMe.md

    
## Installation & Setup for the project

```python
git clone Youtube Transript Summarizer (FastAPI + LangChain + Redis)
cd project-name

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
|---|---|---|---|

---

## Request and Example
### Upload TXT
 - POST(`"/youtube/"`)
    - Body (form-data):
        - `file:` TXT file

### Response
```json

```      

---
# Demo Images
### 1. Uvicorn:
![alt text](/images/image.png)

### 2. FAST API(SWAGGER DOCS):
![alt text](/images/image1.png)
![alt text](/images/image2.png)
![alt text](/images/image3.png)

### 3. Swagger UI POST Tryout:
![alt text](/images/image4.png)
![alt text](/images/image5.png)

### 4. Swagger UI GET Tryout:
![alt text](/images/image6.png)
![alt text](/images/image7.png)

### 5. Postman POST request:
![alt text](/images/image8.png)

### 6. Postman GET request:
![alt text](/images/image9.png)
       
---

## Possible Improvements
- Add persistent chache memory 
- Improve chunking, tokens and API calls
- Different LLM.
---
## License
This project is licensed under the MIT License.

---
## Author
**Akshata Vyas**  
GitHub: [akshatavyas01-byte](https://github.com/akshatavyas01-byte)
