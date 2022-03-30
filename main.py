from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Password(BaseModel):
    password: str
    key: str

app = FastAPI()

origins = [
    "http://search-smartly-6d47ginnn-zyrogatsby.vercel.app",
    "https://search-smartly-6d47ginnn-zyrogatsby.vercel.app",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello from SearchSmartly"}

@app.post("/encode")
async def encode_password(password: Password):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = password.password.upper()
    permutedKey = password.key.upper()
    result = ""

    for i in text:
        if i in alphabet:
            result += permutedKey[alphabet.find(i)]
        else:
            result += i

    return result