from django.db.models import Max, F
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from apps import models


def index(request):
    html = loader.get_template('index.html')
    context = {'nnn': 'hi'}
    stu = models.Student(name="hong", age=20)
    stu.save()
    res = html.render(context=context)

    return HttpResponse(res)


def add_index(request):
    for i in range(1, 50):
        name = "嘿嘿%d" % i
        age = i
        sex = i % 2
        r = models.People(p_name=name, p_age=age, p_sex=sex)
        r.save()
    return HttpResponse("Success")


def get_people(request):
    # p = models.People.objects.filter(p_sex=True).all()
    # p=models.People.objects.aggregate(Max("p_age"))
    # p=models.People.a.filter(p_age__gte=F('p_sex')+20)
    person = models.People.a.all()
    # print(p)
    # context = {'person': p}
    context = locals()
    return render(request, 'people.html', context=context)


def heh(request):
    response = HttpResponse()
    response.write("sfsdfs")
    response.flush()
    return response


def hehe(request):
    url = reverse("jump")
    print(url)
    return HttpResponseRedirect(url)


def get_json(request):
    data = {
        'status': 200,
        'msg': "ok"
    }
    return JsonResponse(data=data)


def set_Cookies(request):
    response = HttpResponseRedirect(reverse("getcookie"))
    # response = HttpResponse("设置cookie")
    response.set_cookie('uname', 'jack')

    return response


def get_Cookies(request):
    r = request.COOKIES.get('uname')
    return HttpResponse(r)
