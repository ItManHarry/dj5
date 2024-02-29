from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404, redirect, reverse
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = '<br>'.join([q.question_text for q in latest_question_list])
    return render(request, 'polls/index.html', dict(latest_question_list=latest_question_list))
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Quest does not exist!')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', dict(question=question))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', dict(question=question))
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', dict(question=question, error_message='You did not select a choice!'))
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return redirect(reverse('polls:results', args=(question.id,)))