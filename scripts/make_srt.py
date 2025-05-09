import os
from text import Course, Speak, split_to_sentences, is_complete

SPEAKER = len("Speaker 0: ")
SRT_PATH = os.path.join('..', 'srt')

GOLUB_SHCHELIN = (Speak.Golub, Speak.Shchelin)
SHCHELIN_GOLUB = (Speak.Shchelin, Speak.Golub)
GOLUB_SHCHELIN_SHEVCHENKO = (Speak.Golub, Speak.Shevchenko, Speak.Shchelin)

ROMANENKO_SHCHELIN = (Speak.Romanenko, Speak.Shchelin)
SHCHELIN_ROMANENKO = (Speak.Shchelin, Speak.Romanenko)

SHCHELIN_IZOTOV_ORLOV = (Speak.Shchelin, Speak.Izotov, Speak.OrlovSm)

SHELEST_SHCHELIN = (Speak.Shelest, Speak.Shchelin)
SHCHELIN_SHELEST = (Speak.Shchelin, Speak.Shelest)
SHCHELIN_BONDARENKO_SHELEST = (Speak.Shchelin, Speak.Bondarenko, Speak.Shelest)

SHCHELIN_PANCHENKO = (Speak.Shchelin, Speak.Panchenko)
PANCHENKO_SHCHELIN = (Speak.Panchenko, Speak.Shchelin)

SHCHELIN_TRANS_PANCHENKO = (Speak.Shchelin, Speak.Translator, Speak.Panchenko)
SHCHELIN_PANCHENKO_TRANS = (Speak.Shchelin, Speak.Panchenko, Speak.Translator)

SHCHELIN_DUDNIK = (Speak.Shchelin, Speak.Dudnik)
SHCHELIN_DUDNIK_TRANS = (Speak.Shchelin, Speak.Dudnik, Speak.Translator)
DUDNIK_SHCHELIN = (Speak.Dudnik, Speak.Shchelin)
KHAZIN_SHCHELIN_DUDNIK = (Speak.Khazin, Speak.Shchelin, Speak.Dudnik)

