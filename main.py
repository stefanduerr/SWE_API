from fastapi import FastAPI
from db import *
import os.path



app = FastAPI()
# create_connection(r"C:\Users\xpara\SWE_API\db\pythonsqlite.db")
create_tables()



@app.get("/my-first-api")
def hello():
  return {"Hello world!"}

@app.get("/listofnames")
def select_names():
  return get_list()