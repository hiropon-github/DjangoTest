from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .forms import TodoForm

# 一覧表示機能
class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Todo
    paginate_by = 5

# 詳細表示機能
class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Todo

# 作成機能
class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# 編集機能
class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super().dispatch(request, *args, **kwargs)

# 削除機能
class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')

    def dispatch(self, request, *args, **kwargs):
        # ownership validation
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to delete.')
        return super().dispatch(request, *args, **kwargs)