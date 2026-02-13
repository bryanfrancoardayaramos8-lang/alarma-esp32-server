from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8442245837:AAHP0MMdKOX5W5_Tywz2nqSu7fgnZ0z4wYA"
CHAT_ID = "6011549713"

@app.route("/")
def home():
    return "Servidor activo"

@app.route("/alerta")
def alerta():
    msg = request.args.get("msg", "Alerta sin mensaje")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    r = requests.post(url, data=data)

    return r.text
