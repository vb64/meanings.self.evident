import os
from text import Course, Speak

MD_PATH = os.path.join('..', 'md')
MDATA = {
  Course.InSearchOfMeaning: [
      ("Singles/2026_01_03", (Speak.Shchelin, Speak.Golub)),
      ("Singles/2026_01_05", (Speak.Shchelin, Speak.Golub)),
      ("Singles/2026_01_07", (Speak.Golub, Speak.Shchelin, Speak.Golub)),
      ("Singles/2026_01_09", (Speak.Shchelin, Speak.Golub)),
      ("Season05/end-of-willpower", (Speak.Shchelin, Speak.Golub)),
      ("Season06/what-is-freedom", (Speak.Shchelin, Speak.Golub)),
      ("Season06/the-only-questtion", (Speak.Golub, Speak.Shchelin)),
      ("Season06/memory", (Speak.Shchelin, Speak.Golub)),
  ],
  Course.NamingTheSelfEvident: [
      ("2026_02_27", (Speak.ShchelinEn, Speak.Hall_J)),
      ("2026_02_28", (Speak.Hall_J, Speak.ShchelinEn)),
      ("2026_03_01", (Speak.Hall_J, Speak.ShchelinEn)),
      ("2026_03_02", (Speak.Hall_J, Speak.ShchelinEn)),
      ("2026_03_03", (Speak.Hall_J, Speak.ShchelinEn)),
      ("2026_03_04", (Speak.ShchelinEn, Speak.Hall_J)),
      ("2026_03_05", (Speak.Hall_J, Speak.ShchelinEn)),
      ("2026_03_06", (Speak.ShchelinEn, Speak.Heers_J)),
      ("2026_03_09", (Speak.Pageau, Speak.ShchelinEn)),
      ("2026_03_12", (Speak.ShchelinEn, Speak.Rohlin)),
      ("2026_03_15", (Speak.ShchelinEn, Speak.Pageau)),
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
      ("2026_03_13", (Speak.Shchelin, Speak.Dudnik)),
  ],
  Course.Panchenko: [
      ("2025_12_04_1", (Speak.Panchenko, Speak.Shchelin)),
      ("2025_12_04_2", (Speak.Panchenko, Speak.MShevchenko, Speak.Shchelin)),
      ("2026_02_25", (Speak.Shchelin, Speak.Panchenko)),
  ],
  Course.Singles: [
      ("2025_12_07", (Speak.Shchelin, Speak.PAndreev)),
      ("2026_01_25", (Speak.Shchelin, Speak.Latynina)),
      ("2026_01_27", (Speak.Shchelin, Speak.NArutunov)),
      ("2026_02_01", (Speak.Shchelin, Speak.DEvstafiev)),
      ("2026_02_10", (Speak.Shchelin, Speak.AIvanchenko)),
      ("2026_03_18", (Speak.Shchelin, Speak.DZlobin)),
  ],
  Course.Safarov: [
      ("2025_12_23", (Speak.Shchelin, Speak.RSafarov)),
      ("2026_01_06", (Speak.Shchelin, Speak.RSafarov)),
      ("2026_02_03", (Speak.Shchelin, Speak.RSafarov)),
      ("2026_03_11", (Speak.Shchelin, Speak.RSafarov)),
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
      ("2026_03_13", (Speak.Shchelin, Speak.ATkachev)),
  ],
  Course.Sputnik: [
      ("2025_12_14", (Speak.Shchelin, Speak.POstrovsky, Speak.PUvarova)),
      ("2026_01_19", (Speak.PUvarova, Speak.POstrovsky, Speak.Shchelin)),
      ("2026_02_16", (Speak.Shchelin, Speak.POstrovsky, Speak.PUvarova)),
      ("2026_03_16", (Speak.POstrovsky, Speak.Shchelin, Speak.PUvarova)),
  ],
  Course.Chernov: [
      ("2026_03_18", (Speak.Shchelin, Speak.Chernov)),
  ],
}


def proc_md(in_file, out_file, speakers):
    print(in_file)
    body = open(in_file, "rt", encoding="utf-8").read()
    for i, speaker in enumerate(speakers):
        body = body.replace("SPK_{}:".format(i), "{}:".format(speaker))

    out_path = os.path.dirname(out_file)
    os.makedirs(out_path, exist_ok=True)
    with open(out_file, "wt", encoding="utf-8") as out:
        out.write(body)


def podcast(folder):
    data = MDATA[folder]
    path = os.path.join(MD_PATH, folder)
    out_path = os.path.join("build", folder)

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
    podcast(Course.NamingTheSelfEvident)
    podcast(Course.Chernov)

if __name__ == '__main__':
    main()
