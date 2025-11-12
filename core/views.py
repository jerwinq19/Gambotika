from django.urls import reverse_lazy
from django.views import generic, View
from .models import Nft
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User

class HomeView(generic.TemplateView):
    template_name = 'app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nfts"] = Nft.objects.all()
        print(self.request.user)
        return context

class RegisterView(generic.FormView):
    template_name = 'app/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        data = form.cleaned_data
        username = data.get('username') 
        password = data.get('password') 
        
        if form.is_valid():
            User.objects.create_user(
                username=username,
                password=password
            )
        
        return super().form_valid(form)
    
    
class ProfileView(generic.TemplateView):
    template_name = 'app/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
