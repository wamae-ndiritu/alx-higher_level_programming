$(document).ready(function() {
	// Make an AJAX request to fetch data
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
		method: 'GET',
		success: function(data) {
			// Update the text to the DIV#character with name
			$('#character').text(data.name);
		},
		error: function(jqXHR, textStatus, errorThrown) {
			// Handle the error
			console.log('Error fetching character data:', textStatus, errorThrown);
		}
	});
});
