//todo: add success check to every ajax call
function getExternal(filepath, callback) { //ajax request function
	var ajax = new XMLHttpRequest(); 
	ajax.onreadystatechange = function () {
		if (ajax.readyState === 4 && ajax.status === 200) {
			callback(ajax.responseText);
		}
	};
	ajax.open("GET", filepath, "true");
	ajax.send();
}
function addCookie(cname, cvalue) { 	//sets cookie with an expiration date of an hour
    var d = new Date();
    d.setTime(d.getTime() + (60*60*1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}
function getCookie(input) {	//gets a specific cookie by splitting the document.cookie property and checking for matches
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
function redirectLoad(data)
{
	var role = data.role;
	if (role === "")
	{
		window.location.replace("login.html");
	}
	var i = 0;
	for (i = 0; i < role.length; i++)
	{
		var jsonObj = {"requestType":"getSections", "sessions":getCookie("token"), "username":data.username};
		if (role[i] === "teacher")
		{
			$('head').load("js/loadTeacher.js");
			 $.post(
			 	"/cgi-bin/request.py",
			 	jsonObj,
			 	loadTeacher,
			 	"json"
			 );
		}
		if (role[i] === "student")
		{
			$('head').load("js/loadStudent.js");
			$.post(
			 	"/cgi-bin/request.py",
			 	jsonObj,
			 	loadStudent,
			 	"json"
			 );
		}
		var name = data.first_name + data.last_name;
		document.getElementById("name").textContent = name;
		
	}
}
function onLoad()
{
	//todo: during authentication setup change this to fetch username and roles
	var username = getCookie("username");
	var session = getCookie("token");
 	username = "boyarskys";
	var loadJSON = {"requestType":"getUser", "username": username, "session":session};
	$.post(
		"/cgi-bin/request.py",
		loadJSON,
		redirectLoad,
		"json"
	);
}
