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
    print("text:",text)
    text = text + '[ Note:answer greetings if asked any, and other stuffs only answer questions about imperial marketing and innovation compay in tanzania only related questions,search information here https://www.imperialinnovations.co.tz [ if you are asked so] use less than 20 words' 
    model = genai.GenerativeModel('gemini-1.0-pro-001')
    chat = model.start_chat(history=[])
    response = chat.send_message(text)
    print(response)
    return response.text
    

# if __name__ == '__main__':
#     app.run(debug=True)
