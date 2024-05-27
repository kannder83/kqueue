# Basic
import logging


# Libraries
from mongoengine import *
from fastapi import APIRouter, HTTPException, status, Depends
from app.client.models import Client, CreateClient
from app.client.controller import db_client

router: APIRouter = APIRouter(
    tags=["Client"],
    prefix="/client"
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Get clients"
)
async def get_clients():
    """
    """
    logging.debug("All is working!")

    all_data: list = []
    for client in Client.objects():
        all_data.append(client.to_dict())

    return {
        "msg": "All is working!",
        "all_data": all_data
    }


@router.post(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Create client"
)
async def post_client(data: CreateClient):
    """
    """
    new_client = db_client.create_page(data.model_dump())
    if not isinstance(new_client, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No se pudo crear")
    return {
        "new_client": new_client
    }
