import os
from text import Course, Speak

MD_PATH = os.path.join('..', 'md')
MDATA = {
  Course.Shelest: [
      ("2025_12_01", (Speak.Shelest, Speak.Shchelin)),
      ("2025_12_22", (Speak.Shchelin, Speak.Shelest)),
  ],
  Course.Dudnik: [
      ("2025_12_19", (Speak.Shchelin, Speak.Dudnik)),
  ],
  Course.Panchenko: [
      ("2025_12_04_1", (Speak.Panchenko, Speak.Shchelin)),
      ("2025_12_04_2", (Speak.Panchenko, Speak.MShevchenko, Speak.Shchelin)),
  ],
  Course.Singles: [
      ("2025_12_07", (Speak.Shchelin, Speak.PAndreev)),
      ("2025_12_14", (Speak.Shchelin, Speak.POstrovsky, Speak.PUvarova)),
  ],
  Course.Safarov: [
      ("2025_12_23", (Speak.Shchelin, Speak.RSafarov)),
      ("2026_01_06", (Speak.Shchelin, Speak.RSafarov)),
  ],
  Course.Uralov: [
      ("2026_01_15", (Speak.Kniazev, Speak.Chadaev, Speak.Shchelin, Speak.Shchelin, Speak.Chadaev, Speak.Uralov)),
  ],
  Course.Tkachev: [
      ("2025_12_13", (Speak.Shchelin, Speak.ATkachev)),
      ("2026_01_04", (Speak.ATkachev, Speak.Shchelin)),
      ("2026_01_17", (Speak.ATkachev, Speak.Shchelin)),
  ],
}


def proc_md(in_file, out_file, speakers):
    print(in_file)
    body = open(in_file, "rt", encoding="utf-8").read()
    for i, speaker in enumerate(speakers):
        body = body.replace("SPK_{}:".format(i), "{}:".format(speaker))

    with open(out_file, "wt", encoding="utf-8") as out:
        out.write(body)


def podcast(folder):
    data = MDATA[folder]
    path = os.path.join(MD_PATH, folder)
    out_path = os.path.join("build", folder)
    os.makedirs(out_path, exist_ok=True)

    for name, speakers in data:
        proc_md(
          os.path.join(path, name + ".md"),
          os.path.join(out_path, name + ".md"),
          speakers
        )


def main():
    podcast(Course.Shelest)
    podcast(Course.Panchenko)
    podcast(Course.Singles)
    podcast(Course.Dudnik)
    podcast(Course.Safarov)
    podcast(Course.Uralov)
    podcast(Course.Tkachev)


if __name__ == '__main__':
    main()
