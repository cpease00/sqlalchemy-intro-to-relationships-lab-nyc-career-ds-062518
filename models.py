from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy
Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character = Column(Text)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", back_populates="roles")

class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    roles = relationship(Role, order_by=Role.id, back_populates="actor")




#teachers = relationship("Teacher", backpopulates="campus")

#campus = relationships(Campus, back_populates="teacher")



engine = create_engine('sqlite:///actors.db')
Base.metadata.create_all(engine)
