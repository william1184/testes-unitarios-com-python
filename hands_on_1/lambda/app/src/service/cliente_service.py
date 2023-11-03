from typing_extensions import Dict


class ClienteService:

    # SE DESCOMENTAR OS TESTES NO EXEMPLO 1 NEM INICIARAO POR QUE ESTAO SENDO INSTANCIADOS
    # ANTES DE SER MOCKADO PELO MOCK.PATH
    # def __init__(self) -> None:
    #     raise NotImplementedError('ClienteService nao deveria estar sendo instanciado')

    def consultar(self, documento: str) -> Dict:
        pass
