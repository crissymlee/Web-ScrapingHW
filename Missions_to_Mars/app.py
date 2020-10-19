from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars'
db = PyMongo(app)
print(db)


@app.route("/")
def index():
   mars = db.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = db
    mars_data = scrape_mars.scrape()
    db.db.mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
