import os

from flask import Flask
from flask_basicauth import BasicAuth
from flask_restful import Resource, Api

#import pymongo

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME', 'user')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD', 'pass')

basic_auth = BasicAuth(app)
api = Api(app)

#mongo_db_client = pymongo.MongoClient(os.environ.get('MONGO_DB_URI', 
#                                        "mongodb://localhost:27017/"))

#measurement_db = mongo_db_client["measurement_db"]

#measurements_collection = measurement_db["measurements"]

class HomeApiMeasurementRest(Resource):

    @basic_auth.required
    def post(self):

        # Simply get info from request and store it into db
        print('request came')


        return {'hello': 'world'}

api.add_resource(HomeApiMeasurementRest, '/')

if __name__ == '__main__':
    app.run(debug=True)