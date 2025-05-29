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
    Arestovich = "Arestovich"
    Baumeister = "Baumeister"
    Chernobaev = "Chernobaev"
    Khimich = "Khimich"
    Mnenie = "Mnenie"
    PolitWorld = "PolitWorld"
    Singles = "Singles"
    Uralov = "Uralov"


class Speak:
    Shchelin = "П.Щелин"
    Ads = "Реклама"
    Translator = "Переводчик"

    Golub = "Е.Голуб"
    Romanenko = "Ю.Романенко"
    Izotov = "С.Изотов"
    OrlovSm = "И.Орлов"
    Shelest = "А.Шелест"
    Bondarenko = "К.Бондаренко"
    Panchenko = "Д.Панченко"
    Shevchenko = "И.Шевченко"
    Dudnik = "С.Дудник"
    Khazin = "М.Хазин"
    Chernov = "А.Чернов"
    Arestovich = "А.Арестович"
    Bobileff = "А.Бобылев"
    Boglaev = "В.Боглаев"
    Burov = "А.Буров"
    Kotar = "Н.Котар"
    Baumeister = "А.Баумейстер"
    Chernobaev = "Н.Чернобаев"
    Khimich = "Р.Химич"
    Askerhanov = "К.Аскерханов"
    Nadolinsky = "А.Надолинский"
    Belkovsky = "С.Белковский"
    Kusa = "И.Куса"
    Svetov = "М.Светов"
    Klizma = "Клизма"

    ShchelinEn = "P.Shchelin"
    Rohlin = "R.Rohlin"
    Pageau = "J.Pageau"
    Hall_J = "J.Hall"
    Heers_J = "J.Heers"


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
