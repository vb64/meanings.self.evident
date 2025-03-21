import os
from markdown_it import MarkdownIt
from docx import Document
from htmldocx import HtmlToDocx

# IMG_SIGN = "<img src=\""

def main():
    folder = os.path.join("..", "content", "InSearchOfMeaning", "Season04")
    fname = os.path.join(folder, "muses_of_tradition.md")
    text = open(fname, "rt", encoding="utf-8").read()
    # zero, commonmark, js-default, gfm-like
    # https://markdown-it-py.readthedocs.io/en/latest/using.html#quick-start
    m_d = (MarkdownIt("commonmark").enable('table'))  # Enable support for tables

    # image_path = IMG_SIGN + folder + os.sep
    # html = m_d.render(text).replace(IMG_SIGN, image_path)
    html = m_d.render(text)

    # print('#html', html)
    # out_file = os.path.join("build", "muses_of_tradition.html")
    # out = open(out_file, "wt", encoding="utf-8")
    # out.write(html)
    # out.close()

    # https://github.com/pqzx/html2docx
    document = Document()
    parser = HtmlToDocx()
    parser.add_html_to_document(html, document)
    document.save(os.path.join("build", 'muses_of_tradition.docx'))


if __name__ == '__main__':
    main()
