# Сборка pdf файлов

На платформе Windows для этого нужно предварительно установить следующие программы.

- [Python3](https://www.python.org/downloads/release/python-3810/)
- GNU [Unix Utils](http://unxutils.sourceforge.net/) для операций через makefile
- [Git for Windows](https://git-scm.com/download/win) для доступа к репозитарию исходных кодов.

Затем в окне командной строки склонировать репозитарий, перейти в каталог `scripts` и запустить установку, указав путь на Python 3.

```bash
git clone https://github.com/vb64/meanings.self.evident.git
cd meanings.self.evident\scripts
make setup PYTHON_BIN=C:\полный\путь\на\python.exe
```

Запустить сборку pdf файлов.

```bash
make pdf
```

Pdf-файлы подкастов будут созданы в подкаталоге `build`.
