import os


class Course:
    InSearchOfMeaning = "InSearchOfMeaning"


class Speak:
    Shchelin = "П.Щелин"
    Golub = "Е.Голуб"

SENTENCE_END = ".!?"

TXT = {
  Course.InSearchOfMeaning: {
    'Season01': [
      ("pinker", (("Евгений Голуб:", Speak.Golub), ("Павел Щелин:", Speak.Shchelin))),
    ]
  }
}


def proc_txt(in_file, out_file, speakers):
    print(in_file)


def in_search_of_meaning():
    data = TXT[Course.InSearchOfMeaning]
    for season in data:
        path = os.path.join('..', Course.InSearchOfMeaning, season)
        for name, speakers in data[season]:
            proc_txt(
              os.path.join(path, name + ".txt"),
              os.path.join("build", name + ".md"),
              speakers
            )


def main():
    in_search_of_meaning()


if __name__ == '__main__':
    main()
