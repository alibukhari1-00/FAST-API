from fastapi import FastAPI,Path,HTTPException

app = FastAPI()

data={1:"ali", 2:"waqas", 3:"Mian", 4:"Suffian", 5:"Mohsin"}

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app.get("/about")
def about():
    return {"message":"This is the about section of my api"}

@app.get("/view")
def load_data():
    return data


@app.get("/info/{id}")
def get_info(id: int=Path(...,description="Id is of the format 1 ,2 ,3 ",title="Patient Data ")):
    if id in data:
        return {"Info found Successfully ":data[id]}
    else:
        raise HTTPException(status_code=404,detail="Information not found")