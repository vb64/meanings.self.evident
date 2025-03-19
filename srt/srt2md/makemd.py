SENTENCE_END = ".!?"
SPEAKER = len("Speaker 0: ")

SRT_PATH = "../InSearchOfMeaning/Season04/"
SRT_EXT = ".srt"


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
        raise Exception("Wrong sentence: {}".format(text))

    return sentences


def write_sentence(out, text):
    for i in split_to_sentences(text):
        out.write(i)
        out.write('\n')


def whisper(in_file, out_file, diarization):
    print(in_file, "->", out_file)
    lines = open(in_file, "rt", encoding="utf-8").readlines()
    start = 0
    text = []
    eof = False
    while not eof:
        chunk = lines[start:start + 4]
        start += 4
        if len(chunk) < 4:
            eof = True
        else:
            item = chunk[2].strip()
            if diarization:
                item = item[SPEAKER:]
            text.append(item)

    out = open(out_file, "wt", encoding="utf-8")
    group = []
    for sentence in text:
        group.append(sentence)
        if is_complete(sentence):
            write_sentence(out, ' '.join(group))
            group = []

    out.close()


def main():
    name = "muses_of_tradition"
    in_file = SRT_PATH + name + SRT_EXT
    out_file = "build/"  + name + ".md"
    whisper(in_file, out_file, True)


if __name__ == '__main__':
    main()
