from random import vonmisesvariate
from django.db import models

# Create your models here.


class Sex(models.Model):
    '''性別フィールド'''
    sex = models.CharField('性別', max_length=10, unique=True)

    def __str__(self):
        return self.sex


class Requirement(models.Model):
    '''資格フィールド'''
    requirement = models.CharField('資格', max_length=50, unique=True)

    def __str__(self):
        return self.requirement


class Citizenship(models.Model):
    '''国籍'''
    citizenship = models.CharField('国籍', max_length=20, unique=True)

    def __str__(self):
        return self.citizenship


class RegisteredStaff(models.Model):
    name = models.CharField(
        blank=False, null=False, max_length=30, verbose_name='名前')  # 名前
    sex = models.ForeignKey(
        Sex, on_delete=models.PROTECT, verbose_name='性別')  # 性別
    age = models.IntegerField(
        blank=False, null=False, verbose_name='年齢')  # 年齢
    requirement = models.ForeignKey(
        Requirement, on_delete=models.PROTECT, blank=True, null=True, verbose_name='資格')  # 資格
    hourly_pay = models.IntegerField(
        blank=True, null=True, verbose_name='希望時給')  # 希望時給
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.PROTECT, blank=True, null=True, verbose_name='国籍')  # 国籍
    residence = models.CharField(
        blank=True, null=True, max_length=100, verbose_name='居住地')  # 居住地
    is_contact = models.BooleanField(
        verbose_name='連絡がすぐ繋がるか')  # すぐに連絡が繋がるかどうか
    created_datetime = models.DateTimeField(auto_now_add=True)  # 作成日
    updated_datetime = models.DateTimeField(auto_now=True)  # 更新日

    def __str__(self):
        return self.name
