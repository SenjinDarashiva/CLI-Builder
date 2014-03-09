#!/usr/bin/env python

# Copyright (C) Fredrik Loch 2013  CLI-Builder
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

__author__ = "Fredrik Loch"
__copyright__ = "Copyright 2013, CLI-Builder"
__license__ = "GPL"
__version__ = "2"
__maintainer__ = "Fredrik Loch"
__email__ = "fredrik.loch@bahnhof.se"
__status__ = "Development"


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
    if not os.path.exists("out"): os.makedirs("out")
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
                    output = err.communicate()[0]

                    err = subprocess.Popen(["pdflatex", "--output-directory", "out/",  basename ], stdout=PIPE)
                    output = err.communicate()[0]

                err = subprocess.Popen(["pdflatex", "--output-directory", "out/",  basename ], stdout=PIPE)
                output = err.communicate()[0]

            except Exception as e:
                logger.warning("Error while compiling " +  basename)
                logger.info(e)
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
                    logger.info("Bibtex for "+ basename)
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
                logger.warning("Error while compiling " +  basename)
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


if args.clean:
    try:
        shutil.rmtree("out")
    except FileNotFoundError:
        logger.info("Temp folder not found")
elif args.latex:
    folderPrep()
    logger.info("Using latex")
    compileLatex(args.bibtex, args.language)
    moveresult()
elif args.pdflatex:
    folderPrep()
    logger.info("Using pdflatex")
    compilePDFLatex(args.bibtex , args.language)
    moveresult()
