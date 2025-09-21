import os
from text import Course, Speak, split_to_sentences

TS_LEN = len("00:00:00 ")
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
      ("2025_09_08", (Speak.Shelest, Speak.Shchelin)),
      ("2025_09_16", (Speak.Shelest, Speak.Shchelin)),
  ],
  Course.Dudnik: [
      ("2025_09_04", (Speak.Dudnik, Speak.Shchelin)),
      ("2025_09_19", (Speak.Dudnik, Speak.Shchelin, Speak.Shchelin)),
  ],
  Course.Singles: [
      ("2025_09_04", (Speak.VKunev, Speak.Shchelin)),
      ("2025_09_06", (Speak.Golub, Speak.AKim, Speak.Shchelin)),
      ("2025_09_07", (Speak.DEvstafiev, Speak.Shchelin)),
      ("2025_09_09", (Speak.VFedosova, Speak.Shchelin)),
      ("2025_09_16", (Speak.VFedosova, Speak.Shchelin, Speak.VFedosova, Speak.Ads)),
  ],
}


# 00:00:22 Павел Щелин
def is_timestamp(line):
    items = line.split()
    if len(items) < 1:
        return False

    items = items[0].split(':')
    if len(items) != 3:
        return False

    return True


def get_speaker_index(line, text_speakers):
    if not is_timestamp(line):
        return None

    speaker = line[TS_LEN:]
    if speaker in text_speakers:
        return text_speakers[speaker]

    index = len(text_speakers)
    text_speakers[speaker] = index

    return index


def proc_line(speaker_index, out, line, speakers, text_speakers):
    index = get_speaker_index(line, text_speakers)
    if index is not None:
        if speaker_index != index:
            out.write('\n')
            try:
                out.write("**{}:**\n".format(speakers[index]))
            except IndexError:
                err = "{}\nindex {}\nspeakers {}\ntext_speakers {}".format(
                  line,
                  index,
                  speakers,
                  text_speakers
                )
                raise IndexError(err)

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
    text_speakers = {}
    for line in lines:
        speaker_index = proc_line(speaker_index, out, line.strip(), speakers, text_speakers)

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
