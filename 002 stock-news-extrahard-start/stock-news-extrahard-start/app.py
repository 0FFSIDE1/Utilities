from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/webhook', methods=['POST'] or ['GET'])
def webhook():
    incoming_message = request.form['Body']
    print(incoming_message)
    if incoming_message.title() == 'More':
        response_message = 'Hi there'
    else:
        response_message = "I can't understand you"

    twiml = MessagingResponse()
    twiml.message(response_message)
    return str(twiml)


app.run(debug=True)
