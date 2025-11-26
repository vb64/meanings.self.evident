import os
from text import Course, Speak, split_to_sentences

TS_LEN = len("00:00:00 ")
TXT_PATH = os.path.join('..', 'txt')
TXT = {
  Course.InSearchOfMeaning: [
      ("veritnelzyaproverit", (Speak.Golub, Speak.Shchelin)),
      ("osedlat-cherta", (Speak.Golub, Speak.Shchelin, Speak.AKim)),
      ("2025_10_04", (Speak.Golub, Speak.Shchelin)),
      ("silicon-overlords", (Speak.Golub, Speak.Golub, Speak.Shchelin, Speak.Shchelin, Speak.Golub)),
      ("the-existential-pub", (Speak.Golub, Speak.Shchelin, Speak.SGrigorishin)),
      ("the-ontological-hangover", (Speak.Golub, Speak.Shchelin)),
  ],
  Course.Mash: [
      ("2025_11_03", (Speak.Izotov, Speak.OrlovSm, Speak.Shchelin)),
  ],
  Course.Mnenie: [
      ("2025_08_23", (Speak.Askerhanov, Speak.Shchelin)),
      ("2025_09_30", (Speak.Askerhanov, Speak.Shchelin)),
  ],
  Course.Uralov: [
      ("2025_08_21", (Speak.Kniazev, Speak.Uralov, Speak.Shchelin, Speak.Chadaev)),
      ("2025_09_19", (Speak.Kniazev, Speak.Chadaev, Speak.Uralov, Speak.Shchelin)),
      ("2025_10_09", (Speak.Kniazev, Speak.Chadaev, Speak.Uralov, Speak.Shchelin)),
      ("2025_10_30", (Speak.Kniazev, Speak.Chadaev, Speak.Uralov, Speak.Shchelin)),
  ],
  Course.Shelest: [
      ("2025_08_25", (Speak.Shelest, Speak.Shchelin)),
      ("2025_09_08", (Speak.Shelest, Speak.Shchelin)),
      ("2025_09_16", (Speak.Shelest, Speak.Shchelin)),
      ("2025_10_20", (Speak.Shelest, Speak.Shchelin)),
      ("2025_11_10", (Speak.Shelest, Speak.Shchelin)),
  ],
  Course.Dudnik: [
      ("2025_09_04", (Speak.Dudnik, Speak.Shchelin)),
      ("2025_09_19", (Speak.Dudnik, Speak.Shchelin, Speak.Shchelin)),
      ("2025_10_24", (Speak.Dudnik, Speak.Shchelin)),
      ("2025_11_26", (Speak.Dudnik, Speak.Shchelin)),
  ],
  Course.Singles: [
      ("2025_09_04", (Speak.VKunev, Speak.Shchelin)),
      ("2025_09_06", (Speak.Golub, Speak.AKim, Speak.Shchelin)),
      ("2025_09_07", (Speak.DEvstafiev, Speak.Shchelin)),
      ("2025_09_09", (Speak.VFedosova, Speak.Shchelin)),
      ("2025_09_16", (Speak.VFedosova, Speak.Shchelin, Speak.VFedosova, Speak.Ads)),
      ("2025_10_21", (Speak.RSafarov, Speak.Shchelin)),
      ("2025_11_04", (Speak.Shchelin, Speak.SIvanov)),
  ],
  Course.Sobolev: [
      ("2025_10_19", (Speak.Sobolev, Speak.Shchelin)),
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


def get_speaker_index(line, text_speakers, real_speakers, speakers):
    if not is_timestamp(line):
        return None

    speaker = line[TS_LEN:]
    if speaker in text_speakers:
        real_speaker = speakers[text_speakers[speaker]]
    else:
        index = len(text_speakers)
        text_speakers[speaker] = index
        real_speaker = speakers[index]

    if real_speaker not in real_speakers:
        real_speakers.append(real_speaker)

    return real_speakers.index(real_speaker)


def proc_line(speaker_index, out, line, speakers, text_speakers, real_speakers):
    index = get_speaker_index(line, text_speakers, real_speakers, speakers)
    if index is not None:
        if speaker_index != index:
            out.write('\n')
            try:
                out.write("**{}:**\n".format(real_speakers[index]))
            except IndexError:
                err = "{}\nindex {}\nspeakers {}\ntext_speakers {}\nreal_speakers {}".format(
                  line,
                  index,
                  speakers,
                  text_speakers,
                  real_speakers
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
    real_speakers = []
    for line in lines:
        speaker_index = proc_line(speaker_index, out, line.strip(), speakers, text_speakers, real_speakers)

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
    podcast(Course.InSearchOfMeaning)
    podcast(Course.Sobolev)
    podcast(Course.Mash)


if __name__ == '__main__':
    main()
