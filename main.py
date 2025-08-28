
from turtle import title
from fastapi import FastAPI


app = FastAPI(title="Blog API", description="A simple blog API using FastAPI", version="1.0.0")

@app.get("/blog")
async def read_blog(limit:int, published:bool):
    return {"message":f"List of blogs with limit of {limit} and it's published status is: {published}"}
