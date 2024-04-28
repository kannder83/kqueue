# Basic
import logging


# Libraries
from mongoengine import *
from fastapi import APIRouter, HTTPException, status, Depends
from app.client.models import Page, CreatePage
from app.client.controller import db_page

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
    for page in Page.objects():
        all_data.append(page.to_dict())

    return {
        "msg": "All is working!",
        "all_data": all_data
    }


@router.post(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Create client"
)
async def get_home(data: CreatePage):
    """
    """
    new_page = db_page.create_page(data.model_dump())
    if not isinstance(new_page, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No se pudo crear")
    return {
        "new_page": new_page
    }
