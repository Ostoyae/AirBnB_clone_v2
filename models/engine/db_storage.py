#!/usr/bin/python3
"""This defines class database storage class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    """This class handles the interation with the database for the
    project

    Attributes:
        __engine: SQLAlchemy engine
        __session: SQLAlchemy session
    """
    __engine = None
    __session = None
    __all_classes = {"User": User, "State": State, "City": City,
                     "Amenity": Amenity, "Place": Place, "Review": Review}

    def __init__(self):
        """Create a DBStorage object
        """
        engine = 'mysql+mysqldb://{usr}:{pwd}@{host}/{db}'\
            .format(
                usr=getenv('HBNB_MYSQL_USER'),
                pwd=getenv('HBNB_MYSQL_PWD'),
                host=getenv('HBNB_MYSQL_HOST'),
                db=getenv('HBNB_MYSQL_DB')
            )
        self.__engine = create_engine(engine, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Querys all objects in the DBStorage session

        Args:
            cls: TODO

        Returns:
            Dictionary: {<class-name>.<object-id>: object}
        """
        collection = dict()
        if cls:
            if type(cls) is not str:
                session = self.__session.query(cls)
            else:
                session = self.__session.query(self.__all_classes[cls])
            for entity in session:
                key = '{}.{}'.format(entity.__class__.__name__, entity.id)
                collection.update({key: entity})
        else:
            for k, obj in self.__all_classes.items():
                session = self.__session.query(obj).all()
                for entity in session:
                    key = '{}.{}'.format(entity.__class__.__name__, entity.id)
                    collection.update({key: entity})

        return collection

    def new(self, obj):
        """Create a new session for the object

        Args:
            obj: object to insert into the database
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current session
        """
        self.__session.commit()

    def delete(self, cls=None):
        """delete a obj

        Args:
            cls: Object to delete from the database
        """
        if cls:
            self.__session.delete(obj)

    def reload(self):
        """Create all the tables in the database and
        add a session to __session
        """
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''This closes as SQLalchemy session
        '''
        print(type(self.__session))
        self.__session.close()
