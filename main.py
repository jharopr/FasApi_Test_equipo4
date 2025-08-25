from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema


app = FastAPI()
conn = UserConnection()

@app.get("/")
def root():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items 

@app.get("/api/user/{id}")
def get_one(id: str):
        dictionary = {}
        data = conn.read_one(id)
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        return dictionary

@app.delete("/api/delete/{id}")
def delete(id: str):
    conn.delete(id)

@app.put("/api/update/{id}")
def update(id: str, user_data: UserSchema):
     data = user_data.dict()
     data["id"] = id
     conn.update(data)


@app.post("/api/insert")
def insert(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id") #ya que no es necesario mostrar el id(es serializado)
    conn.write(data)

