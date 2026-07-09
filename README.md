# Grammeon

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
</p>

Grammeon is a Telegram bot that helps learners improve their English grammar, vocabulary, and exam performance through interactive conversations. It combines a rule-based grammar engine with a friendly chat interface to deliver instant corrections, explanations, definitions, and practice tests.

---

## Features

| Capability | Description |
|---|---|
| **Grammar correction** | Detects errors, provides corrected sentences, and explains issues with a score out of 10 |
| **Dictionary** | Word definitions, phonetics, and usage examples via an external API |
| **Synonyms & Antonyms** | Part-of-speech filtered word relationships |
| **Learning resources** | Curated books, websites, and video channels for self-study |
| **Level tests** | Multiple-choice quizzes for CEFR levels A1 through C1 |
| **Exam simulations** | Full-length IELTS, TOEFL, and CERT practice exams with section scoring |
| **Input validation** | Length limits and character filtering on all user inputs |
| **Rate limiting** | Spam protection at 10 messages per 60-second window |

---

## How it works

Users interact with Grammeon through Telegram. The bot accepts sentences and words, then returns feedback through context-aware inline keyboards:

- **Sentences** are analysed for grammar errors and returned with corrections, explanations, and a score
- **Words** can be looked up for definitions or synonyms and antonyms
- **Interactive flows** guide users through level-based tests and full exam simulations

The grammar engine is implemented in `corrector.py` and `grammar_rules.py`. Formatting and presentation are handled by `formatter.py`.

---

## Project structure

```
grammeon/
├── bot.py                 # Telegram application setup and polling
├── handlers.py            # Command handlers, button routing, interaction flows
├── corrector.py           # Grammar checking and scoring logic
├── grammar_rules.py       # Pattern-based correction rules
├── formatter.py           # Formats results for Telegram output
├── dictionary.py          # Dictionary API client
├── synonyms_antonyms.py   # Synonym and antonym lookup
├── resources.py           # Curated learning materials
├── tests.py               # Level test questions (A1–C1) and evaluation
├── exams.py               # Exam simulations (IELTS, TOEFL, CERT)
└── README.md              # This file
```

---

## Getting started

### Prerequisites

- Python 3.9 or later
- A Telegram bot token from [BotFather](https://t.me/botfather)

### Installation

```bash
git clone https://github.com/Marsh-Edge/Grammeon.git
cd Grammeon
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate

pip install python-telegram-bot python-dotenv httpx
```

Create a `.env` file in the project root:

```env
TELEGRAM_TOKEN=your_bot_token_here
```

### Running

```bash
python bot.py
```

---

## Commands

| Command       | Description |
|---------------|-------------|
| `/start`      | Welcome message and main menu |
| `/help`       | Feature overview and usage instructions |
| `/resources`  | Curated learning resources |
| `/exams`      | Start an IELTS, TOEFL, or CERT practice exam |

All core features are also accessible through the inline keyboard buttons.

---

## Testing

```bash
python -m compileall .
```

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions are welcome — open an issue to discuss major changes, or submit a pull request with a clear description of the improvement.
