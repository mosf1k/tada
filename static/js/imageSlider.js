(function($){
	var defaults = {
		classContainer: 'image-slider',
		classPrev: 'prev',
		classNext: 'next'
	};
	var methods = {
		init : function(currentOptions) {
			var options = $.extend({}, defaults, currentOptions);
			return this.each(function(){
				var $container = $(this), data = $container.data('imageSlider'), $images, $next, $prev;
				if (!data){
					render();
					init();
					$container.data('imageSlider', {
						target : $container,
						options : options
					});
				}

				function render(){
					$container.addClass(options.classContainer);
					$prev = $container.find('.' + options.classPrev);
					$next = $container.find('.' + options.classNext);
					$images = $container.children('img');
				}
				function init(){
					$images.hide().filter(':first').show();
					$prev.on('click', function(e){
						e && e.preventDefault && e.preventDefault();
						toggleActive(false);
					});
					$next.on('click', function(e){
						e && e.preventDefault && e.preventDefault();
						toggleActive(true);
					});
					if ($images.length <=1){
						$prev.hide();
						$next.hide();
					}
				}

				function toggleActive(toRight){
					var $current = $images.filter(':visible').hide();
					if (toRight){
						if ($images.filter(':last').is($current)){
							$images.filter(':first').show();
						} else $current.next().show();
					} else{
						if ($images.filter(':first').is($current)){
							$images.filter(':last').show();
						} else $current.prev().show();
					}
					$prev.css('display', $current.is($images.filter(':visible')) ? 'none' : '');
					if ($images.length <=1){
						$prev.hide();
						$next.hide();
					}
				}
			});
		}
	};

	$.fn.imageSlider = function(method){
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Method ' +  method + ' does not exist on jQuery.imageSlider');
		}
	};
})(jQuery);
