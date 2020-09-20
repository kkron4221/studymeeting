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
    plan_list = []
    for i in range(6):
        i = i + 1
        search_plan = "search" + str(i)
        plan = request.POST.get(search_plan)
        if plan == "":
            continue
        else:
            plan_list.append(plan)
            mes = "明日の予定を設定したよ"
    return render(request, 'todo/plans.html', mes)