from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "hello from docker"}