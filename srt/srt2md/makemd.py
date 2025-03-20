SENTENCE_END = ".!?"
SPEAKER = len("Speaker 0: ")

SRT_PATH = "../InSearchOfMeaning/Season04/"
SRT_EXT = ".srt"


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
    current_speaker = None
    while not eof:
        chunk = lines[start:start + 4]
        start += 4
        if len(chunk) < 4:
            eof = True
        else:
            item = chunk[2].strip()
            if diarization:
                speaker = speaker_index(item)
                if speaker != current_speaker:
                    text.append("\n{}\n".format(speaker))
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
    name = "muses_of_tradition"
    in_file = SRT_PATH + name + SRT_EXT
    out_file = "build/"  + name + ".md"
    whisper(in_file, out_file, True)


if __name__ == '__main__':
    main()
