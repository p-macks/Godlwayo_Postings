from django.shortcuts import render,redirect
from . models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'base/index.html')

class PostList(LoginRequiredMixin,ListView):
    model=Post
    context_object_name='posts'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['posts']=context['posts'].filter(user=self.request.user)

        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['posts']= context['posts'].filter(
                title_icontains=search_input
            )
            context['search_input']=search_input
        return context

class PostDetail(LoginRequiredMixin,DeleteView):
    model=Post
    context_object_name='post'

class PostCreate(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','description','picture']
    success_url=reverse_lazy('index')  

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(PostCreate,self).form_valid(form)  

class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Post
    fields=['title','description','picture']
    success_url=reverse_lazy('index')      

class PostDelete(LoginRequiredMixin,DeleteView):
    model=Post
    context_object_name='post'
    success_url=reverse_lazy('post_list')  

class RegisterView(FormView):
    template_name = 'base/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)  

class MyLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    
    def get_success_url(self):
        return reverse_lazy('index') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
   