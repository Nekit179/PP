from django.shortcuts import render
import sqlite3


def index(request):
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Cargo')
    data = cursor.fetchall()
    conn.close()
    return render(request, 'index.html', {'data': data})


def second(request):
    conn = sqlite3.connect('identifier.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Vehicles')
    data = cursor.fetchall()
    conn.close()
    return render(request, 'second.html', {'data': data})
