#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add():
    a = 10
    b = 20
    return str(a +  b)

if __name__=='__main__':
    app.run(port=5000)