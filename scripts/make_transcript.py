import os
from text import Course, Speak

TXT_PATH = os.path.join('..', 'txt')
TXT = {
  Course.Mnenie: [
      ("2025_08_23", (Speak.Askerhanov, Speak.Shchelin)),
  ],
}


def proc_txt(in_file, out_file, _speakers):
    print(in_file, '->', out_file)


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
