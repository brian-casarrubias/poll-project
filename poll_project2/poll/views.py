from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Choice, Question
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'poll/index.html')


def pollstart(request, pk):
    #instance object we will be working on
    pll = get_object_or_404(Choice, pk=pk)

    #pk_gt primary key greater than
    #then it orders by first, so next one
    next_poll = Choice.objects.filter(pk__gt=pll.pk).order_by().first()

    
    if request.method == 'POST':
        
        selected_choice = request.POST.get('choice', None)

        if selected_choice == pll.choice_text1:
            pll.choice_text1_value+=1

        elif selected_choice == pll.choice_text2:
            pll.choice_text2_value+=1

        pll.save()

        #if there is a next_poll and we didnt get 'none'
        if next_poll:

            return redirect(next_poll.get_absolute_url())
        #else this means our polls are done, so lets redirect user to the 
        #results page which displays all the votes
        else:
            return redirect('results-page')#display the results page
        

    return render(request, 'poll/home.html', {'pll':pll, 'next_poll':next_poll })
    
def results(request):
    context = {
        'zaza':Choice.objects.all()
    }
    return render(request, 'poll/resultspage.html', context)


 #selected_choice = request.POST.get('car', None) 



class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'poll/choice_form.html'
    

    fields = [
        'question',
        'choice_text1',
        'choice_text2',
        
        
    ]

class QuestionCreateView(CreateView):

    model = Question
    template_name = 'poll/question_form.html'

    fields = [
        'question',
    ]



class ChoiceUpdateView(LoginRequiredMixin, UpdateView):

    model = Choice
    
    template_name = 'poll/question_update_form.html'

    fields = [
        'question',
        'choice_text1',
        'choice_text2',
        
    ]
