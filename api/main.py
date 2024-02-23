from fastapi import FastAPI
from qrcode_generator import generate_qrcode

app = FastAPI()

@app.post("api/generate")
async def generate_qrcode_api(url: str):
    qrcode_url = generate_qrcode(url)
    return {"qrcode": qrcode_url}