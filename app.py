from apps import create_app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exit import db

#引用工厂函数
app = create_app()

#实例化flask_script扩展插件中的Manager
manager = Manager(app)

#实例化Migrate命令工具，将app工厂函数和数据库映射传与其建立联系
migrate = Migrate(app,db)

#最后将flask_script和命令工具关联
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
    manager.run()
