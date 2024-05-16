from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import google.generativeai as genai

GOOGLE_API_KEY='AIzaSyB4HXF0ZqI5y6T526nq2s2Ld1f3zIUD2vs'
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route("/get", methods=["POST"])
@cross_origin(supports_credentials=True)
def chat():
    try:
        mesg = request.json.get('msg')
        input = mesg
        return get_Chat_response(input)
    except():
        return jsonify({'error': 'Something went wrong'})


def get_Chat_response(text):
    text = text + ' Note the following: Answer greetings as human do, answer only crdb bank related information, the event going on is crdb chat bot launching day, only use text words with less than 20 words, if asked about activating or launching, launch action simply answer activation successfuly!' 
    model = genai.GenerativeModel('gemini-1.0-pro-001')
    chat = model.start_chat(history=[])
    response = chat.send_message(text)
    return response.text
    

# if __name__ == '__main__':
#     app.run(debug=True)