SRT = {

  Course.Mash: [
    ("2025_03_28", SHCHELIN_IZOTOV_ORLOV),
  ],

  Course.Panchenko: [
    ("2024_06_22", SHCHELIN_PANCHENKO),
    ("2024_11_06", SHCHELIN_PANCHENKO),
    ("2025_01_23", SHCHELIN_PANCHENKO_TRANS),
    ("2025_02_24", SHCHELIN_TRANS_PANCHENKO),
    ("2025_04_06", SHCHELIN_PANCHENKO),
  ],

  Course.Dudnik: [
    ("2022_11_03", SHCHELIN_DUDNIK),
    ("2024_05_14", SHCHELIN_DUDNIK),
    ("2024_06_04", SHCHELIN_DUDNIK),
    ("2024_07_09", SHCHELIN_DUDNIK),
    ("2024_08_14", SHCHELIN_DUDNIK_TRANS),
    ("2024_09_13", SHCHELIN_DUDNIK),
    ("2024_10_02", SHCHELIN_DUDNIK),
    ("2024_10_14", SHCHELIN_DUDNIK),
    ("2024_11_04", SHCHELIN_DUDNIK),
    ("2024_11_23", SHCHELIN_DUDNIK),
    ("2024_12_26", SHCHELIN_DUDNIK),
    ("2025_01_15", DUDNIK_SHCHELIN),
    ("2025_02_19", SHCHELIN_DUDNIK),
    ("2025_03_11", SHCHELIN_DUDNIK),
    ("2025_03_22", SHCHELIN_DUDNIK),
    ("2025_03_25", KHAZIN_SHCHELIN_DUDNIK),
    ("2025_04_24", SHCHELIN_DUDNIK),
  ],

  Course.Shelest: [
    ("2023_02_09", SHCHELIN_SHELEST),
    ("2023_04_01", SHCHELIN_SHELEST),
    ("2023_05_04", SHCHELIN_SHELEST),
    ("2023_06_21", SHCHELIN_SHELEST),
    ("2023_07_15", SHCHELIN_SHELEST),
    ("2023_08_03", SHCHELIN_SHELEST),
    ("2023_08_30", SHCHELIN_SHELEST),
    ("2023_09_23", SHCHELIN_SHELEST),
    ("2023_10_12", SHELEST_SHCHELIN),
    ("2023_11_02", SHELEST_SHCHELIN),
    ("2023_11_22", SHELEST_SHCHELIN),
    ("2023_11_23", SHELEST_SHCHELIN),
    ("2023_12_13", SHCHELIN_SHELEST),
    ("2023_12_28", SHELEST_SHCHELIN),
    ("2024_01_19", SHELEST_SHCHELIN),
    ("2024_02_10", SHCHELIN_SHELEST),
    ("2024_03_14", SHCHELIN_SHELEST),
    ("2024_04_03", SHCHELIN_SHELEST),
    ("2024_04_24", SHCHELIN_SHELEST),
    ("2024_05_10", SHCHELIN_SHELEST),
    ("2024_05_29", SHELEST_SHCHELIN),
    ("2024_06_15", SHCHELIN_SHELEST),
    ("2024_06_26", SHELEST_SHCHELIN),
    ("2024_08_07", SHCHELIN_SHELEST),
    ("2024_08_19", SHCHELIN_SHELEST),
    ("2024_09_04", SHCHELIN_SHELEST),
    ("2024_09_26", SHELEST_SHCHELIN),
    ("2024_10_10", SHELEST_SHCHELIN),
    ("2024_10_25", SHELEST_SHCHELIN),
    ("2024_11_12", SHCHELIN_SHELEST),
    ("2024_11_30", SHCHELIN_SHELEST),
    ("2024_12_10", SHCHELIN_SHELEST),
    ("2024_12_24", SHELEST_SHCHELIN),
    ("2025_01_11", SHELEST_SHCHELIN),
    ("2025_01_27", SHELEST_SHCHELIN),
    ("2025_02_11", SHELEST_SHCHELIN),
    ("2025_02_22", SHELEST_SHCHELIN),
    ("2025_03_06", SHCHELIN_SHELEST),
    ("2025_03_17", SHCHELIN_SHELEST),
    ("2025_03_31", SHCHELIN_BONDARENKO_SHELEST),
    ("2025_04_09", SHELEST_SHCHELIN),
    ("2025_04_21", SHCHELIN_SHELEST),
  ],

  Course.GnosticThinking: [
    ("gnosticism", SHCHELIN_ROMANENKO),
    ("modern", SHCHELIN_ROMANENKO),
    ("gobs", SHCHELIN_ROMANENKO),
    ("enlightenment", SHCHELIN_ROMANENKO),
    ("nationalism", ROMANENKO_SHCHELIN),

    ("marxism", SHCHELIN_GOLUB),
    ("positivism", SHCHELIN_GOLUB),
    ("deep_state", SHCHELIN_GOLUB),
    ("info_wars", GOLUB_SHCHELIN),
  ],

  Course.InSearchOfMeaning: {
    'Season01': [
      ("pinker", GOLUB_SHCHELIN),
      ("apocalypse", SHCHELIN_GOLUB),
      ("faust", SHCHELIN_GOLUB),
      ("identity", SHCHELIN_GOLUB),
      ("orange", GOLUB_SHCHELIN),
      ("snowflakes", GOLUB_SHCHELIN),
      ("limits", GOLUB_SHCHELIN),
      ("ai", SHCHELIN_GOLUB),
      ("vr", SHCHELIN_GOLUB),
      ("mt", SHCHELIN_GOLUB),
      ("otvety", GOLUB_SHCHELIN),
      ("final", SHCHELIN_GOLUB),
    ],
    'Season02': [
      ("your-flash-memory-card-with-identity", SHCHELIN_GOLUB),
      ("placeandtime", SHCHELIN_GOLUB),
      ("political-identity", GOLUB_SHCHELIN),
      ("asabiya", SHCHELIN_GOLUB),
      ("the-crisis-of-identity", SHCHELIN_GOLUB),
      ("mimetic", SHCHELIN_GOLUB),
      ("technology-instead-of-faith", GOLUB_SHCHELIN),
      ("a-leap-of-faith", GOLUB_SHCHELIN),
      ("identity-conclusion", GOLUB_SHCHELIN),
      ("identity-qa", SHCHELIN_GOLUB),
      ("monarchs-and-agenda", SHCHELIN_GOLUB),
      ("the-joy-of-understanding", GOLUB_SHCHELIN),
    ],
    'Season03': [
      ("republic", SHCHELIN_GOLUB),
      ("democracy", GOLUB_SHCHELIN),
      ("imperia", SHCHELIN_GOLUB),
      ("people", SHCHELIN_GOLUB),
      ("reforma", SHCHELIN_GOLUB),
      ("renaissance", SHCHELIN_GOLUB),
      ("varlaam", SHCHELIN_GOLUB),
      ("bacon", SHCHELIN_GOLUB),
      ("mendacium", GOLUB_SHCHELIN),
      ("enlightenment", SHCHELIN_GOLUB),
      ("obscurantism", GOLUB_SHCHELIN),
      ("final3", SHCHELIN_GOLUB),
    ],
    'Season04': [
      ("ontology_of_lies", SHCHELIN_GOLUB),
      ("freedom-and-quadrobers", SHCHELIN_GOLUB),
      ("battle_of_the_sexes", GOLUB_SHCHELIN),
      ("human_vs_humanity", GOLUB_SHCHELIN),
      ("confession", SHCHELIN_GOLUB),
      ("muses_of_tradition", GOLUB_SHCHELIN),
      ("vinaiotvetsvennosti", GOLUB_SHCHELIN),
      ("the-courage-to-be", SHCHELIN_GOLUB),
      ("dukhovny-fast-food", GOLUB_SHCHELIN_SHEVCHENKO),
      ("lukewarm", SHCHELIN_GOLUB),
    ],
    'Other': [
      ("polit_nemota", SHCHELIN_GOLUB),
      ("straw_man", GOLUB_SHCHELIN),
      ("year2024", SHCHELIN_GOLUB),
    ],
  },
}

