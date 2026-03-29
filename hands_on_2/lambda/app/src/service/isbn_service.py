import logging

import requests
from typing_extensions import Dict


class IsbnService:
    __http_session = None

    def __init__(self):
        self.__http_session = requests.Session()

    def consultar(self, isbn: str) -> Dict:
        try:
            url = "https://brasilapi.com.br/api/isbn/v1/{isbn}".replace("{isbn}", isbn)

            ## retornos possiveis na documentação 200, 400, 404, 500
            response = self.__http_session.get(
                url=url
            )

            if response.ok:
                return response.json()

            response.raise_for_status()

        finally:
            logging.info("ISBN_SERVICE__FIM")


__all__ = ['IsbnService']

