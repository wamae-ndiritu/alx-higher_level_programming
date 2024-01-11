$(document).ready(function() {
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		method: 'GET',
		success: function(data) {
			// Select the UL#list_movies element
			var listMovies = $('#list_movies');

			// Loop through each movie in the data an apped new li
			$.each(data.results, function(index, movie){
				listMovies.append('<li>' + movie.title + '</li>');
			});
		},
		error: function(jqXHR, textStatus, errorThrown){
			// Handle error
			console.error('Error fetching movie data:', textStatus, errorThrown);
		}
	});
});
