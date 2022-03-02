from django.shortcuts import render

# Create your views here.
from .models import RegisteredStaff
from django.db.models import Q
from django.http.response import JsonResponse


def index(request):
    '''初期ページ'''
    return render(request, 'service/index.html')


def search_staff(request):
    '''登録スタッフ検索ページ'''

    item_dict = {
        'sex': {
            'called': '性別',
            'type': 'select',
            'contents': {
                'both': 'どちらでも可',
                'man': '男性',
                'woman': '女性',
            },
        },
        'age': {
            'called': '年齢',
            'type': 'number',
            'contents': {
            },
        },
        'requirement': {
            'called': '資格',
            'type': 'select',
            'contents': {
                'noneed': '必要なし',
                'need': '必要'
            },
        },
        'hourly_pay': {
            'called': '希望時給',
            'type': 'number',
            'contents': {
            },
        },
        'citizenship': {
            'called': '国籍',
            'type': 'select',
            'contents': {
                'both': '外国人でも可',
                'japan': '日本人のみ',
            },
        },
        'residence': {
            'called': '居住地',
            'type': 'text',
            'contents': {
            },
        },
    }

    send_data = {
        'item_dict': item_dict
    }

    return render(request, 'service/search_staff.html', send_data)


def search_staff_func(request_data, result_data):
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


# data = { 'sex':str, 'age':int, 'requirement':str, 'hourly_pay':int, 'citizenship':str, 'residence':str }

def exchange_search_staff_data(request):
    data = request.POST
    print(data)

    #  データ加工
    result_data = RegisteredStaff.objects.filter(is_contact=True)
    number = search_staff_func(
        request_data=request.POST, result_data=result_data).count()
    return JsonResponse({"data": data, "number": number})


def search_company(request):
    '''登録企業検索ページ'''
    return render(request, 'service/search_company.html')
