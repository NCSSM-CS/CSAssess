function submitUser()
{
	var username = document.getElementById("usernameField").value;
	var password = document.getElementById("passwordField").value;
	var first_name = "";
	var last_name = "";
	var name = document.getElementById("nameField").value;
	var role = document.getElementById("roleField").value;
	name = name.split(" ");
	first_name = name[0];
	last_name = name[1];
	if (username == "" || username == null || password == "" || password == null || name == "" || name == null || role == "")
	{
		alert("Please fill in all the fields!");
	}
	var toSend = {"username": username, "password": password, "first_name": first_name, "last_name": last_name, "role": role};
	//todo in later versions: add actual validation w/ tokens
	toSend.token = "token-standin";
	toSend.requestType = "addUser";
	console.log(toSend);
	$.post(
	{                                                 
        url:"/cgi-bin/request.py",                                                 
        data: toSend,
        dataType: "json",
        success: console.log("Success!")
	});
}
