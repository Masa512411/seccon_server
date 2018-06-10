from flask import Flask,request
import os

app = Flask(__name__)

@app.route("/agent",methods=["POST"])
def main():
    return request.data

@app.route("/check")
def che():
    return "<p> Hello</p>"

if __name__ == "__main__":
     port = int(os.environ.get("PORT",5000))
         
     app.run(debug=False,port=port,host='0.0.0.0')

