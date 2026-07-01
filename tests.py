QUESTIONS = {
    "A1": [
        {
            "question": "___ a cat.",
            "options": ["This", "These", "Those", "They"],
            "correct": 0,
            "explanation": "\"This\" is used for singular objects near us."
        },
        {
            "question": "She ___ a teacher.",
            "options": ["are", "is", "am", "be"],
            "correct": 1,
            "explanation": "\"She\" is third person singular, so we use \"is\"."
        },
        {
            "question": "I have ___ apple.",
            "options": ["a", "an", "the", "some"],
            "correct": 1,
            "explanation": "\"Apple\" starts with a vowel sound, so we use \"an\"."
        },
        {
            "question": "There ___ five books on the table.",
            "options": ["is", "am", "are", "be"],
            "correct": 2,
            "explanation": "\"Five books\" is plural, so we use \"are\"."
        },
        {
            "question": "He ___ to school every day.",
            "options": ["go", "goes", "going", "gone"],
            "correct": 1,
            "explanation": "\"He\" is third person singular, so the verb takes an \"-s\"."
        },
    ],
    "A2": [
        {
            "question": "She ___ to the store yesterday.",
            "options": ["go", "goes", "went", "going"],
            "correct": 2,
            "explanation": "\"Yesterday\" indicates past tense, so we use \"went\"."
        },
        {
            "question": "This book is ___ than that one.",
            "options": ["more cheap", "cheaper", "cheap", "cheapest"],
            "correct": 1,
            "explanation": "One-syllable adjectives form comparatives with \"-er\"."
        },
        {
            "question": "The meeting is ___ Monday.",
            "options": ["in", "at", "on", "by"],
            "correct": 2,
            "explanation": "We use \"on\" for days of the week."
        },
        {
            "question": "I ___ like coffee.",
            "options": ["don't", "doesn't", "not", "am not"],
            "correct": 0,
            "explanation": "\"I\" uses \"don't\" for negation in present simple."
        },
        {
            "question": "We have ___ friends in this city.",
            "options": ["much", "a lot", "many", "lot of"],
            "correct": 2,
            "explanation": "\"Friends\" is a countable noun, so we use \"many\"."
        },
    ],
    "B1": [
        {
            "question": "She ___ her homework yet.",
            "options": ["didn't finish", "hasn't finished", "doesn't finish", "isn't finishing"],
            "correct": 1,
            "explanation": "\"Yet\" is used with present perfect to talk about something not done up to now."
        },
        {
            "question": "If it rains, I ___ an umbrella.",
            "options": ["will take", "would take", "took", "take"],
            "correct": 0,
            "explanation": "First conditional: \"if + present, will + infinitive\"."
        },
        {
            "question": "You ___ wear a seatbelt. It's the law.",
            "options": ["must", "can", "might", "could"],
            "correct": 0,
            "explanation": "\"Must\" expresses obligation or strong necessity."
        },
        {
            "question": "I've been working here ___ 2019.",
            "options": ["for", "since", "from", "during"],
            "correct": 1,
            "explanation": "\"Since\" is used with a specific point in time (2019)."
        },
        {
            "question": "The book ___ is on the table is mine.",
            "options": ["who", "which", "whose", "whom"],
            "correct": 1,
            "explanation": "\"Which\" is used as a relative pronoun for things."
        },
    ],
    "B2": [
        {
            "question": "The window ___ by the boy.",
            "options": ["was broken", "broke", "is breaking", "has broken"],
            "correct": 0,
            "explanation": "Passive voice (past): object + \"was\" + past participle."
        },
        {
            "question": "If I ___ you, I would accept the offer.",
            "options": ["am", "was", "were", "be"],
            "correct": 2,
            "explanation": "Second conditional uses \"were\" for all subjects (subjunctive mood)."
        },
        {
            "question": "She told me she ___ the next day.",
            "options": ["will come", "would come", "is coming", "comes"],
            "correct": 1,
            "explanation": "In reported speech, \"will\" shifts to \"would\"."
        },
        {
            "question": "___ I had more time, I would travel more.",
            "options": ["If only", "Unless", "Despite", "Even though"],
            "correct": 0,
            "explanation": "\"If only\" expresses a wish about a present situation."
        },
        {
            "question": "The man ___ car was stolen reported it to the police.",
            "options": ["who", "which", "whose", "that"],
            "correct": 2,
            "explanation": "\"Whose\" shows possession in relative clauses."
        },
    ],
    "C1": [
        {
            "question": "___ seen such a beautiful sunset.",
            "options": ["Never have I", "Never I have", "I have never", "Have never I"],
            "correct": 0,
            "explanation": "Negative adverbials at the start require subject-auxiliary inversion."
        },
        {
            "question": "Had I known, I ___ differently.",
            "options": ["will act", "would have acted", "would act", "acted"],
            "correct": 1,
            "explanation": "Inverted third conditional: \"Had + subject + past participle, would have + past participle\"."
        },
        {
            "question": "It's essential that every student ___ on time.",
            "options": ["is", "be", "was", "are"],
            "correct": 1,
            "explanation": "The subjunctive mood uses the base form of the verb after certain adjectives."
        },
        {
            "question": "___ his help, I would have failed.",
            "options": ["But for", "Unless", "Without of", "Except"],
            "correct": 0,
            "explanation": "\"But for\" means \"if it hadn't been for\" in advanced conditionals."
        },
        {
            "question": "Not until she arrived ___ the news.",
            "options": ["she heard", "did she hear", "she did hear", "had she heard"],
            "correct": 1,
            "explanation": "\"Not until\" at the start triggers subject-auxiliary inversion."
        },
    ],
}

LEVEL_LABELS = {
    "A1": "Beginner",
    "A2": "Elementary",
    "B1": "Intermediate",
    "B2": "Upper Intermediate",
    "C1": "Advanced",
}


def get_results(level: str, answers: list) -> dict:
    questions = QUESTIONS[level]
    total = len(questions)
    correct_count = 0
    details = []

    for i, q in enumerate(questions):
        user_answer = answers[i] if i < len(answers) else -1
        is_correct = user_answer == q["correct"]
        if is_correct:
            correct_count += 1
        details.append({
            "question": q["question"],
            "options": q["options"],
            "correct": q["correct"],
            "user_answer": user_answer,
            "is_correct": is_correct,
            "explanation": q["explanation"],
        })

    score = correct_count
    percent = int(round(score / total * 100))

    if percent == 100:
        feedback = f"Perfect! You've mastered {level} ({LEVEL_LABELS[level]}). You're ready for the next level."
    elif percent >= 80:
        feedback = f"Great work! You're comfortable at {level} ({LEVEL_LABELS[level]})."
    elif percent >= 60:
        feedback = f"Good effort! You understand some {level} ({LEVEL_LABELS[level]}), but there's room to improve."
    else:
        feedback = f"Keep practicing! You need more work on {level} ({LEVEL_LABELS[level]}). Try studying the basics first."

    return {
        "level": level,
        "score": score,
        "total": total,
        "percent": percent,
        "feedback": feedback,
        "details": details,
    }
