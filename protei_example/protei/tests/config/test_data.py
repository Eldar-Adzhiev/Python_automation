class DataSearch:
    DATA = [
        "London",
        "pub in Liverpool",
        "лиговский проспект 44"
    ]
    PARAMETERS = {
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }


class DataReverse:
    DATA = [
        {"lat": "52.5487429714954", "lon": "-1.81602098644987"},
        {"lat": "-34.44076", "lon": "-58.70521"},
        {"lat": "44.50155", "lon": "11.33989"}
    ]
    PARAMETERS = {
        "format": "json",
        "addressdetails": 1
    }
