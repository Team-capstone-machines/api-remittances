#!/usr/bin/python3
""" phones module """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Phones(Base):
    """ The phones class, contains sender phone encrypted and decrypted """
    __tablename__ = 'table_phones'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    phone = Column(String(40), nullable=False)
    phone_desencrypt = Column(String(40), nullable=False)

    def __init__(self, **kwargs):
        """ method constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def print_dict(self):
        """ to print the dictionary """
        print(self.__dict__)

    def to_dict(self):
        """ convert class in a dictionary """
        return self.__dict__
