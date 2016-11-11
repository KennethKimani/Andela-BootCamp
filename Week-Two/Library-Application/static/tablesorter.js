
$(document).ready(function(){
$(function(){
$("#mytable").tablesorter(
{
	theme : 'blue',

	sortList : [[0,0],[0,0],[0,0]],

    // header layout template; {icon} needed for some themes
    headerTemplate : '{content}{icon}',

	// initialize column styling of the table
    widgets : ["zebra"],
	widgetOptions : {
      // change the default column class names
      // primary is the first column sorted, secondary is the second, etc
      columns : [ "primary", "secondary", "tertiary" ]
	}
});
});
});
