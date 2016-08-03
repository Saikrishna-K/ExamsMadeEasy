import json


import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core import serializers
from django.http.response import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from OES.models import *


@login_required
def test_home(request):
    return render_to_response('TEST/testhome.html', {'user': request.user})


class ListExamDetails(ListView):
    model = ExamDetails

    def get(self, request, *args, **kwargs):
        queryset = ExamDetails.objects.all()
        queryset = serializers.serialize("json", queryset)
        return HttpResponse(queryset, content_type='application/json')


class ListQuestions(ListView):
    model = Questions

    def get(self, request, *args, **kwargs):
        print request.GET.get('pk');
        queryset = Questions.objects.filter(exam_id=request.GET.get('pk'))

        queryset = serializers.serialize("json", queryset)
        return HttpResponse(queryset, content_type='application/json')


def result(request):
    ename = request.GET.get('pk')
    arr = request.GET.getlist('result[]')
    answers = Questions.objects.filter(exam=ename).values('correct')
    count = 0
    for i in range(0, answers.count()):
        x = answers[i].values()[0]
        y = int(arr[i])
        if y == x:
            count += 1
    user = request.user.id
    test = Result.objects.create(userID_id=user,exam_id=ename,marks=count,attempt_time=time.strftime("%d-%m-%Y %H:%M"))
    test.save()
    return HttpResponse(json.dumps(count), content_type='application/json')


def list_result(request):
    queryset = Result.objects.filter(userID=request.user.id).all()
    queryset = serializers.serialize("json", queryset)
    return HttpResponse(queryset, content_type='application/json')
