from flask import Flask, jsonify, request
#from dotenv import load_dotenv
import os
from twilio.rest import Client

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "Аз обичам моето котееее"



#load the api keys from the the .env file
#load_dotenv()



# @app.route('/data/name', methods=['GET'])
# def send_message():
#     name = request.args.get('name')
#     if name:
    
#         account_sid = 'AC1c4799741d691b06af88758fb50cf8b4'
#         auth_token = '52c1901d677ad2a80a55f51cd422e79f'
#         client = Client(os.getenv("account_sid"), os.getenv("auth_token"))

#         message = client.messages.create(
#             body='test1',
#         to='+359897021485'
        
#         )

#         return jsonify({message.sid})
#     else:
#         return jsonify({"error": "Name parameter is needet"})



if __name__ == '__main__':
    app.run(debug=True)
