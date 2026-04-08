# q is question
def classificar_mcq(q):
    q = q.lower()

    if "heart" in q or "cholesterol" in q:
        area = "cardiology"
    elif "brain" in q:
        area = "neurology"
    elif "infection" in q or "virus" in q:
        area = "infectious_disease"
    elif "hormone" in q:
        area = "endocrinology"
    elif "lung" in q:
        area = "pulmonology"
    elif "psych" in q:
        area = "psychiatry"
    else:
        area = "general_medicine"

    tamanho = len(q)

    if tamanho < 120:
        dificuldade = "easy"
    elif tamanho < 250:
        dificuldade = "medium"
    else:
        dificuldade = "hard"

    return area, dificuldade, "UpToDate"


def classificar_aberta(q):
    q = q.lower()

    if "infection" in q or "virus" in q:
        area = "infectious_disease"
    elif "heart" in q:
        area = "cardiology"
    elif "brain" in q:
        area = "neurology"
    elif "diabetes" in q:
        area = "endocrinology"
    else:
        area = "general_medicine"

    tamanho = len(q)

    if tamanho < 120:
        dificuldade = "easy"
    elif tamanho < 250:
        dificuldade = "medium"
    else:
        dificuldade = "hard"

    return area, dificuldade, "PubMed review"