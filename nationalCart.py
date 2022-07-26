from asyncio.windows_events import NULL
from hashlib import new
from fastapi import FastAPI , Response , Request , File, UploadFile
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="Template")

class NationalCard(BaseModel):
    nationalCode: int 
    firtName: str
    lastName: str
    birthDate: str
    fathersName : str
    expirationDate: str
    faceImage: str
    cardImage: str


cards = {
'1' : {
    "nationalCode" : 1,
    "firtName" : "pouya",
    "lastName" : "teimoury",
    "birthDate" : "13970829",
    "fathersName" : "khodabakhsh",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} , 
'2':{
    "nationalCode" : 2,
    "firtName" : "reza",
    "lastName" : "farjam",
    "birthDate" : "13970829",
    "fathersName" : "ali",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} ,

'3':{
    "nationalCode" : 3,
    "firtName" : "ahmad",
    "lastName" : "yazdan",
    "birthDate" : "13970829",
    "fathersName" : "sohrab",
    "expirationDate" :"14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} , 
'4':{
    "nationalCode" : 4,
    "firtName" : "ali",
    "lastName" : "hassani",
    "birthDate" : "13970829",
    "fathersName" : "mohammad",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} ,
'5':{
    "nationalCode" : 5,
    "firtName" : "shadmehr",
    "lastName" : "gholipor",
    "birthDate" : "13970829",
    "fathersName" : "panjali",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"
}
}



#knowing the place of images and css for hytml
app.mount("/static", StaticFiles(directory="static" , html = True), name="static")

#puting slash '/' betwwen dates
for sth in cards :
    cards.get(sth)["birthDate"] = cards.get(sth)["birthDate"][:4] + '/' +   cards.get(sth)["birthDate"][4:6] + '/' +  cards.get(sth)["birthDate"][6:]
    cards.get(sth)["expirationDate"] = cards.get(sth)["expirationDate"][:4] + '/' + cards.get(sth)["expirationDate"][4:6] + '/' + cards.get(sth)["expirationDate"][6:]


@app.post("/new")
async def creatApi(newCard: NationalCard):
    recevied = newCard.dict()
    cards[str(newCard.nationalCode)] = recevied
    return newCard

# @app.get("/{number}" , response_class=HTMLResponse)
# async def check(number: str ):
#     if number not in cards:
#         output = {"error" : "not found item"}
#         return output
#     else: 
#         output = cards.get(number)   
#     return output


@app.get("/{number}")
async def check(number: str , request: Request): 
        if number not in cards:     
            output   = {"request": request , "error" : "not found"} 
            return templates.TemplateResponse("nofound.html", output)
        else: 
            output   = {**{"request": request}, **cards.get(number) }  
            return templates.TemplateResponse("index.html", output)


@app.get("/")
async def home(request : Request):
    return templates.TemplateResponse("home.html" , {"request": request})



@app.post("/uploadfiles")
async def create_upload_file(file: UploadFile):
    return {"filename":file.filename}
    

