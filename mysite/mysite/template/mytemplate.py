from django.template import Template, Context
from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
        fp = open('/home/work/djangocode/mysite/mysite/template/mytemplate.py')
        t = Template(fp.read())
        fp.close()
        html = t.render(Context({'current_date': now}))
        return HttpResponse(html)