#-*- coding: utf-8 -*-
from django.http import HttpResponse
#自動載入templates(failed)
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from django import template
from django.contrib.sessions.models import Session

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

def session_S(request):
#   request.session['sid'] = '77'
#   s_info = request.session['sid']
    
    request.session['sid'] = '77'
    request.session['sidd'] = '888'
    sid = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:' + sid + '<br>Expire_date:' + str(s.expire_date) + '<br>Data:' + str(s.get_decoded())
    return HttpResponse(s_info)
