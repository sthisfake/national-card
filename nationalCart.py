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


test = NationalCard
test.nationalCode = 8
test.firtName =  "abbbas"
test.lastName =  "abbbas"
test.birthDate =  "13970829"
test.fathersName =  "abbbas"
test.expirationDate = "14011125"
test.faceImage = "14011125"
test.cardImage = "14011125"


test1 = NationalCard
test1.nationalCode = 1
test1.firtName =  "pouya"
test1.lastName =  "teimoury"
test1.birthDate =  "13970829"
test1.fathersName =  "khodabakhsh"
test1.expirationDate = "14011125"
test1.faceImage = "face.JPG"
test1.cardImage = "card.jpg"

test2 = NationalCard
test2.nationalCode = 2
test2.firtName =  "reza"
test2.lastName =  "farjam"
test2.birthDate =  "13970829"
test2.fathersName =  "ali"
test2.expirationDate = "14011125"
test2.faceImage = "face.JPG"
test2.cardImage = "card.jpg"

test3 = NationalCard
test3.nationalCode = 3
test3.firtName =  "ahmad"
test3.lastName =  "yazdan"
test3.birthDate =  "13970829"
test3.fathersName =  "sohrab"
test3.expirationDate = "14011125"
test3.faceImage = "face.JPG"
test3.cardImage = "card.jpg"

test4 = NationalCard
test4.nationalCode = 4
test4.firtName =  "ali"
test4.lastName =  "hassani"
test4.birthDate =  "13970829"
test4.fathersName =  "mohammad"
test4.expirationDate = "14011125"
test4.faceImage = "face.JPG"
test4.cardImage = "card.jpg"


test5 = NationalCard
test5.nationalCode = 5
test5.firtName =  "shadmehr"
test5.lastName =  "gholipor"
test5.birthDate =  "13970829"
test5.fathersName =  "panjali"
test5.expirationDate = "14011125"
test5.faceImage = "face.JPG"
test5.cardImage = "card.jpg"

tests = [test , test1 , test2 , test3 , test4 , test5 ]

#knowing the place of images and css for hytml
app.mount("/static", StaticFiles(directory="static" , html = True), name="static")

#puting slash '/' betwwen dates
for sth in tests :
        sth.birthDate = sth.birthDate[:4] + '/' +  sth.birthDate[4:6] + '/' +  sth.birthDate[6:]
        sth.expirationDate = sth.expirationDate[:4] + '/' + sth.expirationDate[4:6] + '/' + sth.expirationDate[6:]

@app.post("/new")
async def creatApi(newCard: NationalCard):
    tests.append(newCard)
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
    for example in tests:
        print(str(example.firtName))    
        if number == str(example.nationalCode):
            return templates.TemplateResponse("index.html", {"request": request , str(example.nationalCode) : example})
    print("sfgusfsf")        
    return templates.TemplateResponse("nofound.html", {"request": request,"error" : "not found"})      

        
        # newOutput   = {**{"request": request}, **output} 
        # return templates.TemplateResponse("nofound.html", newOutput)
    #     return output
    # else: 
        # output = cards[number] 
        # print(output) 
        # newOutput   = {**{"request": request}, **output}  
        # return templates.TemplateResponse("index.html", newOutput)
        # return output


@app.get("/")
async def home(request : Request):
    return templates.TemplateResponse("home.html" , {"request": request})



@app.post("/uploadfiles")
async def create_upload_file(file: UploadFile):
    return {"filename":file.filename}
    

