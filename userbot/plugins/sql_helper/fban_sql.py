from sqlalchemy import Column, Integer, String

from . import BASE, SESSION


class Fban(BASE):
    __tablename__ = "fban"
    fedids = Column(UnicodeText, primary_key=True)

    def __init__(self, fedids):
        self.fedids = fedids


Fban.__table__.create(checkfirst=True)


def add_fed_in_db(fedids):
    fed_id = Fban(fedids)
    SESSION.add(fed_id)
    SESSION.commit()


def get_all_fed():
    fed_ids = SESSION.query(Fban).all()
    SESSION.close()
    return fed_ids


def removefeds(fedids):
    fednibba = SESSION.query(Fban).get(fedids)
    if fednibba:
        SESSION.delete(fednibba)
        SESSION.commit()


def get_all_feds():
    stark = SESSION.query(Fban).all()
    SESSION.close()
    return stark
