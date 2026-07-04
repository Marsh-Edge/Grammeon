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
    (r'\bIm\b',      "I'm",      "Missing apostrophe in 'I'm'."),
    (r'\biam\b',     "I am",     "'iam' is not a word — use 'I am' (two words)."),

    # ── Verb Form After 'to' (Infinitive) ──────────────────────
    (r'\bto\s+has\b',    "to have",   "Use base verb form after 'to'."),
    (r'\bto\s+does\b',   "to do",     "Use base verb form after 'to'."),
    (r'\bto\s+goes\b',   "to go",     "Use base verb form after 'to'."),
    (r'\bto\s+had\b',    "to have",   "Use base verb form after 'to'."),
    (r'\bto\s+did\b',    "to do",     "Use base verb form after 'to'."),
    (r'\bto\s+(went|said|made|took|came|gave|knew|thought|bought|sold|taught|caught|fought|told|spoke|broke|woke|drove|rode|wrote|sang|drank|swam|ran|ate|sat|stood|built|sent|spent|left|met|lost|meant|paid|forgot|hid|bit|chose|froze|wore|stole|flew|grew|threw|drew|understood|slept|kept|felt|hurt|hit|cost|let|put|set|cut|shut|spread|cast|burst|bent|bled|blew|bred|dealt|dug|fed|hung|held|knelt|laid|led|lent|lit|sank|shrank|slid|smelt|spat|split|stuck|struck|strove|swept|swore|swung|tore|won|wound|withdrew)\b',
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

    # He/She/It + base verb (missing 3rd person -s)
    (r'\b(He|She|It)\s+go\b',       r'\1 goes',    "Use 'goes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+come\b',     r'\1 comes',   "Use 'comes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+make\b',     r'\1 makes',   "Use 'makes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+take\b',     r'\1 takes',   "Use 'takes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+eat\b',      r'\1 eats',    "Use 'eats' with 'He/She/It'."),
    (r'\b(He|She|It)\s+drink\b',    r'\1 drinks',  "Use 'drinks' with 'He/She/It'."),
    (r'\b(He|She|It)\s+read\b',     r'\1 reads',   "Use 'reads' with 'He/She/It'."),
    (r'\b(He|She|It)\s+write\b',    r'\1 writes',  "Use 'writes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+speak\b',    r'\1 speaks',  "Use 'speaks' with 'He/She/It'."),
    (r'\b(He|She|It)\s+swim\b',     r'\1 swims',   "Use 'swims' with 'He/She/It'."),
    (r'\b(He|She|It)\s+sing\b',     r'\1 sings',   "Use 'sings' with 'He/She/It'."),
    (r'\b(He|She|It)\s+run\b',      r'\1 runs',    "Use 'runs' with 'He/She/It'."),
    (r'\b(He|She|It)\s+play\b',     r'\1 plays',   "Use 'plays' with 'He/She/It'."),
    (r'\b(He|She|It)\s+work\b',     r'\1 works',   "Use 'works' with 'He/She/It'."),
    (r'\b(He|She|It)\s+walk\b',     r'\1 walks',   "Use 'walks' with 'He/She/It'."),
    (r'\b(He|She|It)\s+talk\b',     r'\1 talks',   "Use 'talks' with 'He/She/It'."),
    (r'\b(He|She|It)\s+sit\b',      r'\1 sits',    "Use 'sits' with 'He/She/It'."),
    (r'\b(He|She|It)\s+stand\b',    r'\1 stands',  "Use 'stands' with 'He/She/It'."),
    (r'\b(He|She|It)\s+sleep\b',    r'\1 sleeps',  "Use 'sleeps' with 'He/She/It'."),
    (r'\b(He|She|It)\s+wake\b',     r'\1 wakes',   "Use 'wakes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+live\b',     r'\1 lives',   "Use 'lives' with 'He/She/It'."),
    (r'\b(He|She|It)\s+start\b',    r'\1 starts',  "Use 'starts' with 'He/She/It'."),
    (r'\b(He|She|It)\s+stop\b',     r'\1 stops',   "Use 'stops' with 'He/She/It'."),
    (r'\b(He|She|It)\s+help\b',     r'\1 helps',   "Use 'helps' with 'He/She/It'."),
    (r'\b(He|She|It)\s+call\b',     r'\1 calls',   "Use 'calls' with 'He/She/It'."),
    (r'\b(He|She|It)\s+know\b',     r'\1 knows',   "Use 'knows' with 'He/She/It'."),
    (r'\b(He|She|It)\s+think\b',    r'\1 thinks',  "Use 'thinks' with 'He/She/It'."),
    (r'\b(He|She|It)\s+want\b',     r'\1 wants',   "Use 'wants' with 'He/She/It'."),
    (r'\b(He|She|It)\s+need\b',     r'\1 needs',   "Use 'needs' with 'He/She/It'."),
    (r'\b(He|She|It)\s+like\b',     r'\1 likes',   "Use 'likes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+love\b',     r'\1 loves',   "Use 'loves' with 'He/She/It'."),
    (r'\b(He|She|It)\s+hate\b',     r'\1 hates',   "Use 'hates' with 'He/She/It'."),
    (r'\b(He|She|It)\s+feel\b',     r'\1 feels',   "Use 'feels' with 'He/She/It'."),
    (r'\b(He|She|It)\s+hear\b',     r'\1 hears',   "Use 'hears' with 'He/She/It'."),
    (r'\b(He|She|It)\s+say\b',      r'\1 says',    "Use 'says' with 'He/She/It'."),
    (r'\b(He|She|It)\s+see\b',      r'\1 sees',    "Use 'sees' with 'He/She/It'."),
    (r'\b(He|She|It)\s+keep\b',     r'\1 keeps',   "Use 'keeps' with 'He/She/It'."),
    (r'\b(He|She|It)\s+find\b',     r'\1 finds',   "Use 'finds' with 'He/She/It'."),
    (r'\b(He|She|It)\s+hold\b',     r'\1 holds',   "Use 'holds' with 'He/She/It'."),
    (r'\b(He|She|It)\s+put\b',      r'\1 puts',    "Use 'puts' with 'He/She/It'."),
    (r'\b(He|She|It)\s+get\b',      r'\1 gets',    "Use 'gets' with 'He/She/It'."),
    (r'\b(He|She|It)\s+begin\b',    r'\1 begins',  "Use 'begins' with 'He/She/It'."),
    (r'\b(He|She|It)\s+bring\b',    r'\1 brings',  "Use 'brings' with 'He/She/It'."),
    (r'\b(He|She|It)\s+buy\b',      r'\1 buys',    "Use 'buys' with 'He/She/It'."),
    (r'\b(He|She|It)\s+sell\b',     r'\1 sells',   "Use 'sells' with 'He/She/It'."),
    (r'\b(He|She|It)\s+learn\b',    r'\1 learns',  "Use 'learns' with 'He/She/It'."),
    (r'\b(He|She|It)\s+grow\b',     r'\1 grows',   "Use 'grows' with 'He/She/It'."),
    (r'\b(He|She|It)\s+throw\b',    r'\1 throws',  "Use 'throws' with 'He/She/It'."),
    (r'\b(He|She|It)\s+draw\b',     r'\1 draws',   "Use 'draws' with 'He/She/It'."),
    (r'\b(He|She|It)\s+wear\b',     r'\1 wears',   "Use 'wears' with 'He/She/It'."),
    (r'\b(He|She|It)\s+steal\b',    r'\1 steals',  "Use 'steals' with 'He/She/It'."),
    (r'\b(He|She|It)\s+tell\b',     r'\1 tells',   "Use 'tells' with 'He/She/It'."),
    (r'\b(He|She|It)\s+pay\b',      r'\1 pays',    "Use 'pays' with 'He/She/It'."),
    (r'\b(He|She|It)\s+leave\b',    r'\1 leaves',  "Use 'leaves' with 'He/She/It'."),
    (r'\b(He|She|It)\s+meet\b',     r'\1 meets',   "Use 'meets' with 'He/She/It'."),
    (r'\b(He|She|It)\s+send\b',     r'\1 sends',   "Use 'sends' with 'He/She/It'."),
    (r'\b(He|She|It)\s+spend\b',    r'\1 spends',  "Use 'spends' with 'He/She/It'."),
    (r'\b(He|She|It)\s+build\b',    r'\1 builds',  "Use 'builds' with 'He/She/It'."),
    (r'\b(He|She|It)\s+break\b',    r'\1 breaks',  "Use 'breaks' with 'He/She/It'."),
    (r'\b(He|She|It)\s+drive\b',    r'\1 drives',  "Use 'drives' with 'He/She/It'."),
    (r'\b(He|She|It)\s+ride\b',     r'\1 rides',   "Use 'rides' with 'He/She/It'."),
    (r'\b(He|She|It)\s+choose\b',   r'\1 chooses', "Use 'chooses' with 'He/She/It'."),
    (r'\b(He|She|It)\s+forget\b',   r'\1 forgets', "Use 'forgets' with 'He/She/It'."),
    (r'\b(He|She|It)\s+hide\b',     r'\1 hides',   "Use 'hides' with 'He/She/It'."),
    (r'\b(He|She|It)\s+bite\b',     r'\1 bites',   "Use 'bites' with 'He/She/It'."),
    (r'\b(He|She|It)\s+freeze\b',   r'\1 freezes', "Use 'freezes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+teach\b',    r'\1 teaches', "Use 'teaches' with 'He/She/It'."),
    (r'\b(He|She|It)\s+catch\b',    r'\1 catches', "Use 'catches' with 'He/She/It'."),
    (r'\b(He|She|It)\s+fly\b',      r'\1 flies',   "Use 'flies' with 'He/She/It'."),
    (r'\b(He|She|It)\s+study\b',    r'\1 studies', "Use 'studies' with 'He/She/It'."),
    (r'\b(He|She|It)\s+try\b',      r'\1 tries',   "Use 'tries' with 'He/She/It'."),
    (r'\b(He|She|It)\s+carry\b',    r'\1 carries', "Use 'carries' with 'He/She/It'."),
    (r'\b(He|She|It)\s+marry\b',    r'\1 marries', "Use 'marries' with 'He/She/It'."),
    (r'\b(He|She|It)\s+worry\b',    r'\1 worries', "Use 'worries' with 'He/She/It'."),
    (r'\b(He|She|It)\s+watch\b',    r'\1 watches', "Use 'watches' with 'He/She/It'."),
    (r'\b(He|She|It)\s+wash\b',     r'\1 washes',  "Use 'washes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+teach\b',    r'\1 teaches', "Use 'teaches' with 'He/She/It'."),
    (r'\b(He|She|It)\s+cross\b',    r'\1 crosses', "Use 'crosses' with 'He/She/It'."),
    (r'\b(He|She|It)\s+fix\b',      r'\1 fixes',   "Use 'fixes' with 'He/She/It'."),
    (r'\b(He|She|It)\s+go\s+to\b',  r'\1 goes to', "Use 'goes to' with 'He/She/It'."),

    # Subject doubling (redundant pronoun)
    (r'\bMy\s+(names|name)\s+it\b',          None, "Remove 'it' — 'My name is' is correct, not 'My name it is'."),
    (r'\bMy\s+names\s+(is|was)\b',          r'My name \1', "'My names' is plural — use 'My name' when referring to your own name."),
    (r'\bMy\s+names\b',                     None,           "Use 'my name' (singular) when referring to your name."),
    (r'\bMy\s+name\s+(?!is\b|was\b|it\b)\s*([A-Z][a-zA-Z]+)\b',
     None, "Use 'My name is ...' — missing verb 'is'."),
    (r'\b(\w+)\s+(he|she|it)\s+(is|was|has|does)\b',
     None, "Remove the extra pronoun — 'Subject + he/she/it' is redundant."),

    # Copula (am/is/are/was/were) + base verb → should be -ing
    (r'\b(am|is|are|was|were)\s+(go|come|do|make|take|have|eat|drink|read|write|speak|swim|sing|run|work|play|study|leave|arrive|sleep|talk|walk|sit|stand|drive|ride|fly|grow|throw|draw|bring|buy|sell|teach|learn|start|stop|help|call|tell|say|pay|live|die|try|stay|keep|find|hold|put|get|begin|break|catch|choose|forget|hide|bite|freeze|wash|watch|fix|cross|carry|marry|worry|enjoy|love|hate|like|want|need|know|think|believe|hope|expect|plan|promise|refuse|agree|decide|forbid|allow|let|make|hear|see|watch)\b',
     None, "Use the -ing form after 'be' verbs (e.g. 'I am going' not 'I am go')."),

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
    (r'\bthere\s+is\s+(people|children|men|women|teeth|feet|mice|geese|police|cattle|cars|dogs|cats|books|houses|trees|flowers|birds|fish|insects|animals|students|teachers|workers|doctors|nurses|engineers|lawyers|writers|artists|players|fans|members|friends|relatives|neighbors|parents|customers|clients|patients|passengers|drivers|riders|guests|visitors|tourists|strangers|enemies|soldiers|officers|leaders|managers|directors|owners|partners|colleagues|employees|bosses|chiefs|kings|queens|princes|princesses|heroes|villains|angels|devils|giants|dwarfs|elves|witches|wizards|dragons|monsters|ghosts|spirits|gods|goddesses|saints|prophets|apostles|disciples|believers|followers|critics|fans|supporters|opponents|rivals|allies|enemies|companies|organizations|groups|teams|committees|councils|boards|panels|commissions|delegations|delegates|representatives|ambassadors|ministers|senators|congressmen|governors|mayors|judges|attorneys|agents|spies|detectives|reporters|photographers|editors|publishers|authors|poets|musicians|singers|dancers|actors|actresses|directors|producers|writers|artists|painters|sculptors|architects|designers|engineers|technicians|mechanics|electricians|plumbers|carpenters|builders|farmers|gardeners|chefs|cooks|bakers|butchers|waiters|bartenders|servers|hosts|hostesses|cleaners|helpers|assistants|aides|secretaries|receptionists|telllers|cashiers|clerks|salespeople|merchants|traders|shopkeepers|vendors|suppliers|dealers|brokers|agents|managers|supervisors|coordinators|directors|presidents|vice\s+presidents|secretaries|treasurers|accountants|auditors|advisors|consultants|specialists|experts|analysts|scientists|researchers|professors|lecturers|instructors|tutors|coaches|trainers|mentors|guides|pilots|captains|commanders|chiefs|leaders|officials|authorities|figures|personalities|celebrities|stars|icons|legends|geniuses|prodigies|champions|winners|losers|players|competitors|contestants|participants|volunteers|donors|sponsors|patrons|benefactors|philanthropists|investors|shareholders|stakeholders|creditors|debtors|borrowers|lenders|owners|tenants|landlords|renters|occupants|residents|citizens|natives|foreigners|aliens|immigrants|refugees|settlers|colonists|pioneers|explorers|adventurers|travelers|tourists|visitors|passengers|commuters|pedestrians|cyclists|motorists|drivers|riders|hikers|campers|climbers|swimmers|runners|joggers|walkers|dancers|singers|musicians|artists|writers|readers|viewers|listeners|followers|subscribers|members|contributors|participants|attendees|spectators|audiences|crowds|groups|parties|classes|teams|crews|gangs|bands|orchestras|choirs|castes|tribes|clans|families|races|species|breeds|types|kinds|sorts|varieties|categories|classes|groups|sets|collections|assemblies|gatherings|meetings|conferences|conventions|rallies|protests|marches|parades|festivals|carnivals|concerts|shows|performances|exhibitions|displays|demonstrations|presentations|lectures|seminars|workshops|classes|courses|programs|sessions|lessons|tutorials|trainings|practices|exercises|drills|tests|exams|quizzes|surveys|polls|studies|researches|projects|assignments|tasks|jobs|chores|duties|responsibilities|roles|functions|positions|posts|offices|titles|ranks|grades|levels|stages|phases|steps|cycles|periods|eras|ages|epochs|generations|decades|centuries|millennia|years|months|weeks|days|hours|minutes|seconds|moments|instants|times|occasions|events|incidents|accidents|emergencies|crises|disasters|catastrophes|tragedies|dramas|comedies|stories|tales|legends|myths|fables|parables|allegories|metaphors|symbols|signs|indicators|markers|clues|hints|tips|suggestions|recommendations|proposals|plans|strategies|tactics|methods|techniques|approaches|systems|processes|procedures|operations|functions|activities|actions|steps|measures|initiatives|projects|programs|schemes|policies|rules|regulations|laws|statutes|ordinances|bylaws|codes|standards|principles|guidelines|directives|instructions|orders|commands|requests|demands|requirements|specifications|criteria|conditions|terms|provisions|clauses|sections|paragraphs|articles|chapters|pages|lines|words|letters|characters|symbols|numbers|figures|digits|values|amounts|quantities|totals|sums|averages|ratios|percentages|fractions|decimals|integers|wholes|halves|thirds|quarters|fifths|sixths|sevenths|eighths|ninths|tenths|millions|billions|trillions|dozens|hundreds|thousands)\b',
     None, "Use 'there are' with these plural nouns."),
    (r'\bthere\s+(are|were)\s+(a|an)\b',
     None, "Use 'there is/was' with singular nouns."),
    (r'\bthere\s+is\s+(these|those)\b', None, "Use 'there are' with 'these/those' (plural)."),
    (r'\bthere\s+was\s+(these|those)\b', None, "Use 'there were' with 'these/those' (plural)."),

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
    (r'\b(I|He|She|It|You|We|They)\s+drawed\b',   r'\1 drew',     "'drawed' is not valid — past tense of 'draw' is 'drew'."),
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
    (r'\b(I|He|She|It|You|We|They)\s+eated\b',    r'\1 ate',      "'eated' is not valid — past tense of 'eat' is 'ate'."),
    (r'\b(I|He|She|It|You|We|They)\s+sleeped\b',  r'\1 slept',    "'sleeped' is not valid — past tense of 'sleep' is 'slept'."),
    (r'\b(I|He|She|It|You|We|They)\s+feeled\b',   r'\1 felt',     "'feeled' is not valid — past tense of 'feel' is 'felt'."),
    (r'\b(I|He|She|It|You|We|They)\s+leaved\b',   r'\1 left',     "'leaved' is not valid — past tense of 'leave' is 'left'."),
    (r'\b(I|He|She|It|You|We|They)\s+meeted\b',   r'\1 met',      "'meeted' is not valid — past tense of 'meet' is 'met'."),
    (r'\b(I|He|She|It|You|We|They)\s+standed\b',  r'\1 stood',    "'standed' is not valid — past tense of 'stand' is 'stood'."),
    (r'\b(I|He|She|It|You|We|They)\s+sitted\b',   r'\1 sat',      "'sitted' is not valid — past tense of 'sit' is 'sat'."),
    (r'\b(I|He|She|It|You|We|They)\s+hurted\b',   r'\1 hurt',     "'hurted' is not valid — past tense of 'hurt' is 'hurt'."),
    (r'\b(I|He|She|It|You|We|They)\s+hitted\b',   r'\1 hit',      "'hitted' is not valid — past tense of 'hit' is 'hit'."),
    (r'\b(I|He|She|It|You|We|They)\s+puted\b',    None,           "'puted' is not valid — past tense of 'put' is 'put'."),
    (r'\b(I|He|She|It|You|We|They)\s+costed\b',   None,           "'costed' is not valid — past tense of 'cost' is 'cost'."),
    (r'\b(I|He|She|It|You|We|They)\s+meaned\b',   r'\1 meant',    "'meaned' is not valid — past tense of 'mean' is 'meant'."),
    (r'\b(I|He|She|It|You|We|They)\s+keeped\b',   r'\1 kept',     "'keeped' is not valid — past tense of 'keep' is 'kept'."),
    (r'\b(I|He|She|It|You|We|They)\s+losed\b',    r'\1 lost',     "'losed' is not valid — past tense of 'lose' is 'lost'."),
    (r'\b(I|He|She|It|You|We|They)\s+shaked\b',   r'\1 shook',    "'shaked' is not valid — past tense of 'shake' is 'shook'."),
    (r'\b(I|He|She|It|You|We|They)\s+forgived\b', r'\1 forgave',  "'forgived' is not valid — past tense of 'forgive' is 'forgave'."),
    (r'\b(I|He|She|It|You|We|They)\s+builded\b',  r'\1 built',    "'builded' is not valid — past tense of 'build' is 'built'."),
    (r'\b(I|He|She|It|You|We|They)\s+sended\b',   r'\1 sent',     "'sended' is not valid — past tense of 'send' is 'sent'."),
    (r'\b(I|He|She|It|You|We|They)\s+spended\b',  r'\1 spent',    "'spended' is not valid — past tense of 'spend' is 'spent'."),
    (r'\b(I|He|She|It|You|We|They)\s+winned\b',   r'\1 won',      "'winned' is not valid — past tense of 'win' is 'won'."),
    (r'\b(I|He|She|It|You|We|They)\s+bited\b',    r'\1 bit',      "'bited' is not valid — past tense of 'bite' is 'bit'."),
    (r'\b(I|He|She|It|You|We|They)\s+shined\b',   r'\1 shone',    "'shined' is not valid — past tense of 'shine' is 'shone'."),
    (r'\b(I|He|She|It|You|We|They)\s+payed\b',    r'\1 paid',     "'payed' is not valid — past tense of 'pay' is 'paid'."),

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
    (r'\b(has|have|had)\s+slept\b',    r'\1 slept',    "Use past participle: 'slept' (same as past tense)."),
    (r'\b(has|have|had)\s+kept\b',     r'\1 kept',     "Use past participle: 'kept' (same as past tense)."),
    (r'\b(has|have|had)\s+felt\b',     r'\1 felt',     "Use past participle: 'felt' (same as past tense)."),
    (r'\b(has|have|had)\s+left\b',     r'\1 left',     "Use past participle: 'left' (same as past tense)."),
    (r'\b(has|have|had)\s+met\b',      r'\1 met',      "Use past participle: 'met' (same as past tense)."),
    (r'\b(has|have|had)\s+stood\b',    r'\1 stood',    "Use past participle: 'stood' (same as past tense)."),
    (r'\b(has|have|had)\s+shed\b',     r'\1 shed',     "Use past participle: 'shed' (same as past tense)."),
    (r'\b(has|have|had)\s+shook\b',    r'\1 shaken',   "Use past participle: 'shaken'."),
    (r'\b(has|have|had)\s+forgave\b',  r'\1 forgiven', "Use past participle: 'forgiven'."),
    (r'\b(has|have|had)\s+beat\b',     r'\1 beaten',   "Use past participle: 'beaten'."),
    (r'\b(has|have|had)\s+shone\b',    r'\1 shone',    "Use past participle: 'shone' (same as past tense)."),
    (r'\b(has|have|had)\s+hung\b',     r'\1 hung',     "Use past participle: 'hung' (same as past tense)."),

    # Have/Has/Had + base verb (should be past participle)
    (r'\b(has|have|had)\s+(eat|drink|go|come|do|make|take|write|read|speak|break|swim|sing|begin|ring|sink|drive|ride|fly|grow|throw|draw|wear|steal|hide|bite|choose|freeze|forget|get|give|see|know|think|bring|catch|fight|teach|sell|tell|pay|find|hold|buy|build|send|spend|leave|meet|lose|mean|understand|forgive|forbid|prove|shake|beat|seek|shoot|show|shut|sit|sleep|stand|stick|strike|strive|swear|sweep|swing|tear|wake|win|wind|withdraw|dig|feed|feel|hang|hold|kneel|lay|lead|lend|lie|light|ride|rise|seek|shine|shrink|slay|slide|smell|sow|spin|spit|split|spoil|spread|spring|sting|stink|strew|stride|string|strip|strive|stun|sweat|swell|swing|swear|tear|wake|weave|weep|wet)\b',
     None, "Use the past participle after 'have/has/had' (e.g. 'I have eaten' not 'I have eat')."),

    # Bare past participle without auxiliary
    (r'\b(I|You|He|She|It|We|They|The|This|That|These|Those)\s+(?:just|already|never|ever|always|still|recently|barely|hardly|scarcely|nearly|almost|finally|eventually|basically|simply|justly|rightly|wrongly|truly|merely|mostly|pretty|quite|rather|somewhat)\s+(seen|gone|been|done|taken|eaten|drunk|driven|ridden|flown|grown|thrown|drawn|broken|spoken|stolen|woken|frozen|chosen|hidden|bitten|forgotten|gotten|swum|sung|rung|sunk|begun)\b',
     None, "Use an auxiliary verb (have/has) with past participles, or use simple past (e.g. 'I saw' not 'I seen')."),
    (r'\b(I|You|He|She|It|We|They)\s+(seen|gone|been|done|taken|eaten|drunk|driven|ridden|flown|grown|thrown|drawn|broken|spoken|stolen|woken|frozen|chosen|hidden|bitten|forgotten|gotten|swum|sung|rung|sunk|begun)\b',
     None, "Use an auxiliary verb (have/has) with past participles, or use simple past (e.g. 'I saw' not 'I seen')."),

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

    (r'\b(can|must|should|could|would|may|might|will|shall)\s+\w*[a-z]s\b',
     None, "Use base verb after a modal (e.g. 'She can run' not 'She can runs')."),
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

    # Did + past tense → use base form
    (r'\b(?:did|didn\'t|did\s+not)\s+(went|saw|took|ate|drank|drove|rode|flew|grew|threw|drew|wore|stole|sang|swam|ran|came|gave|made|broke|spoke|wrote|read|began|rang|sank|froze|chose|woke|forgot|hid|bit|rode|drove|fought|caught|taught|brought|bought|sold|told|knew|thought|left|met|lost|paid|sent|spent|built|understood|stood|sat|slept|kept|found|held|hung|felt|meant)\b',
     None, "Use the base verb form after 'did/didn't' (e.g. 'I went' → 'I did go' or just 'I went')."),

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
    (r'\bmany\s+informations\b', None,     "'information' has no plural form — use 'much information'."),
    (r'\ban?\s+advices?\b',      None,               "'advice' is uncountable — use 'some advice' or just 'advice'."),

    # Much + countable noun
    (r'\bmuch\s+(books|people|students|cars|houses|chairs|tables|days|weeks|years|hours|minutes|dollars|euros|children|men|women|animals|trees|flowers|bottles|cups|plates|shirts|shoes|words|pages|chapters|lessons|pounds|euros|dollars)\b',
     None, "Use 'many' with countable nouns."),

    # ── Articles (a/an) ──────────────────────────────────────
    (r'\ba\s+(hour|honest|honour|heir|honor|heirloom|herb)\b', r'an \1', "Use 'an' before silent-h words."),
    (r'\ban\s+(university|union|unique|unit|usual|user|use|uniform|unicorn|unilateral|universal|unanimous|European|euphemism|eulogy|euthanasia)\b', r'a \1', "Use 'a' before words starting with a 'y' sound."),

    # Singular countable noun without any article (e.g. "I like apple")
    (r'\b(I|You|He|She|It|We|They)\s+(like|have|eat|love|buy|want|need|see|read|play|watch|use|drive|own|prefer|enjoy|hate|find|make|take|bring|sell|wear|choose|ride|write|call|wash|clean|cook|open|close|hold|lose)\s+(apple|banana|car|book|dog|cat|house|chair|table|phone|shirt|shoe|pen|cup|plate|bottle|bag|hat|ball|tree|flower|bird|fish|song|movie|game|word|page|letter|door|window|room|bed|desk|computer|garden|kitchen|store|shop|park|city|town|school|college|office|bank|hotel|restaurant|hospital|museum|theater|library|bus|train|plane|bike|horse|sheep|cow|pig|chicken|duck|goose|rose|lily|tulip|grape|orange|lemon|peach|pear|mango|tomato|potato|onion|carrot|cake|cookie|pie|burger|pizza|sandwich|salad|soup|drink|coffee|tea|juice|glass|cup|spoon|fork|knife|plate|bowl)\b',
     None, "Use an article (a/an/the) or make it plural with countable singular nouns (e.g. 'I like apples' not 'I like apple')."),

    # Past-tense verbs + missing article
    (r'\b(I|You|He|She|It|We|They)\s+(liked|had|ate|bought|wanted|needed|saw|played|watched|used|enjoyed|hated|found|made|took|brought|wore|rode|called|washed|cooked|held|lost|drove|wrote|chose|opened|closed|cleaned|studied|stopped|started|helped|learned|asked|waited|visited|picked|moved|touched|kicked|pulled|pushed|raised|reached|realized|received|remembered|returned|saved|showed|signed|smiled|solved|sounded|stayed|tested|thanked|trained|turned|used|walked|watched|worked|worried)\s+(apple|banana|car|book|dog|cat|house|chair|table|phone|shirt|shoe|pen|cup|plate|bottle|bag|hat|ball|tree|flower|bird|fish|song|movie|game|word|page|letter|door|window|room|bed|desk|computer|garden|kitchen|store|shop|park|city|town|school|college|office|bank|hotel|restaurant|hospital|museum|theater|library|bus|train|plane|bike|horse|sheep|cow|pig|chicken|duck|goose|rose|lily|tulip|grape|orange|lemon|peach|pear|mango|tomato|potato|onion|carrot|cake|cookie|pie|burger|pizza|sandwich|salad|soup|drink|coffee|tea|juice|glass|cup|spoon|fork|knife|plate|bowl)\b',
     None, "Use an article (a/an/the) or make it plural with countable singular nouns (e.g. 'I liked apples' not 'I liked apple')."),

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
    (r'\bcan\s+not\b',        "cannot",      "Use 'cannot' (one word) in formal English."),

    # ── Comparatives / Superlatives ───────────────────────────
    (r'\bmore\s+(better|worse|bigger|smaller|older|younger|faster|slower|richer|poorer|higher|lower|greater|lesser|hotter|colder|warmer|cooler|darker|brighter|stronger|weaker|taller|shorter|longer|wider|deeper|earlier|later|simpler|happier|prettier|easier|harder|busier|funnier|angrier|friendlier|heavier|healthier|luckier|nicer|sadder|tastier|wealthier|calmer|quieter|cheaper|cleaner|clearer|closer|fresher|fuller|gentler|kinder|larger|looser|narrower|neater|newer|older|plainer|politer|quieter|rarer|safer|sharper|shorter|smarter|softer|steeper|stricter|stronger|sweeter|taller|thicker|thinner|tighter|tougher|warmer|weaker|wider|wiser)\b',
     None, "Double comparative — use the comparative form directly (e.g. 'better' not 'more better')."),
    (r'\bmost\s+(best|worst|biggest|smallest|oldest|youngest|fastest|slowest|richest|poorest|highest|lowest|greatest|least|hottest|coldest|warmest|darkest|brightest|strongest|weakest|tallest|shortest|longest|widest|deepest|earliest|latest|simplest|happiest|prettiest|easiest|hardest|busiest|funniest|angriest|friendliest|heaviest|healthiest|luckiest|nicest|saddest|tastiest|wealthiest|calmest|quietest|cheapest|cleanest|clearest|closest|freshest|fullest|gentlest|kindest|largest|loosest|narrowest|neatest|newest|plainest|politest|rarest|safest|sharpest|shortest|smartest|softest|steepest|strictest|strongest|sweetest|thickest|thinnest|tightest|toughest)\b',
     None, "Double superlative — use the superlative form directly (e.g. 'best' not 'most best')."),

    # ── Subjunctive Mood ─────────────────────────────────────
    (r'\bif\s+(I|he|she|it)\s+was\s+(you|here|there|taller|faster|smarter|richer|older|younger|better|worse|bigger|smaller|stronger|weaker|faster|slower|nicer|kinder|richer|poorer|braver|calmer|happier|luckier|healthier|wealthier)\b',
     None, "Use 'were' in the subjunctive mood (e.g. 'if I were you')."),
    (r'\bwish\s+(I|he|she|it)\s+was\b', None, "Use 'were' after 'wish' in the subjunctive mood (e.g. 'I wish I were')."),
    (r'\b(as\s+though|as\s+if)\s+(I|he|she|it)\s+was\b', None, "Use 'were' after 'as though/as if' in the subjunctive mood."),

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
