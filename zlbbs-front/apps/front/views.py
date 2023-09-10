from flask import Blueprint, request, render_template, jsonify, current_app
import string
import random
from flask_mail import Message
from exts import mail, cache
from utils import restful

bp = Blueprint('front', __name__, url_prefix='/')


@bp.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @bp.get('/email/captcha')
# def email_captcha():
#     # email/captcha?email=xxx@qq.com
#     email = request.args.get('email')
#     if not email:
#         return jsonify({'code': 400, 'message': '请先传入邮箱!'})
#     # 随机6位数字
#     source = list(string.digits)
#     captcha = ''.join(random.sample(source, 6))
#     message = Message(subject='[flask_bbs]注册验证码', recipients=[email], body=f'[flask_bbs]你的注册验证为:{captcha}')
#     try:
#         # 发送邮件实际上是一个网络请求
#         mail.send(message)
#     except Exception as e:
#         print('邮件发送失败')
#         print(e)
#         return jsonify({'code': 500, 'message': '邮件发送失败'})
#     return jsonify({'code': 200})


@bp.get('/email/captcha')
def email_captcha():
    # email/captcha?email=xxx@qq.com
    email = request.args.get('email')
    if not email:
        return restful.params_error(message="请先传入邮箱")

    # 随机6位数字
    source = list(string.digits)
    captcha = ''.join(random.sample(source, 6))
    subject = '[flask_bbs]注册验证码'
    body = f'[flask_bbs]你的注册验证为:{captcha}'
    current_app.celery.send_task('send_mail', (email, subject, body))
    cache.set(email, captcha)
    print(cache.get(email))
    return restful.ok(message='邮件发送成功')


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('front/login.html')


@bp.route('/regist/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('front/register.html')
