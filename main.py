from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from db import *
import os.path

app = FastAPI()
# create_connection(r"C:\Users\xpara\SWE_API\db\pythonsqlite.db")
create_tables()

@app.get("/my-first-api")
def hello():
  return {"Hello world!"}

#Test Case 1: List of Customers
@app.get("/listofnames")
def select_names():
  return get_list()

#Test Case 2: List of Customers with only Name, E-Mail and Status
@app.get("/names_attributes", response_class=HTMLResponse)
def select_names():
  return get_list_with_attributes()

#Test Case 3: List of Customers and their products
@app.get("/belongings")
def select_names():
  return get_belongings()

@app.get("/", response_class=HTMLResponse)
def homepage():
  return """
    <html>
        <head>
            <title>XPara's Test API</title>
        </head>
        <body>
            <h1 style="text-align: center">XPara's Test API</h1>
            <a href="http://127.0.0.1:8000/listofnames">Test Case 1: List of Customers</a> <br>
            <a href="http://127.0.0.1:8000/names_attributes">Test Case 2: List of Customers with only Name, E-Mail and Status</a> <br>
            <a href="http://127.0.0.1:8000/belongings">Test Case 3: List of Customers and their products</a> <br>

        </body>
    </html>
    """