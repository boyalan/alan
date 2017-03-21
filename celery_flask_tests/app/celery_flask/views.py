from app.celery_flask import celery_test

from tasks import send_email
import json
@celery_test.route('/test', methods=['GET', 'POST'])
def reset_password():
    email = '1443556385@qq.com'
    toemail = '1443556385@qq.com'
    subject = 'test'
    content = 'test'
    send_email.delay(email,toemail,subject, content)
    return json.dumps({'code':0})
