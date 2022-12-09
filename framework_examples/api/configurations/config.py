class Config:
    BASE_URL = "https://nominatim.openstreetmap.org/"


class SearchParams:
    PARAMETERS = {
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }


class ReverseParams:
    PARAMETERS = {
        "format": "json",
        "addressdetails": 1
    }