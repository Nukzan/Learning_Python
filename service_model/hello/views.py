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
