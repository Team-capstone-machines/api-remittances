#!/usr/bin/python3
""" Module that contains the class DBStorage """

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.receiver import Receiver, Base
from models.history import History
from models.phones import Phones

classes = {
    "Receiver": Receiver,
    "History": History,
    "Phones": Phones
}


class DBstorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mssql+pyodbc://remittances_user:DUXowU%$dBmB"
            "@remittances.database.windows.net:1433/"
            "remittances_db?driver=ODBC+Driver+17+for+SQL+Server")

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        if str(cls) in classes:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = obj.id
                new_dict[key] = obj
        return new_dict

    def get(self, cls, phone):
        """This method is to retrieve one object """
        list_objs = []
        for value in self.all(cls).values():
            if value.phone == phone:
                list_objs.append(value)
        return list_objs

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def update(self, cls, phone, cash):
        """Update the column payout"""
        self.__session.query(classes[cls]).filter(
            classes[cls].phone == phone).update({'cash': cash})
        self.save()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
