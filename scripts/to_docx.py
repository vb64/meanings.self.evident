import os
from markdown_it import MarkdownIt


def main():
    fname = os.path.join("..", "content", "InSearchOfMeaning", "Season04", "muses_of_tradition.md")
    text = open(fname, "rt", encoding="utf-8").read()
    # zero, commonmark, js-default, gfm-like
    # https://markdown-it-py.readthedocs.io/en/latest/using.html#quick-start
    m_d = (MarkdownIt("commonmark").enable('table'))  # Enable support for tables
    html = m_d.render(text)

    print('#html', html)

    out_file = os.path.join("build", "muses_of_tradition.html")
    out = open(out_file, "wt", encoding="utf-8")
    out.write(html)
    out.close()


if __name__ == '__main__':
    main()
