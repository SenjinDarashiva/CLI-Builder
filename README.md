CLI-Builder
===========

Latex build script in python

usage: python build.py [-h] [-p] [-l] [-b] [-c] [-d LANGUAGE]

Options:

optional arguments:
  -h, --help            show this help message and exit
  -p, --pdflatex        Use pdflatex to compile default is pdflatex
  -l, --latex           Use latex to compile default is pdflatex
  -b, --bibtex          Use bibtex to compile
  -c, --clean           Remove temporary files
  -d LANGUAGE, --language LANGUAGE
                        Specify the language to compile .tex files need to be
                        on the form filename-languagecode.tex for example CV-
                        EN.tex default is to compile all .tex files
