# from django.db import models

# # Create your models here.

# import mongoengine as m


# class AdminUserMaster(models.Model):
#     admName=models.CharField(max_length=100)
#     admEmail=models.EmailField(max_length=100)
#     admPassword=models.CharField(max_length=100)
#     admStatus=models.CharField(max_length=100)


# class MasterCategory(m.Document):
#     catName=m.StringField(max_length=100)
#     catSlug=m.StringField(max_length=100)
#     catStatus=m.BooleanField(default=True)
#     catSeqNo=m.IntField()



from django.db import models

class AdminUserMaster(models.Model):
    admName = models.CharField(max_length=100)
    admEmail = models.EmailField(max_length=100)
    admPassword = models.CharField(max_length=100)
    admStatus = models.CharField(max_length=100)

class MasterCategory(models.Model):  
    catName = models.CharField(max_length=100)
    catSlug = models.CharField(max_length=100)
    catStatus = models.BooleanField(default=True)
    catSeqNo = models.IntegerField()



#article model
class article_master(models.Model):
    title=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    category = models.ForeignKey(MasterCategory, on_delete=models.CASCADE) 
    image=models.ImageField(upload_to="image/")
    description=models.TextField()
    