from django.conf.urls import url
from django.views.generic import RedirectView
from . import views
from . import views as core_views


app_name = 'todo'

urlpatterns = [

    # /label/ ---List all the labels
    url(r'^label/$', views.LabelIndexView.as_view(), name='label_index'),

    #url(r'^home/$', views.LabelIndexView.as_view(), name='label_index'),

    url(r'^accounts/signup/$', views.UserFormView.as_view(), name='signup'),


    # /label/<label name> --- List all the ToDo's in a particular label
    url(r'^label/(?P<name>\w{0,50})/$', views.label_detail, name='label_details'),

    # /add_label/ --- To add a new label
    url(r'^add_label/$', views.LabelCreateView.as_view(), name='add_label'),

    # /label/<label name>/delete
    #url(r'^label/(?P<pk>\w{0,50})/delete/$', views.LabelDeleteView.as_view(), name='delete_label'),

    # /todo/ --- List all the ToDo's
    url(r'^todo/$', views.TodoIndexView.as_view(), name='todo_index'),

    # /details/29/ --- Details page of a particular todo
    url(r'^details/(?P<pk>\w{0,50})/$', views.TodoDetailView.as_view(), name='todo_details'),

    # /add_todo/ --- To add a new Todo
    url(r'^add_todo/$', views.TodoCreateView.as_view(), name='add_todo'),

    # /todo/29/ --- to edit the todo
    url(r'^update_todo/(?P<pk>[0-9]+)/$', views.TodoUpdateView.as_view(), name='update_todo'),

    # /todo/29/delete --- to edit the todo
    url(r'^delete_todo/(?P<pk>[0-9]+)/$', views.TodoDeleteView.as_view(), name='delete_todo'),

    #/contact
    url(r'^contact/$', views.contact, name='contact'),




]

