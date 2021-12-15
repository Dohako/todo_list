from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:8080",
    "localhost:8080"
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


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to todo list"}

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}

@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data" : { "Todo added." }
    }

@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id:int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }
    return {
        "data": f"Todo with id {id} not found."
    }

@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed"
            }
    return {
        "data": f"Todo with id {id} not found"
    }
