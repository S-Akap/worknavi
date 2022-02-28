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
    result_data = ''

    sex_dict = {'called': '性別', 'type': 'select',
                'both': 'どちらでも可', 'man': '男性', 'woman': '女性', }
    age_dict = {'called': '年齢', 'type': 'number', }
    requirement_dict = {'called': '資格',
                        'type': 'select', 'noneed': '必要なし', 'need': '必要'}
    hourly_pay_dict = {'called': '希望時給', 'type': 'number', }
    citizenship_dict = {'called': '国籍', 'type': 'select',
                        'both': '外国人でも可', 'japan': '日本人のみ', }
    residence_dict = {'called': '居住地', 'type': 'text', }
    item_dict = {'sex': sex_dict, 'age': age_dict, 'requirement': requirement_dict,
                 'hourly_pay': hourly_pay_dict, 'citizenship': citizenship_dict, 'residence': residence_dict}

    print('request.GET : {}'.format(request.GET))

    if request.GET != {}:
        result_data = RegisteredStaff.objects.filter(is_contact=True)
        result_data = search_stuff_func(
            request=request, result_data=result_data)

    send_data = {'result_data': result_data, 'item_dict': item_dict}

    return render(request, 'service/search_stuff.html', send_data)


# def search_stuff(request):
#     '''登録スタッフ検索ページ'''
#     sex_dict = {'called': '性別', 'type': 'select',
#                 'both': 'どちらでも可', 'man': '男性', 'woman': '女性', }
#     age_dict = {'called': '年齢', 'type': 'number', }
#     requirement_dict = {'called': '資格',
#                         'type': 'select', 'noneed': '必要なし', 'need': '必要'}
#     hourly_pay_dict = {'called': '希望時給', 'type': 'number', }
#     citizenship_dict = {'called': '国籍', 'type': 'select',
#                         'both': '外国人でも可', 'japan': '日本人のみ', }
#     residence_dict = {'called': '居住地', 'type': 'text', }
#     item_dict = {'sex': sex_dict, 'age': age_dict, 'requirement': requirement_dict,
#                  'hourly_pay': hourly_pay_dict, 'citizenship': citizenship_dict, 'residence': residence_dict}

#     send_data = {'item_dict': item_dict}

#     return render(request, 'service/search_stuff.html', send_data)


def search_stuff_func(request, result_data):
    if request.GET['sex'] != 'both':
        result_data = result_data.filter(sex=request.GET['sex'])

    if request.GET['age'] != '':
        result_data = result_data.filter(age__lte=request.GET['age'])

    if request.GET['requirement'] != 'need':
        pass

    if request.GET['hourly_pay'] != '':
        result_data = result_data.filter(
            Q(hourly_pay__lte=request.GET['hourly_pay']) | Q(hourly_pay__isnull=True))

    if request.GET['citizenship'] != 'both':
        result_data = result_data.filter(
            citizenship=request.GET['citizenship'])

    if request.GET['residence'] == 'japan':
        pass

    return result_data


def randomname(n):
    randlst = [random.choice(string.ascii_letters)
               for i in range(n)]
    return ''.join(randlst)


def exchange_search_stuff_data(request):
    print('request.POST : {}'.format(request.POST))
    print('request.GET : {}'.format(request.GET))
    test_data = {'TEST': randomname(4)}

    return JsonResponse(request.GET)


def search_company(request):
    '''登録企業検索ページ'''
    return render(request, 'service/search_company.html')
