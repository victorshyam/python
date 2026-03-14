from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()


@app.post("/test")
async def chat(request: ChatRequest):
    return {
        "success": True,
        "data": request.user_prompt
    }
