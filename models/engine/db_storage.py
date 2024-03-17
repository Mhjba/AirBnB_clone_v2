#from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    '''This class manages database storage of hbnb models in MySQL DB'''
    __engine = None
    __session = None

    def __init__(self):
        '''Create DBStorage engine and drop tables if testing'''
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')

        db_link = f'mysql+mysqldb://{USER}:{PWD}@{HOST}:3306/{DB}'
        self.__engine = create_engine(db_link, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def new(self, obj=None):
        '''Add the object to the current database session'''
        if obj:
            self.__session.add(obj)

    def save(self):
        '''Commit all the changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete a record from the current database session'''

