# Python Decoder

Este é um servidor web que fornece uma API para fazer o upload do arquivo de um arquivo tipo .txt e processar os dados nele contidos. O objetivo é validar o formato do arquivo e determinar o código secreto mais curto possível de comprimento desconhecido, com base em uma amostra dos dados. A arquitetura escolhida foi a MVC (Model-View-Controller).

## Enviando um Arquivo Keylog

Para fazer o upload de um arquivo keylog.txt para o servidor, utilize o comando `curl` da seguinte maneira:

```
curl --location --request POST 'http://ec2-18-117-168-254.us-east-2.compute.amazonaws.com:8000' --form 'file=@"/caminho/do/arquivo/nome_do_arquivo.txt"'
```

Certifique-se de substituir `/caminho/do/arquivo/nome_do_arquivo.txt` pelo caminho absoluto do arquivo keylog.txt que deseja enviar. Você poderá usar o arquivo ```./exemplo.txt``` como modelo.

## Processamento dos Dados

Quando um arquivo tipo .txt é enviado para o servidor, a API irá validar o formato do arquivo na função ```validate_file_extension``` que está no seguinte arquivo ```./decode/utils.py ``` e coletar uma amostra dos dados para verificar a conformidade com o formato de 3 caracteres nas funções ``` transform_file_to_array count_digits_frequency``` que estão no seguinte arquivo ```./decode/controllers.py```. Em seguida, o servidor irá determinar o código secreto mais curto possível de comprimento desconhecido com base nos dados amostrados na função ```rank_digits_by_score``` que está no seguinte arquivo ```./decode/controllers.py```.

O código secreto será exibido na saída do servidor.
