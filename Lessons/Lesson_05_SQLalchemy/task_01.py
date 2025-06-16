from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy.orm import sessionmaker

proj_path = Path(__file__).parent.parent.parent #learning_adv


sqlite_engine = create_engine(
    url=f"sqlite:///{proj_path}/database.db"
)

Session = sessionmaker(bind=sqlite_engine)
session = Session()

print(session)
session.close()

# user = User(...) # Transient
#
# session.add(user) # Pending
#
# session.commit() # Persistent
#
# session.close() # Detached v1
# session.expunge() # Detached v2 (объект отвязан от сессии, сессия открыта)
#
# user = User.query.get(id=1)
# user.delete()
# session.commit() # Deleted