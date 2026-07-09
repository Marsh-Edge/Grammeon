# Grammeon

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Active">
</p>

Grammeon is a Telegram-based English learning assistant that provides concise, actionable feedback on grammar, vocabulary, and exam readiness. It combines a rule-driven grammar engine with interactive Telegram flows to deliver corrections, explanations, definitions, and practice tests.

Key capabilities:

- Grammar correction with clear explanations and a readability/accuracy score
- Dictionary lookups with definitions, phonetics, and examples
- Synonyms and antonyms search with part-of-speech filtering
- Level-based quizzes (A1–C1) and exam simulations (IELTS, TOEFL, CERT)
- Rate limiting and input validation to ensure robust operation

## Table of contents

- [Features](#features)
- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Testing](#testing)
- [License](#license)
- [Contributing](#contributing)

## Features

- Grammar correction and scoring with explanations
- Word definitions, phonetics, and usage examples
- Synonyms and antonyms with POS filtering
- Curated learning resources for self-study
- Level tests and full exam simulations with section scoring
- Built-in rate limiting and input validation

## How it works

Users interact with the bot through Telegram. The bot accepts a sentence or a word and returns one or more of the following depending on the flow:

- Corrected sentence and suggested improvements
- Identified grammar issues with concise explanations
- Score and guidance to improve writing
- Dictionary entries, synonyms, and antonyms
- Interactive quizzes and exam-style tests

Interactive flows use inline keyboards for navigation and user inputs. The core grammar logic is implemented in `corrector.py` and `grammar_rules.py`; presentation and message formatting are handled by `formatter.py`.

## Project structure

```
grammeon/
├── bot.py                 # Telegram bot entry point and routing
├── handlers.py            # Command handlers and interaction flows
├── corrector.py           # Grammar-checking engine
├── grammar_rules.py       # Rule definitions and patterns
├── formatter.py           # Message formatting for Telegram
├── dictionary.py          # External dictionary API wrapper
├── synonyms_antonyms.py   # Synonym/antonym utilities
├── resources.py           # Curated learning materials
├── tests.py               # Level test questions and evaluation logic
├── exams.py               # Exam simulations and scoring
└── README.md              # Project documentation
```

## Installation

Prerequisites:

- Python 3.9 or newer
- A Telegram bot token from BotFather

Quick setup:

```bash
git clone https://github.com/Marsh-Edge/Grammeon.git
cd Grammeon
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate
pip install -r requirements.txt
```

Create a `.env` file with your bot token:

```env
TELEGRAM_TOKEN=your_bot_token_here
```

## Usage

Start the bot locally:

```bash
python bot.py
```

Open the bot in Telegram and use the provided commands or inline keyboard to interact.

## Commands

- `/start` — Welcome message and primary menu
- `/help` — Usage instructions and feature overview
- `/resources` — Curated learning resources
- `/exams` — Start an exam simulation (IELTS/TOEFL/CERT)

## Testing

Run a quick syntax check for the repository:

```bash
python -m compileall .
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome. Please open an issue to discuss major changes before submitting a pull request. For documentation updates or small fixes, submit a PR with a clear description of the change.

---

If you would like, I can also:

- Run tests or linting on the codebase
- Stage and commit this update to the local Git repository
- Push the commit to a remote branch

