from django.shortcuts import render

# Create your views here.
from .forms import SearchStaffForm
from django.http.response import JsonResponse


def index(request):
    '''初期ページ'''
    return render(request, 'service/index.html')


def search_staff(request):
    '''登録スタッフ検索ページ'''
    forms = SearchStaffForm()
    return render(request, 'service/search_staff.html', {'forms': forms})


def search_company(request):
    '''登録企業検索ページ'''
    return render(request, 'service/search_company.html')


# やり取りするデータ
# data = { 'sex':str, 'age':int, 'requirement':str, 'hourly_pay':int, 'citizenship':str, 'residence':str }
def exchange_search_staff(request):
    '''検索内容のやり取り'''
    get_data = request.POST

    import random
    number = random.randint(0, 100)

    send_data = {
        'raw': {
            'data': get_data,
            'number': number,
        },
        'processed1': {
            'data': {},
            'number': 200,
        },
    }

    print('get_data : {}'.format(get_data))
    return JsonResponse(send_data)


def search_staff_func(data):
    '''登録スタッフ検索'''
    pass
