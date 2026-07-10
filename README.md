<h1 align="center">Grammeon</h1>

<p align="center">
  <em>A Telegram bot that helps you master English grammar, vocabulary, and exam skills through interactive conversation.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/telegram-bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Bot">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="MIT License">
  <img src="https://img.shields.io/badge/lib--python--telegram--bot-v20%2B-26A5E4?style=for-the-badge&logo=python&logoColor=white" alt="python-telegram-bot">
</p>

<p align="center">
  <a href="#about-the-project">About</a> &bull;
  <a href="#features">Features</a> &bull;
  <a href="#tech-stack">Tech Stack</a> &bull;
  <a href="#getting-started">Getting Started</a> &bull;
  <a href="#commands">Commands</a> &bull;
  <a href="#roadmap">Roadmap</a> &bull;
  <a href="#license">License</a>
</p>

---

<!-- SCREENSHOT PLACEMENT
Add screenshots or a GIF of the bot in action here.

Example:
![Grammar Correction](https://your-image-url.com/grammar-correction.png)
![Level Test](https://your-image-url.com/level-test.png)
![Exam Simulation](https://your-image-url.com/exam-simulation.png)
-->

---

## About the Project

Grammeon is a Telegram bot designed for English learners who want to improve their grammar, vocabulary, and exam readiness through interactive conversations. It combines a rule-based grammar engine with a friendly chat interface to deliver instant corrections, explanations, definitions, and practice tests — all within Telegram.

The bot covers the full CEFR spectrum from A1 (Beginner) to C1 (Advanced) and includes practice simulations for internationally recognised English exams: IELTS, TOEFL, and CERT (Cambridge).

### Why This Project?

Learning English grammar traditionally relies on textbooks and static exercises. Grammeon takes a different approach by meeting learners where they already are — in Telegram. Instead of opening a textbook, you send a sentence and get instant, explained feedback. Instead of flipping to an answer key, you take an interactive quiz right in the chat.

The goal is to make grammar practice as frictionless as sending a message.

---

## Features

| Feature | Description |
|:---|:---|
| **Grammar Correction** | Detects errors in English sentences, provides corrected versions, explains each issue, and assigns a score out of 10 |
| **Dictionary Lookup** | Retrieves word definitions, phonetic transcriptions, and usage examples via the Free Dictionary API |
| **Synonyms & Antonyms** | Finds word relationships filtered by part of speech |
| **Learning Resources** | Curated books, websites, and YouTube channels organised by type and level |
| **Level Tests** | Multiple-choice quizzes for CEFR levels A1 through C1 (5 questions per session) |
| **Exam Simulations** | Full-length IELTS, TOEFL, and CERT practice exams with reading comprehension, grammar, and vocabulary sections (15 questions per exam) |
| **Interactive Menus** | Inline keyboard navigation for all features — no need to memorise commands |
| **Input Validation** | Length limits and character filtering on all user inputs to prevent abuse |
| **Rate Limiting** | Spam protection at 10 messages per 60-second window per user |
| **Error Handling** | Graceful recovery from network errors and invalid inputs |

---

## Tech Stack

| Component | Technology |
|:---|:---|
| **Language** | Python 3.9+ |
| **Bot Framework** | [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20+ (async) |
| **HTTP Client** | [httpx](https://github.com/encode/httpx) (async, for API calls) |
| **Configuration** | [python-dotenv](https://github.com/theskumar/python-dotenv) (environment variable management) |
| **External API** | [Free Dictionary API](https://dictionaryapi.dev/) (definitions, phonetics, synonyms, antonyms) |
| **Grammar Engine** | Custom rule-based system using regex pattern matching |
| **Hosting** | Self-hosted (runs anywhere Python is available) |

---

## Project Structure

```
grammeon/
├── bot.py                 # Application setup, handler registration, and polling
├── handlers.py            # Command handlers, callback routing, and interaction flows
├── corrector.py           # Grammar checking engine and scoring logic
├── grammar_rules.py       # Pattern-based correction rules (~170 rules)
├── formatter.py           # Formats grammar results for Telegram output
├── dictionary.py          # Free Dictionary API client
├── synonyms_antonyms.py   # Synonym and antonym lookup via Dictionary API
├── resources.py           # Curated learning materials (books, websites, videos)
├── tests.py               # Level test questions (A1–C1) and evaluation logic
├── exams.py               # Exam simulations (IELTS, TOEFL, CERT) and scoring
├── .env                   # Environment variables (not committed)
├── .gitignore             # Git ignore rules
├── LICENSE                # MIT License
└── README.md              # This file
```

---

## Getting Started

### Prerequisites

- **Python 3.9** or later
- A **Telegram bot token** from [BotFather](https://t.me/botfather)

### Installation

```bash
git clone https://github.com/Marsh-Edge/Grammeon.git
cd Grammeon
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate
```

Install dependencies:

```bash
pip install python-telegram-bot python-dotenv httpx
```

### Configuration

Create a `.env` file in the project root:

```env
TELEGRAM_TOKEN=your_bot_token_here
```

> **Note:** Never commit your `.env` file or expose your bot token. The `.gitignore` is already configured to exclude it.

### Running

```bash
python bot.py
```

The bot will start polling Telegram for messages. Open Telegram, find your bot, and send `/start`.

---

## Commands

| Command | Description |
|:---|:---|
| `/start` | Welcome message and main menu |
| `/help` | Feature overview and usage instructions |
| `/resources` | Curated learning resources (books, websites, videos) |
| `/exams` | Start an IELTS, TOEFL, or CERT practice exam |

All core features are also accessible through the persistent reply keyboard and inline buttons — no need to memorise commands.

---

## Testing

To verify the code compiles without syntax errors:

```bash
python -m compileall .
```

---

## Roadmap

### Completed

- [x] Rule-based grammar correction engine with ~170 patterns
- [x] Grammar scoring system (1–10 scale)
- [x] Dictionary lookup with phonetics and examples
- [x] Synonym and antonym lookup
- [x] CEFR level tests (A1, A2, B1, B2, C1)
- [x] Exam simulations (IELTS, TOEFL, CERT)
- [x] Reading comprehension section in exams
- [x] Curated learning resources
- [x] Interactive inline keyboard navigation
- [x] Rate limiting and input validation
- [x] Persistent reply keyboard with all features

### Planned

- [ ] User progress tracking and statistics
- [ ] Spaced repetition vocabulary trainer
- [ ] Writing practice with paragraph-level feedback
- [ ] Pronunciation feedback via voice messages
- [ ] Multi-language interface (Arabic, French, Spanish)
- [ ] Admin dashboard for monitoring usage
- [ ] Deployment guide for cloud platforms (Railway, Render, etc.)
- [ ] Expand grammar rule set with context-aware corrections

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Author

**Edge Quantum** — [GitHub](https://github.com/Marsh-Edge)

---

## Acknowledgments

- [Free Dictionary API](https://dictionaryapi.dev/) — Open-source dictionary data used for definitions, phonetics, synonyms, and antonyms
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) — The library powering the Telegram bot interface
- [httpx](https://github.com/encode/httpx) — Modern async HTTP client for Python
- All the English teachers and learners whose feedback inspired the grammar rule set
