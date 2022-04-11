from cassandra.cluster import Cluster
cluster = Cluster(contact_points=['172.17.0.1'],port=9042)
session = cluster.connect()


from random import randint
from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextAreaField, validators, StringField, SubmitField
import requests
import time
from time import gmtime, strftime
import json


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY']='UdwnaIDW231'

class ReusableForm(Form):
    Place = StringField('Place:')


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    if request.method == 'POST':

        #Find the latitude and longitude using locationiq
        Place = request.form['Place']
        url = "https://us1.locationiq.com/v1/search.php"
        data = {
            'key': 'pk.4281a94da2a3556355996cd6c04ba2df',
            'q': str(Place),
            'format': 'json'
        }

        #get latitude and longitude and store in respective variables
        resp1 = requests.get(url, params=data)
        if resp1.ok:
            results = resp1.json()[0]
            My_latitude = results['lat']
            My_longitude = results ['lon']
            flash (f' \n The Latitude:- {str(My_latitude)} \n The Longitude:- {str(My_longitude)}')
            session.execute(f"INSERT INTO location.stats(place, my_latitude, my_longitude) VALUES ('{Places}','{My_latitude}','{My_longitude}');" )
        else:
            print (resp1.reason)
    return render_template('index.html', form=form)
@app.route("/places", methods=['GET']) #REST api GET method
def profile():
    rows = session.execute( 'Select * From location.stats')
    places=[]
    for row in rows:
        places.append(row.place)
    return (str(places))
@app.route('/places',  methods=['POST']) #REST api POST method
def create():

    session.execute(f"INSERT INTO location.stats(place, my_latitude, my_longitude) VALUES('{request.json['Place']}',{request.json['My_latitude']},{request.json['My_longitude']});")
    return jsonify({'message': 'created: /place/{}'.format(request.json['Place'])}), 201
@app.route('/places',  methods=['PUT']) #REST api PUT method
def update():

    session.execute(f"UPDATE location.stats SET my_latitude = {request.json['My_latitude']},my_longitude = {request.json['My_longitude']} WHERE place = '{request.json['Place']}'")
    return jsonify({'message': 'updated: /places/{}'.format(request.json['Place'])}), 200
@app.route('/places',  methods=['DELETE']) #REST api DELETE method
def delete():
    session.execute(f"Delete FROM location.stats WHERE place = '{request.json['Place']}'")
    return jsonify({'message': 'deleted: /places/{}'.format(request.json['Place'])}), 200
if __name__ == "__main__":
    #app.run(host='0.0.0.0',port=443,ssl_context=('cert.pem', 'key.pem'))
    app.run(host='0.0.0.0',port = 80)
