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
    <th>Destination MAC Address</th>
    <th>Source IP Address</th>
    <th>Source Port</th>
    <th>Destination IP Address</th>
    <th>Destination Port</th>
    <th>Options</th>
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
    <td>{{row[8]}}</td>
  %end
  </tr>
%end
</table>
</body>
</html>
