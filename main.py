from flask import Flask , jsonify , request 
import csv
allarticle = []

with open("articles.csv" , encoding = "utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allarticle = data[1:]

liked_article = []
not_liked_article = []

app = Flask(__name__)

@app.route("/get-article")
def getarticle():
    return jsonify({
        "data" : allarticle[0],
        "status" : "success"
    })

@app.route("/liked-article" , methods = ["POST"])
def liked_article():
    article = allarticle[0]
    allarticle = allarticle[1:]
    liked_article.append(article)
    return jsonify({
        "status" : "success"
    })

@app.route("/not-liked-article" , methods = ["POST"])
def not_liked_article():
    article = allarticle[0]
    allarticle = allarticle[1:]
    not_liked_article.append(article)
    return jsonify({
        "status" : "success"
    })

if __name__ == "__main__":
    app.run()