from app import db
from models import User

#create the database and db tables
db.create_all()

#insert
db.session.add(User("Zakari Anjuma", "08062191817", "mradeybee@gmail.com", "yaba lagos", "Table 3"))


#commit the changes
db.session.commit()