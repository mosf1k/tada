$(document).ready(function(){
	var $commentsWrapper = $('.comments'), $form = $commentsWrapper.find('form'), $commentText = $form.find('.comment-text'),
		$validationMessage = $form.find('.validation-error'), $loading = $commentsWrapper.find('.loading');
	$validationMessage.hide();
	$form.on('submit', function(e){
		e && e.preventDefault && e.preventDefault();
		var item_id = $form.attr('item_id'), type = $form.attr('type'), text = $.trim($commentText.val());
		if(!text){
			$validationMessage.filter('[rel="text"]').show();
			return;
		}
		$loading.loading({})
		$.when($.ajax({
			url: '/comments/add/',
			type: 'post',
			dataType: 'html',
			data:{
				item_id: item_id,
				type: type,
				text: text
			}
		}).promise()).done(function(result, status, xhr){
			$loading.loading('destroy');
			$('.comments-list').html(result);
			$validationMessage.hide();
			$commentText.val('');
		}).fail(function(){
			$loading.loading('destroy');
			$validationMessage.filter('[rel="server"]').show();
		});
	});
	$commentText.on('change', function(e){
		if ($validationMessage.filter(':visible') && $.trim($commentText.val()).length > 0){
			$validationMessage.hide();
		}
	});
});
