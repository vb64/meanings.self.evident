import os
from markdown_pdf import Section, MarkdownPdf

from text import (
  Course,
  GOLUB_SEASON_01, GOLUB_SEASON_02, GOLUB_SEASON_03, GOLUB_SEASON_04, GOLUB_OTHER,
  COURSE_ARESTOVICH, COURSE_BAUMEISTER, COURSE_CHERNOBAEV, COURSE_GNOSTIC, COURSE_USA,
  COURSE_ENGLISH, COURSE_MASH, COURSE_CHERNOV, COURSE_PANCHENKO, COURSE_DUDNIK,
  COURSE_SHELEST, COURSE_BOBYLEV, COURSE_KHIMICH, COURSE_ASKERHANOV, COURSE_POLITWORLD,
  COURSE_SINGLES, COURSE_URALOV,
)

def for_pdf(data):
    return [(name + '.md', hook) for name, hook, speak in data]

AUTHOR = "Vitaly Bogomolov mail@vitaly-bogomolov.ru"
CONTENT = os.path.join('..', 'content')
TITLE = [('title.md', False)]
PODCAST = {
  Course.InSearchOfMeaning: (
    TITLE + 
    [('title_01.md', False)] + for_pdf(GOLUB_SEASON_01) + 
    [('title_02.md', False)] + for_pdf(GOLUB_SEASON_02) + 
    [('title_03.md', False)] + for_pdf(GOLUB_SEASON_03) + 
    [('title_04.md', False)] + for_pdf(GOLUB_SEASON_04) + 
    [('title_other.md', False)] + for_pdf(GOLUB_OTHER)
  ),

  Course.GnosticThinking: (TITLE + for_pdf(COURSE_GNOSTIC)),
  Course.Mash: (TITLE + for_pdf(COURSE_MASH)),
  Course.Panchenko: (TITLE + for_pdf(COURSE_PANCHENKO)),
  Course.Shelest: (TITLE + for_pdf(COURSE_SHELEST)),
  Course.Dudnik: (TITLE + for_pdf(COURSE_DUDNIK)),
  Course.Chernov: (TITLE + for_pdf(COURSE_CHERNOV)),
  Course.English: (TITLE + for_pdf(COURSE_ENGLISH)),
  Course.Bobileff: (TITLE + for_pdf(COURSE_BOBYLEV)),
  Course.Usa: (TITLE + for_pdf(COURSE_USA)),
  Course.Arestovich: (TITLE + for_pdf(COURSE_ARESTOVICH)),
  Course.Baumeister: (TITLE + for_pdf(COURSE_BAUMEISTER)),
  Course.Chernobaev: (TITLE + for_pdf(COURSE_CHERNOBAEV)),
  Course.Khimich: (TITLE + for_pdf(COURSE_KHIMICH)),
  Course.Mnenie: (TITLE + for_pdf(COURSE_ASKERHANOV)),
  Course.PolitWorld: (TITLE + for_pdf(COURSE_POLITWORLD)),
  Course.Singles: (TITLE + for_pdf(COURSE_SINGLES)),
  Course.Uralov: (TITLE + for_pdf(COURSE_URALOV)),
}

CSS = "h1 {text-align:center;}"

def hook(text):
    return text.replace(
      '# ', '## '
    )


def make_section(file_name, is_hook, folder):
    text = open(os.path.join(folder, file_name), encoding="utf8").read()
    if is_hook:
        text = hook(text)

    return Section(text, root=folder)


def podcast(name, title, pdf_name):
    root = os.path.join(CONTENT, name)
    sections = [
      make_section(file_name, is_hook, root)
      for file_name, is_hook in PODCAST[name]
    ]
    sections[0].toc = False

    pdf = MarkdownPdf(toc_level=3)
    pdf.meta["title"] = title
    pdf.meta["author"] = AUTHOR
    for section in sections:
        pdf.add_section(section)
    pdf.save(os.path.join('build', pdf_name))


def main():
    podcast(
      Course.InSearchOfMeaning,
      "Стенограммы подкаста «В поисках смысла» Евгения Голуба и Павла Щелина.",
      'В_поисках_смысла.pdf'
    )
    podcast(
      Course.GnosticThinking,
      "Cтенограммы цикла «Гностическое Мышление».",
      'Гностическое_мышление.pdf'
    )
    podcast(
      Course.Mash,
      "Cтенограммы подкастов «Mash Room».",
      'Mash_Room.pdf'
    )
    podcast(
      Course.Shelest,
      "Cтенограммы эфиров с А.Шелестом.",
      'Шелест.pdf'
    )
    podcast(
      Course.Panchenko,
      "Cтенограммы эфиров с Д.Панченко.",
      'Панченко.pdf'
    )
    podcast(
      Course.Dudnik,
      "Cтенограммы эфиров с С.Дудником.",
      'Дудник.pdf'
    )
    podcast(
      Course.Chernov,
      "Cтенограммы эфиров с А.Черновым. По следам Пеликана.",
      'Чернов.pdf'
    )
    podcast(
      Course.English,
      "Playlist `Videos with English Speaking guests` at the 'Pavel Shchelin' YouTube channel.",
      'English.pdf'
    )
    podcast(
      Course.Usa,
      "Стенограммы плейлиста 'Архетипы США' YouTube-канала @PavelShchelin.",
      'Архетипы_США.pdf'
    )
    podcast(
      Course.Bobileff,
      "Стенограммы роликов из плейлиста 'Павел Щелин' YouTube канала 'Александр Бобылев и НАРОД'.",
      'Бобылев_и_НАРОД.pdf'
    )
    podcast(
      Course.Baumeister,
      "Беседы с Андреем Баумейстером.",
      'Баумейстер.pdf'
    )
    podcast(
      Course.Arestovich,
      "Стенограммы роликов из плейлиста 'Беседы с Павлом Щелиным' на YouTube канале 'Alexey Arestovych'",
      'Арестович.pdf'
    )
    podcast(
      Course.Chernobaev,
      "Стенограммы роликов из YouTube канала 'Николай Чернобаев'.",
      'Чернобаев.pdf'
    )
    podcast(
      Course.Khimich,
      "Беседы с Романом Химичем.",
      'Химич.pdf'
    )
    podcast(
      Course.Mnenie,
      "Камиль Аскерханов. YouTube канал 'Мнение'.",
      'Мнение.pdf'
    )
    podcast(
      Course.PolitWorld,
      "Эфиры на YouTube канале polit.world.",
      'polit_world.pdf'
    )
    podcast(
      Course.Singles,
      "Отдельные беседы.",
      'Отдельные_беседы.pdf'
    )
    podcast(
      Course.Uralov,
      "Эфиры с Чадаевым и Ураловым 'Чистота Понимания'.",
      'Чистота_Понимания.pdf'
    )


if __name__ == '__main__':
    main()
