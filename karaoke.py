#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:15:41 2018

@author: ylillo
"""

import sys
import smallsmilhandler
from xml.sax import make_parser

if __name__ == "__main__":
    """
    Programa principal
    """
    if len(sys.argv) == 2:
        smil = smallsmilhandler.SmallSMILHandler()
        parser = make_parser()
        parser.setContentHandler(smil)
        parser.parse(open(sys.argv[1]))
        todo = smil.get_tags()
        for frase in todo:
            for atributo in frase:
                if frase[atributo] != "":
                    print(atributo, "=", frase[atributo], end='\t')
            print(end='\n')

    else:
        print("Usage: python3 karaoke.py file.smil.")
