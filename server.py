from dateutil import parser
from fastapi import APIRouter, Depends, FastAPI, Header, Request, Response
from fastapi.responses import JSONResponse
from typing import List

from core import create_app


#Start FastApi application
app = create_app()


@app.get('/')
def index(request: Request): 
    return JSONResponse(content={ "msg": f"Welcome to FastApi starter project!!" })

