from django.shortcuts import render

from .models import Question

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_questions
    }
    return render(request,'polls/index.html', context)