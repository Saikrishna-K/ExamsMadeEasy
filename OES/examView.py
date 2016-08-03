import json


from django.core import serializers
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView

from models import *
from django.shortcuts import render_to_response, render


@csrf_exempt#create ExamDetails
def createExamDetails(request):

    if request.method == 'POST' and request.POST.get("f") == 'exam':
        title = request.POST.get("title")
        about = request.POST.get("about")
        qCount = request.POST.get("qCount")
        total = request.POST.get("total")
        duration = request.POST.get("duration")
        queryset = ExamDetails(examiner_id=request.user.id, title=title, about=about, qCount=qCount, total=total,
                               duration=duration)
        queryset.save()
        return HttpResponse(json.dumps("Done"), content_type='application/json')

    elif request.method == 'POST' and 'question' == request.POST.get("f"):
        question = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        correct = request.POST.get("correct")
        id = ExamDetails.objects.filter(examiner_id=request.user.id).values('title').last().values()[0]
        queryset = Questions(exam_id=id, question=question, option1=option1, option2=option2, option3=option3,
                             option4=option4, correct=correct)
        queryset.save()
        return HttpResponse(json.dumps("Done"), content_type='application/json')


# Lists ExamDetails #Done
class ListUserExamDetails(ListView):
    model = ExamDetails

    def get(self, request, *args, **kwargs):
        queryset = ExamDetails.objects.filter(examiner_id=self.request.user.id)
        queryset = serializers.serialize("json",queryset)
        return HttpResponse(queryset, content_type='application/json')


class ListSpecificExamResults(ListView):

    def get(self, request, *args, **kwargs):
        queryset = ExamDetails.objects.filter(examiner_id=request.GET.get('exam'))
        queryset = serializers.serialize("json", queryset)
        return HttpResponse(queryset, content_type='application/json')


def list_result_user(request):
    queryset = Result.objects.filter(exam=request.GET.get('pk')).all()
    queryset = serializers.serialize("json", queryset)
    return HttpResponse(queryset, content_type='application/json')


