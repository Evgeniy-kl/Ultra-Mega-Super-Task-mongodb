import json

from bson import json_util
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from database import (
    fetch_all_statistic,
    fetch_one_statistic,
    create_statistic,
    update_statistic,
    delete_statistic
)
from schema import Statistic

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get('/stats/', response_model=List[Statistic])
async def get_all():
    response = await fetch_all_statistic()
    return response


@app.get('/stats/{email}', response_model=List[Statistic])
async def get_one(email):
    response = await fetch_one_statistic(email)
    return JSONResponse(content=response, status_code=200)


def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.post('/stats/')
async def create_one(stat: Statistic):
    response = await create_statistic(parse_json(stat.dict()))
    return response
