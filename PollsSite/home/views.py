from django.http import HttpResponse,HttpResponseRedirect#,Http404,
from django.urls import reverse
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice






#the home page,displays the latest 5 questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request,"home/index.html",context)








#details about a particular question
def detail(request, question_id):
    #try:
    #    question=Question.objects.get(pk= question_id)
    #except Question.DoesNotExist:
    #    raise Http404('Question does not exist')
    question=get_object_or_404(Question, pk=question_id)#the function takes in the class,pk
    return render(request,'home/detail.html',{'question':question})






#results about a particular question
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'home/results.html',{'question':question})





def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'home/detail.html',{'question':question, 'error_message':'you didnt select a choice'})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('home:results',args=(question.id,)))
