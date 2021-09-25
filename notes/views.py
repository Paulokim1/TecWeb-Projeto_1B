from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        tag = request.POST.get('tag')
        content = request.POST.get('detalhes')
        Tag.objects.get_or_create(tag = tag)
        note = Note(title = title, tag = Tag.objects.get(tag = tag), content = content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('delete')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        new_title = request.POST.get('titulo')
        new_content = request.POST.get('detalhes')
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        note.title = new_title
        note.content = new_content
        note.save()
        return redirect('update')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def viewTagList(request):
    if request.method == 'GET':
        all_tags = Tag.objects.all()
        return render(request, 'notes/tag_preview.html', {'tags': all_tags})

def viewTags(request):
    if request.method == 'GET':
        tag_id = request.GET.get('id')
        tag = Tag.objects.get(id=tag_id)
        all_notes = Note.objects.all().filter(tag = tag)
        return render(request, 'notes/tags.html', {'notes': all_notes})




