from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def cal(first, second):
    result = int(first) * int(second)
    return result

def home(request):
    data = request.GET.copy()
    data['result'] = Deeplearning(data['first'],data['second'])
    return render(request, 'hello/home.html', context = data)

def form(request):
    return render(request, 'hello/form.html')

import tensorflow as tf
def Deeplearning(first, second):
    my_model = tf.keras.models.load_model('hello/Deeplearning.h5')
    param = [int(first), int(second)]
    result = my_model.predict([param])
    return result

# def XORwithKeras(first, second):
#     new_model = tf.keras.models.load_model('hello/XORwithKeras.h5')
#     param = [int(first), int(second)]
#     result = new_model.predict([param])
#     return result


