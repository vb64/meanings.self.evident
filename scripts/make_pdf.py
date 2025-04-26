import os
from markdown_pdf import Section, MarkdownPdf
from text import Course

AUTHOR = "Vitaly Bogomolov mail@vitaly-bogomolov.ru"
CONTENT = os.path.join('..', 'content')


class InSearchOfMeaning:
    Season01 = 'Season01'
    Season02 = 'Season02'
    Season03 = 'Season03'
    Season04 = 'Season04'
    Other = 'Other'


IN_SEARCH_OF_MEANING_SEASONS = [
  InSearchOfMeaning.Season01,
  InSearchOfMeaning.Season02,
  InSearchOfMeaning.Season03,
  InSearchOfMeaning.Season04,
  InSearchOfMeaning.Other,
]

IN_SEARCH_OF_MEANING = [
  ('', [('title.md', False)]),

  (InSearchOfMeaning.Season01, [
    ('title.md', False),
    ("pinker.md", True),
    ("apocalypse.md", True),
    ("faust.md", True),
    ("identity.md", True),
    ("orange.md", True),
    ("snowflakes.md", True),
    ("limits.md", True),
    ("ai.md", True),
    ("vr.md", True),
    ("mt.md", True),
    ("otvety.md", True),
    ("final.md", True),
  ]),

  (InSearchOfMeaning.Season02, [
    ('title.md', False),
    ("your-flash-memory-card-with-identity.md", True),
    ("placeandtime.md", True),
    ("political-identity.md", True),
    ("asabiya.md", True),
    ("the-crisis-of-identity.md", True),
    ("mimetic.md", True),
    ("technology-instead-of-faith.md", True),
    ("a-leap-of-faith.md", True),
    ("identity-conclusion.md", True),
    ("identity-qa.md", True),
    ("monarchs-and-agenda.md", True),
    ("the-joy-of-understanding.md", True),
  ]),

  (InSearchOfMeaning.Season03, [
    ('title.md', False),
    ("republic.md", True),
    ("democracy.md", True),
    ("imperia.md", True),
    ("people.md", True),
    ("reforma.md", True),
    ("renaissance.md", True),
    ("varlaam.md", True),
    ("bacon.md", True),
    ("mendacium.md", True),
    ("enlightenment.md", True),
    ("obscurantism.md", True),
    ("final3.md", True),
  ]),

  (InSearchOfMeaning.Season04, [
    ('title.md', False),
    ("ontology_of_lies.md", True),
    ("freedom-and-quadrobers.md", True),
    ("battle_of_the_sexes.md", True),
    ("human_vs_humanity.md", True),
    ("confession_on_the_couch.md", True),
    ("muses_of_tradition.md", True),
    ("vinaiotvetsvennosti.md", True),
    ("the-courage-to-be.md", True),
    ("dukhovny-fast-food.md", True),
  ]),

  (InSearchOfMeaning.Other, [
    ('title.md', False),
    ("polit_nemota.md", True),
    ("straw_man.md", True),
    ("year2024.md", True),
  ]),
]

