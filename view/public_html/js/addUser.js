function submitUser()
{
	var username = document.getElementById("usernameField").value;
	var password = document.getElementById("passwordField").value;
	var password2 = document.getElementById("passwordField2").value;
	var first_name = "";
	var last_name = "";
	var name = document.getElementById("nameField").value;
	var roles = document.getElementsByName("roleField");
	var role = "";
	for (var i=0; i<roles.length; i++)
	{
		if(roles[i].checked)
		{
			role+=","+roles[i].value);
		}
	}
	name = name.split(" ");
	first_name = name[0];
	last_name = name[1];
	if (username == "" || username == null || password == "" || password == null || name == "" || name == null || role == "")
	{
		alert("Please fill in all the fields!");
	}
	if (password!=password2)
	{
		alert("Your passwords do not match. Please retype your passwords.");
		throw new Error("Passwords do not match");
	}
	role=role.substring(1);
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

function showSelectedValues()
{
$("input[name=roleField]:checked").map(function(){return this.value;}).get().join(",");
}