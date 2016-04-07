#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
#自動載入templates(failed)
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm

def here(request):
	return HttpResponse('Mother fucker?媽的法克？')

#參數為字串,記得轉型
def math(request, a, b):
	#s = int(a) + int(b)
	#return HttpResponse(str(s))
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	#這是把view logic(Template)混到business logic(views.py負責控制器)的情況
#	html = """
#		<html>
#			sum={s}<br>
#			dif={d}<br>
#			pro={p}<br>
#			quo={q}
#		</html>
#	""".format(s=s,d=d,p=p,q=q)
#	return HttpResponse(html)
	
	#使用template
#	t = template.Template('''
#<html>
#	sum = {{s}}<br>
#	dif = {{d}}<br>
#	pro = {{p}}<br>
#	quo = {{q}}
#</html>''')
#	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
#	return HttpResponse(t.render(c))

	#template分離
		#手動載入templates
#	with open('templates/math.html','r') as reader:
#		t = template.Template(reader.read())
#	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
#	return HttpResponse(t.render(c))

		#自動載入(failed)	
#	t = get_template('math.html')
#	c = template.Context({'s':s, 'd':d, 'p':p, 'q':q})
#	return HttpResponse(t.render(c))

		#get_template + Context+render + HttpResponse = render_to_response 
#	return render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q})

                #使用locals函數 傳送區域變數
        #local_dic = locals()
        #print local_dic['s']        #印出s的內容(字串)
	return render_to_response('math.html', locals())

def meta(request):
	values = request.META.items()
	#values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v))
	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~'+request.GET['user_name'])
    else:
        return render_to_response('welcome.html',locals())

def set_c(request):
    response = HttpResponse('Set your lucky_number as 7')
    response.set_cookie('lucky_number',7)
    return response

def get_c(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.')

def use_session(request):
    request.session['lucky_number'] = 11
    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']
        response = HttpResponse(lucky_number)
    del request.session['lucky_number']
    return response

def session_S(request):
#   request.session['sid'] = '77'
#   s_info = request.session['sid']
    
    request.session['sid'] = '77'        #需要在其他頁面先執行過
    request.session['sidd'] = '888'
    sid = request.session.session_key
    s = Session.objects.get(pk=sid)      #沒先執行過request.session[] = '' 會有錯誤
    s_info = 'Session ID:' + sid + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)

def login(request):

    if request.user.is_authenticated():         #HttpRquest物件中包含一個user屬性
        #如已登入 HttpRequest.user = user物件
        #如未登入 HttpRequest.user = AnonymousUser物件
        #is_authenticated 是否認証過用戶
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')     #如果POST中沒有username 填空值
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)
            #若正確 回傳具名用戶的user物件
            #若錯誤 回傳None
    if user is not None and user.is_active:         #若非None該用戶可登入/is_active是否凍結
        auth.login(request, user)               #保持登入狀態
        return HttpResponseRedirect('/index/')
            #登入狀態 = user屬性 是 user物件
            #登出狀態 = user屬性 是 anonymoususer物件
    else:
        return render_to_response('login.html', RequestContext(request, locals()))


def index(request):
    return render_to_response('index.html', RequestContext(request, locals()))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def register(request):
    if request.method == 'post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login')
    else:       #POST沒有資料
        form = UserCreationForm()
    return render_to_response('register.html', RequestContext(request, locals()))
