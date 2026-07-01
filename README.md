# Grammeon

Grammeon is a Telegram-based English learning assistant designed to help learners improve their grammar, vocabulary, and confidence through interactive conversations.

The bot can analyze English sentences, suggest corrections, explain common grammar issues, provide word definitions, offer synonyms and antonyms, and even guide users through level-based grammar tests from A1 to C1.

## ✨ Features

- Grammar correction for English sentences
- Clear explanations for detected errors
- Automatic suggestions for common grammar mistakes
- Word definition lookup via an online dictionary API
- Synonyms and antonyms lookup
- Learning resources including books, websites, and videos
- Interactive level tests for A1, A2, B1, B2, and C1
- Friendly Telegram interface with buttons and commands

## 🧠 What the project does

Grammeon combines a lightweight grammar engine with a Telegram bot interface. Users can simply send a sentence to receive feedback such as:

- corrected version of the sentence
- list of grammar issues
- score out of 10
- helpful explanations and suggestions

It is especially useful for learners who want quick feedback while practicing English in a conversational environment.

## 🏗️ Project structure

- [bot.py](bot.py) — entry point for the Telegram bot
- [handlers.py](handlers.py) — command handling, buttons, message routing, and interactive flows
- [corrector.py](corrector.py) — grammar checking and scoring logic
- [grammar_rules.py](grammar_rules.py) — rule-based grammar correction patterns
- [formatter.py](formatter.py) — formatting correction results for Telegram messages
- [dictionary.py](dictionary.py) — dictionary lookup using an external API
- [synonyms_antonyms.py](synonyms_antonyms.py) — synonyms and antonyms lookup
- [resources.py](resources.py) — curated grammar learning resources
- [tests.py](tests.py) — grammar test questions and result evaluation

## 🚀 Installation

### Prerequisites

- Python 3.9+
- A Telegram bot token from BotFather

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Marsh-Edge/Grammeon.git
   cd Grammeon
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:
   ```bash
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install python-telegram-bot python-dotenv httpx
   ```

4. Create a `.env` file in the project root and add your Telegram token:
   ```env
   TELEGRAM_TOKEN=your_bot_token_here
   ```

## ▶️ Running the bot

Start the bot with:

```bash
python bot.py
```

Once running, open your bot in Telegram and use the available commands and buttons.

## 🧩 Available commands

- /start — welcome message and keyboard
- /help — shows available features
- /example — demonstrates a correction example
- /resources — shows grammar learning resources

## 💬 How to use it

You can interact with the bot in two main ways:

1. Send a sentence for grammar correction.
2. Use the built-in buttons to:
   - look up a word definition
   - get synonyms and antonyms
   - explore learning resources
   - take grammar tests

Example input:

```text
I goed to school and learned many informations.
```

Example output will include a corrected version, explanations, and a score.

## 🧪 Testing

You can verify that the project files are syntactically valid with:

```bash
python -m compileall .
```

## 📚 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## 🤝 Contributing

Contributions are welcome. If you want to improve the grammar rules, add new features, or expand the learning resources, feel free to open an issue or submit a pull request.
