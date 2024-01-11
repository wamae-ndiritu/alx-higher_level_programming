$(document).ready(function() {
	// Event handler for translating hello
	function translateHello() {
		// Get the language code entered by the user
		var languageCode = $('#language_code').val();

		// Make an AJAX request to fetch translation
		$.ajax({
			url: 'https://www.fourtonfish.com/hellosalut/hello/',
			method: 'GET',
			data: { lang: languageCode },
			success: function(data) {
				// Update the text of DIV#hello with the translation
				$('#hello').text(data.hello);
			},
			error: function(jqXHR, textStatus, errorThrown) {
				// Handle error
				console.error('Error fetching translation:', textStatus, errorThrown);
			}
		});
	}

	// Event handler for clicking the "Translate" button
	$('#btn_translate').click(translateHello);

	// Event handler for pressing ENTER in the language code input
	$('#language_code').keypress(function(event) {
		// 13 => key code for ENTER
		if (event.which == 13){ 
			translateHello();
		}
	});
});
