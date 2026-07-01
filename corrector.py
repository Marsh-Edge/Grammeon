import re
from grammar_rules import GRAMMAR_RULES

def check_grammar(text: str) -> tuple:
    errors = []
    corrected = text
    seen = set()

    for pass_num in range(2):
        for rule in GRAMMAR_RULES:
            pattern, fix, message = rule

            matches = list(re.finditer(pattern, corrected, re.IGNORECASE))
            for match in matches:
                wrong = match.group()
                key = (wrong.lower(), message)
                if key not in seen:
                    seen.add(key)
                    errors.append({
                        "wrong": wrong,
                        "message": message,
                        "suggestions": [re.sub(pattern, fix, wrong, flags=re.IGNORECASE)] if fix else []
                    })

            if fix:
                corrected = re.sub(pattern, fix, corrected, flags=re.IGNORECASE)

    return errors, corrected


def calculate_score(word_count: int, error_count: int) -> int:
    if word_count == 0:
        return 10
    ratio = error_count / word_count
    return min(max(1, round(10 - ratio * 20)), 10)


def check_message(text: str) -> dict:
    errors, corrected = check_grammar(text)

    word_count = len(text.split())
    score = calculate_score(word_count, len(errors))

    return {
        "original": text,
        "corrected": corrected,
        "errors": errors,
        "score": score
    }