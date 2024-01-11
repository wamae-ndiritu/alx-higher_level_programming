$(document).ready(function() {
	// Handle adding a new item
	$('#add_item').click(function() {
		// Create a new <li> element with text Item
		var newListItem = $('<li>Item</li>');

		// Append the new list item to UL.my_list
		$('ul.my_list').append(newListItem);
	});

	// Handle removing the last item of the list
	$('#remove_item').click(function() {
		// Select and remove the last <li> element
		$('ul.my_list li:last-child').remove();
	});

	// Handle clearing the entire list
	$('#clear_list').click(function() {
		// Remove all <li> elements from the UL.my_list
		$('ul.my_list').empty();
	});
});
