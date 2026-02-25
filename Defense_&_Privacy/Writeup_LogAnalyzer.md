# 🛡️ Case Study: SSH Log Analyzer (Otimização com Generators)

**Autor:** Jhader Augusto (Jhader-DevSec)
**Tecnologia:** Python 3
**Foco:** Blue Team / Análise de Logs / Estruturas de Dados Avançadas

## 📌 Sobre o Projeto
Este é um script de estudo focado em defesa cibernética (Blue Team). O objetivo é simular a análise de logs de autenticação de um servidor Linux (`auth.log` fictício) para identificar tentativas de ataque de Força Bruta (Brute-Force) via SSH. 

O script varre o documento linha por linha e extrai apenas as ocorrências de `Failed password`, otimizando o uso de memória do sistema.

## 🧠 Lições Aprendidas e Destaques Técnicos

Durante o desenvolvimento deste analisador, consolidei conhecimentos críticos sobre performance e manipulação de arquivos no sistema operacional:

* **O Poder do `yield` (Generators):** Aprendi que para utilizar o `yield`, ele deve ser incluído dentro da função, retornando o valor diretamente na linha analisada. Diferente do `return` (que encerra a função e joga tudo na memória), o `yield` pausa a execução. Para utilizá-lo na prática, é obrigatório criar um loop (como o `for`) fora da função para consumir os dados sob demanda. Isso é vital para ler logs gigantescos de servidores sem travar a máquina.
* **Tratamento de Caminhos com Raw Strings (`r""`):** Enfrentei e resolvi o problema de leitura de caminhos de diretório no Windows. Aprendi que devo sempre colocar um `r` antes das aspas da string do caminho (ex: `r"C:\Users\..."`). Isso transforma o texto em uma *Raw String*, impedindo que o Python confunda as barras invertidas (`\`) com caracteres de escape.
* **Execução Avançada no Terminal:** Aprimorei minha habilidade de interagir com o terminal, entendendo a forma correta de rodar scripts Python via linha de comando e garantindo que o interpretador esteja rodando no diretório exato do arquivo.
* **Refatoração de Nomenclatura:** Ajuste do vocabulário técnico do código para o padrão global (ex: substituição de `archive` por `file` ou `log_file`, visto que *archive* em TI se refere a arquivos compactados).

## 💻 Como Funciona
O script abre o arquivo de log em modo leitura (`"r"`) e utiliza a estrutura otimizada do gerador para filtrar as ameaças:

```python
def log_analyzer(file_path):
    with open(file_path, "r") as log_file:
        for line in log_file:
            if "Failed password" in line:
                yield line

# Utilizando caminho relativo para o ambiente de testes
for l in log_analyzer("log_reader.txt"):
    print(l)
    print("-" * 50)
