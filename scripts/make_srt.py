import os
from text import (
  Course, split_to_sentences, is_complete,
  GOLUB_SEASON_01, GOLUB_SEASON_02, GOLUB_SEASON_03, GOLUB_SEASON_04, GOLUB_OTHER,
  COURSE_ARESTOVICH, COURSE_BAUMEISTER, COURSE_CHERNOBAEV, COURSE_GNOSTIC, COURSE_USA,
  COURSE_ENGLISH, COURSE_MASH, COURSE_CHERNOV, COURSE_PANCHENKO, COURSE_DUDNIK,
  COURSE_SHELEST, COURSE_BOBYLEV, COURSE_KHIMICH, COURSE_ASKERHANOV, COURSE_POLITWORLD,
  COURSE_SINGLES, COURSE_URALOV, COURSE_SOBOLEV,
)

def for_md(data):
    return [(name, speak) for name, hook, speak in data]

SPEAKER = len("Speaker 0: ")
SRT_PATH = os.path.join('..', 'srt')
SRT = {
  Course.Arestovich: for_md(COURSE_ARESTOVICH),
  Course.Baumeister: for_md(COURSE_BAUMEISTER),
  Course.Chernobaev: for_md(COURSE_CHERNOBAEV),
  Course.Usa: for_md(COURSE_USA),
  Course.English: for_md(COURSE_ENGLISH),
  Course.Mash: for_md(COURSE_MASH),
  Course.Chernov: for_md(COURSE_CHERNOV),
  Course.Panchenko: for_md(COURSE_PANCHENKO),
  Course.Dudnik: for_md(COURSE_DUDNIK),
  Course.Shelest: for_md(COURSE_SHELEST),
  Course.GnosticThinking: for_md(COURSE_GNOSTIC),
  Course.Bobileff: for_md(COURSE_BOBYLEV),
  Course.Khimich: for_md(COURSE_KHIMICH),
  Course.Mnenie: for_md(COURSE_ASKERHANOV),
  Course.PolitWorld: for_md(COURSE_POLITWORLD),
  Course.Singles: for_md(COURSE_SINGLES),
  Course.Uralov: for_md(COURSE_URALOV),
  Course.Sobolev: for_md(COURSE_SOBOLEV),
  Course.InSearchOfMeaning: for_md(
    GOLUB_SEASON_01 + GOLUB_SEASON_02 + GOLUB_SEASON_03 + GOLUB_SEASON_04 + GOLUB_OTHER
  ),
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
      Course.InSearchOfMeaning,
      Course.GnosticThinking,
      Course.Mash,
      Course.Shelest,
      Course.Panchenko,
      Course.Dudnik,
      Course.Chernov,
      Course.English,
      Course.Usa,
      Course.Bobileff,
      Course.Arestovich,
      Course.Baumeister,
      Course.Chernobaev,
      Course.Khimich,
      Course.Mnenie,
      Course.PolitWorld,
      Course.Singles,
      Course.Uralov,
      Course.Sobolev,
    ):
        podcast(i)


if __name__ == '__main__':
    main()
