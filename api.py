from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from src.greenspace import get_lat_long, get_nearby_greenspace
import logging

app = FastAPI()
logger = logging.getLogger("api")
logger.setLevel(logging.INFO)


class Address(BaseModel):
    name: str


@app.post("/greenspace")
def find_greenspace(address: Address):
    address = address.name
    print(address)
    latitude, longitude, full_address = get_lat_long(address)
    print(f"lat: {latitude}, long: {longitude}, full address {full_address}")
    greenspaces = get_nearby_greenspace(latitude, longitude)
    return greenspaces

