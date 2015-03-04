function startLogin()
{
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;
	var md5hash = CryptoJS.MD5(username+password);
	var loginInfo = {"requestType":"login", "username":username, "password": md5hash};
	$.post(
		"/cgi-bin/request.py",
		loginInfo,
		loginFunction,
		"json"
	);
}
function loginFunction(data)
{
	if (data.success == true)
	{
		setCookie("username", document.getElementById("username").value);
		setCookie("token", data.session);
		window.location.replace("login.html");
	}
	
}