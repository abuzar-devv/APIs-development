#In this file i practiced the the concept opf validation the request's data using pydanttic library.



from pydantic import BaseModel
from fastapi import FastAPI

#Task 1 — Book endpoint
# Create a POST endpoint at /books that:
# - Accepts title as text.
# - Accepts pages as an integer.
# - Uses a Pydantic model to validate the request.
# - Returns both values in a JSON response.
# Test it in Postman with:
# - One valid request.
# - One request where pages is "hello".

app=FastAPI()

class Books(BaseModel):
    title:str
    pages:int

@app.post("/books")
def test_1(book:Books):
    return {

        "Title":book.title,
        "Pages":book.pages

    }



#Task 2 — Product endpoint
# Create a POST endpoint at /products that:
# - Accepts name as text.
# - Accepts price as a number (float).
# - Uses a Pydantic model.
# - Returns both values in the response.
# Test it in Postman with:
# - One valid request.
# - One request where price is "expensive".

class Products(BaseModel):
    name:str
    price:float

@app.post("/products")
def test_2_run(product:Products):
    return{
        "name":product.name,
        "price":product.price
    }
