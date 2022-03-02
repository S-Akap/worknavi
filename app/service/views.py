from re import A
import string
import random
from django.shortcuts import render

# Create your views here.
from .models import RegisteredStaff
from django.db.models import Q
from django.http.response import JsonResponse


def index(request):
    '''初期ページ'''
    return render(request, 'service/index.html')


def search_stuff(request):
    '''登録スタッフ検索ページ'''
    sex_dict = {
        'called': '性別',
        'type': 'select',
        'both': 'どちらでも可',
        'man': '男性',
        'woman': '女性',
    }
    age_dict = {
        'called': '年齢',
        'type': 'number',
    }
    requirement_dict = {
        'called': '資格',
        'type': 'select',
        'noneed': '必要なし',
        'need': '必要'
    }
    hourly_pay_dict = {
        'called': '希望時給',
        'type': 'number',
    }
    citizenship_dict = {
        'called': '国籍',
        'type': 'select',
        'both': '外国人でも可',
        'japan': '日本人のみ',
    }
    residence_dict = {
        'called': '居住地',
        'type': 'text',
    }
    item_dict = {
        'sex': sex_dict,
        'age': age_dict,
        'requirement': requirement_dict,
        'hourly_pay': hourly_pay_dict,
        'citizenship': citizenship_dict,
        'residence': residence_dict
    }

    send_data = {
        'item_dict': item_dict
    }

    return render(request, 'service/search_stuff.html', send_data)


def search_stuff_func(request_data, result_data):
    if request_data['sex'] != 'both':
        result_data = result_data.filter(sex=request_data['sex'])

    if request_data['age'] != '':
        result_data = result_data.filter(age__lte=request_data['age'])

    if request_data['requirement'] != 'need':
        pass

    if request_data['hourly_pay'] != '':
        result_data = result_data.filter(
            Q(hourly_pay__lte=request_data['hourly_pay']) | Q(hourly_pay__isnull=True))

    if request_data['citizenship'] != 'both':
        result_data = result_data.filter(
            citizenship=request_data['citizenship'])

    # if request_data['residence'] == '':
    #     pass

    return result_data


# POST /api/search
# data = { 'sex':str, 'age':int, 'requirement':str, 'hourly_pay':int, 'citizenship':str, 'residence':str }
def exchange_search_stuff_data(request):
    data = request.POST
    print(data)

    # return JsonResponse(request.GET)

    #  データ加工
    # number = random.randint(0, 100)
    result_data = RegisteredStaff.objects.filter(is_contact=True)
    number = search_stuff_func(
        request_data=request.POST, result_data=result_data).count()
    return JsonResponse({"data": data, "number": number})


def search_company(request):
    '''登録企業検索ページ'''
    return render(request, 'service/search_company.html')
