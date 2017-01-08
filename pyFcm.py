from pyfcm import FCMNotification
from flask import Flask
from flask_restful import Resource, Api
from flask import Response
from flask import request

app = Flask(__name__)
api = Api(app)



class sendMessage(Resource):
        def post(self):
                regId = request.form["regId"]
                apiKey = request.form["apiKey"]
                push_service = FCMNotification(api_key=apiKey)
                message_title = request.form["title"]
                message_body =  request.form["body"];
                result = push_service.notify_single_device(registration_id=regId, message_title=message_title, message_body=message_body)

                print result

api.add_resource(sendMessage, '/sendMessage/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7001')

