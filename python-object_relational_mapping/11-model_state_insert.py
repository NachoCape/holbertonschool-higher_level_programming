#!/usr/bin/python3
"""
    adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    Lousi_state = State(name="Louisiana")
    session.add(Lousi_state)
    session.commit()
    print(Lousi_state.id)
