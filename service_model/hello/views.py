from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# def cal(first, second):
#     result = int(first) * int(second)
#     return result

def home(request):
    return render(request, 'hello/home.html')

def form(request):
    return render(request, 'hello/form.html')

def result(request):
    data = request.GET.copy()
    return render(request, 'hello/result.html', context = data)

# Using API connected with DB by sqlite
from django.http import JsonResponse
def simpleapi(request):
    date = request.GET['date']
    data = []
    import sqlite3
    conn = sqlite3.connect('db2.sqlite3')
    c = conn.cursor()
    c.execute('SELECT * FROM economic WHERE release_date == "{}"'.format(date))     # 변수 선언한 date를 사용하기 위해 format 넣음 if not 변수를 변수로 읽지 못함
    rows = c.fetchall()
    for row in rows:
        data.append({'released_date':row[0],'title':row[1],'link':row[2]})
    requestDict = {'result_response':data}
    return JsonResponse(requestDict)

# # for using api - BASIC
# from django.http import JsonResponse
# def simpleapi(request):
#     date = request.GET['name']
#     age02 = request.GET['age']
#     result = int(age02) + 5
#     requestDict = {'result_response':result}
#     return JsonResponse(requestDict)

# import tensorflow as tf
# def Deeplearning(first, second):
#     my_model = tf.keras.models.load_model('hello/Deeplearning.h5')
#     param = [int(first), int(second)]
#     result = my_model.predict([param])
#     return result

# def template(request):
#     return render(request, 'hello/template.html')

# def XORwithKeras(first, second):
#     new_model = tf.keras.models.load_model('hello/XORwithKeras.h5')
#     param = [int(first), int(second)]
#     result = new_model.predict([param])
#     return result

# def templatefromsite(request):
#     return render(request, 'hello/templatefromsite.html')

# def bootstrapTemp(request):
#     return render(request, 'hello/bootstrapTemp.html')
