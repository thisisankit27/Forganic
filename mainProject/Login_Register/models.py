from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
ALLOWED_EMAILS = ["protonmail.com", "gmail.com", "yahoo.com", "outlook.com", "zoho.com", "unifive.co",
                  "icloud.com", "aol.com", "mail.com", "yandex.com", "gmx.com", "fastmail.com",
                  "hushmail.com", "tutanota.com", "startmail.com", "posteo.de", "runbox.com",
                  "openmailbox.org", "vfemail.net", "disroot.org", "kolabnow.com", "privaterelay.apple.com",
                  "ctemplar.com", "neomailbox.com", "zimbra.com", "lycos.com", "soverin.net",
                  "thexyz.com", "luxsci.com", "mailfence.com"]

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class CustomerProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    
    @classmethod
    def create_profile(cls, username, email, first_name, last_name, password, password2):
        if not any(email.endswith(e) for e in ALLOWED_EMAILS):
            return {'success': False, 'message': 'Disposable e-mail is not accepted!'}
        if User.objects.filter(username=username).exists():
            return {'success': False, 'message': 'Username Already Exists!'}
        elif User.objects.filter(email=email).exists():
            return {'success': False, 'message': 'Email Already Exists!'}
        else:
            if password == password2:
                userObj = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                userObj.save()
                
                userModel = User.objects.get(username=username)
                newProfile = cls.objects.create(user=userModel, id_user=userModel.id)   
                newProfile.save()
                return {'success': True, 'url': 'login'}
            else:
                return {'success': False, 'message': "Passwords don't Match!"}
    
    @classmethod
    def verify_user(cls, user, username):
        if user is not None:
            return {'success': True, 'url': '/'}
        else:
            if User.objects.filter(username=username).exists():
                return {'success': False, 'message': 'Wrong Password!'}
            else:
                return {'success': False, 'message': 'Username Does Not Exist!'}