from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def todolist(request):
    return render(request, 'todo/main.html')

def today_menu(request):
    return render(request, 'todo/todays.html')

def plans(request):
    return render(request, 'todo/plans.html')

def log(request):
    return render(request, 'todo/log.html')

def plan_date(request):
    for i in range(6):
        i = i + 1
        search_plan = "search" + str(i)
        plan = request.POST.get(search_plan)
        if plan == "":
            err_mes = "空いている項目があります。"
            return render(request, 'todo/plans.html', err_mes)