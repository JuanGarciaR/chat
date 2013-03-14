function main(){

	window.client = new Faye.Client('http://localhost:4000/faye');

	var chat = new Chat();

	$('#chats div').each(function(){
		window.client.subscribe('/message/'+this.id, function(message){
			chat.showMessage(message);
		});
	});
}

$(document).on('ready', main);