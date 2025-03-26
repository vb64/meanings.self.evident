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
      ("pinker", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
      ("apocalypse", {"Евгений:": Speak.Golub, "Павел:": Speak.Shchelin}),
      ("faust", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
      ("limits", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
      ("snowflakes", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
    ],
  },
}


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


def proc_line(out, line, speakers):
    for speaker in speakers:
        if line.startswith(speaker):
            out.write('\n')
            out.write("**{}:**\n".format(speakers[speaker]))
            line = line[len(speaker):]
            break

    line = line.strip()
    if line.startswith('-'):
        line = line.lstrip('-')
    elif line.startswith('—'):
        line = line.lstrip('—')
    line = line.strip()

    for sentence in split_to_sentences(line):
        out.write(sentence)
        out.write('\n')


def proc_txt(in_file, out_file, speakers):
    print(in_file)
    lines = open(in_file, "rt", encoding="utf-8").readlines()
    out = open(out_file, "wt", encoding="utf-8")
    for line in lines:
        proc_line(out, line, speakers)

    out.close()


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
