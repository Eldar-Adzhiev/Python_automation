from api_framework.framework.logger import Logger
from pydantic import ValidationError


class Validations:

    @staticmethod
    def validate_response(schema, response):
        try:
            res = schema(response_model=response)
            Logger.info(f"{res}")
        except ValidationError as e:
            Logger.warning(f"{e}")
            return False
        return True
