import os
from markdown_pdf import Section, MarkdownPdf

SOURCES = [
  ('', [('title.md', False)]),
]

ROOT = os.path.join('..', 'content', 'InSearchOfMeaning')

def hook(text):
    return text.replace(
      '# ', '### '
    )


def make_section(prefix, file_name, is_hook):
    folder = os.path.join(ROOT, prefix)
    text = open(os.path.join(folder, file_name), encoding="utf8").read()
    if is_hook:
        text = hook(text)

    return Section(text, root=folder)


sections = []
for prefix, file_list in SOURCES:
    for file_name, is_hook in file_list:
        sections.append(make_section(prefix, file_name, is_hook))
sections[0].toc = False

pdf = MarkdownPdf(toc_level=3)
pdf.meta["title"] = "Стенограммы подкаста «В поисках смысла» Евгения Голуба и Павла Щелина."
pdf.meta["author"] = "Vitaly Bogomolov mail@vitaly-bogomolov.ru"
for section in sections:
    pdf.add_section(section)
pdf.save(os.path.join('build', 'В_поисках_смысла.pdf'))
