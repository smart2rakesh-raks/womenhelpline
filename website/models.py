from django.db import models

# Create your models here.


class complaintstructure(models.Model):

    cid=models.AutoField(primary_key=True)
    cpname=models.CharField(max_length=4000)
    ctitle=models.CharField(max_length=4000)
    cdes=models.CharField(max_length=20000)
    cimage1=models.FileField(upload_to='documents/%Y/%m/%d')
    cimage2 = models.FileField(upload_to='documents/%Y/%m/%d')
    cimage3 = models.FileField(upload_to='documents/%Y/%m/%d')
    cagainstname=models.CharField(max_length=4000)
    csubmiterphone=models.CharField(max_length=4000)
    date=models.CharField(max_length=4000)

    class Meta:
            db_table="complaints"



class  NewsPost(models.Model):
    email=models.CharField(max_length=30)
    img=models.CharField(max_length=300)
    text=models.CharField(max_length=3000)
    postdate=models.CharField(max_length=30)
    class Meta:
        db_table="newsposts"




