#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.todo = []

    def startElement(self, name, attrs):
        if name == "root-layout":
            self.width = attrs.get("width", "")
            self.height = attrs.get("height", "")
            self.background_color = attrs.get("background-color", "")
            self.todo.append(name)
            self.todo.append({"width": self.width, "height": self.height,
                              "background-color": self.background_color})
        elif name == "region":
            self.id = attrs.get("id", "")
            self.top = attrs.get("top", "")
            self.bottom = attrs.get("bottom", "")
            self.left = attrs.get("left", "")
            self.right = attrs.get("right", "")
            self.todo.append(name)
            self.todo.append({"id": self.id, "top": self.top,
                              "bottom": self.bottom, "left": self.left,
                              "right": self.right})
        elif name == "img":
            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.todo.append(name)
            self.todo.append({"src": self.src, "region": self.region,
                              "begin": self.begin, "dur": self.dur})
        elif name == "audio":
            self.src = attrs.get("src", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.todo.append(name)
            self.todo.append({"src": self.src, "begin": self.begin,
                              "dur": self.dur})
        elif name == "textstream":
            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.todo.append(name)
            self.todo.append({"src": self.src, "region": self.region})

    def get_tags(self):
        return self.todo


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    todo = cHandler.get_tags()
    print(todo)
