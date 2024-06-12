from django.shortcuts import render

# Create your views here.
# permapp/views.py
from django.shortcuts import render
from .forms import WordForm

def permute(word):
    if len(word) <= 1:
        return [word]
    perms = []
    for i in range(len(word)):
        current = word[i]
        remaining = word[:i] + word[i+1:]
        for p in permute(remaining):
            perms.append(current + p)
    return perms

def home(request):
    form = WordForm()
    result = None
    word = ''
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            result = permute(word)
    return render(request, 'app3/home.html', {'form': form, 'word': word, 'result': result})