PODCAST = {
  Course.GnosticThinking: [
    ('', [('title.md', False)]),
    ('', [('gnosticism.md', False)]),
    ('', [('modern.md', False)]),
    ('', [('gobs.md', False)]),
    ('', [('enlightenment.md', False)]),
    ('', [('nationalism.md', False)]),
    ('', [('marxism.md', False)]),
    ('', [('positivism.md', False)]),
    ('', [('deep_state.md', False)]),
    ('', [('info_wars.md', False)]),
  ],

  Course.Mash: [
    ('', [('title.md', False)]),
    ('', [('2025_03_28.md', False)]),
  ],

  Course.Panchenko: [
    ('', [('title.md', False)]),
    ('', [('2024_06_22.md', False)]),
    ('', [('2025_02_24.md', False)]),
    ('', [('2025_04_06.md', False)]),
  ],

  Course.Shelest: [
    ('', [('title.md', False)]),
    ('', [('2023_02_09.md', False)]),
    ('', [('2023_04_01.md', False)]),
    ('', [('2023_05_04.md', False)]),
    ('', [('2023_06_21.md', False)]),
    ('', [('2023_07_15.md', False)]),
    ('', [('2023_08_03.md', False)]),
    ('', [('2023_08_30.md', False)]),
    ('', [('2023_09_23.md', False)]),
    ('', [('2023_10_12.md', False)]),
    ('', [('2023_11_02.md', False)]),
    ('', [('2023_11_22.md', False)]),
    ('', [('2023_11_23.md', False)]),
    ('', [('2023_12_13.md', False)]),
    ('', [('2023_12_28.md', False)]),
    ('', [('2024_01_19.md', False)]),
    ('', [('2024_02_10.md', False)]),
    ('', [('2024_03_14.md', False)]),
    ('', [('2024_04_03.md', False)]),
    ('', [('2024_04_24.md', False)]),
    ('', [('2024_05_10.md', False)]),
    ('', [('2024_05_29.md', False)]),
    ('', [('2024_06_15.md', False)]),
    ('', [('2024_06_26.md', False)]),
    ('', [('2024_08_07.md', False)]),
    ('', [('2024_08_19.md', False)]),
    ('', [('2024_09_04.md', False)]),
    ('', [('2024_09_26.md', False)]),
    ('', [('2024_10_10.md', False)]),
    ('', [('2024_10_25.md', False)]),
    ('', [('2024_11_12.md', False)]),
    ('', [('2024_11_30.md', False)]),
    ('', [('2024_12_10.md', False)]),
    ('', [('2024_12_24.md', False)]),
    ('', [('2025_01_11.md', False)]),
    ('', [('2025_01_27.md', False)]),
    ('', [('2025_02_11.md', False)]),
    ('', [('2025_02_22.md', False)]),
    ('', [('2025_03_06.md', False)]),
    ('', [('2025_03_17.md', False)]),
    ('', [('2025_03_31.md', False)]),
    ('', [('2025_04_09.md', False)]),
    ('', [('2025_04_21.md', False)]),
  ],
}

CSS = "h1 {text-align:center;}"

def hook(text):
    return text.replace(
      '# ', '## '
    )


def make_section(prefix, file_name, is_hook, root):
    folder = os.path.join(root, prefix)
    text = open(os.path.join(folder, file_name), encoding="utf8").read()
    if is_hook:
        text = hook(text)

    return Section(text, root=folder)


def make_sections(src, root):
    sections = []
    for prefix, file_list in src:
        for file_name, is_hook in file_list:
            sections.append(make_section(prefix, file_name, is_hook, root))

    return sections


def in_search_of_meaning():
    root = os.path.join(CONTENT, Course.InSearchOfMeaning)
    sections = make_sections(IN_SEARCH_OF_MEANING, root)
    sections[0].toc = False

    pdf = MarkdownPdf(toc_level=3)
    pdf.meta["title"] = "Стенограммы подкаста «В поисках смысла» Евгения Голуба и Павла Щелина."
    pdf.meta["author"] = AUTHOR
    for section in sections:
        pdf.add_section(section, user_css=CSS)
    pdf.save(os.path.join('build', 'В_поисках_смысла.pdf'))

    for season, file_list in IN_SEARCH_OF_MEANING:
        if season not in IN_SEARCH_OF_MEANING_SEASONS:
            continue

        sections = []
        for file_name, is_hook in file_list:
            sections.append(make_section(season, file_name, is_hook, root))

        pdf = MarkdownPdf(toc_level=3)
        pdf.meta["title"] = season
        pdf.meta["author"] = AUTHOR
        for section in sections:
            pdf.add_section(section, user_css=CSS)
        pdf.save(os.path.join('build', season + '.pdf'))


def podcast(name, title, pdf_name):
    sections = make_sections(
      PODCAST[name],
      os.path.join(CONTENT, name)
    )
    sections[0].toc = False

    pdf = MarkdownPdf(toc_level=3)
    pdf.meta["title"] = title
    pdf.meta["author"] = AUTHOR
    for section in sections:
        pdf.add_section(section)
    pdf.save(os.path.join('build', pdf_name))


def private(name, title, pdf_name):
    pdf = MarkdownPdf(toc_level=3)
    pdf.meta["title"] = title
    pdf.meta["author"] = AUTHOR
    section = make_section('', name, False, 'build')
    pdf.add_section(section)
    pdf.save(os.path.join('build', pdf_name))


def main():
    # private('private.md', 'April_6_session_1', 'April_6_session_1.pdf')
    in_search_of_meaning()
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


if __name__ == '__main__':
    main()
