class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/test2'
    '''
   如果设置成 True (默认情况)，Flask-SQLAlchemy 
   将会追踪对象的修改并且发送信号。这需要额外的内存， 
   如果不必要的可以禁用它。
   '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dvelopment(Config):
    ENV = 'Dvelopment'
    DEBUG = True