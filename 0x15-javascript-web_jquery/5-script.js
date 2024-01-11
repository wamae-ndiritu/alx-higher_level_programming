$(document).ready(function() {
	$('#add_item').click(function() {
		// create a new <li> element
		var newListItem = $('<li>Item</li>');

		// Append the new <li> 
		$('ul.my_list').append(newListItem);
	});
});
