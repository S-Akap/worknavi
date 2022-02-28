from pyexpat import model
from django.db import models

# Create your models here.

SEX_CHOICE = [('man', '男性'), ('woman', '女性')]


class RegisteredStaff(models.Model):
    name = models.CharField(blank=False, null=False, max_length=30)  # 名前
    sex = models.CharField(blank=False, null=False,
                           max_length=5, choices=SEX_CHOICE)  # 性別
    age = models.IntegerField(blank=False, null=False)  # 年齢
    requirement = models.CharField(blank=True, null=True, max_length=30)  # 資格
    hourly_pay = models.IntegerField(blank=True, null=True)  # 希望時給
    citizenship = models.CharField(blank=True, null=True, max_length=25)  # 国籍
    residence = models.CharField(blank=True, null=True, max_length=100)  # 居住地
    is_contact = models.BooleanField()  # すぐに連絡が繋がるかどうか
    created_datetime = models.DateTimeField(auto_now_add=True)  # 作成日
    updated_datetime = models.DateTimeField(auto_now=True)  # 更新日

    def __str__(self):
        '''登録スタッフのID'''
        return self.name
