from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

todos = [
    {
        "id":"1",
        "item":"Make site with python"
    },
    {
        "id":"2",
        "item":"make sites with go"
    },
    {
        "id":"3",
        "item":"learn devops"
    }
]

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to todo list"}