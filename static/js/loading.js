(function($){
	var defaults = {
		classContainer: 'loading-indicator',
		classLoadingIcon: 'icon-spin5'
	};
	var methods = {
		init: function(currentOptions) {
			var options = $.extend({}, defaults, currentOptions);
			return this.each(function(){
				var $container = $(this), data = $container.data('loading');
				if (!data){
					var html = '<div><i class="animate-spin ' + options.classLoadingIcon +  '"></i></div>';
					$container.addClass(options.classContainer).html(html);
					$container.data('loading', {
						target : $container,
						options : options
					});
				}
			});
		},
		destroy: function(){
			return $(this).each(function(){
				var $this = $(this), data = $this.data('loading');
				if (data){
					$this.empty().removeClass(data.options.classContainer).removeData('loading');
				}
			});
		}
	};

	$.fn.loading = function(method){
		if (methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if (typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Method ' +  method + ' does not exist on jQuery.loading');
		}
	};
})(jQuery);
