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
    osm_type: str
    osm_id: Optional[str]
    boundingbox: List[float]
    lat: float
    lon: float
    display_name: str
    address: Address
