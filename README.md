# Grammeon

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/status-active-brightgreen" alt="Active">
</p>

Grammeon is a Telegram-based English learning assistant that helps learners improve their grammar, vocabulary, and exam readiness through interactive conversations.

The bot analyses English sentences, suggests corrections, explains grammar issues, provides word definitions and synonyms, and guides users through level-based tests (A1–C1) and full-length international exam simulations (IELTS, TOEFL, CERT).

---

## Table of Contents

- [Features](#features)
- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Installation](#installation)
- [Running the bot](#running-the-bot)
- [Commands](#commands)
- [Usage examples](#usage-examples)
- [Testing](#testing)
- [License](#license)
- [Contributing](#contributing)

---

## Features

- **Grammar correction** — Detects and explains errors in English sentences with a score out of 10
- **Dictionary** — Word definitions, phonetics, and usage examples via an external API
- **Synonyms & Antonyms** — Finds related words with part-of-speech filtering
- **Learning resources** — Curated books, websites, and video channels for self-study
- **Level tests** — Interactive multiple-choice quizzes for A1, A2, B1, B2, and C1 levels
- **Exam simulations** — Full-length IELTS, TOEFL, and CERT practice exams with section-based scoring
- **Rate limiting** — Built-in spam protection (10 messages per 60 seconds)
- **Input validation** — Length limits and character filtering for all user inputs

---

## How it works

Grammeon combines a lightweight rule-based grammar engine with a Telegram bot interface. Users send a sentence and receive:

- A corrected version of the sentence
- A list of detected grammar issues with explanations
- A score out of 10
- Suggestions for improvement

The bot also supports interactive flows for dictionary lookups, synonyms, level-based tests, and full exam simulations — all through an inline keyboard interface.

---

## Project structure

```
grammeon/
├── bot.py                 # Entry point — Telegram bot setup and polling
├── handlers.py            # Command handling, button routing, interactive flows
├── corrector.py           # Grammar checking and scoring engine
├── grammar_rules.py       # Rule-based correction patterns
├── formatter.py           # Formats correction results for Telegram output
├── dictionary.py          # Word definition lookup via external API
├── synonyms_antonyms.py   # Synonyms and antonyms lookup
├── resources.py           # Curated learning resources (books, websites, videos)
├── tests.py               # A1–C1 level test questions and evaluation
├── exams.py               # IELTS, TOEFL, CERT exam questions and evaluation
└── requirements.txt       # Project dependencies
```

---

## Installation

### Prerequisites

- Python 3.9+
- A Telegram bot token from [BotFather](https://t.me/botfather)

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

   ```powershell
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install python-telegram-bot python-dotenv httpx
   ```

4. Create a `.env` file in the project root:

   ```env
   TELEGRAM_TOKEN=your_bot_token_here
   ```

---

## Running the bot

```bash
python bot.py
```

Once running, open your bot in Telegram and use the available commands and buttons.

---

## Commands

| Command       | Description                                    |
|---------------|------------------------------------------------|
| `/start`      | Welcome message with main keyboard             |
| `/help`       | List of available features and how to use them |
| `/resources`  | Curated grammar learning resources             |
| `/exams`      | Start an IELTS, TOEFL, or CERT exam simulation |

---

## Usage examples

**Grammar correction** — Send any English sentence:

```text
I goed to school and learned many informations.
```

The bot replies with a corrected version, error explanations, and a score.

**Dictionary** — Press the **Dictionary** button and send a word.

**Synonyms** — Press the **Synonyms** button and send a word.

**Level tests** — Press the **Tests** button, choose a level (A1–C1), and answer 5 multiple-choice questions.

**Exam simulations** — Press the **Exams** button, accept the conditions, choose IELTS/TOEFL/CERT, and complete 15 questions with section-based scoring.

---

## Testing

Verify all project files are syntactically valid:

```bash
python -m compileall .
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions are welcome. If you want to improve the grammar rules, add new features, or expand the learning resources, feel free to open an issue or submit a pull request.
