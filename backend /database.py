from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///files.db")

def session():
    with Session(engine) as s:
        yield s
