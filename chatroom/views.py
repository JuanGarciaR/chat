from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from chatroom.models import Chats, User

@login_required
def home(request):
	users = User.objects.all().exclude(username=request.user.username).order_by('id')
	username = request.user.username
	userid = request.user.id
	div_ids = []
	for user in users:
		if userid < user.id:
			channel = '%s-%s' % (username, user.username)
		else:
			channel = '%s-%s' % (user.username, username)

		comments = Chats.objects.filter(channel=channel).order_by('id')
		div_ids.append({'id': channel, 'name': user.username, 'comments': comments})

	return render_to_response('index.jade', {'div_ids' : div_ids, 'users': users})