from flask import Flask, render_template, request, jsonify
import google.generativeai as genai



GOOGLE_API_KEY='AIzaSyB4HXF0ZqI5y6T526nq2s2Ld1f3zIUD2vs'
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input)


def get_Chat_response(text):
    text = text + '[explain with less than 20 words but if you are asked about CRDB BANK , use descriptive words to explain that today is crdb bank chat bot\
          launching day, be more friendly and creative unless otherwise if the different question and it is a greeting , just reply nicely as human do ] ' 
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(text)
    return response.text
    

