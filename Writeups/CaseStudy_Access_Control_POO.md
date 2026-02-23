# 🛡️ Case Study: Implementação de Segurança em Sistema Bancário Fictício

**Autor:** Jhader Augusto (Jhader-DevSec)
**Tecnologia:** Python 3 (POO)
**Tipo de Projeto:** Simulação Educacional / Desenvolvimento Seguro

## 1. Introdução e Contexto

Este projeto consiste no desenvolvimento de um **simulador bancário fictício**, criado integralmente por mim como parte dos meus estudos avançados em Python e Lógica de Programação.

O objetivo inicial era praticar **Programação Orientada a Objetos (POO)**. No entanto, identifiquei a necessidade de aplicar conceitos de **Cibersegurança (DevSec)** para mitigar vulnerabilidades lógicas, como transferências não autorizadas e manipulação indevida de saldo.

## 2. O Desafio (Cenário de Ameaça)

Em um sistema bancário sem camadas de segurança, qualquer instância de objeto poderia acessar métodos críticos (como `.sacar()` ou `.transferir()`) sem validação. Isso simula um cenário de **Quebra de Controle de Acesso (Broken Access Control)**, onde um usuário mal-intencionado poderia movimentar fundos de terceiros apenas conhecendo a referência do objeto.

## 3. Soluções de Segurança Implementadas

Para proteger o sistema fictício, implementei as seguintes camadas de defesa diretamente no código:

### A. Autenticação e Controle de Acesso

Integrei o meu script de **Gerador de Senhas** (`password_generator.py`) ao sistema bancário.

* **Implementação:** Cada objeto `ContaCorrente` agora possui um atributo privado de senha.
* **Gatekeeper:** Criei o método `check_password()`, que atua como um *gatekeeper*. Nenhuma operação sensível (Saque, Extrato, Transferência) é executada sem que este método retorne `True`.

```python
def check_password(self):
    """Validação de segurança antes de executar métodos críticos."""
    attempt = input(f"Digite a senha para a conta de {self.name}: ")
    if attempt == self.password:
        return True
    return False

```

### B. Integridade e Rastreabilidade (Logging)

Para garantir o princípio da **Integridade** (da tríade CIA), implementei um sistema de logs imutável via código.

* **Histórico:** Cada transação bem-sucedida é gravada em uma lista `self.historical`.
* **Auditoria:** O usuário pode consultar o extrato para verificar a origem e destino de cada movimentação, garantindo transparência.

### C. Validação de Entrada (Input Validation)

Para prevenir erros lógicos e exceções que poderiam derrubar o sistema (DoS - Denial of Service), utilizei tratamento de erros (`try/except`) e condicionais robustas.

* O sistema verifica se o saldo é suficiente (`if amount <= self.balance`) antes de alterar qualquer estado do objeto.
* Entradas de texto em campos numéricos são tratadas para não interromper a execução.

## 4. Conclusão Técnica

O desenvolvimento deste simulador demonstrou na prática como a segurança deve ser pensada desde a fase de design do software (**Security by Design**).

A utilização de Classes e Métodos (POO) facilitou o **Encapsulamento** dos dados, garantindo que o saldo de um cliente não seja acessado diretamente por outro sem passar pelos métodos de validação de senha.
