%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>SDN DETECTIVE</title>
	
	<link rel="stylesheet" href="main.css" />
</head>
 
<body id="index" class="home">
 
	<header id="banner" class="body">
		<h1><a href="#">SDN DETECTIVE <strong>IDS system using RYU controller</strong></a></h1>
	 
		<nav><ul>
			<li ><a href="#">Home</a></li>
			<li class="active"><a href="/">Traffic</a></li>
	 
			<li><a href="/attacks">Attacks</a></li>
			<li><a href="#">Visulaization</a></li>
		</ul></nav>
	 
	</header><!-- /#banner -->	
	
	<section id="content" class="body">
		<header>
			<h2 class="entry-title">The IDS rules to catch attacks</h2>
		</header>
		<section>
			<article>
				<div class="entry-content">
					%for row in rows:
						<p>{{row}}</p>
					%end
				</div><!-- /.entry-content -->
			</article>
		</section>
		<footer class="post-info">

		</footer><!-- /.post-info -->
	 
				
	</section><!-- /#content --> 
</body>
</html>
