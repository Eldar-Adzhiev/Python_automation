from framework_examples.api.framework.logger import Logger

import requests
from requests import Response


class ShellRequestAPI:
    @staticmethod
    def make_a_custom_request(method: str, url: str, **kwargs) -> Response:
        """
        Request method
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        Logger.info(f"Request {method} on {url} (with {kwargs})")
        return requests.request(method, url, **kwargs)
