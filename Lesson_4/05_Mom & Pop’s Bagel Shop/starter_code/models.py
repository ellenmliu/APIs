from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
Base = declarative_base()

#USER MODEL
class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  username = Column(String(32), index=True)
  password_hash = Column(String(64))

  # Takes a plain password and stores a hash version
  def hash_password(self, password):
    self.password_hash = pwd_context.encrypt(password)

  # Takes a plain password and verifies the password
  def verify_password(self, password):
    return pwd_context.verify(password, self.password_hash)

class Bagel(Base):
	__tablename__ = 'bagel'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	picture = Column(String)
	description = Column(String)
	price = Column(String)
	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	    'name' : self.name,
	    'picture' : self.picture,
	    'description' : self.description,
	    'price' : self.price
	        }


engine = create_engine('sqlite:///bagelShop.db')
 

Base.metadata.create_all(engine)
