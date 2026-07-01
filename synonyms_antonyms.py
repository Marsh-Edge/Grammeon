import httpx

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"


async def synonyms(word: str) -> str:
    url = API_URL.format(word.strip().lower())
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, timeout=10)

    if resp.status_code == 404:
        return f"❌ Sorry, I couldn't find the word *{word}*."
    if resp.status_code != 200:
        return f"⚠️ Something went wrong (status {resp.status_code}). Try again later."

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
