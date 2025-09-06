import os
from text import Course, Speak, split_to_sentences

SPEAKER_MARK = "SPK_"
TXT_PATH = os.path.join('..', 'txt')
TXT = {
  Course.Mnenie: [
      ("2025_08_23", (Speak.Askerhanov, Speak.Shchelin)),
  ],
  Course.Uralov: [
      ("2025_08_21", (Speak.Kniazev, Speak.Uralov, Speak.Shchelin, Speak.Chadaev)),
  ],
  Course.Shelest: [
      ("2025_08_25", (Speak.Shelest, Speak.Shchelin)),
  ],
  Course.Dudnik: [
      ("2025_09_04", (Speak.Dudnik, Speak.Shchelin)),
  ],
  Course.Singles: [
      ("2025_09_04", (Speak.VKunev, Speak.Shchelin)),
      ("2025_09_06", (Speak.Golub, Speak.Shchelin, Speak.AKim)),
  ],
}


def proc_line(speaker_index, out, line, speakers):
    if SPEAKER_MARK in line:
        index = int(line.split(SPEAKER_MARK)[1]) - 1
        if speaker_index != index:
            out.write('\n')
            out.write("**{}:**\n".format(speakers[index]))
        return index

    for sentence in split_to_sentences(line):
        out.write(sentence)
        out.write('\n')

    return speaker_index


def proc_txt(in_file, out_file, speakers):
    print(in_file)
    lines = open(in_file, "rt", encoding="utf-8").readlines()
    out = open(out_file, "wt", encoding="utf-8")
    speaker_index = -1
    for line in lines:
        speaker_index = proc_line(speaker_index, out, line.strip(), speakers)

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
    podcast(Course.Mnenie)
    podcast(Course.Uralov)
    podcast(Course.Shelest)
    podcast(Course.Dudnik)
    podcast(Course.Singles)


if __name__ == '__main__':
    main()
