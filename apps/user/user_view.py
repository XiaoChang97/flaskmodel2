import datetime
import hashlib
import time

from flask import Blueprint, render_template, request, redirect, url_for
from apps.user.user_model import User
#定义蓝图，Blueprint（）有两个必填参数，一个名字，一个__name__
from exit import db
blueprint_us = Blueprint('user',__name__)
users = User()
ok = {
        'code': 200,
        'msg': '填写成功'
    }

msg = {
        'code': 1002,
        'msg': '填写信息不正确，请重新填写'
    }

msg1 = {'code': 1003,
        'msg':'用户名已存在,提交失败'}

@blueprint_us.route('/')
def user_index():
    return render_template('user/user_index.html')

@blueprint_us.route('/show',methods = ['GET','POST'])
def show():
    sel_users = User.query.filter(User.isdelete == False).order_by(User.id.asc()).all()
    return render_template('user/show.html',users = sel_users)

@blueprint_us.route('/search_user')
def search_user():
    if request.method == 'GET':
        re = request.args
        reusername = re.get('username')
        relevel = re.get('level')
        register_timeA = re.get('register_timeA')
        register_timeB = re.get('register_timeB')
        if register_timeA != '' and register_timeB != '':
            print("走条件查询，带注册时间{0}，{1}".format(register_timeA, register_timeB))
            # 将时间字符串解析为时间元组
            register_timeA = datetime.datetime.strptime(re.get('register_timeA'), "%Y-%m-%dT%H:%M")
            register_timeB = datetime.datetime.strptime(re.get('register_timeB'), "%Y-%m-%dT%H:%M")
            sel_users = User.query.filter(db.and_(User.username.contains(reusername), User.level == relevel,User.isdelete == False,
                                                  User.rdatetime.__ge__(register_timeA),
                                                  User.rdatetime.__le__(register_timeB))).all()
        else:
            print("走条件查询，不带注册时间{0}，{1}".format(register_timeA, register_timeB))
            sel_users = User.query.filter(User.username.contains(reusername), User.level == relevel,User.isdelete == False) .all()
        return render_template('user/show.html', users=sel_users)

@blueprint_us.route('/del')
def delete():
    reid = request.args.get('id')
    del_user = User.query.filter(User.id == reid).first()
    #物理删除     db.session.delete(del_user)
    #逻辑删除，修改数据库状态
    del_user.isdelete = True
    db.session.commit()

    return redirect(url_for('user.show'))

@blueprint_us.route('/update_user',methods = ['GET','POST'],endpoint= 'update')
def update_user():
    # GET请求表示show.html页面执行修改点击事件
    if request.method == 'GET':
        re_id = request.args['id']
        sel_user = User.query.filter(User.id == re_id).first()
        if sel_user:
            return render_template('user/update.html',n = sel_user)
        else:
            return redirect(url_for('user.show'))
    if request.method == 'POST':
            id = request.form['id']
            username = request.form['username']
            password = request.form['password']
            password2 = request.form['password2']
            level = request.form['level']
            if username and password and password2 and level:
                if password == password2:
                    up_user = User.query.filter(User.id == id).first()
                    up_user.username = username
                    up_user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                    up_user.level = level
                    db.session.add(up_user)
                    db.session.commit()
            return redirect(url_for('user.show'))

@blueprint_us.route('/login',methods = ['GET','POST'])
def login():
    loginmsg = ''
    if request.method == 'POST':
        reloginname = request.form.get('username')
        reloginpassword = hashlib.sha256((request.form.get('password')).encode('utf-8')).hexdigest()
        seluser = User.query.filter(db.and_(User.username == reloginname,User.password == reloginpassword)).first()
        if seluser == None:
            loginmsg = '账号或密码错误'
        else:
            print(seluser.username, seluser.password)
            loginmsg = '登录成功'
    return render_template('user/login.html',loginmsg = loginmsg)

@blueprint_us.route('/register',methods = ['GET','POST'])
def register():
    users = User()
    ms = ''
    if request.method == 'POST':
        r = request.form
        if r.get('username') and r.get('password') and r.get('password2') and r.get('level'):
            if r.get('password') == r.get('password2'):
                '''
                #用户唯一识别
                for u in users:
                    if u.username == r.get('username'):
                        print(u)
                        return render_template('user/register.html',ms = msg1)
                        '''
                users.username = r.get('username')
                users.password = hashlib.sha256(r.get('password').encode('utf-8')).hexdigest()
                users.level = r.get('level')
                #将user对象添加到session中
                db.session.add(users)
                db.session.commit()
                ms = ok
            else:
                ms = msg
        else:
            ms = msg
    return render_template('user/register.html',ms = ms)

@blueprint_us.route('/logout')
def logout():
    return render_template('user/logout.html')