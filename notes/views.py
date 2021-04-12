from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from .filters import NotesFilter

def home(request):
    all_notes = Note.objects.all()

    return render(request, 'notes/base.html', {'notes': all_notes})


def createNote(request): 
    form = NoteForm()
    # form_class = NoteForm
    if request.method == 'POST':
        form = NoteForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('e valido')
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'notes/index.html', context)


def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}

    return render(request, 'notes/index.html', context)

def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/')
    context = {'item':note}
    return render(request, 'notes/delete.html', context)


def tagList(request):
    all_notes = Note.objects.all()

    myFilter = NotesFilter(request.GET, queryset=all_notes)
    all_notes = myFilter.qs

    form = NoteForm(request.POST)


    context = {'tag_notes':all_notes,'myFilter':myFilter, 'form':form}

    return render(request, 'notes/taglist.html', context)


