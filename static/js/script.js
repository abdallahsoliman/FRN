$(document).ready(function() {

/*************************  One Page Navigation  *****************************/
	$('.nav').onePageNav({
		filter: ':not(.external)',
		scrollThreshold: 0.25,
		scrollOffset: 90,
	});
         
	$(window).scroll(function(){
		if ($(this).scrollTop() > 100) {
			$('.scrollup').fadeIn();
		} else {
			$('.scrollup').fadeOut();
		}
	}); 
 


/******************************  ScrollUp  *********************************/
	 $('.scrollup').click(function(){
		 $("html, body").animate({ scrollTop: 0 }, 600);
		 return false;
	 });



/*************************  Slider Revolution  *****************************/
if($('.fullwidthbanner').length) {

	$('.fullwidthbanner').revolution({
		hideThumbs:1,
		startwidth:1140,
		startheight:370,
		shadow:0,
		touchenabled:"on",
		navigationType: "bullet",
		navigationStyle: "round-old",
		hideAllCaptionAtLimit: 350,
	});
}



/*******************************  gMaps  ***********************************/

	if ($('#map').length) {
		var map;
		map = new GMaps({
			div: '#map',
			lat: 41.8902624,
			lng: 12.4923096
		});
		map.addMarker({
			lat: 41.8902624,
			lng: 12.4923096,
			title: 'Contanct',
			infoWindow: {
				content: '15rd Avenue, New York,<br /> 156408, US<br /> <br /> Email: info@company.com <br /> Web: company.com'
			}
		});
	}




/******************************  jPlayer  **********************************/
// http://www.jplayer.org/ 

    $("#jquery_jplayer_1").jPlayer({
        ready: function(event) {
            $(this).jPlayer("setMedia", {
				m4a: "http://www.jplayer.org/video/m4v/Big_Buck_Bunny_Trailer.m4v",
				oga: "http://www.jplayer.org/video/ogv/Big_Buck_Bunny_Trailer.ogv",
				poster: "img/player/player1.jpg"
			});
        },
        swfPath: "../jPlayer",
        supplied: "oga, m4a",
        size: {
			width: $('.player-container').width()+"px",
			height: $('.player-container').height()+"px",
			cssClass: "jp-video-360p"
		},
		smoothPlayBar: true,
		keyEnabled: true
    });



/*****************************  Playlist  **********************************/
	if( $('.sermons .playlist li a').length ) {
		$('.sermons .playlist li a').click(function(e){
			e.preventDefault();

			$('#jquery_jplayer_1').jPlayer('stop');
			
			$('.sermons .playlist li a').removeClass('active');
			$(this).addClass('active');

			$('.sermons .playlist li a i.icon-pause').removeClass('icon-pause').addClass('icon-play');
			$(this).children('i').removeClass('icon-play').addClass('icon-pause');

			$('.jp-title').html('<strong>' + $(this).data('title') + '</strong> ' + $(this).data('by'))

			$('#jquery_jplayer_1').jPlayer('setMedia', {
				m4a: $(this).data('url'),
				ogv: $(this).data('url'),
				webmv: $(this).data('url'),
				poster: $(this).data('poster')
			}) 
		});
    }



/***************************  prettyPhoto  ********************************/

	$('a[data-rel]').each(function() {
		$(this).attr('rel', $(this).data('rel'));
	});

    $("a[rel^='prettyPhoto']").prettyPhoto();



}); //end document ready