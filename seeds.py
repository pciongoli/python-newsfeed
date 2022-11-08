from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables
# drops all existing tables
Base.metadata.drop_all(engine)
# creates any table that Base mapped, in a class that inherits Base
Base.metadata.create_all(engine)

# establish temporary session connection
db = Session()

# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

# run the INSERT statements
db.commit()
# if no other db transactions are made close the session connection calling db.close()
db.close()