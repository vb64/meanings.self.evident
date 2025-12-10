import os
from text import Course, Speak

MD_PATH = os.path.join('..', 'md')
MDATA = {
  Course.Shelest: [
      ("2025_12_01", (Speak.Shelest, Speak.Shchelin)),
  ],
  Course.Panchenko: [
      ("2025_12_04_1", (Speak.Panchenko, Speak.Shchelin)),
      ("2025_12_04_2", (Speak.Panchenko, Speak.MShevchenko, Speak.Shchelin)),
  Course.Singles: [
      ("2025_12_07", (Speak.Shchelin, Speak.PAndreev)),
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


if __name__ == '__main__':
    main()
