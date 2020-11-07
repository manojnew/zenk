from django.shortcuts import render
from django.http import HttpResponse
def home(request):
     return HttpResponse("<li><ul>employee 1 <ul><ul> employee 2 <ul><ul> employee 3<ul><li>")
