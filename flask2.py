#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    return str( int(a) + int(b))
    

if __name__=='__main__':
    app.run(port=5000)