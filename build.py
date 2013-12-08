#!/usr/bin/python
import argparse
import subprocess
import re
import string, random
import shutil, os
import logging
from subprocess import Popen, PIPE

# Parses arguments from cli
def parseCLIArguments():
    # TODO add arguments to specify temp folders 
    parser = argparse.ArgumentParser(description='Options')
    parser.add_argument("-p", "--pdflatex", action="store_true", 
        help="Use pdflatex to compile default is pdflatex", 
        default=True)
    parser.add_argument("-l", "--latex", action="store_true", 
        help="Use latex to compile default is pdflatex", 
        default=False)
    parser.add_argument("-b", "--bibtex", action="store_true", 
        help="Use bibtex to compile", 
        default=False)
    parser.add_argument("-c", "--clean", action="store_true", 
        help="Remove temporary files", 
        default=False)
    parser.add_argument("-d", "--language", type=str, 
        help="Specify the language to compile .tex files need to be on the" + 
        " form filename-languagecode.tex for example CV-EN.tex default is " +
        "to compile all .tex files", default=".tex")
    args = parser.parse_args()
    
    return args;

def folderPrep():
    logger.info("Creating temporary folder")
    subprocess.call(["mkdir", "-p", "out"])
    dstdir = "out/"
    return;

def compilePDFLatex(bib, lang):
    # adds .tex to lang if .tex is not supplied
    if(lang.endswith(".tex") != True):
        lang = lang + ".tex"
    for basename in os.listdir(os.getcwd()):
        if basename.endswith(lang):
            logger.info("Compiling "+ basename)
            try:
                if(bib):
                    logger.info("Bibtex for "+ basename)
                    err = subprocess.Popen(["pdflatex", "--output-directory", "out/",  basename ], stdout=PIPE)
                    output = err.communicate()[0]

                    logger.info("Running bibtex")
                    err = subprocess.Popen(["bibtex","out/" + basename[:-4]], stdout=PIPE)
                    output = err.communicate()[1]

                    err = subprocess.Popen(["pdflatex", "--output-directory", "out/",  basename ], stdout=PIPE)
                    output = err.communicate()[2]

                err = subprocess.Popen(["pdflatex", "--output-directory", "out/",  basename ], stdout=PIPE)
                output = err.communicate()[3]

            except Exception:
                logger.warning("Error while compiling " +  basename)
    return;

def compileLatex(bib, lang):
    # adds .tex to lang if .tex is not supplied
    if(lang.endswith(".tex") != True):
        lang = lang + ".tex"
    for basename in os.listdir(os.getcwd()):
        if basename.endswith(lang):
            logger.info("Compiling "+ basename)
            try:
                if( bib):
                    err = subprocess.Popen(["latex", "--output-directory", "out/",  basename ], stdout=PIPE)
                    output = err.communicate()[0]

                    logger.info("Running bibtex")
                    err = subprocess.Popen(["bibtex","out/" + basename[:-4]], stdout=PIPE)
                    output = err.communicate()[1]

                    err = subprocess.Popen(["latex", "--output-directory", "out/",  basename ], stdout=PIPE)
                    output = err.communicate()[2]

                err = subprocess.Popen(["latex", "--output-directory", "out/",  basename ], stdout=PIPE)
                output = err.communicate()[3]
            except Exception:
                logger.warning("Error while compiling " +  basename + " trace: " + output)
    return;
def moveresult():
    logger.info("Moving output from temp directory")
    for basename in os.listdir(os.getcwd() + "/out/"):
        if basename.endswith('.dvi') | basename.endswith('.pdf') :
            subprocess.call(["mv", "out/" + basename, "."])

    return;

# =============================================================================
# ======================== Main Program =======================================
# =============================================================================

logger = logging.getLogger("standard logger")
logger.setLevel(logging.INFO)
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

args = parseCLIArguments();
folderPrep()

if args.clean:
    subprocess.call(["rm", "-rf", "out"])
elif args.latex:
    logger.info("Using latex")
    compileLatex(args.bibtex, args.language)
    moveresult()
elif args.pdflatex:
    logger.info("Using pdflatex")
    compilePDFLatex(args.bibtex , args.language)
    moveresult()
