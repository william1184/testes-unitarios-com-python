class ClienteNaoExisteException(BaseException):

    def __init__(self, documento: str) -> None:
        super().__init__(f'Cliente nao existe: {documento}')
