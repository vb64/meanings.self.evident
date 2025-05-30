import os
from text import Course, Speak, split_to_sentences

TXT_PATH = os.path.join('..', 'txt')
TXT = {

  Course.InSearchOfMeaning: [
      ("pinker", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
      ("apocalypse", {"Евгений:": Speak.Golub, "Павел:": Speak.Shchelin}),
      ("faust", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
      ("limits", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
      ("snowflakes", {"Евгений Голуб:": Speak.Golub, "Павел Щелин:": Speak.Shchelin}),
  ],

  Course.Chernov: [
      ("2024_04_23", {"Алексей:": Speak.Chernov, "Павел:": Speak.Shchelin}),
  ],

  Course.GnosticThinking: [
      ("gnosticism", {"Романенко:": Speak.Romanenko, "Щелин:": Speak.Shchelin}),
      ("modern", {"Романенко:": Speak.Romanenko, "Щелин:": Speak.Shchelin}),
      ("deep_state", {"Е.Голуб:": Speak.Golub, "П.Щелин:": Speak.Shchelin}),
  ],
}


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

    if not line:
        out.write('\n')
        return

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


def podcast(folder):
    data = TXT[folder]
    path = os.path.join(TXT_PATH, folder)
    out_path = os.path.join("build", folder)
    os.makedirs(out_path, exist_ok=True)

    for name, speakers in data:
        proc_txt(
          os.path.join(path, name + ".txt"),
          os.path.join(out_path, name + ".md"),
          speakers
        )


def main():
    podcast(Course.InSearchOfMeaning)
    podcast(Course.Chernov)
    podcast(Course.GnosticThinking)


if __name__ == '__main__':
    main()
