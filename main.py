from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from faker import Faker
from sqlalchemy.orm import declarative_base

Base = declarative_base()



engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group')
    grades = relationship('Grade')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher')
    grades = relationship('Grade')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship('Subject')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    date = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    student_id = Column(Integer, ForeignKey('students.id'))


fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    pass


def select_10():
    pass
