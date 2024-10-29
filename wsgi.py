from app import app
from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)

password = 'sparta'
MONGODB_URI = f'mongodb+srv://test:{password}@cluster0.1et8z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(MONGODB_URI)

db = client.dbsparta_plus_week2

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
