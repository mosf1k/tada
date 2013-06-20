(function($){
	var defaults = {
		classContainer: 'liker',
		classLikeIcon: 'icon-thumbs-up',
		classDisLikeIcon: 'icon-thumbs-down',
		classCurrent: 'current',
		classLoading: 'loading',
		classLoadingIcon: 'icon-spin5',
		likesDatapoint: '/like/',
		dislikesDatapoint: '/dislike/'
	};
	var methods = {
		init : function(currentOptions) {
			var options = $.extend({}, defaults, currentOptions);
			return this.each(function(){
				var $container = $(this), data = $container.data('liker'), itemId = -1, currentState = null, type = null,
					likesCount = 0, dislikesCount = 0;
				if (!data){
					itemId = $container.attr('item-id');
					currentState = $container.attr('state');
					type = $container.attr('type');
					likesCount = parseInt($container.attr('likes'));
					dislikesCount = parseInt($container.attr('dislikes'));
					render();
					init();
					$container.data('liker', {
						target : $container,
						options : options
					});
				}

				function render(){
					var html =
						'<a class="like-link" href="javascript:void(0);">' +
							'<i class="' + options.classLikeIcon +  '"></i>' +
							'<span>' +(likesCount ? likesCount : '') + '</span>' +
						'</a> / ' +
						'<a class="dislike-link" href="javascript:void(0);">' +
							'<i class="' + options.classDisLikeIcon +  '"></i>' +
							'<span>' +(dislikesCount ? dislikesCount : '') + '</span>' +
						'</a><i class="animate-spin ' + options.classLoadingIcon +  '"></i>';
					$container.addClass(options.classContainer).html(html);
				}
				function init(){
					setState();
					$container.find('.like-link').on('click.liker', function(e){
						e && e.preventDefault && e.preventDefault();
						if ($container.hasClass(options.classLoading)) return;
						updateState('like');
					});
					$container.find('.dislike-link').on('click.liker', function(e){
						e && e.preventDefault && e.preventDefault();
						if ($container.hasClass(options.classLoading)) return;
						updateState('dislike');
					});
				}
				function setState(){
					if (currentState){
						$container.find('.' + options.classCurrent).removeClass(options.classCurrent);
						if (currentState == 'like'){
							$container.find('.like-link').addClass(options.classCurrent);
						}
						if (currentState == 'dislike'){
							$container.find('.dislike-link').addClass(options.classCurrent);
						}
						$container.find('.like-link').find('span').html(likesCount ? likesCount : '');
						$container.find('.dislike-link').find('span').html(dislikesCount ? dislikesCount : '');
					}
				}
				function updateState(newState){
					if (newState && itemId && type && newState != currentState){
						$container.addClass(options.classLoading);
						$.when($.ajax({
							type: 'post',
							url: newState == 'like' ? options.likesDatapoint : options.dislikesDatapoint,
							data: {
								type: type,
								item_id: itemId
							},
							dataType: 'json'
						}).promise()).done(function(result, status, xhr){
							$container.removeClass(options.classLoading);
							if (result && result.success){
								currentState = newState;
								likesCount = result.likes;
								dislikesCount = result.dislikes;
								setState();
							}
						}).fail(function(){
							$container.removeClass(options.classLoading);
						});
					}
				}
			});
		}
	};

	$.fn.liker = function(method){
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Method ' +  method + ' does not exist on jQuery.liker');
		}
	};
})(jQuery);
