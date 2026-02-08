from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "Agriculture System API Running"

@app.route("/soil")
def soil():
  return jsonify({
    "soil" : "Loamy",
    "moisture" : "Medium"
  })

@app.route("/crop")
def crop():
  return jsonify({
    "crop" : "Wheat"
  })

@app.route("/weather")
def weather():
  return jsonify({
    "temperature" : "30c",
    "humidity" : "60%"
  })

if __name__ = "__main__":
  app.run(host="0.0.0.0",port=5000)
    
