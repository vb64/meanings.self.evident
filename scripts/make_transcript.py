import os
from text import Course, Speak, split_to_sentences

SPEAKER_MARK = "SPK_"
TXT_PATH = os.path.join('..', 'txt')
TXT = {
  Course.Mnenie: [
      ("2025_08_23", (Speak.Askerhanov, Speak.Shchelin)),
  ],
}


def proc_line(out, line, speakers):
    if SPEAKER_MARK in line:
        index = int(line.split(SPEAKER_MARK)[1]) - 1
        out.write('\n')
        out.write("**{}:**\n".format(speakers[index]))
        return

    for sentence in split_to_sentences(line):
        out.write(sentence)
        out.write('\n')


def proc_txt(in_file, out_file, speakers):
    print(in_file)
    lines = open(in_file, "rt", encoding="utf-8").readlines()
    out = open(out_file, "wt", encoding="utf-8")
    for line in lines:
        proc_line(out, line.strip(), speakers)

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


if __name__ == '__main__':
    main()
