function delete_button_clicked(songId) {
	console.log("hit");
	var action = window.confirm("Do you really want to delete this song?");
	if (action) {
		send_delete_request(songId);
	}
};

function send_delete_request(songId) {
	console.log("hit", songId);

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			console.log(xhttp.responseText);
			window.location.href = window.location.origin;
		}
	}
	xhttp.open("DELETE", "/song");
	xhttp.send("id=" + songId);
}




