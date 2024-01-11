$(document).ready(function() {
	$('#btn_translate').click(function() {
		// Get the language code entered by the user
		var languageCode = $('#language_code').val();

		// Make an AJAX request to fetch for translation
		$.ajax({
			url: 'https://www.fourtonfish.com/hellosalut/hello/',
			method: 'GET',
			data: { lang: languageCode },
			success: function(data) {
				// Update the text of #DIV#hello
				$('#hello').text(data.hello);
			},
			error: function(jqXHR, textStatus, errorThrown) {
				// Handle error
				console.error('Error fetching translation:', textStatus, errorThrown);
			}
		});
	});
});
