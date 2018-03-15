# coding=utf-8
from flask import Flask,render_template,request,flash
from config import Config
# 导入flask_wtf提供的表单类
from flask_wtf import FlaskForm
# 导入表单类提供的字段
from wtforms import StringField,PasswordField,SubmitField
# 导入表单类提供的验证函数
from wtforms.validators import DataRequired,EqualTo


app = Flask(__name__)
# 使用配置文件
app.config.from_object(Config)
# 使用csrf设密钥
# app.config['SECRET_KEY'] = 'ASBADSF'

# 需求:注册页面
# 自定义表单类
class Form(FlaskForm):
    # 定义表单字段/input/password/submit
    user = StringField(validators=[DataRequired()])
    pswd = PasswordField(validators=[DataRequired(),EqualTo('pswd2')])
    pswd2 = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label=u'注册')



@app.route("/demo3")
def demo3():
    return render_template('register.html')

@app.route('/',methods=['GET','POST'])
def demo2():
    # 实例化表单类对象
    form = Form()
    # form.validate_on_submit()函数会依次调用验证器,验证器条件满足,会查看表单页面中是否设置csrf_token
    if form.validate_on_submit():
        # 获取表单数据
        us = form.user.data
        ps = form.pswd.data
        ps2 = form.pswd2.data
        print us,ps,ps2
    else:
        flash(u'请输入数据!!')
    print form.validate_on_submit()
    return render_template('login.html',form=form)



@app.route('/demo1',methods=['GET','POST'])
def demo1():
    # 获取表单数据
    user = request.form.get('user')
    pswd = request.form.get('pswd')
    print user,pswd
    return render_template('login.html')


if __name__ == '__main__':
    print app.url_map
    app.run()
