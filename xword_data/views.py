from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import random

# Create your views here.
from models import puzzle
from models import clue
from models import entry

def cross_word(request):
    ind = random.randint(0, clue.objects.count() - 1)
    c = clue.objects.all()[ind]
    context = {'clue': c, 'user_message':''}
    return render(request, 'drill.html', context)

def guess(request, clue_id):
    c = clue.objects.filter(id=clue_id).first()

    a = request.POST.get("user_answer")
    actual = c.entry.entry_text.strip().upper()
    if a.strip().upper() == c.entry.entry_text.strip().upper():
        # return answer(request, clue_id)
        return redirect('/answer/{}'.format(clue_id))
    else:
        user_message = 'You\'re Wrong!!!'
    context = {'clue': c, 'user_message':actual}
    return render(request, 'drill.html', context)

def answer(request, clue_id):
    '''
    Figure out if the clue is unique in the database
    if it is, state that the clue is unique

    Otherwise, count the number of entries associated with the clue and the count of
    clue entry pairs
    :param request:
    :param clue_id:
    :return:
    '''
    c = clue.objects.filter(id=clue_id).first() #find clue from url
    c_set = clue.objects.filter(clue_text = c.clue_text)
    unique = None
    if len(c_set) > 1:
        unique = False
    else:
        unique = True
    context = {'entry_list':[x.entry for x in c_set], 'unique':unique, 'num_entries':len(c_set)}
    return render(request, 'answer.html', context)



    #assume the user is right already

# def cross_word(request, clue=None):
#     ind = random.randint(0,)