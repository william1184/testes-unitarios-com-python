from unittest import TestCase

import requests.exceptions
import requests_mock

from src.service.isbn_service import IsbnService


# Temos de nos atentar que os cenários são criados com base nos cenários reais demonstrados na api real
# https://brasilapi.com.br/docs#tag/ISBN/paths/~1isbn~1v1~1%7Bisbn%7D/get
class TestISBNService(TestCase):
    __service = None

    def setUp(self):
        self.__service = IsbnService()

    # Teste do cenario positivo, caso sucesso, entao retorna payload
    # Esse cenário nao foi mockado
    def test__caso__codigo_existe_e_retorna_200__entao__retorna_payload(self):
        ## arrange
        isbn = "978-8532530783"

        ## act
        response = self.__service.consultar(isbn=isbn)

        ## assert
        self.assertEqual("Harry Potter e a Pedra Filosofal", response['title'])

    # Teste do cenario positivo, caso sucesso, entao retorna payload
    # Esse cenário foi mockado, e o response é mockado
    @requests_mock.Mocker()
    def test__caso__codigo_existe_e_retorna_200__entao__retorna_payload(self, http_mock: requests_mock.Mocker):
        ## arrange
        isbn = "978-8532530783"

        http_mock.get(
            "https://brasilapi.com.br/api/isbn/v1/978-8532530783",
            json={"title": "Harry Chapa e a Pedra Filosofal"},
            status_code=200
        )

        ## act
        response = self.__service.consultar(isbn=isbn)

        ## assert
        self.assertEqual("Harry Chapa e a Pedra Filosofal", response['title'])

    # Teste do cenario negativo 1, caso erro 400, entao retorna excecao
    @requests_mock.Mocker()
    def test__caso__codigo_falhe_e_retorna_400__entao__retorna_excecao(self, http_mock: requests_mock.Mocker):
        ## arrange
        isbn = "978-8532530783"

        http_mock.get(
            "https://brasilapi.com.br/api/isbn/v1/978-8532530783",
            json={},
            status_code=400
        )

        ## act
        with self.assertRaises(requests.exceptions.HTTPError) as ctx:
            ## o response nao é mais importante
            ## pois temos raises do status_code de erro retornado
            self.__service.consultar(isbn=isbn)

        ## assert
        ## Utiliza-se In para validar parte relevante do erro
        self.assertIn("400 Client Error: None for url:", ctx.exception.args[0])

    # Teste do cenario negativo 2, caso erro 404, entao retorna excecao,
    # esse cenário pode ser interpretado como caminho possivel e ser um erro esperado
    @requests_mock.Mocker()
    def test__caso__codigo_falhe_e_retorna_404__entao__retorna_excecao(self, http_mock: requests_mock.Mocker):
        ## arrange
        isbn = "978-8532530783"

        http_mock.get(
            "https://brasilapi.com.br/api/isbn/v1/978-8532530783",
            json={},
            status_code=404
        )

        ## act
        with self.assertRaises(requests.exceptions.HTTPError) as ctx:
            ## o response nao é mais importante
            ## pois temos raises do status_code de erro retornado
            self.__service.consultar(isbn=isbn)

        ## assert
        ## Utiliza-se In para validar parte relevante do erro
        self.assertIn("404 Client Error: None for url:", ctx.exception.args[0])

    # Teste do cenario negativo 3, caso erro 500, entao retorna excecao
    @requests_mock.Mocker()
    def test__caso__codigo_falhe_e_retorna_500__entao__retorna_excecao(self, http_mock: requests_mock.Mocker):
        ## arrange
        isbn = "978-8532530783"

        http_mock.get(
            "https://brasilapi.com.br/api/isbn/v1/978-8532530783",
            json={},
            status_code=500
        )

        ## act
        with self.assertRaises(requests.exceptions.HTTPError) as ctx:
            ## o response nao é mais importante
            ## pois temos raises do status_code de erro retornado
            self.__service.consultar(isbn=isbn)

        ## assert
        ## Utiliza-se In para validar parte relevante do erro
        self.assertIn("500 Server Error: None for url:", ctx.exception.args[0])
