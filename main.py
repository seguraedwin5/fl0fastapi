from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def inicio():
    return { 'message' : "este es el inicio"}

@app.get('/productos')
def listproductos():
    return [
  {
    "id": "1",
    "nombre": "Milk",
    "precio": "2.99"
  },
  {
    "id": "2",
    "nombre": "Bread",
    "precio": "1.99"
  },
  {
    "id": "3",
    "nombre": "Eggs",
    "precio": "3.49"
  },
  {
    "id": "4",
    "nombre": "Butter",
    "precio": "2.49"
  },
  {
    "id": "5",
    "nombre": "Cheese",
    "precio": "4.99"
  },
  {
    "id": "6",
    "nombre": "Yogurt",
    "precio": "1.49"
  },
  {
    "id": "7",
    "nombre": "Cereal",
    "precio": "3.99"
  },
  {
    "id": "8",
    "nombre": "Juice",
    "precio": "2.99"
  },
  {
    "id": "9",
    "nombre": "Coffee",
    "precio": "5.99"
  },
  {
    "id": "10",
    "nombre": "Tea",
    "precio": "3.49"
  },
  {
    "id": "11",
    "nombre": "Sugar",
    "precio": "1.99"
  },
  {
    "id": "12",
    "nombre": "Flour",
    "precio": "2.49"
  },
  {
    "id": "13",
    "nombre": "Rice",
    "precio": "4.99"
  },
  {
    "id": "14",
    "nombre": "Pasta",
    "precio": "1.49"
  },
  {
    "id": "15",
    "nombre": "Sauce",
    "precio": "3.99"
  }
]