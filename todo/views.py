from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


#* Class Views --------------------------------

class TodoListView(ListView):
    model = Todo
    # context_object_name = 'todos'
    # template_name = 'todo/list.html'
    
class TodoCreateView(CreateView):
    model = Todo    
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    
class TodoUpdateView(UpdateView):
    model = Todo    
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
    template_name = 'todo/update.html'  # the default was 'todo/todo_form.html

class TodoDeleteView(DeleteView):
    model = Todo    
    success_url = reverse_lazy('todo_list')
    
class TodoDetailView(DetailView):
    model = Todo


#* Function Based Views --------------------------------

def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/list.html', context)

def todo_add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "The task added successfully!")
        return redirect('todo_list')
    return render(request, 'todo/add.html', {'form': form})

def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.info(request, 'The task updated successfully')
            return redirect('todo_list')
            
    return render(request, 'todo/update.html', {'form': form, 'todo': todo})

def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.warning(request, 'The task deleted successfully')
    return redirect('todo_list')

