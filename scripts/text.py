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
    Sobolev = 'Sobolev'
    Uralov = "Uralov"
    Singles = "Singles"


class Speak:
    Shchelin = "П.Щелин"
    Ads = "Реклама"
    Translator = "Переводчик"
    Guest = "Слушатель"

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
    Klizma = "Виктор"
    Datsuk = "С.Дацюк"
    Feldman = "Н.Фельдман"
    Leybin = "В.Лейбин"
    Uralov = "С.Уралов"
    Chadaev = "А.Чадаев"
    Kniazev = "И.Князев"
    Sobolev = "Н.Соболев"

    ShchelinEn = "P.Shchelin"
    Rohlin = "R.Rohlin"
    Pageau = "J.Pageau"
    Hall_J = "J.Hall"
    Heers_J = "J.Heers"


ARESTOVICH = (Speak.Arestovich, Speak.Shchelin)
COURSE_ARESTOVICH = [
  ('2021_12_24', False, ARESTOVICH),
  ('2021_12_29', False, ARESTOVICH),
  ('2022_01_06', False, ARESTOVICH),
  ('2022_01_17', False, ARESTOVICH),
  ('2022_02_07', False, reversed(ARESTOVICH)),
  ('2022_02_09', False, reversed(ARESTOVICH)),
  ('2022_02_18', False, reversed(ARESTOVICH)),
  ('2022_04_22', False, reversed(ARESTOVICH)),
  ('2022_05_31', False, reversed(ARESTOVICH)),
  ('2022_07_19', False, reversed(ARESTOVICH)),
  ('2022_08_20', False, (Speak.Datsuk, Speak.Romanenko, Speak.Arestovich, Speak.Shchelin)),  # Feldman
  ('2022_09_19', False, reversed(ARESTOVICH)),
  ('2022_10_04', False, reversed(ARESTOVICH)),
  ('2022_12_27', False, reversed(ARESTOVICH)),
  ('2023_02_12', False, ARESTOVICH),
]
BAUMEISTER = (Speak.Baumeister, Speak.Shchelin)
COURSE_BAUMEISTER = [
  ('2022_04_18', False, BAUMEISTER),
  ('2022_05_17', False, BAUMEISTER),
  ('2025_02_19', False, (Speak.Baumeister, Speak.Shchelin, Speak.Golub)),
]
CHERNOBAEV = (Speak.Chernobaev, Speak.Shchelin)
COURSE_CHERNOBAEV = [
  ('2024_08_15', False, (Speak.Chernobaev, Speak.Shchelin, Speak.Ads)),
  ('2024_09_27', False, reversed(CHERNOBAEV)),
  ('2024_11_22', False, reversed(CHERNOBAEV)),
]
GOLUB = (Speak.Golub, Speak.Shchelin)
ROMANENKO = (Speak.Romanenko, Speak.Shchelin)
COURSE_GNOSTIC = [
  ("gnosticism", False, reversed(ROMANENKO)),
  ("modern", False, reversed(ROMANENKO)),
  ("gobs", False, reversed(ROMANENKO)),
  ("enlightenment", False, reversed(ROMANENKO)),
  ("nationalism", False, ROMANENKO),

  ("marxism", False, reversed(GOLUB)),
  ("positivism", False, reversed(GOLUB)),
  ("deep_state", False, reversed(GOLUB)),
  ("info_wars", False, GOLUB),
]
COURSE_USA =  [
  ('2022_01_06', False, reversed(ARESTOVICH)),
  ('2022_01_10', False, ROMANENKO),
  ('2022_01_14', False, reversed(ROMANENKO)),
]
KOTAR = (Speak.Kotar, Speak.Shchelin)
ROHLIN = (Speak.Rohlin, Speak.ShchelinEn)
PAGEAU = (Speak.Pageau, Speak.ShchelinEn)
HALLJ = (Speak.Hall_J, Speak.ShchelinEn)
HEERSJ = (Speak.Heers_J, Speak.ShchelinEn)
COURSE_ENGLISH = [
  ('2024_05_04', False, ROHLIN),
  ('2024_05_31', False, KOTAR),
  ('2024_06_12', False, reversed(ROHLIN)),
  ('2024_06_22', False, reversed(PAGEAU)),
  ('2024_09_17', False, PAGEAU),
  ('2024_10_14', False, KOTAR),
  ('2025_01_20', False, HALLJ),
  ('2025_03_21', False, reversed(HEERSJ)),
  ('2025_06_02', False, HALLJ),
]
COURSE_MASH = [
    ("2025_03_28", False, (Speak.Shchelin, Speak.Izotov, Speak.OrlovSm)),
    ('2025_05_25', False, (Speak.OrlovSm, Speak.Shchelin, Speak.Izotov)),
]
CHERNOV = (Speak.Chernov, Speak.Shchelin)
COURSE_CHERNOV = [
  ("2023_12_16", False, reversed(CHERNOV)),
  ("2024_04_16", False, CHERNOV),
  ("2024_04_23", False, reversed(CHERNOV)),
  ("2024_05_22", False, reversed(CHERNOV)),
  ("2024_08_13", False, reversed(CHERNOV)),
  ("2025_04_07", False, reversed(CHERNOV)),
  ('2025_05_30', False, reversed(CHERNOV)),
]
PANCHENKO = (Speak.Panchenko, Speak.Shchelin)
COURSE_PANCHENKO = [
  ("2024_06_22", False, reversed(PANCHENKO)),
  ("2024_11_06", False, reversed(PANCHENKO)),
  ("2025_01_23", False, (Speak.Shchelin, Speak.Panchenko, Speak.Translator)),
  ("2025_02_24", False, (Speak.Shchelin, Speak.Translator, Speak.Panchenko)),
  ("2025_04_06", False, reversed(PANCHENKO)),
  ("2025_05_16", False, reversed(PANCHENKO)),
]
DUDNIK = (Speak.Dudnik, Speak.Shchelin)
COURSE_DUDNIK = [
  ("2022_11_03", False, reversed(DUDNIK)),
  ("2024_05_14", False, reversed(DUDNIK)),
  ("2024_06_04", False, reversed(DUDNIK)),
  ("2024_07_09", False, reversed(DUDNIK)),
  ("2024_08_14", False, (Speak.Shchelin, Speak.Dudnik, Speak.Ads)),
  ("2024_09_13", False, reversed(DUDNIK)),
  ("2024_10_02", False, reversed(DUDNIK)),
  ("2024_10_14", False, reversed(DUDNIK)),
  ("2024_11_04", False, reversed(DUDNIK)),
  ("2024_11_23", False, reversed(DUDNIK)),
  ("2024_12_26", False, reversed(DUDNIK)),
  ("2025_01_15", False, DUDNIK),
  ("2025_02_19", False, reversed(DUDNIK)),
  ("2025_03_11", False, reversed(DUDNIK)),
  ("2025_03_22", False, reversed(DUDNIK)),
  ("2025_03_25", False, (Speak.Khazin, Speak.Shchelin, Speak.Dudnik)),
  ("2025_04_24", False, reversed(DUDNIK)),
  ("2025_05_23", False, reversed(DUDNIK)),
  ("2025_06_24", False, DUDNIK),
]
SHELEST = (Speak.Shelest, Speak.Shchelin)
COURSE_SHELEST = [
  ("2023_02_09", False, reversed(SHELEST)),
  ("2023_04_01", False, reversed(SHELEST)),
  ("2023_05_04", False, reversed(SHELEST)),
  ("2023_06_21", False, reversed(SHELEST)),
  ("2023_07_15", False, reversed(SHELEST)),
  ("2023_08_03", False, reversed(SHELEST)),
  ("2023_08_30", False, reversed(SHELEST)),
  ("2023_09_23", False, reversed(SHELEST)),
  ("2023_10_12", False, SHELEST),
  ("2023_11_02", False, SHELEST),
  ("2023_11_22", False, SHELEST),
  ("2023_11_23", False, SHELEST),
  ("2023_12_13", False, reversed(SHELEST)),
  ("2023_12_28", False, SHELEST),
  ("2024_01_19", False, SHELEST),
  ("2024_02_10", False, reversed(SHELEST)),
  ("2024_03_14", False, reversed(SHELEST)),
  ("2024_04_03", False, reversed(SHELEST)),
  ("2024_04_24", False, reversed(SHELEST)),
  ("2024_05_10", False, reversed(SHELEST)),
  ("2024_05_29", False, SHELEST),
  ("2024_06_15", False, reversed(SHELEST)),
  ("2024_06_26", False, SHELEST),
  ("2024_08_07", False, reversed(SHELEST)),
  ("2024_08_19", False, reversed(SHELEST)),
  ("2024_09_04", False, reversed(SHELEST)),
  ("2024_09_26", False, SHELEST),
  ("2024_10_10", False, SHELEST),
  ("2024_10_25", False, SHELEST),
  ("2024_11_12", False, reversed(SHELEST)),
  ("2024_11_30", False, reversed(SHELEST)),
  ("2024_12_10", False, reversed(SHELEST)),
  ("2024_12_24", False, SHELEST),
  ("2025_01_11", False, SHELEST),
  ("2025_01_27", False, SHELEST),
  ("2025_02_11", False, SHELEST),
  ("2025_02_22", False, SHELEST),
  ("2025_03_06", False, reversed(SHELEST)),
  ("2025_03_17", False, reversed(SHELEST)),
  ("2025_03_31", False, (Speak.Shchelin, Speak.Bondarenko, Speak.Shelest)),
  ("2025_04_09", False, SHELEST),
  ("2025_04_21", False, reversed(SHELEST)),
  ("2025_05_12", False, reversed(SHELEST)),
  ('2025_05_27', False, reversed(SHELEST)),
  ("2025_06_02", False, (
    Speak.Shelest, Speak.Bondarenko, Speak.Shchelin,
    Speak.Bondarenko, Speak.Shelest, Speak.Shchelin,
  )),
  ("2025_06_18", False, reversed(SHELEST)),
]
BOBYLEV = (Speak.Bobileff, Speak.Shchelin)
COURSE_BOBYLEV = [
  ('2022_09_10', False, BOBYLEV),
  ('2022_09_12', False, BOBYLEV),
  ('2023_09_10', False, (Speak.Shchelin, Speak.Bobileff, Speak.Boglaev)),
  ('2023_09_13', False, reversed(BOBYLEV)),
  ('2023_10_03', False, (Speak.Boglaev, Speak.Shchelin, Speak.Bobileff)),
  ('2023_10_12', False, (Speak.Bobileff, Speak.Shchelin, Speak.Boglaev)),
  ('2023_10_15', False, BOBYLEV),
  ('2023_10_18', False, BOBYLEV),
  ('2023_12_01', False, BOBYLEV),
  ('2023_12_03', False, (Speak.Shchelin, Speak.Bobileff, Speak.Ads)),
  ('2024_01_18', False, BOBYLEV),
  ('2024_01_20', False, BOBYLEV),
  ('2024_03_25', False, BOBYLEV),
  ('2024_04_21', False, BOBYLEV),
  ('2024_04_24', False, reversed(BOBYLEV)),
  ('2024_06_06', False, BOBYLEV),
  ('2024_06_11', False, BOBYLEV),
  ('2024_07_13', False, reversed(BOBYLEV)),
  ('2024_07_15', False, BOBYLEV),
  ('2024_10_05', False, (Speak.Burov, Speak.Shchelin, Speak.Bobileff)),
  ('2024_10_12', False, (Speak.Bobileff, Speak.Burov, Speak.Shchelin)),
  ('2024_11_20', False, reversed(BOBYLEV)),
  ('2024_11_21', False, reversed(BOBYLEV)),
  ('2025_01_12', False, BOBYLEV),
  ('2025_01_14', False, reversed(BOBYLEV)),
  ('2025_02_03', False, reversed(BOBYLEV)),
  ('2025_03_25', False, BOBYLEV),
  ('2025_03_26', False, reversed(BOBYLEV)),
  ('2025_04_25', False, BOBYLEV),
  ('2025_04_28', False, BOBYLEV),
]
KHIMICH = (Speak.Khimich, Speak.Shchelin)
COURSE_KHIMICH = [
  ('2022_11_25', False, KHIMICH),
  ('2022_12_11', False, KHIMICH),
  ('2023_01_31', False, reversed(KHIMICH)),
  ('2024_03_20', False, KHIMICH),
]
ASKERHANOV = (Speak.Askerhanov, Speak.Shchelin)
COURSE_ASKERHANOV = [
  ('2025_01_16', False, ASKERHANOV),
  ('2025_02_10', False, reversed(ASKERHANOV)),
  ('2025_03_09', False, reversed(ASKERHANOV)),
  ('2025_03_24', False, (Speak.Shchelin, Speak.Askerhanov, Speak.Nadolinsky)),
  ('2025_05_02', False, (Speak.Askerhanov, Speak.Shchelin, Speak.Guest)),
  ('2025_05_16', False, ASKERHANOV),
  ('2025_06_22', False, ASKERHANOV),
]
SHCHELIN = (Speak.Shchelin, )
COURSE_POLITWORLD = [
  ('2023_04_25', False, SHCHELIN),
  ('2023_11_03', False, SHCHELIN),
  ('2023_11_30', False, (Speak.Shchelin, Speak.Leybin)),
  ('2023_12_13', False, SHCHELIN),
]
SOBOLEV = (Speak.Shchelin, Speak.Sobolev)
COURSE_SOBOLEV = [
  ('2025_01_31', False, SOBOLEV),
  ('2025_06_18', False, SOBOLEV),
]
COURSE_SINGLES = [
  ('2014_05_08', False, (Speak.Shchelin, Speak.Guest)),
  ('2021_12_28', False, reversed(ROMANENKO)),
  ('2022_03_04', False, SHCHELIN),
  ('2022_04_04', False, (Speak.Belkovsky, Speak.Shchelin)),
  ('2022_04_08', False, (Speak.Kusa, Speak.Shchelin)),
  ('2022_06_13', False, (Speak.Shchelin, Speak.Burov)),
  ('2022_08_27', False, (Speak.Svetov, Speak.Shchelin)),
  ('2025_05_08', False, (Speak.Shchelin, Speak.Klizma)),
]
COURSE_URALOV = [
  ('2024_12_25', False, (Speak.Uralov, Speak.Shchelin, Speak.Kniazev, Speak.Chadaev)),
  ('2025_01_29', False, (Speak.Uralov, Speak.Shchelin, Speak.Kniazev, Speak.Chadaev)),
  ('2025_03_06', False, (Speak.Shchelin, Speak.Kniazev, Speak.Uralov, Speak.Chadaev)),
  ('2025_04_03', False, (Speak.Kniazev, Speak.Shchelin, Speak.Uralov, Speak.Chadaev)),
  ('2025_05_15', False, (Speak.Uralov, Speak.Kniazev, Speak.Shchelin, Speak.Chadaev)),
  ('2025_06_19', False, (
    Speak.Shchelin, Speak.Kniazev, Speak.Uralov,
    Speak.Shchelin, Speak.Chadaev, Speak.Uralov, Speak.Kniazev,
  )),
]

