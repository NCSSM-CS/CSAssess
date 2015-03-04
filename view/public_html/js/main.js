function setCookie(cname, cvalue) { 	//sets cookie with an expiration date of an hour
    var d = new Date();
    d.setTime(d.getTime() + (60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}
function checkCookie(input) {	//gets a specific cookie by splitting the document.cookie property and checking for matches
	var name = input + "=",
		ca = document.cookie.split(';');
	for (var i = 0;i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0)===' ') {
			c = c.substr(1, c.length);
		}
		if (c.indexOf(name) === 0) {
			return c.substr(name.length, c.length);
		}
	}
	return 0;
}
function parseJSON(script)
{
	$.getJSON(script, function(data)
	{
		return data;
	});
}
function onLoad()
{
	//todo: change this later to a database call to see if user is teacher/student/admin
	//how this will work: on page load, the page will check the username + authentication with the database based on cookies
	//then if it doesn't validate, redirect to login; if it does, get teacher/student/admin status and load page based on user
	setCookie("authentication", "3134134"); //dummy teacher/admin login & authentication
	setCookie("username", "boyarsky");
	var id = checkCookie("username");
	var auth = checkCookie("authentication");
	var user = parseJSON("/cgi-bin/JSON.py");
	var i = 0;
	var user_id;
	while (i < user.length && id != user_id)
	{
		user_id = user[i].name;
		i++;
	}
	if (i == user.length && id != user[i].name)
	{
		window.location.replace("login.html");
	}
	i = 0;
	user = parseJSON("auth.txt");
	var user_auth;
	while (i < user.length && auth != user_auth)
	{
		user_auth = user[i].auth;
	}
	if (i == user.length && id != user[i].auth)
	{
		window.location.replace("login.html");
	}
}
