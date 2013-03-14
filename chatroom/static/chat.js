var Chat = function(){

	that = this;
	var entry = $('#entry');


	this.activateChat = function(data){
		var div_active = $('#chats div[id*="' + data.currentTarget.innerHTML + '"]');
		div_active.attr('data-active', 'true');
		
		$('#chats div').not(div_active).each(function(){
			$(this).attr('data-active', 'false');
		});
		entry.attr('disabled', false).focus();
	}

	this.showMessage = function(message){
		$('#' + message.channel + ' ul').append('<li>' + message.text + '</li>');
	}


	this.pubMessage = function(data){
		if(data.status == '200')
			window.client.publish('/message/'+data.channel, data);
	}

	$('#users').on('click', 'a', this.activateChat);

	entry.on('keypress', function(event){
		if(event.keyCode != 13) return;
		if(entry.val() == '') return;

		var chat_id = $('#chats div[data-active="true"]').attr('id');

		Dajaxice.chatroom.chat(that.pubMessage, {
			channel: chat_id,
			text: entry.val()
		});

		entry.val('');
	});
}