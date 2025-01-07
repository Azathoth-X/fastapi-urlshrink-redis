import random
import string
from pydantic import BaseModel,AnyHttpUrl
from fastapi import FastAPI,Request,status


class url(BaseModel):
    fqd : AnyHttpUrl
dic={}
app=FastAPI()

def ran_gen(chars=string.ascii_uppercase+string.digits):
    return "".join(random.choice(chars) for i in range(5))


@app.get("/{short}")
def get_url(short:str):
    return dic[short] 

@app.post("/",status_code=status.HTTP_201_CREATED)
def create_url(tmpurl:url):
    data=tmpurl.fqd
    key=ran_gen()
    dic[key]=data
    return key