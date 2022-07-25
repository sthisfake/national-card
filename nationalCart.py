from asyncio.windows_events import NULL
from fastapi import FastAPI , Response , Request
from pydantic import BaseModel

app = FastAPI()

class NationalCard(BaseModel):
    nationalCode: int
    firtName: str
    lastName: str
    birthDate: int
    fathersName : str
    expirationDate: int
    faceImage: str
    cardImage: str


cards = {

"1" : {
    "nationalCode" : 1,
    "firtName" : "pouya",
    "lastName" : "teimoury",
    "birthDate" : 13970829,
    "fathersName" : "khodabakhsh",
    "expirationDate" : 14011125 ,
    "faceImage" : "face.jpeg",
    "cardImage" : "card.jpeg"} , 
"2":{
    "nationalCode" : 2,
    "firtName" : "reza",
    "lastName" : "farjam",
    "birthDate" : 13970829,
    "fathersName" : "ali",
    "expirationDate" : 14011125 ,
    "faceImage" : "face.jpeg",
    "cardImage" : "card.jpeg"} ,

"3":{
    "nationalCode" : 3,
    "firtName" : "ahmad",
    "lastName" : "yazdan",
    "birthDate" : 13970829,
    "fathersName" : "sohrab",
    "expirationDate" : 14011125 ,
    "faceImage" : "face.jpeg",
    "cardImage" : "card.jpeg"} , 
"4":{
    "nationalCode" : 4,
    "firtName" : "ali",
    "lastName" : "hassani",
    "birthDate" : 13970829,
    "fathersName" : "mohammad",
    "expirationDate" : 14011125 ,
    "faceImage" : "face.jpeg",
    "cardImage" : "card.jpeg"} ,
"5":{
    "nationalCode" : 5,
    "firtName" : "shadmehr",
    "lastName" : "gholipor",
    "birthDate" : 13970829,
    "fathersName" : "panjali",
    "expirationDate" : 14011125 ,
    "faceImage" : "face.jpeg",
    "cardImage" : "card.jpeg"
}
}

@app.post("/new")
async def creatApi(newCard: NationalCard):
    cards[str(newCard.nationalCode)] = newCard
    return newCard

@app.get("/{number}")
async def check(number: str ):
    if number not in cards:
        output = {"error" : "not found item"}
        return output
    else: 
        output = cards.get(number)   
        return output