GOLUB_SEASON_01 = [
  ("pinker", True, GOLUB),
  ("apocalypse", True, reversed(GOLUB)),
  ("faust", True, reversed(GOLUB)),
  ("identity", True, reversed(GOLUB)),
  ("orange", True, GOLUB),
  ("snowflakes", True, GOLUB),
  ("limits", True, GOLUB),
  ("ai", True, reversed(GOLUB)),
  ("vr", True, reversed(GOLUB)),
  ("mt", True, reversed(GOLUB)),
  ("otvety", True, GOLUB),
  ("final", True, reversed(GOLUB)),
]
GOLUB_SEASON_02 = [
  ("your-flash-memory-card-with-identity", True, reversed(GOLUB)),
  ("placeandtime", True, reversed(GOLUB)),
  ("political-identity", True, GOLUB),
  ("asabiya", True, reversed(GOLUB)),
  ("the-crisis-of-identity", True, reversed(GOLUB)),
  ("mimetic", True, reversed(GOLUB)),
  ("technology-instead-of-faith", True, GOLUB),
  ("a-leap-of-faith", True, GOLUB),
  ("identity-conclusion", True, GOLUB),
  ("identity-qa", True, reversed(GOLUB)),
  ("monarchs-and-agenda", True, reversed(GOLUB)),
  ("the-joy-of-understanding", True, GOLUB),
]
GOLUB_SEASON_03 = [
  ("republic", True, reversed(GOLUB)),
  ("democracy", True, GOLUB),
  ("imperia", True, reversed(GOLUB)),
  ("people", True, reversed(GOLUB)),
  ("reforma", True, reversed(GOLUB)),
  ("renaissance", True, reversed(GOLUB)),
  ("varlaam", True, reversed(GOLUB)),
  ("bacon", True, reversed(GOLUB)),
  ("mendacium", True, GOLUB),
  ("enlightenment", True, reversed(GOLUB)),
  ("obscurantism", True, GOLUB),
  ("final3", True, reversed(GOLUB)),
]
GOLUB_SEASON_04 = [
  ("ontology_of_lies", True, reversed(GOLUB)),
  ("freedom-and-quadrobers", True, reversed(GOLUB)),
  ("battle_of_the_sexes", True, GOLUB),
  ("human_vs_humanity", True, GOLUB),
  ("confession", True, reversed(GOLUB)),
  ("muses_of_tradition", True, GOLUB),
  ("vinaiotvetsvennosti", True, GOLUB),
  ("the-courage-to-be", True, reversed(GOLUB)),
  ("dukhovny-fast-food", True, (Speak.Golub, Speak.Shevchenko, Speak.Shchelin)),
  ("lukewarm", True, reversed(GOLUB)),
  ("narrative-wars", True, GOLUB),
  ("eschatological-optimism", True, GOLUB),
]
GOLUB_OTHER = [
  ("polit_nemota", True, reversed(GOLUB)),
  ("straw_man", True, GOLUB),
  ("year2024", True, reversed(GOLUB)),
]


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
