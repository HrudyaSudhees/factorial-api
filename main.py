'''from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math
import uvicorn

app = FastAPI()

@app.get("/factorial/{n}")
def factorial_cal(n):
    return { "n": n, "factorial": math.factorial(n)}

@app.get("/factorial/{bad}")
async def read_num(n:int):
    if n not in range(0,1001):
        raise HTTPException(
    status_code=400, detail= "Bad Request"
    header= {"error": "n must be a whole number from 0 to 1000"},)
    return (n)

@app.get("/health")
def health_check():
    return ("status ok")'''

    ########################################

from fastapi import FastAPI, HTTPException
import asyncio

app = FastAPI()

async def factorial_calc(n:int):
    if n ==0 or n ==1:
        return 1
    result = 1

    for i in range(2, n+1):
      result = result * i
    return result

@app.get("/factorial/{n}")
async def get_fact(n:int):
    print(type(n))
    if n<0 or n>1000:
        raise HTTPException(
            status_code=400, detail={"error": "n must be a whole number from 0 to 1000"},
        )
    

    final_value =  await factorial_calc(n)
    print(final_value, n)
    return {"n": n, "factorial":  str(final_value)}

@app.get("/health")
def health_check():
    return ("status OK")