from fastapi import FastAPI
import requests
from jose import JWTError, jwt
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Connected Success"}

class BaseToken(BaseModel):
    sub: str
    name: str
    nickname: str

class BaseNickName(BaseModel):
    nickname: str

header={
     "X-Riot-Token":"RGAPI-70a2ae76-9056-4d7b-b6b7-a06dd5346efb"
}

my_secret = 'dad23123qwdasd'
ALGORITHM = "HS256"

@app.post("/getToken")
async def token(payload_data:BaseToken):
    payload_data = payload_data.dict()
    token = jwt.encode(
        payload_data,
        my_secret,
        algorithm=ALGORITHM
    )
    return token

@app.post("/stats")
async def getStats(BaseName:BaseNickName):
    nickname = BaseName.dict()
    request = requests.get(f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname["nickname"]}',headers=header)
    json_request = request.json()
    return json_request



