from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "web application [2]"+"\n"

if __name__=="__main__":
      app.run(debug=True,host="0.0.0.0")
    
