import httpx

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"
MAX_LENGTH = 4000


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
    url = API_URL.format(word.strip().lower())
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=10)

    if resp.status_code == 404:
        return f"❌ Sorry, I couldn't find the word *{word}*."
    if resp.status_code != 200:
        return f"⚠️ Something went wrong (status {resp.status_code}). Try again later."

    data = resp.json()
    return format_definition(data)
