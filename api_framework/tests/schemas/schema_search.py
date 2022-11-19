from pydantic import BaseModel, Field
from typing import List, Optional


class Address(BaseModel):
    building: Optional[str]
    highway: Optional[str]
    house_number: Optional[str]
    road: Optional[str]
    hamlet: Optional[str]
    town: Optional[str]
    village: Optional[str]
    city_district: Optional[str]
    city: Optional[str]
    ISO31662lvl15: Optional[str] = Field(alias='ISO3166-2-lvl15')
    ISO31662lvl4: Optional[str] = Field(alias='ISO3166-2-lvl4')
    state: Optional[str]
    region: Optional[str]
    postcode: Optional[str]
    country: Optional[str]
    country_code: Optional[str]


class Schema(BaseModel):
    place_id: int
    licence: str
    osm_type: Optional[str]
    osm_id: Optional[str]
    boundingbox: list
    lat: float
    lon: float
    display_name: str
    class_str: str = Field(alias="class")
    type_str: str = Field(alias="type")
    importance: Optional[int]
    icon: Optional[str]
    address: Address


class ResponseSchemaSearch(BaseModel):
    response_model: List[Schema]
