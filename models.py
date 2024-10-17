from sqlalchemy import String , Integer , Column
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key =True , index = True)
    name = Column(String , index = True)
    fathername = Column(String , index = True)
    email = Column(String , unique=True , index = True)
    phone = Column(String , index = True)
    age = Column(Integer , index = True)
    degree = Column(String , index = True)
    


