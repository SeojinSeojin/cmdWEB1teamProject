from django.shortcuts import render, redirect, reverse
import copy
# Create your views here.

# 매번 졸업요건을 초기화해주기 위한 dictionary
gradu_save = {
    '전공핵심학점': 24, '전공일반학점': 42, '교직선택학점': 12, '교직학점': 22, '교양': 52,
    '전공핵심': ['기본프로그래밍', '컴퓨터교육개론', '자료구조', '데이타베이스', '컴퓨터구조', '운영체제', '컴퓨터네트워크', '프로그래밍언어론'],        '교직학점': 22, '교직선택학점': 12,
    '교직선택': ['교육학개론', '교육의역사.철학적이해', '교육의사회학적이해', '교육의심리학적이해', '교육과정', '교육평가', '교육방법및교육공학', '교육행정및교육경영'],
    '교직필수': ['특수교육학개론', '교직실무', '학교폭력의예방및이해', '교육실습', '교육봉사활동'],
    '전공일반': ['알고리즘', '인공지능', '소프트웨어공학'],
    '교과교육영역': ['컴퓨터교과교육론', '컴퓨터교재연구및지도법', '상업,정보교과논리논술']
}

gradu = dict()


def gradu_index(request):
    return render(request, 'gradu_index.html')


def gradu_cal(request):
    return render(request, 'gradu_cal.html')


def calculate(request):
    # 졸업요건 관리 초기화
    global gradu
    gradu.clear()
    gradu = copy.deepcopy(gradu_save)
    print(gradu)

    # 졸업요건 계산

    req = request.POST.getlist('major_req[]')  # 수강한 전공핵심 리스트로 받기
    majorEdu = request.POST.getlist('major_edu[]')  # 교과교육영역
    majorOne = request.POST.getlist('major_1[]')  # 전공일반중 기본이수과목
    gen = request.POST.getlist('major_2[]')  # 전공일반 과목
    edu = request.POST.getlist('teach[]')  # 교직
    elec = int(request.POST.get('general'))  # 교양학점

    # 들은 전공핵심 삭제
    for i in req:
        gradu['전공핵심'].remove(i)
    gradu['전공핵심학점'] = gradu['전공핵심학점'] - 3*len(req)
    # 수강한 전공일반 기본이수 삭제
    for i in majorOne:
        gradu['전공일반'].remove(i)
    # 수강한 교과교육영역 삭제
    for i in majorEdu:
        if i == '알고리즘':
            gradu['교과교육영역'].remove('인공지능')
        if i == '인공지능':
            gradu['교과교육영역'].remove('알고리즘')
        gradu['교과교육영역'].remove(i)
    # 남은 학점
    gradu['전공일반학점'] = gradu['전공일반학점'] - \
        len(majorOne)*3 - len(majorEdu)*3 - len(gen)*3
    if '1' in gen:
        gradu['전공일반학점'] += 2
    if '상업,정보교과논리논술' in majorEdu:
        gradu['전공일반학점'] += 1

    for i in edu:
        if i in gradu['교직선택']:
            gradu['교직선택'].remove(i)
        elif i in gradu['교직필수']:
            gradu['교직필수'].remove(i)
    gradu['교직학점'] = gradu['교직학점'] - 2 * len(edu)
    gradu['교직선택학점'] = 12 - (16 - 2 * len(gradu['교직선택']))
    gradu['교양'] = gradu['교양'] - elec

    '''
    print(gradu['교직선택'])
    print(gradu['교직필수'])
    print(gradu['교직학점'], gradu['교직선택학점'])
    print("===========================")
    '''

    return redirect(reverse('graduate:gradu_result'))


def gradu_result(request):
    global gradu
    return render(request, 'result.html', gradu)
