# 🤖 Bot da FURIA no Telegram

Um bot interativo feito com Python que conecta os fãs à paixão pelo CS:GO e pela organização brasileira **FURIA Esports**. Com ele, os usuários podem acessar rapidamente informações sobre jogadores, próximos jogos, histórico de partidas, estatísticas, e até links oficiais da organização. Tudo isso direto pelo Telegram!

---

## 🚀 Funcionalidades

- ✅ **Mensagens interativas com botões** (InlineKeyboard)
- 📅 **Informações atualizadas** sobre os próximos jogos
- 📜 **Histórico de partidas recentes**
- 🎯 **Estatísticas e records** da equipe e dos jogadores
- 👥 **Biografias resumidas dos jogadores** da line atual
- 🌐 **Links para redes sociais oficiais** da FURIA
- 🧠 **Respostas automáticas a mensagens de texto** com base em palavras-chave

---

## 👥 Jogadores Suportados

- **FalleN** – O Professor, lenda brasileira do CS
- **KSCERATO** – Frieza e clutches de outro mundo
- **yuurih** – Precisão e consistência
- **chelo** – Energia e agressividade
- **arT** – O IGL agressivo e criativo

---

## 📲 Como Usar

1. Acesse o bot no Telegram (após configurá-lo).
2. Envie o comando `/start` para iniciar a interação.
3. Use o botão **"Menu de Opções"** para navegar pelas informações disponíveis.
4. Ou envie mensagens como:
   - `"Fala do FalleN"`
   - `"Quais são os próximos jogos?"`
   - `"Me mostra o histórico da FURIA"`
   - `"Quais são os stats?"`

---

## 📷 Imagem de Boas-Vindas

O bot envia uma imagem com o logo da FURIA para dar boas-vindas, junto com instruções claras de como interagir.

---

## 🧑‍💻 Tecnologias Usadas

- **Python 3.9+**
- **python-telegram-bot v20+**
- Markdown para formatação de mensagens
- Integração com o Telegram Bot API

---

## 🛠️ Como Executar Localmente

Siga os passos abaixo para rodar o bot na sua máquina:

### 1. Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- **Python 3.9 ou superior**. Você pode verificar a versão do Python instalada com o comando:

  ```bash
  python --version
  ```

- **pip**: O gerenciador de pacotes do Python (normalmente vem junto com o Python).

### 2. Instale as dependências

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate       # No Windows: venv\Scriptsctivate
```

Instale a biblioteca necessária:

```bash
pip install python-telegram-bot==20.3
```

### 3. Configure seu bot no Telegram

1. Acesse o [@BotFather](https://t.me/BotFather) no Telegram.
2. Use o comando `/newbot` para criar um novo bot.
3. Escolha um nome e um @username.
4. Copie o token gerado para o seu bot (algo como `123456789:ABCDefghIjkLmnoPQRstuVWxyz`).

### 4. Atualize o código com seu token

No arquivo do bot (por exemplo, `furia_bot.py`), substitua a linha abaixo com o token do seu bot:

```python
app = ApplicationBuilder().token('SEU_TOKEN_AQUI').build()
```

Substitua `'SEU_TOKEN_AQUI'` pelo token real gerado pelo **BotFather**.

### 5. Execute o bot

No terminal, execute o script Python:

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python furia_bot.py
```

### 6. Teste no Telegram

- Abra o **Telegram** e busque pelo **@username** do seu bot.
- Envie o comando `/start` para testar o bot.

Agora o bot estará ativo e pronto para interagir com os fãs da FURIA!

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

---

## 📬 Contato

Quer contribuir, sugerir melhorias ou reportar bugs?  
Fale comigo via email: [Gugab1249@gmail.com]!
