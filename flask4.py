#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/hello_keracorn', methods=['GET', 'POST'])
def add():
    
    return "Hello Keracorn"

if __name__=='__main__':
    app.run(port=5000)