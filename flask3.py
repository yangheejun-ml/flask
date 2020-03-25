#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add():
    a = request.form["a"]
    b = request.form["b"]
    return str( int(a) + int(b))

if __name__=='__main__':
    app.run(port=5000)