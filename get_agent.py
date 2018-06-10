from flask import Flask,request,render_template
import os

app = Flask(__name__)

@app.route("/agent",methods=["GET","POST"])
def main():
    req = request.headers.get("User-Agent")
#    req = req.decode("utf-8")
    return req
@app.route("/check")
def che():
    return render_template("agent.html")

if __name__ == "__main__":
     port = int(os.environ.get("PORT",5000))
         
     app.run(debug=False,port=port,host='0.0.0.0')
