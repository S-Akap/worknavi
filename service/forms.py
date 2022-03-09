from .models import RegisteredStaff

from django import forms


class SearchStaffForm(forms.Form):
    # selectタグの選択肢
    SEX_CHOICE = (
        ('both', 'どちらでも可'),
        ('man', '男性のみ'),
        ('woman', '女性のみ'),
    )
    REQUIREMENT_CHOICE = (
        ('nothing', '特に必要なし'),
    )
    RESIDENCE_CHOICE = (
        ('both', '外国人でも可'),
        ('japan', '日本人のみ'),
    )

    # formタグ作成
    sex = forms.ChoiceField(label='性別', choices=SEX_CHOICE)
    age = forms.IntegerField(label='年齢', initial=99)
    requirement = forms.ChoiceField(label='資格', choices=REQUIREMENT_CHOICE)
    hourly_pay = forms.IntegerField(label='希望時給', initial=9999)
    residence = forms.ChoiceField(label='国籍', choices=RESIDENCE_CHOICE)
    citizenship = forms.CharField(label='居住地', required=False)
