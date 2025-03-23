import os


class Course:
    InSearchOfMeaning = "InSearchOfMeaning"
    GnosticThinking = "GnosticThinking"


class Speak:
    Schelin = "П.Щелин"
    Golub = "Е.Голуб"
    Romanenko = "Ю.Романенко"


SENTENCE_END = ".!?"
SPEAKER = len("Speaker 0: ")

GOLUB_SCHELIN = (Speak.Golub, Speak.Schelin)
SCHELIN_GOLUB = (Speak.Schelin, Speak.Golub)
ROMANENKO_SCHELIN = (Speak.Romanenko, Speak.Schelin)
SCHELIN_ROMANENKO = (Speak.Schelin, Speak.Romanenko)

SRT = {

  Course.GnosticThinking: [
    ("gnosticism", ROMANENKO_SCHELIN),
    ("modern", ROMANENKO_SCHELIN),
    ("gobs", ROMANENKO_SCHELIN),
    ("enlightenment", ROMANENKO_SCHELIN),
    ("nationalism", ROMANENKO_SCHELIN),

    ("marxism", SCHELIN_GOLUB),
    ("positivism", SCHELIN_GOLUB),
    ("deep_state", SCHELIN_GOLUB),
    ("info_wars", SCHELIN_GOLUB),
  ],

  Course.InSearchOfMeaning: {
    'Season01': [
      ("pinker", GOLUB_SCHELIN),
      ("apocalypse", SCHELIN_GOLUB),
      ("faust", SCHELIN_GOLUB),
      ("identity", SCHELIN_GOLUB),
      ("orange", GOLUB_SCHELIN),
      ("snowflakes", GOLUB_SCHELIN),
      ("limits", GOLUB_SCHELIN),
      ("ai", SCHELIN_GOLUB),
      ("vr", SCHELIN_GOLUB),
      ("mt", SCHELIN_GOLUB),
      ("otvety", GOLUB_SCHELIN),
      ("final", SCHELIN_GOLUB),
    ],
    'Season02': [
      ("your-flash-memory-card-with-identity", SCHELIN_GOLUB),
      ("placeandtime", SCHELIN_GOLUB),
      ("political-identity", GOLUB_SCHELIN),
      ("asabiya", SCHELIN_GOLUB),
      ("the-crisis-of-identity", SCHELIN_GOLUB),
      ("mimetic", SCHELIN_GOLUB),
      ("technology-instead-of-faith", GOLUB_SCHELIN),
      ("a-leap-of-faith", GOLUB_SCHELIN),
      ("identity-conclusion", GOLUB_SCHELIN),
      ("identity-qa", SCHELIN_GOLUB),
      ("monarchs-and-agenda", SCHELIN_GOLUB),
      ("the-joy-of-understanding", GOLUB_SCHELIN),
    ],
    'Season03': [
      ("republic", SCHELIN_GOLUB),
      ("democracy", GOLUB_SCHELIN),
      ("imperia", SCHELIN_GOLUB),
      ("people", SCHELIN_GOLUB),
      ("reforma", SCHELIN_GOLUB),
      ("renaissance", SCHELIN_GOLUB),
      ("varlaam", SCHELIN_GOLUB),
      ("bacon", SCHELIN_GOLUB),
      ("mendacium", GOLUB_SCHELIN),
      ("enlightenment", SCHELIN_GOLUB),
      ("obscurantism", GOLUB_SCHELIN),
      ("final3", SCHELIN_GOLUB),
      ("year2024", SCHELIN_GOLUB),
    ],
    'Season04': [
      ("ontology_of_lies", SCHELIN_GOLUB),
      ("freedom-and-quadrobers", SCHELIN_GOLUB),
      ("battle_of_the_sexes", GOLUB_SCHELIN),
      ("human_vs_humanity", GOLUB_SCHELIN),
      ("confession", SCHELIN_GOLUB),
      ("muses_of_tradition", GOLUB_SCHELIN),
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
        path = os.path.join('..', Course.InSearchOfMeaning, season)
        for name, speakers in data[season]:
            whisper(
              os.path.join(path, name + ".srt"),
              os.path.join("build", name + ".md"),
              speakers
            )


def gnostic_thinking():
    data = SRT[Course.GnosticThinking]
    path = os.path.join('..', Course.GnosticThinking)
    for name, speakers in data:
        whisper(
          os.path.join(path, name + ".srt"),
          os.path.join("build", name + ".md"),
          speakers
        )


def main():
    # in_search_of_meaning()
    gnostic_thinking()


if __name__ == '__main__':
    main()
