from requests import Session
from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, declarative_base


# engine = create_engine('sqlite:///example.sqlite')
#
# conn = engine.connect()
#
# metadata = db.MetaData()
#
# Student = db.Table('Student', metadata,
#                    db.Column('Id', db.Integer, primary_key=True),
#                    db.Column('Name', db.String(255), nullable = False),
#                    db.Column('Major', db.String(255), default = 'Math'),
#                    db.Column('Pass', db.Boolean, default= True)
#                    )
# metadata.create_all(engine)
#
# query = db.insert(Student).values(Id=1, Name = 'Bob', Major = 'English', Pass = True)
# conn.execute(query)
# conn.commit()
#
# output = conn.execute(Student.select()).fetchall()
# print(output)
#
# query = db.insert(Student)
# values_list = [
#     {"Id": 2, "Name": "Alice", "Major": "Science", "Pass": False},
#     {"Id": 3, "Name": "Ben", "Major": "Math", "Pass": True},
#     {"Id": 4, "Name": "John", "Major": "English", "Pass": False}
# ]
#
# conn.execute(query, values_list)
#
# output = conn.execute(Student.select()).fetchall()
# print(output)

# print(conn.execute(Student.select()).fetchall())
# query = Student.select().where(Student.columns.Major == 'English')
# output = conn.execute(query).fetchall()
# print(output)

# query = Student.update().values(Pass = True).where(Student.columns.Name == 'Alice')
# conn.execute(query)
# conn.commit()
#
# output = conn.execute(Student.select()).fetchall()
# print(output)
#
# query = Student.delete().where(Student.columns.Name == 'Ben')
# conn.execute(query)
# conn.commit()
# print(conn.execute(Student.select()).fetchall())

# Divisions = db.Table('Divisions', metadata,
#                      db.Column('Division', db.String(10), primary_key= True),
#                      db.Column('Name', db.String(255)),
#                      db.Column('Country', db.String(255))
#                      )
# Matchs = db.Table("Matchs", metadata,
#     db.Column("Id", db.Integer, primary_key=True),
#     db.Column("Div", db.String(10)),
#     db.Column("HomeTeam", db.String(255)),
#     db.Column("FTHG", db.Integer),
#     db.Column("FTAG", db.Integer)
# )
#
# metadata.create_all(engine)

# conn.execute(db.insert(Divisions), [
#     {'Division': 'E1', "Name": "Premier League", "Country": "England"},
#     {'Division': 'D1', "Name": "Bundesliga", "Country": "Germany"}
# ])
#
# conn.execute(db.insert(Matchs), [
#     {"Div": "E1", "HomeTeam": "Norwich", "FTHG": 1, "FTAG": 1},
#     {"Div": "E1", "HomeTeam": "Liverpool", "FTHG": 2, "FTAG": 1},
#     {"Div": "D1", "HomeTeam": "Bayern", "FTHG": 3, "FTAG": 0}
# ])

# conn.commit()
#
# query_join = db.join(Matchs, Divisions, Matchs.c.Div == Divisions.c.Division)
# query_select = db.select(
#     Divisions.c.Division,
#     Divisions.c.Name,
#     Divisions.c.Country,
#     Matchs.c.HomeTeam,
#     Matchs.c.FTHG,
#     Matchs.c.FTAG,
# ).select_from(query_join)
#
# result = conn.execute(query_select).fetchall()
#
# for row in result:
#     print(row)


# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key = True)
#     username = Column(String)
#     email = Column(String)
#
#     def __repr__(self):
#         return f'<User(id = {self.id}, username = {self.username}, email = {self.email})>'
#
# engine = create_engine('sqlite://example.db', echo = True)
#
# Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind = engine)
# session = Session()
#
# new_user = User(username= 'JohnDoe', email= 'join@example.com')
#
#
# session.add(new_user)
# session.commit()
#
# user = session.query(User).filter_by(username='Johndoe').first()
# print(f'Знайдено користувача: {user}')
#
# user.email = 'john.doe@example.com'
# session.commit()
#
# user = session.query(User).filter_by(username='Johndoe').first()
# print(f'Знайдено користувача: {user}')
#
# session.delete(user)
# session.commit()