#  Validador de Registros por CPF

Este projeto é uma ferramenta de auditoria de dados projetada para verificar a integridade de registros em arquivos Excel, focando especificamente na contagem de entradas por CPF. Ele é ideal para garantir que cada cliente (ou CPF) tenha o número exato de registros esperados (neste caso, 12), ajudando a identificar rapidamente dados faltantes ou incompletos.

## Funcionalidades

  * **Processamento Flexível**: Pode analisar um único arquivo ou todos os arquivos Excel (`.xlsx`, `.xls`) dentro de uma pasta.
  * **Extração Inteligente de CPF**: Extrai o CPF da primeira coluna, mesmo que os dados estejam combinados com outros valores e separados por `|` (pipe).
  * **Limpeza de Dados**: Ignora CPFs de CNPJ padrão (`00.000.000/0001-00`) que não representam pessoas físicas.
  * **Auditoria de Contagem**: Conta o número de registros para cada CPF e compara com o valor de referência (12).
  * **Relatório de Anomalias**: Lista todos os CPFs que não possuem a quantidade esperada de registros, facilitando a identificação de problemas.

-----

##  Tecnologias Utilizadas

  * **Python**: A base de todo o projeto.
  * **Pandas**: Biblioteca essencial para a leitura e manipulação eficiente dos dados.
  * **openpyxl**: Necessária para que o Pandas possa ler arquivos `.xlsx`.

-----

##  Como Usar

### Pré-requisitos

Certifique-se de que o **Python** e as bibliotecas necessárias estão instaladas. Você pode instalá-las com o seguinte comando:

```sh
pip install pandas openpyxl
```

### Configuração

1.  **Ajuste o caminho**: No código, edite a variável `caminho` na função `main()`.

<!-- end list -->

```python
def main():
    caminho = r"caminho/para/sua/pasta_ou_arquivo"
```

  * Se você apontar para uma **pasta**, o script processará todos os arquivos `.xlsx` e `.xls` que encontrar lá.
  * Se você apontar para um **arquivo específico**, apenas ele será processado.

### Execução

Basta rodar o script diretamente no terminal:

```sh
python nome_do_seu_script.py
```

O script exibirá o status de processamento de cada arquivo e, ao final, listará os CPFs com problemas ou confirmará que todos os registros estão completos.

-----

## ✍️ Licença

Este projeto está sob a licença **MIT**.
