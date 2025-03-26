import os


class Course:
    InSearchOfMeaning = "InSearchOfMeaning"


class Speak:
    Shchelin = "П.Щелин"
    Golub = "Е.Голуб"

SENTENCE_END = ".!?"

GOLUB_SHCHELIN = (Speak.Golub, Speak.Shchelin)
SHCHELIN_GOLUB = (Speak.Shchelin, Speak.Golub)

TXT = {
  Course.InSearchOfMeaning: {
    'Season01': [
      ("pinker", GOLUB_SHCHELIN),
    ]
  }
}


def in_search_of_meaning():
    data = TXT[Course.InSearchOfMeaning]
    for season in data:
        path = os.path.join('..', Course.InSearchOfMeaning, season)
        for name, speakers in data[season]:
            print(os.path.join(path, name + ".txt"))


def main():
    in_search_of_meaning()


if __name__ == '__main__':
    main()
