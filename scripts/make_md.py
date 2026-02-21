import os
from text import Course, Speak

MD_PATH = os.path.join('..', 'md')
MDATA = {
  Course.InSearchOfMeaning: [
      ("2026_01_03", (Speak.Shchelin, Speak.Golub)),
      ("2026_01_05", (Speak.Shchelin, Speak.Golub)),
      ("2026_01_07", (Speak.Golub, Speak.Shchelin, Speak.Golub)),
      ("2026_01_09", (Speak.Shchelin, Speak.Golub)),
      ("end-of-willpower", (Speak.Shchelin, Speak.Golub)),
  ],
  Course.Shelest: [
      ("2025_12_01", (Speak.Shelest, Speak.Shchelin)),
      ("2025_12_22", (Speak.Shchelin, Speak.Shelest)),
      ("2026_01_19", (Speak.Shchelin, Speak.Shelest)),
      ("2026_02_16", (Speak.Shchelin, Speak.Shelest)),
  ],
  Course.Dudnik: [
      ("2025_12_19", (Speak.Shchelin, Speak.Dudnik)),
      ("2026_01_23", (Speak.Shchelin, Speak.Dudnik)),
      ("2026_02_09", (Speak.Shchelin, Speak.Dudnik)),
  ],
  Course.Panchenko: [
      ("2025_12_04_1", (Speak.Panchenko, Speak.Shchelin)),
      ("2025_12_04_2", (Speak.Panchenko, Speak.MShevchenko, Speak.Shchelin)),
  ],
  Course.Singles: [
      ("2025_12_07", (Speak.Shchelin, Speak.PAndreev)),
      ("2026_01_25", (Speak.Shchelin, Speak.Latynina)),
      ("2026_01_27", (Speak.Shchelin, Speak.NArutunov)),
      ("2026_02_01", (Speak.Shchelin, Speak.DEvstafiev)),
      ("2026_02_10", (Speak.Shchelin, Speak.AIvanchenko)),
  ],
  Course.Safarov: [
      ("2025_12_23", (Speak.Shchelin, Speak.RSafarov)),
      ("2026_01_06", (Speak.Shchelin, Speak.RSafarov)),
      ("2026_02_03", (Speak.Shchelin, Speak.RSafarov)),
  ],
  Course.Uralov: [
      ("2026_01_15", (Speak.Kniazev, Speak.Chadaev, Speak.Shchelin, Speak.Shchelin, Speak.Chadaev, Speak.Uralov)),
      ("2026_02_19", (Speak.Kniazev, Speak.Shchelin, Speak.Uralov, Speak.Chadaev, Speak.Shchelin, Speak.Uralov, Speak.Kniazev)),
  ],
  Course.Tkachev: [
      ("2025_12_13", (Speak.Shchelin, Speak.ATkachev)),
      ("2026_01_04", (Speak.ATkachev, Speak.Shchelin)),
      ("2026_01_17", (Speak.ATkachev, Speak.Shchelin)),
      ("2026_02_14", (Speak.ATkachev, Speak.Shchelin)),
  ],
  Course.Sputnik: [
      ("2025_12_14", (Speak.Shchelin, Speak.POstrovsky, Speak.PUvarova)),
      ("2026_01_19", (Speak.PUvarova, Speak.POstrovsky, Speak.Shchelin)),
      ("2026_02_16", (Speak.Shchelin, Speak.POstrovsky, Speak.PUvarova)),
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
    podcast(Course.InSearchOfMeaning)
    podcast(Course.Sputnik)


if __name__ == '__main__':
    main()
