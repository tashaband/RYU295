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
		<h1><img src="security_guard_icon.png" alt="Logo" class="photo" />
		<a href="#">SDN DETECTIVE <strong>IDS system using RYU controller</strong></a></h1>
	 
		<nav><ul>
			<li ><a href="#">Home</a></li>
			<li class="active"><a href="/">Traffic</a></li>
	 
			<li><a href="/attacks">Attacks</a></li>
			<li><a href="/rules">Rules</a></li>
			<li><a href="#">Visualization</a></li>
		</ul></nav>
	 
	</header><!-- /#banner -->	
	
	<section id="content" class="body">
		<header>
			<h2 class="entry-title">The Packets received by IDS-controller are as follows:</h2>
 
		</header>
		<section>
			<table border="1" id= "attacks-list">
				  <tr>
				    <th>Protocol</th>
				    <th>Source MAC Address</th>
				    <th>Source Ip Address</th>
				    <th>Source Port</th>
				    <th>Destination MAC Address</th>
				    <th>Destination IP Address</th>
				    <th>Destination Port</th>
				    <th>Options</th>
				  </tr>
				%for row in rows:
				  <tr>
				    <td>{{row[1]}}</td>
				    <td>{{row[2]}}</td>
				    <td>{{row[4]}}</td>
				    <td>{{row[6]}}</td>
				    <td>{{row[3]}}</td>
				    <td>{{row[5]}}</td>
				    <td>{{row[7]}}</td>
				    <td>{{row[8]}}</td>
				  %end
				  </tr>
				%end
			</table>
		</section>
		<footer class="post-info">

		</footer><!-- /.post-info -->
	 
				
	</section><!-- /#content --> 
</body>
</html>
