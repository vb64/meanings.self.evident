import os


class Course:
    InSearchOfMeaning = "InSearchOfMeaning"
    GnosticThinking = "GnosticThinking"


class Speak:
    Shchelin = "П.Щелин"
    Golub = "Е.Голуб"
    Romanenko = "Ю.Романенко"


SENTENCE_END = ".!?"
SPEAKER = len("Speaker 0: ")

GOLUB_SHCHELIN = (Speak.Golub, Speak.Shchelin)
SHCHELIN_GOLUB = (Speak.Shchelin, Speak.Golub)
ROMANENKO_SHCHELIN = (Speak.Romanenko, Speak.Shchelin)
SHCHELIN_ROMANENKO = (Speak.Shchelin, Speak.Romanenko)

SRT_PATH = os.path.join('..', 'srt')

SRT = {

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
      ("year2024", SHCHELIN_GOLUB),
    ],
    'Season04': [
      ("ontology_of_lies", SHCHELIN_GOLUB),
      ("freedom-and-quadrobers", SHCHELIN_GOLUB),
      ("battle_of_the_sexes", GOLUB_SHCHELIN),
      ("human_vs_humanity", GOLUB_SHCHELIN),
      ("confession", SHCHELIN_GOLUB),
      ("muses_of_tradition", GOLUB_SHCHELIN),
      ("vinaiotvetsvennosti", GOLUB_SHCHELIN),
    ],
  },
}

def speaker_index(text):
    return int(text.split()[1].strip(':'))


def is_complete(sentence):
    return sentence[-1] in SENTENCE_END


def split_to_sentences(text):
    sentences = []
    current = []
    for word in text.split():
        current.append(word)
        if word[-1] in SENTENCE_END:
            sentences.append(' '.join(current))
            current = []

    if current:
        print("***WARN sentence: {}".format(text))
        sentences.append(' '.join(current))

    return sentences


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


def in_search_of_meaning():
    data = SRT[Course.InSearchOfMeaning]
    for season in data:
        path = os.path.join(SRT_PATH, Course.InSearchOfMeaning, season)
        for name, speakers in data[season]:
            whisper(
              os.path.join(path, name + ".srt"),
              os.path.join("build", name + ".md"),
              speakers
            )


def gnostic_thinking():
    data = SRT[Course.GnosticThinking]
    path = os.path.join(SRT_PATH, Course.GnosticThinking)
    for name, speakers in data:
        whisper(
          os.path.join(path, name + ".srt"),
          os.path.join("build", name + ".md"),
          speakers
        )

def private():
    whisper(
      os.path.join("build", "private.srt"),
      os.path.join("build", "private.md"),
      (Speak.Shchelin, "Speaker")
    )


def main():
    in_search_of_meaning()
    gnostic_thinking()
    # private()


if __name__ == '__main__':
    main()
