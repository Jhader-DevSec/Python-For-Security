# 💀 Python for Security & Ethical Hacking

Coleção de scripts, ferramentas e estudos focados em Cibersegurança, Defesa de Infraestrutura (Blue Team) e Automação Ofensiva (Red Team).

![Security](https://img.shields.io/badge/Security-Ethical%20Hacking-red?style=for-the-badge&logo=kali-linux&logoColor=white) ![Python](https://img.shields.io/badge/Python-Scripting-blue?style=for-the-badge&logo=python&logoColor=yellow)

## ⚠️ Legal Disclaimer
**Atenção:** Todo o código e informação neste repositório tem propósito **estritamente educacional**. As ferramentas são desenvolvidas para estudos de infraestrutura, redes e testes em ambientes controlados. O autor não se responsabiliza pelo uso indevido.

## 🛡️ Blue Team (Defense & Privacy)
Ferramentas focadas em proteção de aplicações, análise de logs e gestão de credenciais.

| Projeto | Descrição | Status | Link |
| :--- | :--- | :--- | :--- |
| **Mini WAF Simulator** | Middleware com decorators para interceptar e bloquear SQLi e XSS. | ✅ Concluído | [Ver Código](./Defense_&_Privacy/waf_simulator.py) |
| **SSH Log Analyzer** | Analisador de força bruta em logs de servidor usando generators. | ✅ Concluído | [Ver Código](./Defense_&_Privacy/log_reader.py) |
| **Password Generator** | Gerador de senhas seguras com alta entropia. | ✅ Concluído | [Ver Pasta](./Defense_&_Privacy) |

## ⚔️ Red Team & Recon
Scripts para mapeamento de rede e automação ofensiva.

| Projeto | Descrição | Status | Link |
| :--- | :--- | :--- | :--- |
| **Port Scanner** | Scanner de portas TCP/UDP utilizando a biblioteca socket. | 🛠️ Em Desenv. | [Ver Pasta](./Red_Team_Tools) |

## 📝 Writeups & Case Studies
Relatórios técnicos documentando aprendizados e resoluções de problemas aplicados à cibersegurança.

| Título | Descrição | Status | Link |
| :--- | :--- | :--- | :--- |
| **SSH Log Analyzer** | Estudo sobre otimização de memória com `yield` e raw strings. | ✅ Concluído | [Ler Writeup](./Defense_&_Privacy/Writeup_LogAnalyzer.md) |

## 🧪 Laboratório e Tecnologias Ativas
Conceitos e bibliotecas que estou aplicando nos códigos atuais:
* `Decorators (@)` (Implementação de Middlewares de segurança)
* `Generators (yield)` (Otimização de consumo de memória em logs pesados)
* `Tratamento de Exceções` (Criação de scripts resilientes a falhas)
* `socket` (Interação com redes e portas - *Em andamento*)

---
Developed by **Jhader-DevSec**
