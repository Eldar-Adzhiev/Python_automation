from pydantic import BaseModel, Field
from typing import Optional


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