from fastapi import FastAPI

#khoi tao web app
app = FastAPI()

#Xay dung api dau tien
@app.get("/home")
def get_homepage():
    return {"home"}

    