from sqlalchemy import create_engine
from pathlib import Path

proj_path = Path(__file__).parent.parent.parent #learning_adv


sqlite_engine = create_engine(
    url=f"sqlite:///{proj_path}/database.db"
)


print(sqlite_engine)