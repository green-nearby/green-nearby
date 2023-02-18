import fastapi
from pydantic import BaseModel
from src.green_nearby.greenspace import get_lat_long, get_nearby_greenspace

router = fastapi.APIRouter()


class Address(BaseModel):
    name: str


@router.post("/")
def find_greenspace(address: Address):
    print(address.name)
    latitude, longitude, full_address = get_lat_long(address.name)
    print(f"lat: {latitude}, long: {longitude}, full address {full_address}")
    greenspaces = get_nearby_greenspace(latitude, longitude)
    return greenspaces
