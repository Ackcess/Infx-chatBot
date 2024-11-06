from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import google.generativeai as genai

GOOGLE_API_KEY='AIzaSyB4HXF0ZqI5y6T526nq2s2Ld1f3zIUD2vs'
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)
CORS(app,supports_credentials=True)

multi_line_text = """
IMC is a full service Sales and Marketing agency, with our core focuses being the creative and innovative brand solutions on the digital landscape and our vast experience with on-the-ground consumer engagement.We combine strategy, creativity and organization under one roof to deliver top quality work. Our hard work puts us on the map, and our commitment to creative innovation keeps us there. Not only are we a nimble team of qualified personnel, we guarantee positive game changing results with our creative and strategic solutions to smarter marketing.

We are an established, innovative development team with years of experience in hardware and software development, schematic and layout-design, and development and production of complete control systems.

Internet of Things (IoT)
Control and get updates of your devices from all around the world using portable devices carried on your pockets.
Web Development
We carry more than just good coding skills. Our experience makes us stand out from other web development.
Software Development
Create complex enterprise software, ensure reliable software integration, with high level of security.
Electronic Development
Build the product you need on time with an experienced team that uses a clear and effective design process.
Marketing & Customer Engagement
We improve the way you can advertise your business and bring your customers closer.
Artificial Intelligence
We add intellect to the machines that enables them to perform different task without human interaction.
Markerting & Customer Engagement
We provide creative and innovative brand solutions on the digital landscape and our vast experience with on-the-ground consumer engagement.
Our sister company Imperial Marketing and Communications challenges us with various briefs from clients who need interactive engagement mechanics across experiential marketing and customer service experience. We have developed an array of customer engagement solutions which enables brands to connect with their target audiences and be able to amplify brand engagement through technology.
Some of the Interactive Engagements


Interactive Touch Wall
We are able to turn any surface (floor, wall , table, glass etc) into an interactive surface. Widely used to showcase offerings in a more engaging way, harvesting data from audiences or fun games to be played with brand knowledge being communicated at the same time.
 video


Interactive Vending Machine & Game Vending Machine
With this activation, audiences are asked to perform activities (based on campaign communication and brief), with these interactions performed, the progress is seen on the screen, if they are able to perform with in the given time, the dispensing unit will dispense a gift.
 video


Hologram
Holograms are one of the most unique way to communicate with your targeted audiences. You are able to reach your customers at multiple locations in a physical form through live sessions, the feeling is as if you are present with them in their environment and they are able to interact with you either through AI (pre feeding of information) or through live interaction via IoT.
 video


Interactive Installations
Our techno creative team is able to brainstorm and execute interactive installations for your store / outlet which is going to stay for a longer time.
Interactive installations use various technologies such as IR and or a mix of technologies such as VR and AR, motion and gesture to make your content / product or service more interactive and engaging to your audiences.
Some of the examples includes - smart kiosks, smart tables, interactive touch wall / floor , whiteboards, interactive TV.
 video


Social Media / Digital Activation
Social media activations are one of our most trending interactive engagements. We are fully able to create an experience using the known platforms such as Instagram, Facebook, Google and Twitter.
Example – now you are able to snap a photo, post it on your favorite social media with a specific hashtag, and instantly see yourself on a billboard.
With Twitter we are also able to do hardware integrations such as fFully interactive vending machine (tweet to dispense), tweet to unveil, tweet to reveal and so much more.
 video


Kinetic Game Integration
Want to engage your audiences with physical experience? Our kinetic activations are among the most popular in consumer engagement. For the interaction to happen, the audience would have to preform certain movements and gestures to find themselves immersed in an experience. These activities can also be linked to vending machines.
 video


Fully Interactive Photobooth
We also had an opportunity to design a full HD frameless touch mirror photobooth that helps you make your events memorable, click snaps, record gifs, boomerang, slow - more videos and add filters of your choice and share it on social media or print them instantly.
 video


Digital Slingshot
Data harvesting has never been so much fun. This is a unique experience for event events, now you can harvest data of your visitors through unique experience. Your visitor will be required to take a photo and feed information on the device and sling it on the screen. These information will splash on the screen and data will be collected by the system.
 video


Virtual Reality
This is one of the most exciting ways to engage with your customer, with the fully immersive ability, you are able to promote your brand in a more interactive way. We can help you with an end to end solution, i.e from creating the content to executing it.


Augmented Reality
We are able to create and AR experience for various market segments.


RFID Technology
We are able to create various interactive engagements in the retail marketing based on client briefs using RFID. Engagement such as:
Play a specific music when moving into a certain area.
Be able to connect on social media with other people at an event with a touch of your glasses, or taping of plates.
Or be able to download an app with a simple tap on a OOH advertisement.
Whatever the brief, we are able to create a fully digitalized experience for your next campaign using RFID.


Magic Screen Technology
This is a unique activation for brands that are looking to surprise their audiences , or conceal the content. We develop special screens and glasses, when seen with normal eyes, the screen appears to be blank, as soon as the glasses are worn, the content is revealed.



In a competitive market with price sensitive consumers and big budget competitors you need more than a creative agency.

You Need, Imperial Marketing & Communications
    CONTACTS.
 +255 713 525 152
 md@imc.co.tz
    ADDRESS.
 Tunisia Street, Ada Estate, Plot No. 3

"""

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
    text = text + '[ Note: respond to greetings review all questions about imperial innovation and marketing only, to answers from the following script----> ' + multi_line_text 
    model = genai.GenerativeModel('gemini-1.0-pro-001')
    chat = model.start_chat(history=[])
    response = chat.send_message(text)
    print(response)
    return response.text
    

# if __name__ == '__main__':
#     app.run(debug=True)
