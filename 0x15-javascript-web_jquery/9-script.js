$(document).ready(function() {
	$.ajax({
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		method: 'GET',
		success: function(data) {
			// Update the text of DIV#hello
			$('#hello').text(data.hello);
		},
		error: function(jqXHR, textStatus, errorThrown){
			// Handle error
			console.error('Error fetching translation:', textStatus, errorThrown);
		}
	});
});
