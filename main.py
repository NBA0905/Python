from fastapi import FastAPI
from features import MAIL
#khoi tao web app
app = FastAPI()

#Xay dung api dau tien
#root
@app.get("/")
def get_root():
    return{'data': 'this is root dir'}
    #json


@app.get("/home")
def get_homepage():
    return {"home"}

@app.get("/calculator")
def get_calculator(a:int, b:int):
    return{"data": a + b}


@app.get("/login_get")
def login_with_get_method(ps: str, un: str ):
    return{"login":{"username":un,"password":ps }}

    #uvicorn main:app --reload

@app.post("/login_post")
def login_with_post_method(ps: str, un: str ):
    return{"login":{"username":un,"password":ps }}
    
@app.get("/send_mail")
def send_email_for_client(receiver: str, content: str, subject: str):
    status = MAIL.send_mail(receiver,content,subject)
    if status:
        return{"receiver": receiver, "sent": status}
    else:
        return{"sent": status}