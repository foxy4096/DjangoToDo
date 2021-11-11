from django.views.generic import *
from django.shortcuts import redirect

from .models import ToDo



class ToDoListView(ListView):
    model = ToDo
    context_object_name = "todos"



class ToDoCreateView(CreateView):
    model = ToDo
    success_url = '/'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class ToDoUpdateView(UpdateView):
    model = ToDo
    success_url = '/'
    fields = '__all__'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class ToDoDeleteView(DeleteView):
    model = ToDo
    success_url = '/'

    
    def get_context_data(self, **kwargs):
        context = super(ToDoDeleteView, self).get_context_data(**kwargs)
        context['todo'] = ToDo.objects.get(pk=self.object.pk)
        return context