import os
from markdown_pdf import Section, MarkdownPdf

AUTHOR = "Vitaly Bogomolov mail@vitaly-bogomolov.ru"

IN_SEARCH_OF_MEANING = [
  ('', [('title.md', False)]),

  ('Season01', [
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

  ('Season02', [
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

  ('Season03', [
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
    ("year2024.md", True),
  ]),

  ('Season04', [
    ('title.md', False),
    ("ontology_of_lies.md", True),
    ("freedom-and-quadrobers.md", True),
    ("battle_of_the_sexes.md", True),
    ("human_vs_humanity.md", True),
    ("confession_on_the_couch.md", True),
    ("muses_of_tradition.md", True),
    ("vinaiotvetsvennosti.md", True),
  ]),
]

GNOSTIC_THINKING = [
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
]

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
    sections = make_sections(
      IN_SEARCH_OF_MEANING,
      os.path.join('..', 'content', 'InSearchOfMeaning')
    )
    sections[0].toc = False

    pdf = MarkdownPdf(toc_level=3)
    pdf.meta["title"] = "Стенограммы подкаста «В поисках смысла» Евгения Голуба и Павла Щелина."
    pdf.meta["author"] = AUTHOR
    for section in sections:
        pdf.add_section(section, user_css=CSS)
    pdf.save(os.path.join('build', 'В_поисках_смысла.pdf'))


def gnostic_thinking():
    sections = make_sections(
      GNOSTIC_THINKING,
      os.path.join('..', 'content', 'GnosticThinking')
    )
    sections[0].toc = False

    pdf = MarkdownPdf(toc_level=3)
    pdf.meta["title"] = "Cтенограммы цикла «Гностическое Мышление»."
    pdf.meta["author"] = AUTHOR
    for section in sections:
        pdf.add_section(section)
    pdf.save(os.path.join('build', 'Гностическое_мышление.pdf'))


def main():
    in_search_of_meaning()
    gnostic_thinking()


if __name__ == '__main__':
    main()
