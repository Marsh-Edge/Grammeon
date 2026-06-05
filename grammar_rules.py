GRAMMAR_RULES = [
    (r'\bI\s+does\b',     "I do",     "'does' is wrong with 'I' → use 'do'"),
    (r'\bI\s+has\b',      "I have",   "'has' is wrong with 'I' → use 'have'"),
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

    (r'\ba\s+[aeiou]',    None,       "Use 'an' before vowel sounds → 'a' should be 'an'"),
    (r'\ban\s+[^aeiou\s]',None,       "Use 'a' before consonant sounds → 'an' should be 'a'"),

    (r'\bis\s+\w+s\b',    None,       "Possible agreement error: singular 'is' with plural noun"),
    (r'\bdo\s+\w+s\b',    None,       "Use 'does' with singular noun, not 'do'"),

    (r'\bhim\s+and\s+me\b',     "him and I",   "After 'and' use nominative: 'me' → 'I'"),
    (r'\bme\s+\w+\s+and\b',     "I",           "Subject pronoun should be 'I' not 'me'"),
    (r'\bbetween\s+you\s+and\s+me\b', None, "'between you and me' is correct (objective)"),

    (r'\bmore\s+(?:big|small|good|bad|fast|slow)\b', None, "Use 'bigger', 'smaller', 'better', 'worse', 'faster', 'slower'"),
    (r'\bmost\s+(?:big|small|good|bad|fast|slow)\b', None, "Use 'biggest', 'smallest', 'best', 'worst', 'fastest', 'slowest'"),
    (r'\bbetter\s+than\s+\w+\s+are\b', None, "'better than' already comparative → use 'better than' not 'more better'"),

    (r'\bdon\'t\s+\w*\s+no\b', None, "Double negative: 'don't... no' → use either 'don't' OR 'no'"),
    (r'\bcan\'t\s+\w*\s+nothing\b', None, "Double negative: 'can't... nothing' → use 'can't' or 'nothing'"),
    (r'\bno\s+\w+\s+not\b', None, "Double negative: remove either 'no' or 'not'"),

    (r'\bI\s+will\s+goes\b', "I will go", "Future tense uses base form: 'will goes' → 'will go'"),
    (r'\bhe\s+will\s+go\s+last\s+week\b', "he went", "Past time marker 'last week' needs past tense"),
    (r'\byesterday\s+\w+\s+will\b', None, "'yesterday' (past) cannot use 'will' (future)"),
    (r'\bnext\s+week\s+\w+\s+(went|was)\b', None, "Future time 'next week' cannot use past tense"),

    (r'\bif\s+\w+\s+will\b', None, "In 'if' clause: use present, not future 'will'"),
    (r'\bif\s+\w+\s+go\b', None, "Type 1 conditional: 'if' + present → 'will' + base form"),

    (r'\bwant\s+going\b', "want to go", "'want' + infinitive: 'going' → 'to go'"),
    (r'\bstop\s+to\s+\w+ing\b', "stop going", "'stop' + gerund: change to gerund form"),
    (r'\bkeep\s+to\s+\w+ing\b', None, "'keep' needs gerund, not infinitive"),

    (r'\badverb\s+very\s+\w+\b', None, "Adverbs of frequency go before main verb"),
    (r'\balways\s+am\b', "am always", "Adverb of frequency: place after 'be' verb"),
    (r'\bnever\s+is\b', "is never", "Adverb of frequency: place after 'be' verb"),

    (r'\byou\s+can\s+help\s+\?', "Can you help?", "Questions: invert auxiliary and subject"),
    (r'\bwhat\s+you\s+doing\b', "what are you doing", "Present continuous question needs 'are'"),

    (r'\bwas\s+\w+\s+by\b', None, "Passive voice: 'was' + past participle"),
    (r'\bbe\s+\w+ing\b', None, "Passive requires past participle, not '-ing' form"),

    (r'\bon\s+time\b', "in time", "Use 'in time', not 'on time' (unless meaning punctual)"),
    (r'\bat\s+the\s+end\s+of\b', None, "'at the end of' is correct"),
    (r'\bin\s+the\s+end\b', "at the end", "Use 'at the end', not 'in the end'"),
    (r'\baccording\s+with\b', "according to", "Use 'according to', not 'according with'"),
    (r'\bdepend\s+of\b', "depend on", "Use 'depend on', not 'depend of'"),
    (r'\bfocus\s+in\b', "focus on", "Use 'focus on', not 'focus in'"),
    (r'\binterested\s+on\b', "interested in", "Use 'interested in', not 'interested on'"),

    (r'\bgo\s+to\s+school\b', None, "Normally 'go to school' (without 'the')"),
    (r'\bgo\s+to\s+the\s+(?:school|university|hospital|bed)\b', None, "Usually no article or different meaning"),
    (r'\bin\s+hospital\b', "in the hospital", "Use 'in the hospital', not 'in hospital' (AmE)"),

    (r'\bi\s+', "I ", "First-person pronoun 'I' must be capitalized"),
    (r'\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b', None, "Days of week must be capitalized"),
    (r'\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b', None, "Months must be capitalized"),

    (r'\bmuch\s+students\b', "many students", "Countable nouns use 'many', not 'much'"),
    (r'\bfew\s+water\b', "little water", "Uncountable use 'little'; countable use 'few'"),
    (r'\bsince\s+\w+\s+years\b', "for ... years", "Use 'for' with duration; 'since' with point in time"),
    (r'\bsince\s+last\s+week\b', None, "'since' with specific past time is correct"),
    (r'\bfor\s+\d+\s+(?:o\'?clock|AM|PM)\b', None, "'for' with duration is correct"),
    (r'\balready\s+yet\b', None, "Use 'already' or 'yet', not both"),
    (r'\byet\s+already\b', None, "Use 'already' (positive) or 'yet' (negative/question)"),
    (r'\bstill\s+already\b', None, "'still' and 'already' have different meanings"),
]
