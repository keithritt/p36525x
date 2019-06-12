from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm

from . models import Exercise, Set

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
import sys
from pprint import pprint

#from django import forms
from django.forms.widgets import Select


def index(request):

  if request.user.is_authenticated:
    #username = request.user.username
    return redirect('dashboard')


  context = {
  }

  return render(request, 'web/homepage.html', context)

@login_required
def dashboard(request):
  queryset = Exercise.objects.all().order_by('name')
  exercises = []

  for row in queryset:
    tmp_tpl = (row.id, row.name)
    exercises.append(tmp_tpl)

  select = Select(choices=exercises, attrs={'id':'exercise_id'})
  exercise_select = select.render('exercise', 1) # 1 = push ups

  rows = Set.objects.filter(user = request.user).order_by('ts')

  rep_counts = {}

  reps_remaining = 36525;

  for row in rows:
    pprint(row)
    pprint(row.reps)
    pprint(row.exercise.name)
    if not row.exercise.name in rep_counts:
      rep_counts[row.exercise.name] = row.reps
    else:
      rep_counts[row.exercise.name] += row.reps

    reps_remaining -= row.reps

  pprint(rep_counts)






  context = {
    'exercise_select' : exercise_select,
    'rep_counts': rep_counts,
    'reps_remaining': reps_remaining
  }

  return render(request, 'web/dashboard.html', context)

@login_required
def ajax(request, action):
  if action == 'save_set':
    #exchange = Exchange.objects.get(pk=request.POST.get('exchange_id'))
    set = Set()
    set.user = request.user
    set.exercise_id = request.POST['exercise_id']
    set.reps = request.POST['reps']

    set.save()
    return HttpResponse('Set saved.')

def register(request):
  if request.method == 'POST':



    form = MyUserCreationForm(request.POST)

    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')

      user = authenticate(username=username, password=password)
      login(request, user)

      return redirect('dashboard')
  else:

    form = MyUserCreationForm()

  context = {
    'form' : form
  }

  return render(request, 'registration/register.html', context)