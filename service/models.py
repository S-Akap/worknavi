from django.db import models

# Create your models here.
from django.db.models import Q


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
    '''国籍フィールド'''
    citizenship = models.CharField('国籍', max_length=20, unique=True)

    def __str__(self):
        return self.citizenship


class RegisteredStaffQuerySet(models.QuerySet):
    '''クエリセットのメソッド追加'''

    def search(self, query=None):
        # クエリセットの取得
        query_set = self
        # 連絡が繋がるスタッフのみにフィルタリング
        query_set = query_set.filter(is_contact=True)

        try:
            # 性別絞り込み
            if query['sex'] != 'both':  # 性別指定がある時
                query_set = query_set.filter(sex__sex=query['sex'])

            # 年齢絞り込み
            query_set = query_set.filter(age__lte=query['age'])

            # 資格絞り込み
            query_set = query_set.filter(
                Q(requirement__requirement__exact=query['requirement']) | Q(requirement__requirement__isnull=True))

            # 希望時給絞り込み
            query_set = query_set.filter(
                Q(hourly_pay__lte=query['hourly_pay']) | Q(hourly_pay__isnull=True))

            # 国籍絞り込み
            if query['citizenship'] != 'both':  # 国籍指定がある時
                query_set = query_set.filter(
                    Q(citizenship__citizenship__exact=query['citizenship']) | Q(citizenship__citizenship__isnull=True))

            # 居住地絞り込み
            # 未実装

            # アップデート順に並び替え
            query_set = query_set.order_by('-updated_datetime')
        except:
            import traceback
            traceback.print_exc()
            query_set = None

        return query_set


class RegisteredStaffManager(models.Manager):
    '''objectsからのメソッド追加'''

    def get_queryset(self):
        return RegisteredStaffQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class RegisteredStaff(models.Model):
    '''派遣スタッフフィールド'''
    name = models.CharField(
        blank=False, null=False, max_length=30, verbose_name='名前'
    )  # 名前
    sex = models.ForeignKey(
        Sex, on_delete=models.PROTECT, verbose_name='性別'
    )  # 性別
    age = models.IntegerField(
        blank=False, null=False, verbose_name='年齢'
    )  # 年齢
    requirement = models.ForeignKey(
        Requirement, on_delete=models.PROTECT, blank=True, null=True, verbose_name='資格'
    )  # 資格
    hourly_pay = models.IntegerField(
        blank=True, null=True, verbose_name='希望時給'
    )  # 希望時給
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.PROTECT, blank=True, null=True, verbose_name='国籍'
    )  # 国籍
    residence = models.CharField(
        blank=True, null=True, max_length=100, verbose_name='居住地'
    )  # 居住地
    is_contact = models.BooleanField(
        verbose_name='連絡がすぐ繋がるか'
    )  # すぐに連絡が繋がるかどうか
    created_datetime = models.DateTimeField(
        auto_now_add=True
    )  # 作成日
    updated_datetime = models.DateTimeField(
        auto_now=True
    )  # 更新日

    objects = RegisteredStaffManager()

    def __str__(self):
        return self.name


class Address(models.Model):
    '''住所フィールド'''
    zip_code = models.CharField(
        verbose_name='郵便番号', max_length=8, blank=True,
    )  # 郵便番号
    address1 = models.CharField(
        verbose_name='都道府県', max_length=40, blank=True,
    )  # 都道府県
    address2 = models.CharField(
        verbose_name='市区町村番地', max_length=40, blank=True,
    )  # 市区町村番地
    address3 = models.CharField(
        verbose_name='建物名', max_length=40, blank=True,
    )  # 建物名

    def __str__(self):
        return self.address1 + self.address2 + self.address3


class Company(models.Model):
    '''会社フィールド'''
    name = models.CharField(
        '会社名', max_length=10, unique=True
    )  # 会社名
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, verbose_name='会社住所'
    )  # 会社住所

    def __str__(self):
        return self.name


class RegisteredCompany(models.Model):
    '''求人希望情報フィールド'''
    name = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name='求人会社'
    )  # 求人会社名
    sex = models.ForeignKey(
        Sex, on_delete=models.PROTECT, verbose_name='性別'
    )  # 性別
    age = models.IntegerField(
        blank=False, null=False, verbose_name='年齢'
    )  # 年齢
    requirement = models.ForeignKey(
        Requirement, on_delete=models.PROTECT, blank=True, null=True, verbose_name='資格'
    )  # 資格
    hourly_pay = models.IntegerField(
        blank=True, null=True, verbose_name='希望時給'
    )  # 希望時給
    citizenship = models.ForeignKey(
        Citizenship, on_delete=models.PROTECT, blank=True, null=True, verbose_name='国籍'
    )  # 国籍
    created_datetime = models.DateTimeField(
        auto_now_add=True
    )  # 作成日
    updated_datetime = models.DateTimeField(
        auto_now=True
    )  # 更新日

    def __str__(self):
        return self.name
