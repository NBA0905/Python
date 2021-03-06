from fastapi import FastAPI, Request, File, UploadFile
from features import MAIL
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import aiofiles

#khoi tao web app
app = FastAPI()

# static file directory registry
app.mount("/media", StaticFiles(directory = "media"), name = "media")
app.mount("/tabs", StaticFiles(directory = "tabs"), name = "tabs")

templates = Jinja2Templates(directory="templates")
game = Jinja2Templates(directory="K2-Proj")

#Xay dung api dau tien
#root
@app.get("/")
def get_root():
    # return{'data': 'this is root dir'}
    #json
    return "this is root" 


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

@app.get("/form")
def get_demo_form(request: Request):
     return templates.TemplateResponse("ajax.html", {"request": request})

@app.get("/template")
def get_demo_template(request: Request):
    return templates.TemplateResponse("Account.html", {"request": request})

@app.get("/game")
def get_game(request: Request):
    return game.TemplateResponse("Bai2.html",  {"request": request})

@app.post("/Files")
async def upload_file(upload_file: UploadFile = File(...)):
    file_name = upload_file.filename
    file_path = f"media/{file_name}"
    async with aiofiles.open(file_path, "wb") as file_handler:
        content = upload_file.read();
        file_handler.write(content)

    return{"status":True}

