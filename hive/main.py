from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_version():
    return {"version": "v0.0.2"}
