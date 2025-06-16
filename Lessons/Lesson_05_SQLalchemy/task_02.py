from sqlalchemy import create_engine, Column, Integer, String, Table, Text
from pathlib import Path
from sqlalchemy.orm import sessionmaker, declarative_base, registry

proj_path = Path(__file__).parent.parent.parent #learning_adv
sqlite_engine = create_engine(url=f"sqlite:///{proj_path}/database.db")

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)


Session = sessionmaker(bind=sqlite_engine)
session = Session()
print(session)

Base.metadata.create_all(bind=sqlite_engine)

user = User(
    name='Ivan',
    age=29
)

session.add(user)
session.commit()
session.close()