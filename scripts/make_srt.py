import os
from text import Course, Speak, split_to_sentences, is_complete

SPEAKER = len("Speaker 0: ")
SRT_PATH = os.path.join('..', 'srt')

GOLUB = (Speak.Golub, Speak.Shchelin)
ROMANENKO = (Speak.Romanenko, Speak.Shchelin)
SHELEST = (Speak.Shelest, Speak.Shchelin)
PANCHENKO = (Speak.Panchenko, Speak.Shchelin)
DUDNIK = (Speak.Dudnik, Speak.Shchelin)
CHERNOV = (Speak.Chernov, Speak.Shchelin)
BOBYLEV = (Speak.Bobileff, Speak.Shchelin)
ARESTOVICH = (Speak.Arestovich, Speak.Shchelin)
KOTAR = (Speak.Kotar, Speak.Shchelin)
BAUMEISTER = (Speak.Baumeister, Speak.Shchelin)
CHERNOBAEV = (Speak.Chernobaev, Speak.Shchelin)
KHIMICH = (Speak.Khimich, Speak.Shchelin)
ASKERHANOV = (Speak.Askerhanov, Speak.Shchelin)

ROHLIN = (Speak.Rohlin, Speak.ShchelinEn)
PAGEAU = (Speak.Pageau, Speak.ShchelinEn)
HALLJ = (Speak.Hall_J, Speak.ShchelinEn)
HEERSJ = (Speak.Heers_J, Speak.ShchelinEn)

