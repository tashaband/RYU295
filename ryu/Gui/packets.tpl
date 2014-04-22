%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<!DOCTYPE html>
<html>
<head>
<style>
#attacks-list
{
font-family:"Trebuchet MS", Arial, Helvetica, sans-serif;
width:100%;
border-collapse:collapse;
}

#attacks-list td, #attacks-list th 
{
font-size:1em;
border:1px solid #98bf21;
padding:3px 7px 2px 7px;
}

#attacks-list th 
{
font-size:1.1em;
text-align:left;
padding-top:5px;
padding-bottom:4px;
background-color:#A7C942;
color:#ffffff;
}

#attacks-list tr.alt td 
{
color:#000000;
background-color:#EAF2D3;
}
</style>
</head>

<body>
<p>The Packets received by IDS-controller are as follows:</p>
<table border="1" id= "attacks-list">
  <tr>
    <th>Protocol</th>
    <th>Source MAC Address</th>
    <th>Source IP Address</th>
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
    <td>{{row[7]}}</td>
    <td>{{row[3]}}</td>
    <td>{{row[5]}}</td>
    <td>{{row[6]}}</td>
    <td>{{row[8]}}</td>
  %end
  </tr>
%end
</table>
</body>
</html>

%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>SDN DETECTIVE</title>
	
	<style>
		
		#global
		
		/***** Global *****/
		/* Body */
			body {
				background: #F5F4EF;
				color: #000305;
				font-size: 87.5%; /* Base font size: 14px */
				font-family: 'Trebuchet MS', Trebuchet, 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
				line-height: 1.429;
				margin: 0;
				padding: 0;
				text-align: left;
			}
		 
		 
				/*
			Header
		*****************/
		#banner {
			margin: 0 auto;
			padding: 2.5em 0 0 0;
		}
		 
		/* Banner */
		#banner h1 {
			font-size: 3em; 
			line-height: .6;
			margin-left: 30px;
		}
		#banner h1 a:link, #banner h1 a:visited {
			color: #000305;
			display: block;
			font-weight: bold;
			margin: 0 0 .6em .2em;
			text-decoration: none;
			width: 500px;
		}
		#banner h1 a:hover, #banner h1 a:active {
			background: none;
			color: #C74350;
			text-shadow: none;
		}
	 
		#banner h1 strong {font-size: 0.36em; font-weight: normal;}
		
			/* Main Nav */
		#banner nav {
			background: #000305;
			font-size: 1.143em;
			height: 40px;
			line-height: 30px;
			padding: 0;
			text-align: center;
			width: 800px;
			margin-left: 40px;
			
			border-radius: 5px;
			-moz-border-radius: 5px;
			-webkit-border-radius: 5px;
		}
		
		#banner nav ul {list-style: none; margin: 0 auto; width: 800px;}
		#banner nav li {float: left; display: inline; margin: 0;}
		
		#banner nav a:link, #banner nav a:visited {
			color: #fff;
			display: inline-block;
			height: 30px;
			padding: 5px 1.5em;
			text-decoration: none;
		}
		#banner nav a:hover, #banner nav a:active,
		#banner nav .active a:link, #banner nav .active a:visited {
			background: #C74451;
			color: #fff;
			text-shadow: none !important;
		}
		
		#banner nav li:first-child a {
			border-top-left-radius: 5px;
			-moz-border-radius-topleft: 5px;
			-webkit-border-top-left-radius: 5px;
			
			border-bottom-left-radius: 5px;
			-moz-border-radius-bottomleft: 5px;
			-webkit-border-bottom-left-radius: 5px;
		}
		
		/*
		Body
		*****************/
		#content {
			background: #fff;
			margin-bottom: 2em;
			overflow: hidden;
			padding: 20px 20px;
			width: 760px;
		    margin-left: 20px;
			border-radius: 10px;
			-moz-border-radius: 10px;
			-webkit-border-radius: 10px;
		}
				
		#attacks-list td, #attacks-list th 
		{
		font-size:1em;
		border:1px solid #98bf21;
		padding:3px 7px 2px 7px;
		}
		
		#attacks-list th 
		{
		font-size:1.1em;
		text-align:left;
		padding-top:5px;
		padding-bottom:4px;
		background-color:#A7C942;
		color:#ffffff;
		}
		
		#attacks-list tr.alt td 
		{
		color:#000000;
		background-color:#EAF2D3;
		}
	</style>
	
	<link rel="stylesheet" href="css/main.css" type="text/css" />
</head>
 
<body id="index" class="home">
 
	<header id="banner" class="body">
		<h1><a href="#">SDN DETECTIVE <strong>IDS system using RYU controller</strong></a></h1>
	 
		<nav><ul>
			<li class="active"><a href="#">home</a></li>
			<li><a href="#">Traffic</a></li>
	 
			<li><a href="#">Attacks</a></li>
			<li><a href="#">Visulaization</a></li>
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
			    <th>Source IP Address</th>
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
			    <td>{{row[7]}}</td>
			    <td>{{row[3]}}</td>
			    <td>{{row[5]}}</td>
			    <td>{{row[6]}}</td>
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

