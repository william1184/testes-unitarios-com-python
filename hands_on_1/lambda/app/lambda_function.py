from aws_lambda_powertools.utilities.typing import LambdaContext

from src.exception.ClienteNaoExisteException import ClienteNaoExisteException
from src.service.cliente_service import ClienteService
from src.service.email_service import EmailService

cliente_service = ClienteService()
email_service = EmailService()


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    # SE EU COMENTAR ESTA LINHA ? DURANTE O TESTE 2 DO EXEMPLO 2?
    if 'documento' not in event or \
            event['documento'] is None or \
            len(event['documento']) == 0:
        documento = 'nao-preenchido'
        if 'documento' in event:
            documento = event['documento']

        raise ValueError(f"Documento Invalido: {documento}")

    if 'email' not in event or \
            event['email'] is None or \
            len(event['email']) == 0:
        email = 'nao-preenchido'

        if 'email' in event:
            email = event['email']

        raise ValueError(f"Email Invalido: {email}")

    documento_cliente = event['documento']
    email_cliente = event['email']

    # SE EU TROCAR A CHAMADA POR UM VALOR FIXO AINDA VAI PASSAR?
    dados_cliente = cliente_service.consultar(documento=documento_cliente)

    if dados_cliente is None:
        raise ClienteNaoExisteException(documento=documento_cliente)

    # SE EU COMENTAR ESTA LINHA, O TESTE AINDA VAI PASSAR?
    email_service.enviar(email=email_cliente)

    return {
        'statusCode': 200
    }
