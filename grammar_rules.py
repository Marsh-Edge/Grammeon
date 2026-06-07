"""
Grammar rules for corrector.py
Each rule: (pattern, fix, message)
fix=None means report only, no auto-correct
"""

GRAMMAR_RULES = [

    # ── Subject-Verb Agreement ────────────────────────────────

    (r'\bI\s+does\b',          "I do",       "Use 'do' with 'I'."),
    (r'\bI\s+has\b',           "I have",     "Use 'have' with 'I'."),
    (r'\bI\s+is\b',            "I am",       "Use 'am' with 'I'."),
    (r'\bI\s+are\b',           "I am",       "Use 'am' with 'I'."),
    (r'\bI\s+doesn\'t\b',      "I don't",    "Use 'don't' with 'I'."),

    (r'\bYou\s+does\b',        "You do",     "Use 'do' with 'You'."),
    (r'\bYou\s+has\b',         "You have",   "Use 'have' with 'You'."),
    (r'\bYou\s+is\b',          "You are",    "Use 'are' with 'You'."),

    (r'\bWe\s+does\b',         "We do",      "Use 'do' with 'We'."),
    (r'\bWe\s+has\b',          "We have",    "Use 'have' with 'We'."),
    (r'\bWe\s+is\b',           "We are",     "Use 'are' with 'We'."),

    (r'\bThey\s+does\b',       "They do",    "Use 'do' with 'They'."),
    (r'\bThey\s+has\b',        "They have",  "Use 'have' with 'They'."),
    (r'\bThey\s+is\b',         "They are",   "Use 'are' with 'They'."),

    (r'\b(He|She|It)\s+do\b',    r'\1 does',   "Use 'does' with 'He/She/It'."),
    (r'\b(He|She|It)\s+have\b',  r'\1 has',    "Use 'has' with 'He/She/It'."),
    (r'\b(He|She|It)\s+are\b',   r'\1 is',     "Use 'is' with 'He/She/It'."),
    (r'\b(He|She|It)\s+don\'t\b',r"\1 doesn't","Use 'doesn't' with 'He/She/It'."),

    (r'\b(This|That)\s+do\b',    r'\1 does',   "Use 'does' with singular subjects."),
    (r'\b(This|That)\s+have\b',  r'\1 has',    "Use 'has' with singular subjects."),
    (r'\b(This|That)\s+are\b',   r'\1 is',     "Use 'is' with singular subjects."),

    (r'\b(These|Those)\s+is\b',  r'\1 are',    "Use 'are' with plural subjects."),
    (r'\b(These|Those)\s+has\b', r'\1 have',   "Use 'have' with plural subjects."),
    (r'\b(These|Those)\s+does\b',r'\1 do',     "Use 'do' with plural subjects."),

    # ── Possessive 's ─────────────────────────────────────────
    # "my friend house" → "my friend's house"
    (r'\b(my|his|her|our|their|your)\s+(\w+)\s+(house|car|bag|book|phone|room|job|name|idea|cat|dog|son|daughter|wife|husband|sister|brother|mother|father|friend|teacher|boss|team|school|office|company)\b',
     None,
     "Missing possessive 's — e.g. 'my friend's house' not 'my friend house'."),

    # ── Irregular Past Tense ──────────────────────────────────
    (r'\bI\s+goed\b',          "I went",      "'goed' is not valid — past tense of 'go' is 'went'."),
    (r'\bI\s+comed\b',         "I came",      "'comed' is not valid — past tense of 'come' is 'came'."),
    (r'\bI\s+runned\b',        "I ran",       "'runned' is not valid — past tense of 'run' is 'ran'."),
    (r'\bI\s+buyed\b',         "I bought",    "'buyed' is not valid — past tense of 'buy' is 'bought'."),
    (r'\bI\s+taked\b',         "I took",      "'taked' is not valid — past tense of 'take' is 'took'."),
    (r'\bI\s+maked\b',         "I made",      "'maked' is not valid — past tense of 'make' is 'made'."),
    (r'\bI\s+writed\b',        "I wrote",     "'writed' is not valid — past tense of 'write' is 'wrote'."),
    (r'\bI\s+readed\b',        "I read",      "'readed' is not valid — past tense of 'read' is 'read'."),
    (r'\bI\s+knowed\b',        "I knew",      "'knowed' is not valid — past tense of 'know' is 'knew'."),
    (r'\bI\s+selled\b',        "I sold",      "'selled' is not valid — past tense of 'sell' is 'sold'."),
    (r'\b(He|She|It)\s+goed\b',  r'\1 went',  "'goed' is not valid — past tense of 'go' is 'went'."),
    (r'\b(He|She|It)\s+comed\b', r'\1 came',  "'comed' is not valid — past tense of 'come' is 'came'."),
    (r'\b(He|She|It)\s+runned\b',r'\1 ran',   "'runned' is not valid — past tense of 'run' is 'ran'."),
    (r'\b(They|We|You)\s+goed\b',r'\1 went',  "'goed' is not valid — past tense of 'go' is 'went'."),

    # ── Past Participle ───────────────────────────────────────
    (r'\bhave\s+went\b',       "have gone",   "Use past participle: 'have gone'."),
    (r'\bhave\s+saw\b',        "have seen",   "Use past participle: 'have seen'."),
    (r'\bhave\s+took\b',       "have taken",  "Use past participle: 'have taken'."),
    (r'\bhave\s+gave\b',       "have given",  "Use past participle: 'have given'."),
    (r'\bhave\s+wrote\b',      "have written","Use past participle: 'have written'."),
    (r'\bhave\s+ate\b',        "have eaten",  "Use past participle: 'have eaten'."),
    (r'\bhave\s+ran\b',        "have run",    "Use past participle: 'have run'."),
    (r'\bhas\s+went\b',        "has gone",    "Use past participle: 'has gone'."),
    (r'\bhas\s+saw\b',         "has seen",    "Use past participle: 'has seen'."),
    (r'\bhas\s+took\b',        "has taken",   "Use past participle: 'has taken'."),
    (r'\bhas\s+gave\b',        "has given",   "Use past participle: 'has given'."),

    # ── Modal Verbs ───────────────────────────────────────────
    (r'\bwill\s+goes\b',       "will go",     "Use base verb after 'will'."),
    (r'\bwill\s+comes\b',      "will come",   "Use base verb after 'will'."),
    (r'\bwill\s+works\b',      "will work",   "Use base verb after 'will'."),
    (r'\bwill\s+studies\b',    "will study",  "Use base verb after 'will'."),
    (r'\bwill\s+has\b',        "will have",   "Use base verb after 'will'."),
    (r'\bwill\s+is\b',         "will be",     "Use base verb after 'will'."),

    (r'\b(can|must|should|could|would|may|might)\s+goes\b',   r'\1 go',    "Use base verb after a modal."),
    (r'\b(can|must|should|could|would|may|might)\s+comes\b',  r'\1 come',  "Use base verb after a modal."),
    (r'\b(can|must|should|could|would|may|might)\s+works\b',  r'\1 work',  "Use base verb after a modal."),
    (r'\b(can|must|should|could|would|may|might)\s+studies\b',r'\1 study', "Use base verb after a modal."),
    (r'\b(can|must|should|could|would|may|might)\s+is\b',     r'\1 be',    "Use base verb after a modal."),
    (r'\b(can|must|should|could|would|may|might)\s+has\b',    r'\1 have',  "Use base verb after a modal."),

    # ── Uncountable Nouns ─────────────────────────────────────
    (r'\bmany\s+informations\b', "much information", "'information' is uncountable — use 'much information'."),
    (r'\bmany\s+advices\b',      "much advice",      "'advice' is uncountable — use 'much advice'."),
    (r'\bmany\s+luggages\b',     "much luggage",     "'luggage' is uncountable — use 'much luggage'."),
    (r'\bmany\s+furnitures\b',   "much furniture",   "'furniture' is uncountable — use 'much furniture'."),
    (r'\bmany\s+waters\b',       "much water",       "'water' is uncountable — use 'much water'."),
    (r'\bmany\s+knowledges\b',   "much knowledge",   "'knowledge' is uncountable — use 'much knowledge'."),
    (r'\ban?\s+informations?\b', "information",      "'information' has no plural form."),
    (r'\ban?\s+advices?\b',      "advice",           "'advice' has no plural form."),

    # ── Articles ──────────────────────────────────────────────
    (r'\ba\s+(hour|honest|honour|heir)\b', r'an \1', "Use 'an' before silent-h words."),
    (r'\ban\s+(university|union|unique|unit|usual|user|use|uniform)\b', r'a \1', "Use 'a' before words starting with a 'y' sound."),

    # ── Prepositions ──────────────────────────────────────────
    (r'\baccording\s+with\b',   "according to",  "Use 'according to'."),
    (r'\bdepend\s+of\b',        "depend on",     "Use 'depend on'."),
    (r'\bfocus\s+in\b',         "focus on",      "Use 'focus on'."),
    (r'\binterested\s+on\b',    "interested in", "Use 'interested in'."),
    (r'\bsimilar\s+with\b',     "similar to",    "Use 'similar to'."),
    (r'\bmarried\s+with\b',     "married to",    "Use 'married to'."),
    (r'\barrived\s+to\b',       "arrived at",    "Use 'arrived at'."),
    (r'\blisten\s+me\b',        "listen to me",  "Use 'listen to'."),

    # ── Double Negative ───────────────────────────────────────
    (r'\bdon\'t\s+\w+\s+nothing\b', None, "Avoid double negatives — use 'don't have anything'."),
    (r'\bcan\'t\s+\w+\s+nothing\b', None, "Avoid double negatives — use 'can't find anything'."),

    # ── Capitalization ────────────────────────────────────────
    (r'(?<![.\?!]\s)\bi\b', "I", "The pronoun 'I' must always be capitalized."),
    (r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b',
     None, "Days of the week must be capitalized."),
    (r'\b(january|february|march|april|june|july|august|september|october|november|december)\b',
     None, "Month names must be capitalized."),

    # ── Punctuation ───────────────────────────────────────────
    (r'\s+([,\.!?])', r'\1', "Remove space before punctuation."),
]