%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>SDN DETECTIVE</title>
	
	<link rel="stylesheet" href="main.css" />
</head>
 
<body id="index" class="home">
	<script type="text/javascript">
		function ImgClick(e){
                        var evt = e ? e:window.event;
                        var clickX=0, clickY=0;
                        var pageX=0, pageY=0;
                        if ((evt.clientX || evt.clientY) &&
                            document.body &&
                            document.body.scrollLeft!=null) {
                         clickX = evt.clientX + document.body.scrollLeft;
                         clickY = evt.clientY + document.body.scrollTop;
                        }
                        if ((evt.clientX || evt.clientY) &&
                            document.compatMode=='CSS1Compat' && 
                            document.documentElement && 
                            document.documentElement.scrollLeft!=null) {
                         clickX = evt.clientX + document.documentElement.scrollLeft;
                         clickY = evt.clientY + document.documentElement.scrollTop;
                        }
                        if (evt.pageX || evt.pageY) {
                         clickX = evt.pageX;
                         clickY = evt.pageY;
                        }


			if((clickX>430 && clickX<650) && (clickY>315 && clickY<400)  ){
			  window.location.assign("http://localhost:8080/attacks");
			}
			
			if((clickX>490 && clickX<600) && (clickY>470 && clickY<560)  ){
                          window.location.assign("http://localhost:8080/packets");
                        }

                        if((clickX>327 && clickX<400) && (clickY>647 && clickY<707)  ){
                          window.location.assign("http://localhost:8080/packets-ip/10.0.0.1");
                        } 

                        if((clickX>506 && clickX<576) && (clickY>647 && clickY<707)  ){
                          window.location.assign("http://localhost:8080/packets-ip/10.0.0.2");
                        } 

                        if((clickX>677 && clickX<747) && (clickY>647 && clickY<707)  ){
                          window.location.assign("http://localhost:8080/packets-ip/10.0.0.3");
                        } 		
                        alert (evt.type.toUpperCase() + ' mouse event:'
                         +'\n pageX = ' + clickX
                         +'\n pageY = ' + clickY 
                         +'\n clientX = ' + evt.clientX
                         +'\n clientY = '  + evt.clientY 
                         +'\n screenX = ' + evt.screenX 
                         +'\n screenY = ' + evt.screenY
                        )
                        return false;
		}

	        window.onload = function ()
                {	
			var img = document.getElementById("content");
			img.addEventListener("click", ImgClick, false);
                }

	</script>
 
	<header id="banner" class="body">
	        <h1><img src="security_guard_icon_mod.png" alt="Logo" class="photo" />
                <a href="/">SDN DETECTIVE <strong>IDS system using RYU controller</strong></a></h1> 
		<nav><ul>
			<li class="active"><a href="/">Home</a></li>
			<li ><a href="/packets">Traffic</a></li>
	 
			<li><a href="/attacks">Attacks</a></li>
			<li><a href="/rules">Rules</a></li>
		</ul></nav>
	 
	</header><!-- /#banner -->	
	
	<section id="content" class="body">
		<header>
			<h2 class="entry-title">Topology</h2>
		</header>
		<section>
			<article>
				<div class="entry-content">
		                    <img id="topologyimg" src="topology.png" alt="Logo" class="topo" />                 
				</div><!-- /.entry-content -->
			</article>
		</section>
	 
				
	</section><!-- /#content --> 
</body>
</html>
