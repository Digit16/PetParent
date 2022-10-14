from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from rest_framework import viewsets, views
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer, HelloSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HelloView(viewsets.ViewSet):
    #
    # def list(self, request):
    #     return Response(5)

    def retrieve(self, request, pk=None):
        return Response(6)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')


def current_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        return HttpResponse(username)
    else:
        return HttpResponse("No user!")
