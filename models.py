from extensions import db
from sqlalchemy import Integer,String,Date
class UID(db.Model):
    __tablename__ = 'UID_TABLE'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

class TASK_TABLE(db.Model):
    __tablename__ = 'TASK_TABLE'    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    task_name = db.Column(db.String(100), nullable=False)
    task_assigned_to = db.Column(db.String(25), nullable=False)
    task_assigned_by = db.Column(db.String(25), nullable=False)
    task_deadline = db.Column(db.Date, nullable=False)
    task_description = db.Column(db.String(100),nullable=False)
    task_progress = db.Column(db.String(100),nullable=True)
    task_remaining = db.Column(db.String(100),nullable=True)
    task_percentage = db.Column(db.Integer,nullable=True)
    task_people_working = db.Column(db.String(100),nullable=True)

