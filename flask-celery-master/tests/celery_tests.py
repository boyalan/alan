#coding:utf-8
# from celery import Celery
#
#
# def make_celery(app):
#
#     celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
#
#     TaskBase = celery.Task
#
#     class ContextTask(TaskBase):
#         abstract = True
#
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#     celery.Task = ContextTask
#
#     return celery

import uuid,random

from flask import Flask, request, jsonify
from celery import Celery
import smtplib,string
app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


def do_send_email(to,subject):
    SUBJECT = "临时登录密码"
    HOST = "smtp.163.com"
    # TO = passwords['config']['email']
    TO='1443556385@qq.com'
    FROM = "hshsdays@163.com"
    text = str(random.randint(1000, 9999))
    BODY = string.join((

        "From:%s" % FROM,

        "To:%s" % TO,

        "Subject:%s" % SUBJECT,

        "", text), "\r\n")

    server = smtplib.SMTP(HOST)

    server.login("1443556385@qq.com", "zmudpwcqciiujbdg")

    server.sendmail(FROM, [TO], BODY)
    server.quit()

@celery.task
def send_email(to, subject):
    return do_send_email(to, subject)


@app.route('/password/forgot/', methods=['GET','POST'])
def reset_password():
    # email = request.form['email']
    email = '1443556385@qq.com'
    token = str(uuid.uuid4())
    content = u'请点击链接重置密码：http://example.com/password/reset/?token=%s' % token
    send_email.delay(email, content)
    return jsonify(code=0, message=u'发送成功')


if __name__ == '__main__':
    app.run(debug=True)


