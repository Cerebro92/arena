from django.template import Template, Context
from django.http import HttpResponse
from models import Author, Article
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, render 
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
	fp=open('demo/templates/homepage.html')
	t=Template(fp.read())
	fp.close()
	html=t.render(Context())
	return HttpResponse(html)


def login(request):
	fp=open('demo/templates/login.html')
	t=Template(fp.read())
	fp.close()
	html=t.render(Context())
	return HttpResponse(html)


def login_view(request):
	a = Author.objects.get(email=request.GET['email'])
	if a.password == request.GET['password']:
		request.session['author_id'] = a.id
		request.session['author_name'] = a.name
		request.session['author_email'] = a.email
		return render(request,'../../demo/templates/nsession.html/',{"author":a})
	else:
		return render(request,'../../demo/templates/incorrect_login.html/')


def signup(request):
	fp = open('demo/templates/signup.html')
	t=Template(fp.read())
	fp.close()
	html=t.render(Context())
	return HttpResponse(html)


def new_session(request):
	q=Author(name=request.GET['name'],email=request.GET['email'],password=request.GET['password'])
	q.save()
	request.session['author_id']=q.id
	request.session['author_name']=q.name
	request.session['author_email']=q.email
	return render(request,'../../demo/templates/nsession.html',{"author":q})


def logout(request):
	try:
		del request.session['author_id']
		del request.session['author_name']
		del request.session['author_email']
	except KeyError:
		pass
	return render(request,'../../demo/templates/logout.html/')


def add_view(request):
	q = Author(id=request.session.get('author_id'), name=request.session.get('author_name'), email=request.session.get('author_email'))
	return render(request,'../../demo/templates/user1.html',{"author":q})


def new_article(request):
	i=request.session.get('author_id')
	n=request.session.get('author_name')
	e=request.session.get('author_email')
	fp = open('demo/templates/add_article.html')
	t = Template(fp.read())
	fp.close()
	html=t.render(Context({"author_id":i,"author_name":n,"author_email":e}))
	return HttpResponse(html)


def view_article(request):
	aid = request.session.get('author_id')
	a_name=request.session.get('author_name')
	if aid == None:
		article = Article.objects.all()
		return render(request,'../../demo/templates/view_title.html',{"article_list":article})
	else:
		all_article = Article.objects.all()
		article = Article.objects.filter(author_name=a_name)
		return render(request,'../../demo/templates/view_title_aut.html',{'author_name':a_name,'article_list':article})
				
'''def view_article_content(request):
	aid = request.session.get('author_id')
	a_name=request.session.get('author_name')
	if aid == None:
		article = Article.objects.all()
		return render(request,'../../demo/templates/view_article.html',{"article_list":article})
	else:
		all_article = Article.objects.all()
		article = Article.objects.filter(author_name=a_name)
		return render(request,'../../demo/templates/view_article_aut.html',{'author_name':a_name,'article_list':article})
'''


def success(request):
	name=request.session.get('author_name')
	at = Article(author_name=name, article_title=request.GET['title'], article_content=request.GET['content'])
	at.save()
	fp = open('demo/templates/success.html')
	t = Template(fp.read)
	fp.close()
	html = t.render(Context({"title":at.article_title}))
	return HttpResponse(html)
