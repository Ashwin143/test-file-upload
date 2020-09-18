# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
# Create your views here.
# class Another(View):
    
#     books = Book.objects.all()
#     output=''

#     # for book in books:
#     #     output+=f"we have{book.title} book in DB<br>"

#     def get(self,request):
#         return HttpResponse('class First message')

# def first(request):
#     return HttpResponse('First message')        