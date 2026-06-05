import re
import language_tool_python
from grammar_rules import GRAMMAR_RULES

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text: str) -> list:
    errors = []
    corrected = text

    for pattern, fix, message in GRAMMAR_RULES:
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


def check_message(text: str) -> dict:
    manual_errors, pre_corrected = check_grammar(text)

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