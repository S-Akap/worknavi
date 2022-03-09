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


# data = { 'sex':str, 'age':int, 'requirement':str, 'hourly_pay':int, 'citizenship':str, 'residence':str }
def exchange_search_staff(request):
    '''登録スタッフ検索'''
    data = request.POST
    number = 200
    print('data : {}'.format(data))
    return JsonResponse({"data": data, "number": number})
