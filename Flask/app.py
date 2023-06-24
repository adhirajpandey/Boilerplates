#Importing Libraries
from flask import Flask, request, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os


#load environment variables
load_dotenv()


#Function Definitions
def connect_mongo(database:str, collection:str):
        cluster = os.getenv("MONGO_CLUSTER")
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASSWORD")
        
        connectionstring = "mongodb+srv://" + user + ":" + password + "@" + cluster + ".mongodb.net/test?retryWrites=true&w=majority"
        
        client = MongoClient(connectionstring)

        #connecting with database
        db = client[database]
        #connecting with collection
        col = db[collection]

        return col

collection = connect_mongo("Test", "HTMLTest")

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        
        #extracting form data from HTML
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        mnum = request.form.get("mnum")
        age = request.form.get("age")
        email = request.form.get("email")
        username = request.form.get("username")

        #Inserting collected data to collection
        collection.insert_one({"First Name": fname, 
                               "Last Name": lname, 
                               "Mobile Number": mnum, 
                               "Age": age, 
                               "Email": email, 
                               "Username": username})
    
    elif request.method == "GET":
        return render_template("index.html")
    
    return render_template("index.html")


app.run(debug=True)