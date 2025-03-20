import os

SENTENCE_END = ".!?"
SPEAKER = len("Speaker 0: ")

SPEAK_GOLUB = "Е.Голуб"
SPEAK_SCHELIN = "П.Щелин"
FIRST_GOLUB = (SPEAK_GOLUB, SPEAK_SCHELIN)
FIRST_SCHELIN = (SPEAK_SCHELIN, SPEAK_GOLUB)

SRT_PATH = os.path.join("..", "InSearchOfMeaning")

SRT = {
  'Season03': [
    ("republic", FIRST_GOLUB),
    ("democracy", FIRST_GOLUB),
    ("imperia", FIRST_GOLUB),
    ("people", FIRST_GOLUB),
    ("reforma", FIRST_GOLUB),
    ("renaissance", FIRST_GOLUB),
    ("varlaam", FIRST_GOLUB),
    ("bacon", FIRST_GOLUB),
    ("mendacium", FIRST_GOLUB),
    ("enlightenment", FIRST_GOLUB),
    ("obscurantism", FIRST_GOLUB),
    ("final3", FIRST_GOLUB),
    ("year2024", FIRST_GOLUB),
  ],
  'Season04': [
    ("ontology_of_lies", FIRST_GOLUB),
    ("freedom-and-quadrobers", FIRST_GOLUB),
    ("battle_of_the_sexes", FIRST_GOLUB),
    ("human_vs_humanity", FIRST_GOLUB),
    ("muses_of_tradition", FIRST_GOLUB),
  ],
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


def main():
    for season in SRT:
        path = os.path.join(SRT_PATH, season)
        for name, speakers in SRT[season]:
            whisper(
              os.path.join(path, name + ".srt"),
              os.path.join("build", name + ".md"),
              speakers
            )


if __name__ == '__main__':
    main()
