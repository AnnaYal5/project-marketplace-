from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

test_db = [
    {
    'name': "test1",
    "author": "atest1",
    },
    {
    'name': "test2",
    "author": "atest2",
    }

]


@app.get('/')
async def products():
    return test_db


@app.post("/register")
async def register():
    pass


@app.post("/add")
async def add_products():
    pass


@app.delete("/del")
def delete():
    pass





