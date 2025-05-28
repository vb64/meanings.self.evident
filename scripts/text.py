SENTENCE_END = ".!?"


class Course:
    InSearchOfMeaning = "InSearchOfMeaning"
    GnosticThinking = "GnosticThinking"
    Mash = "Mash"
    Shelest = "Shelest"
    Panchenko = "Panchenko"
    Dudnik = "Dudnik"
    Chernov = "Chernov"
    English = "English"
    Usa = "Usa"
    Bobileff = "Bobileff"


class Speak:
    Shchelin = "П.Щелин"
    ShchelinEn = "P.Shchelin"
    Golub = "Е.Голуб"
    Romanenko = "Ю.Романенко"
    Izotov = "С.Изотов"
    OrlovSm = "И.Орлов"
    Shelest = "А.Шелест"
    Bondarenko = "К.Бондаренко"
    Panchenko = "Д.Панченко"
    Translator = "Переводчик"
    Shevchenko = "И.Шевченко"
    Dudnik = "С.Дудник"
    Khazin = "М.Хазин"
    Chernov = "А.Чернов"
    Rohlin = "R.Rohlin"
    Kotar = "Н.Котар"
    Pageau = "J.Pageau"
    Hall_J = "J.Hall"
    Heers_J = "J.Heers"
    Arestovich = "А.Арестович"
    Bobileff = "А.Бобылев"
    Boglaev = "В.Боглаев"
    Burov = "А.Буров"


def is_complete(sentence):
    return sentence and (sentence[-1] in SENTENCE_END)


def split_to_sentences(text):
    sentences = []
    current = []
    for word in text.split():
        current.append(word)
        if word[-1] in SENTENCE_END:
            sentences.append(' '.join(current))
            current = []

    if current:
        print("***WARN sentence: {}".format(text))
        sentences.append(' '.join(current))

    return sentences
