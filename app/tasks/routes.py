# Basic
import logging


# Libraries
from mongoengine import *
from fastapi import APIRouter, HTTPException, status, Depends
from workers.main_worker import create_task

router: APIRouter = APIRouter(
    tags=["Tasks"],
    prefix="/task"
)


@router.post("/")
def run_task(data: dict):
    time = int(data["time"])
    x = data["x"]
    y = data["y"]
    task = create_task.delay(time, x, y)
    # return {"Result": task.get()}
    return {"Result": "Task successfully"}
