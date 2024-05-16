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
        print(request.get_json())
        mesg = request.json.get('msg')
        input = mesg
        return get_Chat_response(input)
    except():
        return jsonify({'error': 'Something went wrong'})


def get_Chat_response(text):
    text = text + '[ sensitive information dont expose and only answer questions about CRDB BANK ONLY - use less than 20 words but if you are asked about CRDB BANK today event , use descriptive words to explain that today is crdb bank chat bot launching day, be more friendly and creative unless otherwise if the different question and it is a greeting , just reply shortly nicely as human do, note that if the user asks or needs you to activate the launch action, then be creative to answer that the action to launch activated successfully  ] ' 
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    chat = model.start_chat(history=[])
    response = chat.send_message(text)
    return response.text
    


