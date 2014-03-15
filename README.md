CLI-Builder
===========

A simple latex build script written in python that compiles all tex files in the current folder
with the output data in a temporary out folder.<br/>
After compilation it transfers the output .pdf or .dvi files to the current location.<br/>

usage: 
---------------------
python build.py [-h] [-p] [-l] [-b] [-c] [-d LANGUAGE] FILENAME<br/>

Options:
---------------------
optional arguments:<br/>
  -h, --help            show this help message and exit<br/>
  -p, --pdflatex        Use pdflatex to compile default is pdflatex<br/>
  -l, --latex           Use latex to compile default is pdflatex<br/>
  -b, --bibtex          Use bibtex to compile<br/>
  -c, --clean           Remove temporary files<br/>
  -d LANGUAGE, --language LANGUAGE<br/>
                        Specify the language to compile .tex files need to be
                        on the form filename-languagecode.tex for example CV-
                        EN.tex default is to compile all .tex files<br/>
   FILENAME 			IF supplied only builds the specified file<br/>
