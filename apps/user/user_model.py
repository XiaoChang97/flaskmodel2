from datetime import datetime
from exit import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    level = db.Column(db.String(10), nullable=False)
    #datetime.now()和datetime.now的区别，加（）程序运行时间，不加动态时间
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    isdelete = db.Column(db.Integer, nullable=False, default=0)
    def __str__(self):
        return self.username
