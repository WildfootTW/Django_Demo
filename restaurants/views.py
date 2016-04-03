#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
#自動載入templates(failed)
#from django.template.loader import get_template
from django.utils import timezone
from django.shortcuts import render_to_response
from django import template
from restaurants.models import Restaurant, Food, Comment
from django.template import RequestContext
	
def menu(request):
#    food1 = {
#            'name' : '番茄炒蛋','price' : 60,'comment' : '好吃','is_spicy' : False}
#    food2 = {
#            'name' : '蒜泥白肉','price' : 100,'comment' : '人氣','is_spicy' : False}
#    foods = [food1, food2]
    path = request.path
    restaurants = Restaurant.objects.all()
    return render_to_response('menu.html', locals())

def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', locals())

def foods(request):
    if 'id' in request.GET and request.GET['id'] != '':
        r = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('foods.html', locals())
    else:
        return HttpResponseRedirect("/restaurants_list/")
#    return HttpResponse(r)

def comment (request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
        )
    return render_to_response('comments.html', RequestContext(request, locals()))
