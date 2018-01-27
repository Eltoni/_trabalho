from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    path('',views.index, name ='index'),
    path('topics/',views.topics, name ='topics'),
    #Adciona um novo Topico
    path(r'topics/new_topic/',views.new_topic, name = 'new_topic'),
    #Adciona um nova Entrada
    path(r'topics/new_entry/<int:topic_id>',views.new_entry, name = 'new_entry'),
    #Ver o topico individualmente
    path(r'topics/<int:topic_id>',views.topic, name = 'topic'),

    #Editando um nova Entrada
    path(r'topics/edit_entry/<int:entry_id>',views.edit_entry, name = 'edit_entry'),
]
