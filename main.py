from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://encryptwave.vercel.app",
    "https://encryptwave.vercel.app",
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
# Models
class Password(BaseModel):
    password: str
    key: str

class Message(BaseModel):
    text: str
    shift: int

# Helper Function
def caesar_shift(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + key) % 26)

# Routes
@app.get("/")
async def read_root():
    return {"Hello from Encryptwave"}

@app.post("/substitution/encode")
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

@app.post("/caesar/encode")
async def encode_shift(message: Message):
    text = message.text.upper()
    shift = message.shift
    punctuation = " .,!"
    result = ""

    for i in text:
        if i not in punctuation:
            result += caesar_shift(i, shift)
        else:
            result += i
    
    return result
