#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:15:41 2018

@author: ylillo
"""

import sys
import smallsmilhandler
import json
import urllib.request
from xml.sax import make_parser


class KaraokeLocal:

    def __init__(self, archivo):
        try:
            archivo = sys.argv[1]
            smil = smallsmilhandler.SmallSMILHandler()
            parser = make_parser()
            parser.setContentHandler(smil)
            parser.parse(open(archivo))
            self.todo = smil.get_tags()

        except FileNotFoundError:
            sys.exit('File not found')

    def __str__(self):
        r = ''
        for frase in self.todo:
            for atributo in frase:
                if frase[atributo] != "":
                    r += atributo + "=" + "'" + frase[atributo] + "'" + '\t'
            r += '\n'
        return r

    def to_json(self, smil, ficherojson=''):
        if ficherojson == '':
            ficherojson = smil.replace('.smil', '.json')

        with open(ficherojson, 'w') as filejson:
            json.dump(self.todo, filejson, indent=3)

    def do_local(self):
        for frase in self.todo:
            for atributo in frase:
                if atributo == "src":
                    if frase[atributo].startswith('http://'):
                        direccion = frase[atributo].split('/')[-1]
                        urllib.request.urlretrieve(frase[atributo])
                        frase[atributo] = direccion


if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        archivo = sys.argv[1]
        karaoke = KaraokeLocal(archivo)

    except IndexError:
        sys.exit('usage error: python3 karaoke.py file.smil')
    karaoke.to_json(archivo)
    karaoke.do_local()
    karaoke.to_json(archivo, 'local.json')
    print(karaoke)
