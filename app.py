# The C2 Server 

import os

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load in .env variables to connect to PostgreSQL server 
try:
    host = os.environ['host']
    password = os.environ['password']
    username = os.environ['username']
    port = os.environ['port']
    database = os.environ['database']
except: 
    print("failure getting keys")

#Connect to C2
# try:
#     print("Connecting")
#     conn = psycopg2.connect(f"dbname={database} user={username} password={password} host={host} port={port}")
#     print("Success? Should be 0: ", conn.closed)
#     cursor = conn.cursor()
# except:
#     print("failed to connect")

# For when you want to any query, used to avoid connections timing out 
def executeQuery(query):
    cursor.execute(query)
    returnThis = cursor.fetchall()

    return returnThis 

@app.route("/whoami", methods=["GET"])
def handle_whoami():
    #TO IMPLEMENT 
    pass 

@app.route("/test", methods=["GET"])
def handle_test():
    stuff = executeQuery("SELECT * from test")
    return ("<p>%s</p>" % stuff)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"
