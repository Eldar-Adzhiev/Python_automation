from pydantic import BaseModel
from typing import List, Optional
from api_framework.tests.schemas.schema_address import Address


class Schema(BaseModel):
    place_id: int
    licence: str
    osm_type: str
    osm_id: Optional[str]
    boundingbox: List[float]
    lat: float
    lon: float
    display_name: str
    address: Address


class ResponseSchemaReverse(BaseModel):
    response_model: List[Schema]
