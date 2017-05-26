from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.core.exceptions import  PermissionDenied, ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserForm, ContactForm
from .models import Todo, Label


'''class OwnerMixin(object):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj'''


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from mysite.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = 'Thanks!'
        confirm_message = 'Thanks for yur message! we will get right back to you.'
        form = None
    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'contact.html'
    return render(request, template, context)


class LabelIndexView(LoginRequiredMixin, generic.ListView):  # The list view of Labels
    model = Label
    template_name = 'home.html'
    context_object_name = 'labels'

    '''def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)'''
    # here the above get_queryset is not necessary when to display all the items in a object
    # LoginRequiredMixin indicates that login is required to view the LabelIndexView


@login_required
def label_detail(request, name):  # The Details view of Labels
    todo_list = Todo.objects.filter(label__label_title=name)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'label_detail.html', context)


class LabelCreateView(LoginRequiredMixin, CreateView):  # To create a new Or add a new label
    model = Label
    fields = ['label_title']

    '''def get_success_url(self):
        return reverse('todo:label_details')'''
   # To redirect the user when the form is successfully submitted
   # Here commented out because get_absolute_url been used


'''class LabelUpdateView(UpdateView):  # To edit a  label
    model = Label
    fields = ['label_title']'''


'''class LabelDeleteView(DeleteView,name):  # To delete  a label
    model = Label
    success_url = reverse_lazy('todo:label_index')'''


class TodoIndexView(LoginRequiredMixin, generic.ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todos'

    '''def get_queryset(self):
        return Todo.objects.all()'''
    # here the above get_queryset is not necessary when to display all the items in a object


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Todo
    template_name = 'details.html'  # change the url (baad mein karna hai)


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'text', 'label']


class TodoUpdateView(LoginRequiredMixin, UpdateView):  # To Edit the todo
    model = Todo
    fields = ['title', 'text', 'label']


class TodoDeleteView(LoginRequiredMixin, DeleteView):  # To Delete the Todo
    model = Todo
    success_url = reverse_lazy('todo:label_index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('todo:label_index')

        return render(request, self.template_name, {'form': form})

'''def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


# Manually creating Forms
def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        label = request.POST['label']
        todo = Todo(title=title, text=text, label=label)
        todo.save()

        return redirect('LabelIndexView')
    else:
        return render(request, 'add.html')'''