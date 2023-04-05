from django.core.mail import send_mail
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
import time
from datetime import datetime, timedelta


def genrate_jwt(user_id, delay_time = 3000):
    now = datetime.utcnow()
    encoded_jwt = jwt.encode({
        'id':str(user_id),
        'exp':(now + timedelta(seconds=delay_time)).timestamp(),
    }, "secret", algorithm="HS256") #inenv
    return encoded_jwt

def validate_jwt(token):
    try:
        data = jwt.decode(token, "secret", algorithms=["HS256"])
        print("data",data)
        id = data['id']
        return {'status':True,'id':id}
    except jwt.ExpiredSignatureError:
            return {'status':False,'id':None}

def genratelink(*args,**kwargs):
    user_id = kwargs['user_pk']
    jwt_token = genrate_jwt(user_id)
    domain = "127.0.0.1:8000"   #in env
    relative_link = reverse('linkvalidate',kwargs = {'token':jwt_token})
    link = 'http://'+domain+relative_link
    return link


def verifyemail(email,link):
    email = 'parmanu2020@gmail.com' #email
    send_mail(
            'Meddi tracker',
                        f'Click this link to activate the account {link}',
                        'donotreply@gmail.com', 
                        [email],
                        fail_silently=False
                )
    

