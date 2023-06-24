#Importing Libraries
from fastapi import FastAPI
from pydantic import BaseModel
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

app = FastAPI()

class Form(BaseModel):
    fname: str
    lname: str
    mnum: str
    age: int
    email: str

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/{name}")
def simple_get(name: str):
    return {"message": "Hello " + name}

@app.post("/")
def simple_post(formpost: Form):
    #converting form data to dictionary
    formdata = formpost.dict()
    
    #extracting form data from HTML
    fname = formdata["fname"]
    lname = formdata["lname"]
    mnum = formdata["mnum"]
    age = formdata["age"]
    email = formdata["email"]

    #Inserting collected data to collection
    collection.insert_one({"First Name": fname,
                            "Last Name": lname,
                            "Mobile Number": mnum,
                            "Age": age,
                            "Email": email})
    
    #returning inserted data
    return {"inserted": formdata}
