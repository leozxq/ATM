
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core import src

if __name__=="__main__":
    src.run()
    
    from sqlalchemy import * 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relation, sessionmaker 
  
Base = declarative_base() 
  
class Movie(Base) : 
    __tablename__ = 'movies' 
  
    id = Column(Integer, primary_key=True) 
    title = Column(String(255), nullable=True) 
    year = Column(Integer) 
    directed_by = Column(Integer, ForeignKey('directors.id')) 
    director = relation('Director', backref='movies', lazy=False) 
  
    def __init__(self, title=None, year=None) : 
        self.title = title 
        self.year = year 
 
    def __repr__(self) : 
        return 'Movie(%r, %r, %r)' % (self.title, self.year, self.director) 
  
class Director(Base) : 
    __tablename__ = 'directors' 
  
    id = Column(Integer, primary_key=True) 
    name = Column(String(50), nullable=False, unique=True) 
  
    def __init__(self, name=None) : 
        self.name = name 
  
    def __repr__(self) : 
        return 'Director(%r)' % (self.name) 
  
Base.metadata.create_all(create_engine('dbms://user:pwd@host/dbname'))