SRT = {

  Course.Arestovich: [
    ('2021_12_24', ARESTOVICH),
    ('2021_12_29', ARESTOVICH),
    ('2022_01_17', ARESTOVICH),
    ('2022_02_07', reversed(ARESTOVICH)),
    ('2022_02_09', reversed(ARESTOVICH)),
    ('2022_02_18', reversed(ARESTOVICH)),
    ('2022_04_22', reversed(ARESTOVICH)),
    ('2022_05_31', reversed(ARESTOVICH)),
    ('2022_07_19', reversed(ARESTOVICH)),
    ('2022_08_20', (Speak.Datsuk, Speak.Romanenko, Speak.Arestovich, Speak.Shchelin)),  # Feldman
    ('2022_09_19', reversed(ARESTOVICH)),
    ('2022_10_04', reversed(ARESTOVICH)),
    ('2022_12_27', reversed(ARESTOVICH)),
    ('2023_02_12', ARESTOVICH),
  ],

  Course.Baumeister: [
    ('2022_04_18', BAUMEISTER),
    ('2022_05_17', BAUMEISTER),
    ('2025_02_19', (Speak.Baumeister, Speak.Shchelin, Speak.Golub)),
  ],

  Course.Chernobaev: [
    ('2024_08_15', (Speak.Chernobaev, Speak.Shchelin, Speak.Ads)),
    ('2024_09_27', reversed(CHERNOBAEV)),
    ('2024_11_22', reversed(CHERNOBAEV)),
  ],

  Course.Usa: [
    ('2022_01_06', reversed(ARESTOVICH)),
    ('2022_01_10', ROMANENKO),
    ('2022_01_14', reversed(ROMANENKO)),
  ],

  Course.English: [
    ('2024_05_04', ROHLIN),
    ('2024_05_31', KOTAR),
    ('2024_06_12', reversed(ROHLIN)),
    ('2024_06_22', reversed(PAGEAU)),
    ('2024_09_17', PAGEAU),
    ('2024_10_14', KOTAR),
    ('2025_01_20', HALLJ),
    ('2025_03_21', reversed(HEERSJ)),
  ],

  Course.Mash: [
    ("2025_03_28", (Speak.Shchelin, Speak.Izotov, Speak.OrlovSm)),
    ('2025_05_25', (Speak.OrlovSm, Speak.Shchelin, Speak.Izotov)),
  ],

  Course.Chernov: [
    ("2023_12_16", reversed(CHERNOV)),
    ("2024_04_16", CHERNOV),
    ("2024_04_23", reversed(CHERNOV)),
    ("2024_05_22", reversed(CHERNOV)),
    ("2024_08_13", reversed(CHERNOV)),
    ("2025_04_07", reversed(CHERNOV)),
  ],

  Course.Panchenko: [
    ("2024_06_22", reversed(PANCHENKO)),
    ("2024_11_06", reversed(PANCHENKO)),
    ("2025_01_23", (Speak.Shchelin, Speak.Panchenko, Speak.Translator)),
    ("2025_02_24", (Speak.Shchelin, Speak.Translator, Speak.Panchenko)),
    ("2025_04_06", reversed(PANCHENKO)),
    ("2025_05_16", reversed(PANCHENKO)),
  ],

  Course.Dudnik: [
    ("2022_11_03", reversed(DUDNIK)),
    ("2024_05_14", reversed(DUDNIK)),
    ("2024_06_04", reversed(DUDNIK)),
    ("2024_07_09", reversed(DUDNIK)),
    ("2024_08_14", (Speak.Shchelin, Speak.Dudnik, Speak.Ads)),
    ("2024_09_13", reversed(DUDNIK)),
    ("2024_10_02", reversed(DUDNIK)),
    ("2024_10_14", reversed(DUDNIK)),
    ("2024_11_04", reversed(DUDNIK)),
    ("2024_11_23", reversed(DUDNIK)),
    ("2024_12_26", reversed(DUDNIK)),
    ("2025_01_15", DUDNIK),
    ("2025_02_19", reversed(DUDNIK)),
    ("2025_03_11", reversed(DUDNIK)),
    ("2025_03_22", reversed(DUDNIK)),
    ("2025_03_25", (Speak.Khazin, Speak.Shchelin, Speak.Dudnik)),
    ("2025_04_24", reversed(DUDNIK)),
    ("2025_05_23", reversed(DUDNIK)),
  ],

  Course.Shelest: [
    ("2023_02_09", reversed(SHELEST)),
    ("2023_04_01", reversed(SHELEST)),
    ("2023_05_04", reversed(SHELEST)),
    ("2023_06_21", reversed(SHELEST)),
    ("2023_07_15", reversed(SHELEST)),
    ("2023_08_03", reversed(SHELEST)),
    ("2023_08_30", reversed(SHELEST)),
    ("2023_09_23", reversed(SHELEST)),
    ("2023_10_12", SHELEST),
    ("2023_11_02", SHELEST),
    ("2023_11_22", SHELEST),
    ("2023_11_23", SHELEST),
    ("2023_12_13", reversed(SHELEST)),
    ("2023_12_28", SHELEST),
    ("2024_01_19", SHELEST),
    ("2024_02_10", reversed(SHELEST)),
    ("2024_03_14", reversed(SHELEST)),
    ("2024_04_03", reversed(SHELEST)),
    ("2024_04_24", reversed(SHELEST)),
    ("2024_05_10", reversed(SHELEST)),
    ("2024_05_29", SHELEST),
    ("2024_06_15", reversed(SHELEST)),
    ("2024_06_26", SHELEST),
    ("2024_08_07", reversed(SHELEST)),
    ("2024_08_19", reversed(SHELEST)),
    ("2024_09_04", reversed(SHELEST)),
    ("2024_09_26", SHELEST),
    ("2024_10_10", SHELEST),
    ("2024_10_25", SHELEST),
    ("2024_11_12", reversed(SHELEST)),
    ("2024_11_30", reversed(SHELEST)),
    ("2024_12_10", reversed(SHELEST)),
    ("2024_12_24", SHELEST),
    ("2025_01_11", SHELEST),
    ("2025_01_27", SHELEST),
    ("2025_02_11", SHELEST),
    ("2025_02_22", SHELEST),
    ("2025_03_06", reversed(SHELEST)),
    ("2025_03_17", reversed(SHELEST)),
    ("2025_03_31", (Speak.Shchelin, Speak.Bondarenko, Speak.Shelest)),
    ("2025_04_09", SHELEST),
    ("2025_04_21", reversed(SHELEST)),
    ("2025_05_12", reversed(SHELEST)),
    ('2025_05_27', reversed(SHELEST)),
  ],

  Course.GnosticThinking: [
    ("gnosticism", reversed(ROMANENKO)),
    ("modern", reversed(ROMANENKO)),
    ("gobs", reversed(ROMANENKO)),
    ("enlightenment", reversed(ROMANENKO)),
    ("nationalism", ROMANENKO),

    ("marxism", reversed(GOLUB)),
    ("positivism", reversed(GOLUB)),
    ("deep_state", reversed(GOLUB)),
    ("info_wars", GOLUB),
  ],

  Course.InSearchOfMeaning: [

    # Season01
    ("pinker", GOLUB),
    ("apocalypse", reversed(GOLUB)),
    ("faust", reversed(GOLUB)),
    ("identity", reversed(GOLUB)),
    ("orange", GOLUB),
    ("snowflakes", GOLUB),
    ("limits", GOLUB),
    ("ai", reversed(GOLUB)),
    ("vr", reversed(GOLUB)),
    ("mt", reversed(GOLUB)),
    ("otvety", GOLUB),
    ("final", reversed(GOLUB)),

    # Season02
    ("your-flash-memory-card-with-identity", reversed(GOLUB)),
    ("placeandtime", reversed(GOLUB)),
    ("political-identity", GOLUB),
    ("asabiya", reversed(GOLUB)),
    ("the-crisis-of-identity", reversed(GOLUB)),
    ("mimetic", reversed(GOLUB)),
    ("technology-instead-of-faith", GOLUB),
    ("a-leap-of-faith", GOLUB),
    ("identity-conclusion", GOLUB),
    ("identity-qa", reversed(GOLUB)),
    ("monarchs-and-agenda", reversed(GOLUB)),
    ("the-joy-of-understanding", GOLUB),

    # Season03
    ("republic", reversed(GOLUB)),
    ("democracy", GOLUB),
    ("imperia", reversed(GOLUB)),
    ("people", reversed(GOLUB)),
    ("reforma", reversed(GOLUB)),
    ("renaissance", reversed(GOLUB)),
    ("varlaam", reversed(GOLUB)),
    ("bacon", reversed(GOLUB)),
    ("mendacium", GOLUB),
    ("enlightenment", reversed(GOLUB)),
    ("obscurantism", GOLUB),
    ("final3", reversed(GOLUB)),

    # Season04
    ("ontology_of_lies", reversed(GOLUB)),
    ("freedom-and-quadrobers", reversed(GOLUB)),
    ("battle_of_the_sexes", GOLUB),
    ("human_vs_humanity", GOLUB),
    ("confession", reversed(GOLUB)),
    ("muses_of_tradition", GOLUB),
    ("vinaiotvetsvennosti", GOLUB),
    ("the-courage-to-be", reversed(GOLUB)),
    ("dukhovny-fast-food", (Speak.Golub, Speak.Shevchenko, Speak.Shchelin)),
    ("lukewarm", reversed(GOLUB)),
    ("narrative-wars", GOLUB),

    # Other
    ("polit_nemota", reversed(GOLUB)),
    ("straw_man", GOLUB),
    ("year2024", reversed(GOLUB)),
  ],

  Course.Bobileff: [
    ('2022_09_10', BOBYLEV),
    ('2022_09_12', BOBYLEV),
    ('2023_09_10', (Speak.Shchelin, Speak.Bobileff, Speak.Boglaev)),
    ('2023_09_13', reversed(BOBYLEV)),
    ('2023_10_03', (Speak.Boglaev, Speak.Shchelin, Speak.Bobileff)),
    ('2023_10_12', (Speak.Bobileff, Speak.Shchelin, Speak.Boglaev)),
    ('2023_10_15', BOBYLEV),
    ('2023_10_18', BOBYLEV),
    ('2023_12_01', BOBYLEV),
    ('2023_12_03', (Speak.Shchelin, Speak.Bobileff, Speak.Ads)),
    ('2024_01_18', BOBYLEV),
    ('2024_01_20', BOBYLEV),
    ('2024_03_25', BOBYLEV),
    ('2024_04_21', BOBYLEV),
    ('2024_04_24', reversed(BOBYLEV)),
    ('2024_06_06', BOBYLEV),
    ('2024_06_11', BOBYLEV),
    ('2024_07_13', reversed(BOBYLEV)),
    ('2024_07_15', BOBYLEV),
    ('2024_10_05', (Speak.Burov, Speak.Shchelin, Speak.Bobileff)),
    ('2024_10_12', (Speak.Bobileff, Speak.Burov, Speak.Shchelin)),
    ('2024_11_20', reversed(BOBYLEV)),
    ('2024_11_21', reversed(BOBYLEV)),
    ('2025_01_12', BOBYLEV),
    ('2025_01_14', reversed(BOBYLEV)),
    ('2025_02_03', reversed(BOBYLEV)),
    ('2025_03_25', BOBYLEV),
    ('2025_03_26', reversed(BOBYLEV)),
    ('2025_04_25', BOBYLEV),
    ('2025_04_28', BOBYLEV),
  ],

  Course.Khimich: [
    ('2022_11_25', KHIMICH),
    ('2022_12_11', KHIMICH),
    ('2023_01_31', reversed(KHIMICH)),
    ('2024_03_20', KHIMICH),
  ],

  Course.Mnenie: [
    ('2025_01_16', ASKERHANOV),
    ('2025_02_10', reversed(ASKERHANOV)),
    ('2025_03_09', reversed(ASKERHANOV)),
    ('2025_03_24', (Speak.Shchelin, Speak.Askerhanov, Speak.Nadolinsky)),
    ('2025_05_02', (Speak.Askerhanov, Speak.Shchelin, Speak.Guest)),
    ('2025_05_16', ASKERHANOV),
  ],

  Course.PolitWorld: [
    ('2023_04_25', (Speak.Itskovich, Speak.Shchelin)),
    ('2023_11_03', (Speak.Safronov, Speak.Shchelin)),
    ('2023_11_30', (Speak.Leybin, Speak.Shchelin)),
    ('2023_12_13', (Speak.Gromov, Speak.Shchelin)),
  ],

  Course.Singles: [
    ('2014_05_08', (Speak.Shchelin, )),
    ('2021_12_28', ROMANENKO),
    ('2022_03_04', (Speak.Romanenko, Speak.Shchelin)),
    ('2022_04_04', (Speak.Belkovsky, Speak.Shchelin)),
    ('2022_04_08', (Speak.Kusa, Speak.Shchelin)),
    ('2022_06_13', (Speak.Burov, Speak.Shchelin)),
    ('2022_08_27', (Speak.Svetov, Speak.Shchelin)),
    ('2025_05_08', (Speak.Klizma, Speak.Shchelin)),
  ],

  Course.Uralov: [
    ('2024_12_25', (Speak.Ads, Speak.Shchelin)),
    ('2025_01_29', (Speak.Ads, Speak.Shchelin)),
    ('2025_03_06', (Speak.Ads, Speak.Shchelin)),
    ('2025_04_03', (Speak.Ads, Speak.Shchelin)),
    ('2025_05_15', (Speak.Ads, Speak.Shchelin)),
  ],

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


def call_whisper(path, out_path, name, speakers):
    whisper(
      os.path.join(path, name + ".srt"),
      os.path.join(out_path, name + ".md"),
      speakers
    )


def podcast(name):
    data = SRT[name]
    path = os.path.join(SRT_PATH, name)
    out_path = os.path.join("build", name)
    os.makedirs(out_path, exist_ok=True)

    for name, speakers in data:
        call_whisper(path, out_path, name, list(speakers))


def main():
    for i in (
      # Course.InSearchOfMeaning,
      # Course.GnosticThinking,
      # Course.Mash,
      # Course.Shelest,
      # Course.Panchenko,
      # Course.Dudnik,
      # Course.Chernov,
      # Course.English,
      # Course.Usa,
      # Course.Bobileff,
      # Course.Arestovich,
      # Course.Baumeister,
      # Course.Chernobaev,
      Course.Khimich,
      Course.Mnenie,
      # Course.PolitWorld,
      # Course.Singles,
      # Course.Uralov,
    ):
        podcast(i)


if __name__ == '__main__':
    main()
