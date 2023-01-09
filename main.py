from flask import Flask
from faker import Faker
from markupsafe import escape
import requests


app = Flask(__name__)


@app.route('/requirements/', methods=['GET', 'POST'])
def requirements():
    with open('requirements.txt') as a:
        return a.read().split()


@app.route('/generate-users/<count>', methods=['GET', 'POST'])
def fakes(count):
    fake = Faker()
    fakers = {}
    for x in range(int(escape(count))):
        n = fake.email()
        e = fake.name()
        fakers[n] = e
    return fakers


@app.route('/mean/', methods=['GET', 'POST'])
def mean():
    index, height, weight = [0, 0, 0]
    with open('hw.csv') as a:
        for i in a:
            i = i.split(',')
            if len(i) == 3 and i[0].isdigit():
                index += 1
                height += float(i[1])
                weight += float(i[2])
        return {'Average Height': str(height / index * 2.54),
                'Average Weight': str(weight / index * 0.45)}


@app.route('/space/', methods=['GET', 'POST'])
def space():
    s = requests.get('http://api.open-notify.org/astros.json')
    return {'The number of astronauts at the moment': s.json()["number"]}
