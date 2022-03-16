from django.shortcuts import render

from service.models import RegisteredStaff

# Create your views here.
from .forms import SearchStaffForm, SearchCompanyForm
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
    # 入力フォーム
    forms = SearchCompanyForm()
    # 順位表示用range
    for_range = [i+1 for i in range(10)]

    send_data = {
        'forms': forms,
        'for_range': for_range,
        'ranking': None,
    }
    return render(request, 'service/search_company.html', send_data)


# やり取りするデータ
# data = { 'sex':, 'age':, 'requirement':, 'hourly_pay':, 'citizenship':, 'residence': }
def exchange_search_staff(request):
    '''スタッフ検索内容のやり取り'''
    get_data = request.POST

    try:
        # 検索結果の該当者数を取得
        raw_number = search_staff_func(data=get_data).count()
    except:
        import traceback
        traceback.print_exc()
        raw_number = -1

    try:
        # 条件緩和での検索
        result = processed_stuff_search(data=get_data)
        processed1_data, processed2_data = result[0], result[1]
        processed1_number = search_staff_func(data=processed1_data).count()
        processed2_number = search_staff_func(data=processed2_data).count()

        # 緩和前のデータと等しい時
        if processed1_data == get_data:
            processed1_data, processed1_number = {}, -1
            if processed2_data == get_data:
                processed2_data, processed2_number = {}, -1
    except:
        import traceback
        traceback.print_exc()
        processed1_data, processed1_number = {}, -1
        processed2_data, processed2_number = {}, -1

    send_data = {
        'raw': {
            'data': get_data,
            'number': raw_number,
        },
        'processed1': {
            'data': processed1_data,
            'number': processed1_number,
        },
        'processed2': {
            'data': processed2_data,
            'number': processed2_number,
        },
    }

    return JsonResponse(send_data)


def processed_stuff_search(data):
    '''複数の条件緩和案を実行し、最適案を確定'''
    # try_data = [
    #     [検索内容, 検索結果数],
    #     [検索内容, ...]
    # ]
    try_data = [[data.copy(), 0] for i in range(5)]

    # 性別緩和
    if data['sex'] != 'both':  # 緩和可能な時
        # 条件内容の変更
        try_data[0][0]['sex'] = 'both'
        # 検索結果
        try_data[0][1] = search_staff_func(data=try_data[0][0]).count()

    # 年齢緩和
    if data['age'] != '99':  # 緩和可能な時
        # 条件内容の変更
        try_data[1][0]['age'] = str(int(try_data[1][0]['age']) + 10)
        # 検索結果
        try_data[1][1] = search_staff_func(data=try_data[1][0]).count()

    # 資格緩和
    if data['requirement'] != 'nothing':  # 緩和可能な時
        # 条件内容の変更
        try_data[2][0]['requirement'] = 'nothing'
        # 検索結果
        try_data[2][1] = search_staff_func(data=try_data[2][0]).count()

    # 希望時給緩和
    if data['hourly_pay'] != '9999':  # 緩和可能な時
        # 条件内容の変更
        try_data[3][0]['hourly_pay'] = str(
            int(try_data[3][0]['hourly_pay']) + 50)
        # 検索結果
        try_data[3][1] = search_staff_func(data=try_data[3][0]).count()

    # 国籍緩和
    if data['citizenship'] != 'both':  # 緩和可能な時
        # 条件内容の変更
        try_data[4][0]['citizenship'] = 'both'
        # 検索結果
        try_data[4][1] = search_staff_func(data=try_data[4][0]).count()

    # 人数の多い順にソート
    result = sorted(try_data, key=lambda x: x[1], reverse=True)

    return [result[i][0] for i in range(len(result))]


def search_staff_func(data):
    '''登録スタッフ検索'''
    data = RegisteredStaff.objects.search(query=data)
    return data


def exchange_search_company(request):
    '''会社検索内容のやり取り'''
    pass
