from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import activate
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class Home(View):

    def get(self, request):
        return render(request, 'slideshow/home.html')


class ChangeLanguage(View):

    def get(self, request):
        activate(request.GET.get('lang'))
        return redirect(request.GET.get('next'))


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect(request.GET.get('next'))

# class Logout(LogoutView):
#     next_page = reverse_lazy(request.GET.get('next'))
