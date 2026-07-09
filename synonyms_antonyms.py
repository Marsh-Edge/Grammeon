import re
import httpx

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"
MAX_WORD_LENGTH = 100
VALID_WORD_PATTERN = re.compile(r"^[a-zA-Z\s\-']+$")


def _is_valid_word(word: str) -> bool:
    return bool(word) and len(word) <= MAX_WORD_LENGTH and bool(VALID_WORD_PATTERN.match(word))


async def synonyms(word: str) -> str:
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
    entry = data[0]
    parts = entry.get("meanings", [])

    lines = [f"🔄 *Synonyms & Antonyms — {word.capitalize()}*"]
    found = False
    for m in parts:
        pos = m.get("partOfSpeech", "")
        syns = m.get("synonyms", [])
        ants = m.get("antonyms", [])
        if not syns and not ants:
            continue
        found = True
        lines.append(f"\n🔹 *{pos}*")
        if syns:
            lines.append(f"✦ *Synonyms:* {', '.join(syns[:8])}")
        if ants:
            lines.append(f"✦ *Antonyms:* {', '.join(ants[:8])}")

    if not found:
        return f"❌ No synonyms or antonyms found for *{word}*."

    return "\n".join(lines)
