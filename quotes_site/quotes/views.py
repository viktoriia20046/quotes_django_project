from django.shortcuts import render, redirect
from .models import Author, Quote
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm
from django.shortcuts import render

def home(request):
    return render(request, 'quotes/home.html')

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})