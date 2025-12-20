from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "fastapi",
        "hostname": socket.gethostname()
    }
