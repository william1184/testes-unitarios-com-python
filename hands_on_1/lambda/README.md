# testes-unitarios-com-python em AWS LAMBDA
Exemplos utilizados no hands on de testes unitários com python

Apresentação visa mostrar a forma como é feito os testes unitários
no lambda_function para lambdas.

Utiliza-se pytest e unittest


Testar comportamento é por exemplo:
Meu lambda busca um cliente, e caso o mesmo exista eu devo enviar um email, 
caso não exista eu devo retornar a execeção ClienteNaoEncontradoException.


Fluxo Comportamental
    Recebo um evento
        valido documento
        valido email
        Busco Cliente
        Valido Existencia Cliente
            ->  Envio Email
                Retorno 200
            ->  Retorno Excecao
        

No cenário de sucesso:
    Invoca:
    -> validação documento
    -> validação email
    -> busca cliente
    -> envio email
    -> retorno 200

* Acima temos o comportamento esperado do lambda em caso de sucesso, e podemos assegurar com o uso de assert_called_once.
        