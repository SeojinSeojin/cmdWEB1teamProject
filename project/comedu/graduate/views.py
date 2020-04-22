from django.shortcuts import render, redirect
# Create your views here.

gradu = {'전공핵심' : ['기본프로그래밍','컴퓨터교육개론','자료구조','데이타베이스','컴퓨터구조','운영체제','컴퓨터네트워크','프로그래밍언어론'],
         '전공핵심학점' : 24, '전공일반' : 42,
         '교직선택' : ['교육학개론','교육의역사.철학적이해','교육의사회학적이해','교육의심리학적이해','교육과정','교육평가','교육방법및교육공학','교육행정및교육경영'],
         '교직필수' : ['특수교육학개론','교직실무','학교폭력의예방및이해','교육실습','교육봉사활동'],
         '교직선택학점' : 12, '교직학점' : 22, '교양' : 52 }

def gradu_index(request):
    return render(request, 'gradu_index.html')

def gradu_cal(request):
    return render(request,'gradu_cal.html')

def calculate(request):
    req = request.POST.getlist('major_req[]')
    gen = int(request.POST.get('major_gen'))
    edu = request.POST.getlist('teach[]')
    elec = int(request.POST.get('elective'))
    
    for i in req:
        gradu['전공핵심'].remove(i)
    gradu['전공핵심학점'] = gradu['전공핵심학점'] - 3*len(req)
    gradu['전공일반'] = gradu['전공일반'] - gen
    for i in edu:
        if i in gradu['교직선택']:
            gradu['교직선택'].remove(i)
        elif i in gradu['교직필수']:
            gradu['교직필수'].remove(i)
    gradu['교직학점'] =  gradu['교직학점'] - 2 * len(edu)
    gradu['교직선택학점'] = 12 - (16 - 2 * len(gradu['교직선택']))
    gradu['교양'] = gradu['교양'] - elec

    print(gradu['교직선택'])
    print(gradu['교직필수'])
    print(gradu['교직학점'], gradu['교직선택학점'])
    print("===========================")

    return redirect('gradu_result')

def gradu_result(request):
    return render(request,'result.html',gradu)