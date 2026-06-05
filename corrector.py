import re
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

SUBJECT_VERB_RULES = [
    (r'\bI\s+does\b',     "I do",     "'does' is wrong with 'I' → use 'do'"),
    (r'\bI\s+has\b',      "I have",   "'has' is wrong with 'I' → use 'have'"),
    (r'\bI\s+was\b',      None,       None),  # "I was" درسته، چک نکن
    (r'\bI\s+is\b',       "I am",     "'is' is wrong with 'I' → use 'am'"),
    (r'\bI\s+are\b',      "I am",     "'are' is wrong with 'I' → use 'am'"),

    (r'\bYou\s+does\b',   "You do",   "'does' is wrong with 'You' → use 'do'"),
    (r'\bWe\s+does\b',    "We do",    "'does' is wrong with 'We' → use 'do'"),
    (r'\bThey\s+does\b',  "They do",  "'does' is wrong with 'They' → use 'do'"),
    (r'\bYou\s+has\b',    "You have", "'has' is wrong with 'You' → use 'have'"),
    (r'\bWe\s+has\b',     "We have",  "'has' is wrong with 'We' → use 'have'"),
    (r'\bThey\s+has\b',   "They have","'has' is wrong with 'They' → use 'have'"),
    (r'\bYou\s+is\b',     "You are",  "'is' is wrong with 'You' → use 'are'"),
    (r'\bWe\s+is\b',      "We are",   "'is' is wrong with 'We' → use 'are'"),
    (r'\bThey\s+is\b',    "They are", "'is' is wrong with 'They' → use 'are'"),

    (r'\bHe\s+do\b',      "He does",  "'do' is wrong with 'He' → use 'does'"),
    (r'\bShe\s+do\b',     "She does", "'do' is wrong with 'She' → use 'does'"),
    (r'\bIt\s+do\b',      "It does",  "'do' is wrong with 'It' → use 'does'"),
    (r'\bHe\s+have\b',    "He has",   "'have' is wrong with 'He' → use 'has'"),
    (r'\bShe\s+have\b',   "She has",  "'have' is wrong with 'She' → use 'has'"),
    (r'\bIt\s+have\b',    "It has",   "'have' is wrong with 'It' → use 'has'"),
    (r'\bHe\s+are\b',     "He is",    "'are' is wrong with 'He' → use 'is'"),
    (r'\bShe\s+are\b',    "She is",   "'are' is wrong with 'She' → use 'is'"),
    (r'\bIt\s+are\b',     "It is",    "'are' is wrong with 'It' → use 'is'"),
]


def check_subject_verb(text: str) -> list:
    errors = []
    corrected = text

    for pattern, fix, message in SUBJECT_VERB_RULES:
        if message is None:
            continue
        match = re.search(pattern, corrected, re.IGNORECASE)
        if match:
            wrong = match.group()
            errors.append({
                "wrong": wrong,
                "message": message,
                "suggestions": [fix] if fix else []
            })
            if fix:
                corrected = re.sub(pattern, fix, corrected, flags=re.IGNORECASE)

    return errors, corrected


def calculate_score(text: str, total_errors: int) -> int:
    word_count = len(text.split())
    if word_count == 0:
        return 10
    ratio = total_errors / word_count
    return min(max(1, round(10 - ratio * 20)), 10)


def check_text(text: str) -> dict:
    manual_errors, pre_corrected = check_subject_verb(text)

    lt_matches = tool.check(pre_corrected)
    lt_corrected = language_tool_python.utils.correct(pre_corrected, lt_matches)

    lt_errors = []
    for m in lt_matches:
        wrong = pre_corrected[m.offset: m.offset + m.errorLength]
        lt_errors.append({
            "wrong": wrong,
            "message": m.message,
            "suggestions": m.replacements[:3]
        })

    all_errors = manual_errors + lt_errors
    total_errors = len(all_errors)
    score = calculate_score(text, total_errors)

    return {
        "original": text,
        "corrected": lt_corrected,
        "errors": all_errors,
        "score": score
    }