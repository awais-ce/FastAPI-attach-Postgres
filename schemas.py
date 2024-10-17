from pydantic import EmailStr , BaseModel

class UserCreate(BaseModel):
    name  : str
    fathername : str
    email : str
    phone : str
    age : int
    degree : str







