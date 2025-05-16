import os
import sys

def get_link(folder, fname):
    fname = os.path.join(folder, fname)
    inp = open(fname, 'rt', encoding='utf-8')
    lines = inp.readlines()
    inp.close()

    for line in lines:
        if '[Аудиоверсия]' in line:
            return line.split('](')[1].split(')')[0]


folder = sys.argv[1]

inp = open(os.path.join(folder, 'README.md'), 'rt', encoding='utf-8')
lines = inp.readlines()
inp.close()

for line in lines:
    if line.startswith('- [ ] '):
        fname = line.split('](')[1].split(')')[0]
        print(fname, get_link(folder, fname))
