class ResponseModel:
    def __init__(self, status: int, response: dict = None, url: str = None):
        self.status = status
        self.response = response
        self.url = url
