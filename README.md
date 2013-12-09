CLI-Builder
===========

Latex build script in python

usage: python build.py [-h] [-p] [-l] [-b] [-c] [-d LANGUAGE]
---------------------
Options:
---------------------
optional arguments:
  -h, --help            show this help message and exit<br/>
  -p, --pdflatex        Use pdflatex to compile default is pdflatex<br/>
  -l, --latex           Use latex to compile default is pdflatex<br/>
  -b, --bibtex          Use bibtex to compile<br/>
  -c, --clean           Remove temporary files<br/>
  -d LANGUAGE, --language LANGUAGE<br/>
                        Specify the language to compile .tex files need to be
                        on the form filename-languagecode.tex for example CV-
                        EN.tex default is to compile all .tex files