def speaker_index(text):
    return int(text.split()[1].strip(':'))


def write_sentence(out, text):
    for i in split_to_sentences(text):
        out.write(i)
        out.write('\n')


def whisper(in_file, out_file, speakers):
    print(out_file)
    lines = open(in_file, "rt", encoding="utf-8").readlines()
    start = 0
    text = []
    eof = False
    current_speaker = None
    while not eof:
        chunk = lines[start:start + 4]
        start += 4
        if len(chunk) < 4:
            eof = True
        else:
            item = chunk[2].strip()
            if speakers:
                speaker = speaker_index(item)
                if speaker != current_speaker:
                    text.append("\n**{}:**\n".format(speakers[speaker]))
                    current_speaker = speaker
                item = item[SPEAKER:]

            text.append(item)

    out = open(out_file, "wt", encoding="utf-8")
    group = []
    for sentence in text:
        if sentence.startswith('\n'):  # speaker sign
            if group:
                write_sentence(out, ' '.join(group))
            group = []
            out.write(sentence)
            continue

        group.append(sentence)
        if is_complete(sentence):
            write_sentence(out, ' '.join(group))
            group = []

    out.close()


def call_whisper(path, name, speakers):
    whisper(
      os.path.join(path, name + ".srt"),
      os.path.join("build", name + ".md"),
      speakers
    )


def in_search_of_meaning():
    data = SRT[Course.InSearchOfMeaning]
    for season in data:
        path = os.path.join(SRT_PATH, Course.InSearchOfMeaning, season)
        for name, speakers in data[season]:
            call_whisper(path, name, speakers)


def podcast(name):
    data = SRT[name]
    path = os.path.join(SRT_PATH, name)
    for name, speakers in data:
        call_whisper(path, name, speakers)


def main():
    in_search_of_meaning()
    podcast(Course.GnosticThinking)
    podcast(Course.Mash)
    podcast(Course.Shelest)
    podcast(Course.Panchenko)
    podcast(Course.Dudnik)


if __name__ == '__main__':
    main()
