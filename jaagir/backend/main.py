from fastapi import FastAPI

app = FastAPI(title="Jaagir api", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
async def about():
    return {"message": "Hello about page"}
