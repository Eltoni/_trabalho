from django.http import HttpResponseRedirect,Http404
from django.contrib.auth import logout
from django.shortcuts import render,reverse
from django.contrib.auth.decorators import login_required
from .models import*
from .forms import*

# Create your views here.
def index(request):
    """ Página Inicial do Diário """
    return render(request,'app/index.html')
@login_required
def topics(request):
    """ Mostra todos os Tópicos """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context ={'topics':topics}
    return render (request, 'app/topics.html', context)
@login_required
def topic(request, topic_id):
    """Mostra um Único Assunto e todas as Entradas"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    """topic.entry_set.order_by("-date_added") pega do topic(Para identificar
    qual entrada está relacionada com o Tópico )"""
    entries = topic.entry_set.order_by("-date_added")
    context = {'topic': topic,'entries': entries}
    return render(request,'app/topic.html',context)
@login_required
def new_topic(request):
    """ Adiciona um novo Assunto """
    if request.method != 'POST':
        #Nenhum dado Submetido; Cria um Formulário em Branco
        form = TopicForm()
    else:
        #Dados Submetido; Processa os Dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #form.save()
            return HttpResponseRedirect(reverse('app:topics'))
    context = {'form': form}
    return render(request,'app/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    """ Adicona um Assunto """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse ('app:topic', args = [topic_id]))

    context = {'topic': topic , 'form': form}
    return render (request,'app/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):
    """ Edita uma Entrada Existente """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance = entry)

    else:
        #Dados Post processados
        form = EntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse ('app:topic', args = [topic.id]))
    context = {'topic': topic ,'entry': entry, 'form': form}
    return render (request,'app/edit_entry.html',context)
