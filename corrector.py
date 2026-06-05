import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def calculate_score(text:str, matches:list) -> int:
  word_count = len(text.split())
  if word_count == 0:
    return 100
  ratio = len(matches) / word_count
  score = max(0, 100 - int(ratio * 100))
  return score

def check_text(text:str) -> dict:
  matches = tool.check(text)
  corrected_text = language_tool_python.utils.correct(text, matches)
  score = calculate_score(text, matches)
  
  errors = []
  for match in matches:
    wrong = text[match.offset:match.offset + match.error_length]
    errors.append({
      "wrong": wrong,
      "message": match.message,
      "suggestions": match.replacements[:3]
    })
  
  return {
    "original": text,
    "corrected": corrected_text,
    "score": score,
    "errors": errors
  }