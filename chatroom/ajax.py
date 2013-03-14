from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from chatroom.models import Chats
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@dajaxice_register
def chat(request, channel, text):
	Chats.objects.create(user_from=request.user, channel=channel, message=text)
	return simplejson.dumps({'status': '200', 'channel': channel, 'text': request.user.username + ': ' + text})