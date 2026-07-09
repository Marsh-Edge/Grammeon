import re
import httpx

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"
MAX_LENGTH = 4000
MAX_WORD_LENGTH = 100
VALID_WORD_PATTERN = re.compile(r"^[a-zA-Z\s\-']+$")


def _is_valid_word(word: str) -> bool:
    return bool(word) and len(word) <= MAX_WORD_LENGTH and bool(VALID_WORD_PATTERN.match(word))


def _phonetic(data: list) -> str:
    for p in data:
        if p.get("text"):
            return p["text"]
    return ""


def _format_meaning(parts: list) -> str:
    lines = []
    for m in parts:
        pos = m.get("partOfSpeech", "")
        lines.append(f"\n🔹 *{pos}*")
        for i, d in enumerate(m.get("definitions", [])[:3], 1):
            lines.append(f"{i}. {d['definition']}")
            if d.get("example"):
                lines.append(f"   ✏️ *Example:* {d['example']}")
        if m.get("synonyms"):
            lines.append(f"   🔄 *Synonyms:* {', '.join(m['synonyms'][:5])}")
        if m.get("antonyms"):
            lines.append(f"   🔄 *Antonyms:* {', '.join(m['antonyms'][:5])}")
    return "\n".join(lines)


def format_definition(data: list) -> str:
    entry = data[0]
    word = entry["word"]
    phonetic = _phonetic(entry.get("phonetics", []))
    parts = entry.get("meanings", [])

    header = f"📖 *{word}*"
    if phonetic:
        header += f"  {phonetic}"

    meaning = _format_meaning(parts)

    result = f"{header}\n\n{meaning}"

    if len(result) > MAX_LENGTH:
        result = result[:MAX_LENGTH].rsplit("\n", 1)[0]
        result += "\n\n... (more definitions on the web)"

    return result


async def define(word: str) -> str:
    word = word.strip()
    if not _is_valid_word(word):
        return "❌ Invalid input. Please enter only letters, spaces, hyphens, or apostrophes."
    url = API_URL.format(word.lower())
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=10)
    except httpx.HTTPError:
        return "⚠️ Network error while looking up the word. Please try again later."

    if resp.status_code == 404:
        return "❌ Sorry, I couldn't find that word."
    if resp.status_code != 200:
        return "⚠️ Something went wrong. Try again later."
    data = resp.json()
    return format_definition(data)
