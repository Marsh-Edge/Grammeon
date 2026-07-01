"""
Grammar rules for corrector.py
Each rule: (pattern, fix, message)
fix=None means report only, no auto-correct
"""

GRAMMAR_RULES = [

    # ── Missing Apostrophe in Contractions ────────────────────
    # Must come FIRST so other rules can match the fixed contractions
    (r'\bdoesnt\b',  "doesn't",  "Missing apostrophe in 'doesn't'."),
    (r'\bdont\b',    "don't",    "Missing apostrophe in 'don't'."),
    (r'\bwont\b',    "won't",    "Missing apostrophe in 'won't'."),
    (r'\bcant\b',    "can't",    "Missing apostrophe in 'can't'."),
    (r'\bisnt\b',    "isn't",    "Missing apostrophe in 'isn't'."),
    (r'\barent\b',   "aren't",   "Missing apostrophe in 'aren't'."),
    (r'\bwasnt\b',   "wasn't",   "Missing apostrophe in 'wasn't'."),
    (r'\bwerent\b',  "weren't",  "Missing apostrophe in 'weren't'."),
    (r'\bhasnt\b',   "hasn't",   "Missing apostrophe in 'hasn't'."),
    (r'\bhavent\b',  "haven't",  "Missing apostrophe in 'haven't'."),
    (r'\bhadnt\b',   "hadn't",   "Missing apostrophe in 'hadn't'."),
    (r'\bcouldnt\b', "couldn't", "Missing apostrophe in 'couldn't'."),
    (r'\bwouldnt\b', "wouldn't", "Missing apostrophe in 'wouldn't'."),
    (r'\bshouldnt\b',"shouldn't","Missing apostrophe in 'shouldn't'."),
    (r'\bmustnt\b',  "mustn't",  "Missing apostrophe in 'mustn't'."),
    (r'\bmightnt\b', "mightn't", "Missing apostrophe in 'mightn't'."),
    (r'\bdidnt\b',   "didn't",   "Missing apostrophe in 'didn't'."),

    # ── Verb Form After 'to' (Infinitive) ──────────────────────
    (r'\bto\s+has\b',    "to have",   "Use base verb form after 'to'."),
    (r'\bto\s+does\b',   "to do",     "Use base verb form after 'to'."),
    (r'\bto\s+goes\b',   "to go",     "Use base verb form after 'to'."),
    (r'\bto\s+had\b',    "to have",   "Use base verb form after 'to'."),
    (r'\bto\s+did\b',    "to do",     "Use base verb form after 'to'."),
    (r'\bto\s+(went|said|made|took|came|gave|knew|thought|bought|sold|taught|caught|fought|told|spoke|broke|woke|drove|rode|wrote|sang|drank|swam|ran|ate|sat|stood|built|sent|spent|left|met|lost|meant|paid|forgot|hid|bit|chose|froze|wore|stole|flew|grew|threw|drew|understood)\b',
     None, "Use base verb form after 'to' (infinitive), not past tense."),

    # ── Subject-Verb Agreement ────────────────────────────────

    # First person singular (I)
    (r'\bI\s+does\b',          "I do",       "Use 'do' with 'I'."),
    (r'\bI\s+has\b',           "I have",     "Use 'have' with 'I'."),
    (r'\bI\s+is\b',            "I am",       "Use 'am' with 'I'."),
    (r'\bI\s+are\b',           "I am",       "Use 'am' with 'I'."),
    (r'\bI\s+doesn\'t\b',      "I don't",    "Use 'don't' with 'I'."),

    # Second person (You)
    (r'\bYou\s+does\b',        "You do",     "Use 'do' with 'You'."),
    (r'\bYou\s+has\b',         "You have",   "Use 'have' with 'You'."),
    (r'\bYou\s+is\b',          "You are",    "Use 'are' with 'You'."),
    (r'\bYou\s+was\b',         "You were",   "Use 'were' with 'You'."),

    # First person plural (We)
    (r'\bWe\s+does\b',         "We do",      "Use 'do' with 'We'."),
    (r'\bWe\s+has\b',          "We have",    "Use 'have' with 'We'."),
    (r'\bWe\s+is\b',           "We are",     "Use 'are' with 'We'."),
    (r'\bWe\s+was\b',          "We were",    "Use 'were' with 'We'."),

    # Third person plural (They)
    (r'\bThey\s+does\b',       "They do",    "Use 'do' with 'They'."),
    (r'\bThey\s+has\b',        "They have",  "Use 'have' with 'They'."),
    (r'\bThey\s+is\b',         "They are",   "Use 'are' with 'They'."),
    (r'\bThey\s+was\b',        "They were",  "Use 'were' with 'They'."),
    (r'\b(They|We|You)\s+doesn\'t\b',  r"\1 don't",   "Use 'don't' with 'They/We/You'."),

    # Third person singular (He/She/It)
    (r'\b(He|She|It)\s+do\b',    r'\1 does',   "Use 'does' with 'He/She/It'."),
    (r'\b(He|She|It)\s+have\b',  r'\1 has',    "Use 'has' with 'He/She/It'."),
    (r'\b(He|She|It)\s+are\b',   r'\1 is',     "Use 'is' with 'He/She/It'."),
    (r'\b(He|She|It)\s+am\b',    r'\1 is',     "Use 'is' with 'He/She/It'."),
    (r'\b(He|She|It)\s+don\'t\b',r"\1 doesn't","Use 'doesn't' with 'He/She/It'."),
    (r'\b(He|She|It)\s+were\b',  r'\1 was',    "Use 'was' with 'He/She/It' in indicative mood."),

    # This/That (singular)
    (r'\b(This|That)\s+do\b',    r'\1 does',   "Use 'does' with singular subjects."),
    (r'\b(This|That)\s+have\b',  r'\1 has',    "Use 'has' with singular subjects."),
    (r'\b(This|That)\s+are\b',   r'\1 is',     "Use 'is' with singular subjects."),

    # These/Those (plural)
    (r'\b(These|Those)\s+is\b',  r'\1 are',    "Use 'are' with plural subjects."),
    (r'\b(These|Those)\s+has\b', r'\1 have',   "Use 'have' with plural subjects."),
    (r'\b(These|Those)\s+does\b',r'\1 do',     "Use 'do' with plural subjects."),

    # Indefinite pronouns (always singular)
    (r'\b(Everybody|Everyone|Everything)\s+(are|were)\b',
     None, "Indefinite pronouns like 'everybody' take singular verbs ('is/was')."),
    (r'\b(Somebody|Someone|Something)\s+(are|were)\b',
     None, "Indefinite pronouns like 'somebody' take singular verbs ('is/was')."),
    (r'\b(Anybody|Anyone|Anything)\s+(are|were)\b',
     None, "Indefinite pronouns like 'anybody' take singular verbs ('is/was')."),
    (r'\b(Nobody|No one|Nothing)\s+(are|were)\b',
     None, "Indefinite pronouns like 'nobody' take singular verbs ('is/was')."),
    (r'\bEach\s+(are|were)\b',
     None, "'Each' takes a singular verb ('is/was')."),
    (r'\b(Either|Neither)\s+(are|were)\b',
     None, "'Either/Neither' take singular verbs ('is/was')."),

    # There is/are agreement
    (r'\bthere\s+is\s+(many|several|a\s+few|a\s+lot\s+of|lots\s+of|plenty\s+of|numerous|various)\b',
     None, "Use 'there are' with plural quantifiers."),
    (r'\bthere\s+is\s+(people|children|men|women|teeth|feet|mice|geese|police|cattle)\b',
     None, "Use 'there are' with these plural nouns."),
    (r'\bthere\s+(are|were)\s+(a|an)\b',
     None, "Use 'there is/was' with singular nouns."),

    # I/You/We/They + 3rd person verb form (common verbs)
    (r'\b(I|You|We|They)\s+(goes|does|has|says|makes|takes|comes|gives|knows|thinks|wants|needs|likes|loves|works|plays|talks|walks|runs|eats|drinks|reads|writes|lives|starts|stops|helps|calls|buys|sells|brings|teaches|learns|catches|fights|flies|grows|throws|draws|wears|steals|swims|sings|begins|rings|sinks|freezes|chooses|wakes|forgets|gets|hides|bites|rides|drives|speaks|breaks)\b',
     None, "Use the base verb form with 'I/You/We/They', not the 3rd person singular form."),

    # Me and X -> X and I
    (r'\bMe\s+and\s+(\w+)\b',
     None, "Use 'X and I' not 'Me and X' as a sentence subject."),

    # ── Possessive 's ─────────────────────────────────────────
    (r'\b(my|his|her|our|their|your)\s+(\w+)\s+(house|car|bag|book|phone|room|job|name|idea|cat|dog|son|daughter|wife|husband|sister|brother|mother|father|friend|teacher|boss|team|school|office|company|car|bike|office|home|website|blog|page|report|email|account|money|time|life|world|city|country|garden|kitchen|bedroom|office|apartment|flat|shop|store|restaurant|hotel|hospital|church|bank|park|street|road|village|town)\b',
     None,
     "Missing possessive 's — e.g. 'my friend's house' not 'my friend house'."),

    # ── Irregular Past Tense ──────────────────────────────────
    (r'\b(I|He|She|It|You|We|They)\s+goed\b',     r'\1 went',     "'goed' is not valid — past tense of 'go' is 'went'."),
    (r'\b(I|He|She|It|You|We|They)\s+comed\b',    r'\1 came',     "'comed' is not valid — past tense of 'come' is 'came'."),
    (r'\b(I|He|She|It|You|We|They)\s+runned\b',   r'\1 ran',      "'runned' is not valid — past tense of 'run' is 'ran'."),
    (r'\b(I|He|She|It|You|We|They)\s+buyed\b',    r'\1 bought',   "'buyed' is not valid — past tense of 'buy' is 'bought'."),
    (r'\b(I|He|She|It|You|We|They)\s+taked\b',    r'\1 took',     "'taked' is not valid — past tense of 'take' is 'took'."),
    (r'\b(I|He|She|It|You|We|They)\s+maked\b',    r'\1 made',     "'maked' is not valid — past tense of 'make' is 'made'."),
    (r'\b(I|He|She|It|You|We|They)\s+writed\b',   r'\1 wrote',    "'writed' is not valid — past tense of 'write' is 'wrote'."),
    (r'\b(I|He|She|It|You|We|They)\s+readed\b',   r'\1 read',     "'readed' is not valid — past tense of 'read' is 'read'."),
    (r'\b(I|He|She|It|You|We|They)\s+knowed\b',   r'\1 knew',     "'knowed' is not valid — past tense of 'know' is 'knew'."),
    (r'\b(I|He|She|It|You|We|They)\s+selled\b',   r'\1 sold',     "'selled' is not valid — past tense of 'sell' is 'sold'."),
    (r'\b(I|He|She|It|You|We|They)\s+telled\b',   r'\1 told',     "'telled' is not valid — past tense of 'tell' is 'told'."),
    (r'\b(I|He|She|It|You|We|They)\s+speaked\b',  r'\1 spoke',    "'speaked' is not valid — past tense of 'speak' is 'spoke'."),
    (r'\b(I|He|She|It|You|We|They)\s+breaked\b',  r'\1 broke',    "'breaked' is not valid — past tense of 'break' is 'broke'."),
    (r'\b(I|He|She|It|You|We|They)\s+teached\b',  r'\1 taught',   "'teached' is not valid — past tense of 'teach' is 'taught'."),
    (r'\b(I|He|She|It|You|We|They)\s+thinked\b',  r'\1 thought',  "'thinked' is not valid — past tense of 'think' is 'thought'."),
    (r'\b(I|He|She|It|You|We|They)\s+bringed\b',  r'\1 brought',  "'bringed' is not valid — past tense of 'bring' is 'brought'."),
    (r'\b(I|He|She|It|You|We|They)\s+catched\b',  r'\1 caught',   "'catched' is not valid — past tense of 'catch' is 'caught'."),
    (r'\b(I|He|She|It|You|We|They)\s+fighted\b',  r'\1 fought',   "'fighted' is not valid — past tense of 'fight' is 'fought'."),
    (r'\b(I|He|She|It|You|We|They)\s+flyed\b',    r'\1 flew',     "'flyed' is not valid — past tense of 'fly' is 'flew'."),
    (r'\b(I|He|She|It|You|We|They)\s+growed\b',   r'\1 grew',     "'growed' is not valid — past tense of 'grow' is 'grew'."),
    (r'\b(I|He|She|It|You|We|They)\s+throwed\b',  r'\1 threw',    "'throwed' is not valid — past tense of 'throw' is 'threw'."),
    (r'\b(I|He|She|It|You|We|They)\s+drowed\b',   r'\1 drew',     "'drowed' is not valid — past tense of 'draw' is 'drew'."),
    (r'\b(I|He|She|It|You|We|They)\s+weared\b',   r'\1 wore',     "'weared' is not valid — past tense of 'wear' is 'wore'."),
    (r'\b(I|He|She|It|You|We|They)\s+stealed\b',  r'\1 stole',    "'stealed' is not valid — past tense of 'steal' is 'stole'."),
    (r'\b(I|He|She|It|You|We|They)\s+swimmed\b',  r'\1 swam',     "'swimmed' is not valid — past tense of 'swim' is 'swam'."),
    (r'\b(I|He|She|It|You|We|They)\s+sanged\b',   r'\1 sang',     "'sanged' is not valid — past tense of 'sing' is 'sang'."),
    (r'\b(I|He|She|It|You|We|They)\s+dranked\b',  r'\1 drank',    "'dranked' is not valid — past tense of 'drink' is 'drank'."),
    (r'\b(I|He|She|It|You|We|They)\s+beginned\b', r'\1 began',    "'beginned' is not valid — past tense of 'begin' is 'began'."),
    (r'\b(I|He|She|It|You|We|They)\s+ringed\b',   r'\1 rang',     "'ringed' is not valid — past tense of 'ring' is 'rang'."),
    (r'\b(I|He|She|It|You|We|They)\s+sinked\b',   r'\1 sank',     "'sinked' is not valid — past tense of 'sink' is 'sank'."),
    (r'\b(I|He|She|It|You|We|They)\s+shranked\b', r'\1 shrank',   "'shranked' is not valid — past tense of 'shrink' is 'shrank'."),
    (r'\b(I|He|She|It|You|We|They)\s+freezed\b',  r'\1 froze',    "'freezed' is not valid — past tense of 'freeze' is 'froze'."),
    (r'\b(I|He|She|It|You|We|They)\s+choosed\b',  r'\1 chose',    "'choosed' is not valid — past tense of 'choose' is 'chose'."),
    (r'\b(I|He|She|It|You|We|They)\s+waked\b',    r'\1 woke',     "'waked' is not valid — past tense of 'wake' is 'woke'."),
    (r'\b(I|He|She|It|You|We|They)\s+forgeted\b', r'\1 forgot',   "'forgeted' is not valid — past tense of 'forget' is 'forgot'."),
    (r'\b(I|He|She|It|You|We|They)\s+geted\b',    r'\1 got',      "'geted' is not valid — past tense of 'get' is 'got'."),
    (r'\b(I|He|She|It|You|We|They)\s+hided\b',    r'\1 hid',      "'hided' is not valid — past tense of 'hide' is 'hid'."),

    # ── Past Participle ───────────────────────────────────────
    (r'\b(has|have|had)\s+went\b',     r'\1 gone',     "Use past participle: 'gone'."),
    (r'\b(has|have|had)\s+saw\b',      r'\1 seen',     "Use past participle: 'seen'."),
    (r'\b(has|have|had)\s+took\b',     r'\1 taken',    "Use past participle: 'taken'."),
    (r'\b(has|have|had)\s+gave\b',     r'\1 given',    "Use past participle: 'given'."),
    (r'\b(has|have|had)\s+wrote\b',    r'\1 written',  "Use past participle: 'written'."),
    (r'\b(has|have|had)\s+ate\b',      r'\1 eaten',    "Use past participle: 'eaten'."),
    (r'\b(has|have|had)\s+ran\b',      r'\1 run',      "Use past participle: 'run'."),
    (r'\b(has|have|had)\s+drove\b',    r'\1 driven',   "Use past participle: 'driven'."),
    (r'\b(has|have|had)\s+spoke\b',    r'\1 spoken',   "Use past participle: 'spoken'."),
    (r'\b(has|have|had)\s+broke\b',    r'\1 broken',   "Use past participle: 'broken'."),
    (r'\b(has|have|had)\s+wore\b',     r'\1 worn',     "Use past participle: 'worn'."),
    (r'\b(has|have|had)\s+stole\b',    r'\1 stolen',   "Use past participle: 'stolen'."),
    (r'\b(has|have|had)\s+swam\b',     r'\1 swum',     "Use past participle: 'swum'."),
    (r'\b(has|have|had)\s+sang\b',     r'\1 sung',     "Use past participle: 'sung'."),
    (r'\b(has|have|had)\s+drank\b',    r'\1 drunk',    "Use past participle: 'drunk'."),
    (r'\b(has|have|had)\s+began\b',    r'\1 begun',    "Use past participle: 'begun'."),
    (r'\b(has|have|had)\s+rang\b',     r'\1 rung',     "Use past participle: 'rung'."),
    (r'\b(has|have|had)\s+sank\b',     r'\1 sunk',     "Use past participle: 'sunk'."),
    (r'\b(has|have|had)\s+froze\b',    r'\1 frozen',   "Use past participle: 'frozen'."),
    (r'\b(has|have|had)\s+chose\b',    r'\1 chosen',   "Use past participle: 'chosen'."),
    (r'\b(has|have|had)\s+woke\b',     r'\1 woken',    "Use past participle: 'woken'."),
    (r'\b(has|have|had)\s+forgot\b',   r'\1 forgotten',"Use past participle: 'forgotten'."),
    (r'\b(has|have|had)\s+hid\b',      r'\1 hidden',   "Use past participle: 'hidden'."),
    (r'\b(has|have|had)\s+bit\b',      r'\1 bitten',   "Use past participle: 'bitten'."),
    (r'\b(has|have|had)\s+rode\b',     r'\1 ridden',   "Use past participle: 'ridden'."),
    (r'\b(has|have|had)\s+flew\b',     r'\1 flown',    "Use past participle: 'flown'."),
    (r'\b(has|have|had)\s+grew\b',     r'\1 grown',    "Use past participle: 'grown'."),
    (r'\b(has|have|had)\s+threw\b',    r'\1 thrown',   "Use past participle: 'thrown'."),
    (r'\b(has|have|had)\s+drew\b',     r'\1 drawn',    "Use past participle: 'drawn'."),

    # ── Tense Consistency ──────────────────────────────────────
    (r'\b(buys|goes|does|has|says|makes|takes|comes|gives|eats|drinks|reads|writes|plays|works|talks|walks|runs|swims|sings|dances|watches|listens|studies|sleeps|sits|stands|teaches|learns|catches|flies|grows|throws|draws|wears|steals|brings|sells|tells|lives|starts|stops|helps|calls|knows|thinks|wants|needs|likes|loves|hates|looks|seems|feels|hears|sees|keeps|finds|holds|puts|gets|begins|becomes|happens|arrives|leaves|returns|changes|stays|follows|belongs|contains|remains|appears|offers|provides|receives|uses|requires|prefers|prepares|reports|believes|considers|describes|develops|discovers|discusses|expects|explains|improves|includes|introduces|mentions|observes|performs|presents|produces|promises|protects|recognizes|recommends|records|reflects|refuses|remembers|reminds|represents|reveals|shares|signs|solves|suggests|supports|survives|threatens|touches|trades|trains|treats|trusts|understands|visits|waits|wins|wishes|wonders)\b(?:\s+\w+){0,6}\s+yesterday\b',
     None, "Use past tense (not present) with 'yesterday'."),
    (r'\b(buys|goes|does|has|says|makes|takes|comes|gives|eats|drinks|reads|writes|plays|works|talks|walks|runs|swims|sings|dances|watches|listens|studies|sleeps|sits|stands|teaches|learns|catches|flies|grows|throws|draws|wears|steals|brings|sells|tells|lives|starts|stops|helps|calls|knows|thinks|wants|needs|likes|loves|hates|looks|seems|feels|hears|sees|keeps|finds|holds|puts|gets|begins|becomes|happens|arrives|leaves|returns|changes|stays|follows|belongs|contains|remains|appears|offers|provides|receives|uses|requires|prefers|prepares|reports|believes|considers|describes|develops|discovers|discusses|expects|explains|improves|includes|introduces|mentions|observes|performs|presents|produces|promises|protects|recognizes|recommends|records|reflects|refuses|remembers|reminds|represents|reveals|shares|signs|solves|suggests|supports|survives|threatens|touches|trades|trains|treats|trusts|understands|visits|waits|wins|wishes|wonders)\b(?:\s+\w+){0,6}\s+last\s+(night|week|month|year|decade|century|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|weekend|summer|winter|spring|autumn|fall|term|semester|session|season|quarter|hour|minute)\b',
     None, "Use past tense (not present) with 'last ...'."),
    (r'\b(buys|goes|does|has|says|makes|takes|comes|gives|eats|drinks|reads|writes|plays|works|talks|walks|runs|swims|sings|dances|watches|listens|studies|sleeps|sits|stands|teaches|learns|catches|flies|grows|throws|draws|wears|steals|brings|sells|tells|lives|starts|stops|helps|calls|knows|thinks|wants|needs|likes|loves|hates|looks|seems|feels|hears|sees|keeps|finds|holds|puts|gets|begins|becomes|happens|arrives|leaves|returns|changes|stays|follows|belongs|contains|remains|appears|offers|provides|receives|uses|requires|prefers|prepares|reports|believes|considers|describes|develops|discovers|discusses|expects|explains|improves|includes|introduces|mentions|observes|performs|presents|produces|promises|protects|recognizes|recommends|records|reflects|refuses|remembers|reminds|represents|reveals|shares|signs|solves|suggests|supports|survives|threatens|touches|trades|trains|treats|trusts|understands|visits|waits|wins|wishes|wonders)\b(?:\s+\w+){0,6}\s+\w+\s+ago\b',
     None, "Use past tense (not present) with 'ago'."),
    (r'\b(eat|drink|go|come|do|have|make|take|write|read|speak|break|swim|sing|run|sit|stand|sleep|wake|begin|ring|sink|shrink|drive|ride|fly|grow|throw|draw|wear|steal|hide|bite|choose|freeze|forget|get|give|see|know|think|bring|catch|fight|teach|sell|tell|build|send|spend|leave|meet|lose|mean|pay|understand|buy|say)\b(?:\s+\w+){0,6}\s+yesterday\b',
     None, "Use past tense (not present) with 'yesterday'."),

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
    (r'\b(can|must|should|could|would|may|might)\s+was\b',    r'\1 be',    "Use base verb after a modal."),
    (r'\b(can|must|should|could|would|may|might)\s+were\b',   r'\1 be',    "Use base verb after a modal."),

    # Modal + to (incorrect)
    (r'\b(must|should|could|would|may|might)\s+to\s+(\w+)\b', r'\1 \2', "Do not use 'to' after a modal verb."),
    (r'\bcan\s+to\s+(\w+)\b',  r'can \1',     "Do not use 'to' after 'can'."),

    # Auxiliary + to (remove extra "to")
    (r'\b(don\'t|doesn\'t|didn\'t|won\'t|can\'t|couldn\'t|wouldn\'t|shouldn\'t|mustn\'t|shan\'t|mightn\'t|needn\'t|daren\'t)\s+to\s+(\w+)\b',
     r'\1 \2', "Do not use 'to' after a negated auxiliary."),
    (r'\b(do|does|did)\s+not\s+to\s+(\w+)\b',
     r'\1 not \2', "Do not use 'to' after 'do/does/did not'."),

    # Verb form after negated auxiliaries
    (r'\b(don\'t|doesn\'t|didn\'t)\s+goes\b',  r'\1 go',    "Use base verb after 'don't/doesn't/didn't'."),
    (r'\b(?:don\'t|doesn\'t|didn\'t)\s+(does|has|says|makes|takes|comes|gives|knows|eats|drinks|reads|writes|plays|works|talks|walks|runs|swims|sings|teaches|learns|catches|flies|grows|throws|draws|wears|steals|brings|sells|tells|lives|starts|stops|helps|calls|thinks|wants|needs|likes|loves|hates|looks|seems|feels|hears|sees|keeps|finds|holds|puts|gets|begins|happens|arrives|leaves|returns|changes|stays|follows|belongs|appears|offers|provides|receives|uses|requires|waits|wins|wishes|prefers|prepares|reports|believes|considers|describes|develops|discovers|discusses|expects|explains|includes|introduces|mentions|observes|performs|presents|produces|promises|protects|recognizes|recommends|records|reflects|refuses|remembers|reminds|represents|reveals|shares|signs|solves|suggests|supports|survives|threatens|touches|trades|trains|treats|trusts|understands|visits)\b',
     None, "Use base verb form after 'don't/doesn't/didn't'."),

    # Need to / Dare to
    (r'\bneed\s+(go|come|do|be|make|take|have|see|get|give|find|tell|ask|try|leave|work|play|talk|walk|eat|drink|read|write|buy|sell|bring|teach|learn|start|stop|help|call|put|keep|let|begin|show|hear|think|know|want|look|seem|feel|say|use|pay|run|sit|stand|sleep|swim|sing|draw|fly|grow|throw|catch|fight|wear|steal|hide|forget|choose|freeze|wake|ride|drive|speak|break)\b',
     None, "Use 'need to' + base verb (e.g. 'need to go' not 'need go')."),
    (r'\bdare\s+(go|come|do|be|make|take|have|see|get|say|try|ask|tell|speak|look|think|believe|hope|dream|enter|leave|stay|live|work|play)\b',
     None, "Use 'dare to' + base verb."),

    # ── Uncountable Nouns ─────────────────────────────────────
    (r'\bmany\s+informations\b', "much information", "'information' is uncountable — use 'much information'."),
    (r'\bmany\s+advices\b',      "much advice",      "'advice' is uncountable — use 'much advice'."),
    (r'\bmany\s+luggages\b',     "much luggage",     "'luggage' is uncountable — use 'much luggage'."),
    (r'\bmany\s+furnitures\b',   "much furniture",   "'furniture' is uncountable — use 'much furniture'."),
    (r'\bmany\s+waters\b',       "much water",       "'water' is uncountable — use 'much water'."),
    (r'\bmany\s+knowledges\b',   "much knowledge",   "'knowledge' is uncountable — use 'much knowledge'."),
    (r'\bmany\s+equipments\b',   "much equipment",   "'equipment' is uncountable — use 'much equipment'."),
    (r'\bmany\s+homeworks\b',    "much homework",    "'homework' is uncountable — use 'much homework'."),
    (r'\bmany\s+researches\b',   "much research",    "'research' is uncountable — use 'much research'."),
    (r'\bmany\s+progresses\b',   "much progress",    "'progress' is uncountable — use 'much progress'."),
    (r'\bmany\s+informations?\b', "information",     "'information' has no plural form."),
    (r'\ban?\s+advices?\b',      "advice",           "'advice' has no plural form."),

    # Much + countable noun
    (r'\bmuch\s+(books|people|students|cars|houses|chairs|tables|days|weeks|years|hours|minutes|dollars|euros|children|men|women|animals|trees|flowers|bottles|cups|plates|shirts|shoes|words|pages|chapters|lessons|pounds|euros|dollars)\b',
     None, "Use 'many' with countable nouns."),

    # ── Articles (a/an) ──────────────────────────────────────
    (r'\ba\s+(hour|honest|honour|heir|honor|heirloom|herb)\b', r'an \1', "Use 'an' before silent-h words."),
    (r'\ban\s+(university|union|unique|unit|usual|user|use|uniform|unicorn|unilateral|universal|unanimous|European|euphemism|eulogy|euthanasia)\b', r'a \1', "Use 'a' before words starting with a 'y' sound."),

    # ── Prepositions ──────────────────────────────────────────
    (r'\baccording\s+with\b',   "according to",  "Use 'according to'."),
    (r'\bdepend\s+of\b',        "depend on",     "Use 'depend on'."),
    (r'\bfocus\s+in\b',         "focus on",      "Use 'focus on'."),
    (r'\binterested\s+on\b',    "interested in", "Use 'interested in'."),
    (r'\bsimilar\s+with\b',     "similar to",    "Use 'similar to'."),
    (r'\bmarried\s+with\b',     "married to",    "Use 'married to'."),
    (r'\barrived\s+to\b',       "arrived at",    "Use 'arrived at'."),
    (r'\blisten\s+me\b',        "listen to me",  "Use 'listen to'."),
    (r'\bdifferent\s+than\b',   None,            "Use 'different from' in formal English."),
    (r'\bbored\s+of\b',         "bored with",    "Use 'bored with'."),
    (r'\bdiscuss\s+about\b',    "discuss",       "Use 'discuss' directly (no preposition needed)."),
    (r'\bcommented\s+about\b',  None,            "Use 'commented on', not 'commented about'."),
    (r'\bpayed\b',              "paid",          "'payed' is incorrect — past tense of 'pay' is 'paid'."),

    # ── Double Negative ───────────────────────────────────────
    (r'\b(?:don\'t|doesn\'t|didn\'t)\s+\w+\s+nothing\b',  None, "Avoid double negatives — use 'anything' instead of 'nothing'."),
    (r'\b(?:can\'t|couldn\'t|wouldn\'t|shouldn\'t|won\'t)\s+\w+\s+nothing\b',  None, "Avoid double negatives — use 'anything' instead of 'nothing'."),
    (r'\b(?:don\'t|doesn\'t|didn\'t)\s+\w+\s+nobody\b', None, "Avoid double negatives — use 'anybody' instead of 'nobody'."),
    (r'\b(?:don\'t|doesn\'t|didn\'t)\s+\w+\s+nowhere\b', None, "Avoid double negatives — use 'anywhere' instead of 'nowhere'."),
    (r'\b(?:can\'t|couldn\'t|wouldn\'t|shouldn\'t|won\'t)\s+\w+\s+never\b', None, "Avoid double negatives."),
    (r'\b(hardly|scarcely|barely)\s+\w+\s+(no|none|nothing|nobody|nowhere|never)\b', None, "Avoid double negatives — 'hardly/scarcely/barely' are already negative."),

    # ── Homophones ────────────────────────────────────────────
    # Your vs You're
    (r'\bYour\s+(welcome|right|wrong|crazy|funny|serious|kidding|lying|going|doing|coming|leaving|talking|saying|telling|mistaken|late|early|next|wonderful|amazing|terrible)\b',
     None, "Use 'You're' (you are) not 'Your' (possessive)."),
    (r'\byou\'re\s+(house|car|book|phone|idea|job|name|friend|family|team|office|room|life|money|time|world|wife|husband|daughter|son|mother|father|sister|brother|boss|teacher|company)\b',
     None, "Use 'Your' (possessive) not 'You're' (you are)."),

    # Its vs It's
    (r"\bIt's\s+(house|car|book|phone|idea|job|name|friend|family|team|office|room|life|money|color|size|shape|smell|taste|sound|owner|origin|purpose)\b",
     None, "Use 'Its' (possessive) not 'It's' (it is)."),
    (r"\bits\s+(not|a|an|the|very|really|quite|just|also|always|never|still|already|even|only|actually|certainly|definitely|probably|possibly)\b",
     None, "Use 'It's' (it is) not 'Its' (possessive)."),

    # Their vs There vs They're
    (r'\bThere\s+(car|house|book|phone|idea|job|name|friend|family|team|office|room|life|money|time|world|kids|children|parents|dogs|cats|clothes|shoes|bags|keys|phones|computers)\b',
     None, "Use 'Their' (possessive) not 'There'."),
    (r'\bTheir\s+(is|are|was|were|has|have|had|will|can|could|should|would|may|might|do|does|did|must|shall)\b',
     None, "Use 'There' (existential) or 'They're' (they are) not 'Their'."),
    (r"\bThey're\s+(car|house|book|phone|idea|job|name|friend|family|team|office|room|house|dog|cat)\b",
     None, "Use 'Their' (possessive) not 'They're' (they are)."),

    # Then vs Than
    (r'\b(more|less|better|worse|bigger|smaller|faster|slower|older|younger|richer|poorer|higher|lower|greater|lesser|easier|harder|sooner|later|hotter|colder|warmer|earlier|further|farther)\s+then\b',
     None, "Use 'than' for comparisons, not 'then'."),

    # To vs Too vs Two
    (r'\btoo\s+(the|a|an|my|your|his|her|our|their|this|that|these|those)\b',
     None, "Use 'to' (preposition) not 'too' (meaning also/excessively)."),
    (r'\btwo\s+(the|a|an|my|your|his|her|our|their|this|that|these|those)\b',
     None, "Use 'to' (preposition) not 'two' (number 2)."),

    # Loose vs Lose
    (r'\bloose\s+(weight|money|time|control|sight|touch|hope|interest|patience|focus|balance|confidence|faith|cool|mind|temper|track|ground)\b',
     None, "Use 'lose' (misplace/not win) not 'loose' (not tight)."),

    # Whose vs Who's
    (r"\bWhose\s+(is|are|was|were|has|have|had|going|coming|doing|making|taking|saying|telling|asking|talking|speaking|walking|running|working)\b",
     None, "Use 'Who's' (who is) not 'Whose' (possessive)."),
    (r"\bWho's\s+(car|house|book|phone|idea|job|name|friend|family|team|office|room|money|life|time|world|turn|fault)\b",
     None, "Use 'Whose' (possessive) not 'Who's' (who is)."),

    # ── Common Error Patterns ─────────────────────────────────
    # Could/should/would of
    (r'\b(could|should|would)\s+of\b',  r'\1 have',  "Use 'have' not 'of' after modals."),
    (r'\b(might|may)\s+of\b',           r'\1 have',  "Use 'have' not 'of' after modals."),
    (r'\b(must)\s+of\b',                "must have", "Use 'must have' not 'must of'."),

    # Suppose to -> supposed to
    (r'\bsuppose\s+to\b',     "supposed to", "Use 'supposed to' (past participle)."),
    # Use to -> used to
    (r'\b(He|She|It|I|You|We|They)\s+use\s+to\b', r'\1 used to', "Use 'used to' for past habits."),

    # Common misspellings
    (r'\balot\b',             "a lot",       "'alot' is not a word — use 'a lot' (two words)."),
    (r'\beachother\b',        "each other",  "Use 'each other' (two words)."),
    (r'\binfact\b',           "in fact",     "Use 'in fact' (two words)."),
    (r'\bincharge\b',         "in charge",   "Use 'in charge' (two words)."),
    (r'\bapart\s+of\b',       None,          "Use 'a part of' or 'apart from'."),

    # ── Comparatives / Superlatives ───────────────────────────
    (r'\bmore\s+(better|worse|bigger|smaller|older|younger|faster|slower|richer|poorer|higher|lower|greater|lesser|hotter|colder|warmer|cooler|darker|brighter|stronger|weaker|taller|shorter|longer|wider|deeper|earlier|later|simpler|happier|prettier|easier|harder|busier|funnier|angrier|friendlier|heavier|healthier|luckier|nicer|sadder|tastier|wealthier|calmer|quieter|cheaper|cleaner|clearer|closer|fresher|fuller|gentler|kinder|larger|looser|narrower|neater|newer|older|plainer|politer|quieter|rarer|safer|sharper|shorter|smarter|softer|steeper|stricter|stronger|sweeter|taller|thicker|thinner|tighter|tougher|warmer|weaker|wider|wiser)\b',
     None, "Double comparative — use the comparative form directly (e.g. 'better' not 'more better')."),
    (r'\bmost\s+(best|worst|biggest|smallest|oldest|youngest|fastest|slowest|richest|poorest|highest|lowest|greatest|least|hottest|coldest|warmest|darkest|brightest|strongest|weakest|tallest|shortest|longest|widest|deepest|earliest|latest|simplest|happiest|prettiest|easiest|hardest|busiest|funniest|angriest|friendliest|heaviest|healthiest|luckiest|nicest|saddest|tastiest|wealthiest|calmest|quietest|cheapest|cleanest|clearest|closest|freshest|fullest|gentlest|kindest|largest|loosest|narrowest|neatest|newest|plainest|politest|rarest|safest|sharpest|shortest|smartest|softest|steepest|strictest|strongest|sweetest|thickest|thinnest|tightest|toughest)\b',
     None, "Double superlative — use the superlative form directly (e.g. 'best' not 'most best')."),

    # ── Subjunctive Mood ─────────────────────────────────────
    (r'\bif\s+(I|he|she|it)\s+was\s+(you|here|there|taller|faster|smarter|richer|older|younger|better|worse|bigger|smaller|stronger|weaker|faster|slower|nicer|kinder|richer|poorer|braver|calmer|happier|luckier|healthier|wealthier)\b',
     None, "Use 'were' in the subjunctive mood (e.g. 'if I were you')."),

    # ── Less vs Fewer ─────────────────────────────────────────
    (r'\bless\s+(people|children|men|women|students|workers|members|participants|customers|users|readers|viewers|listeners|patients|passengers|drivers|residents|citizens|families|animals|plants|trees|flowers|birds|fish|insects|days|hours|minutes|seconds|weeks|years|months|times|occasions|instances|cases|examples|reasons|factors|issues|problems|questions|answers|items|products|goods|services|words|pages|books|articles|stories|reports|emails|messages|letters|notes|files|documents|images|photos|videos|songs|movies|shows|games|jobs|tasks|projects|goals|ideas|thoughts|plans|decisions|chances|opportunities|choices|options|alternatives|countries|cities|towns|villages|shops|restaurants|hotels|schools|hospitals|banks|parks|roads|streets)\b',
     None, "Use 'fewer' with countable plural nouns."),

    # ── Gerund / Infinitive ───────────────────────────────────
    (r'\b(enjoy|avoid|suggest|recommend|mind|keep|consider|imagine|practice|finish|quit|resist|miss|appreciate|delay|postpone|deny|admit|regret|involve|mention|recall|report|risk|stop)\s+to\b',
     None, "Use the gerund (-ing form) after this verb, not the infinitive."),
    (r'\b(want|hope|expect|decide|plan|need|promise|refuse|manage|offer|agree|fail|tend|pretend|threaten|seem|appear|claim|learn|afford|arrange|choose|deserve|prepare|pretend|struggle|swear|volunteer|wait)\s+(going|coming|doing|making|taking|having|being|seeing|eating|drinking|running|walking|talking|telling|swimming|playing|working|studying|reading|writing|listening|speaking|sleeping|getting|saying|staying|living|giving|finding|keeping|starting|stopping|helping|calling|setting|buying|selling|building|watching|paying|asking|answering|sending|receiving|showing|meeting|leaving|arriving|returning|thinking|feeling|looking|trying|putting|breaking|bringing|teaching|learning)\b',
     None, "Use 'to' + base verb (infinitive) after this verb, not the gerund."),

    # ── Capitalization ────────────────────────────────────────
    (r'(?-i:\bi\b)', "I", "The pronoun 'I' must always be capitalized."),
    (r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b',
     None, "Days of the week must be capitalized."),
    (r'\b(january|february|march|april|may|june|july|august|september|october|november|december)\b',
     None, "Month names must be capitalized."),

    # ── Punctuation ───────────────────────────────────────────
    (r'\s+([,\.!?])', r'\1', "Remove space before punctuation."),
    (r'([\.!?])(\w)', r'\1 \2', "Add space after sentence-ending punctuation."),
    (r'  +', ' ', "Replace multiple spaces with a single space."),
]
