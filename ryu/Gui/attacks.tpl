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
<p>The Attacks caught by IDS-controller are as follows:</p>
<table border="1" id= "attacks-list">
  <tr>
    <th>Attack Name</td>
    <th>Protocol</td>
    <th>Message</td>
    <th>Source Ip Address</td>
    <th>Source Port</td>
    <td>Destination IP Address</td>
    <td>Destination Port</td>
  </tr>
%for row in rows:
  <tr>
    <td>{{row[1]}}</td>
    <td>{{row[2]}}</td>
    <td>{{row[3]}}</td>
    <td>{{row[4]}}</td>
    <td>{{row[6]}}</td>
    <td>{{row[5]}}</td>
    <td>{{row[7]}}</td>
  %end
  </tr>
%end
</table>
</body>
</html>
