function submitUser()
{
	var username = document.getElementById("usernameField").value;
	var password = document.getElementById("passwordField").value;
	var password2 = document.getElementById("passwordField2").value;
	var firstName = "";
	var lastName = "";
	var name = document.getElementById("nameField").value;
	var roles = document.getElementsByName("roleField");
	var role = [];
	for (var i=0; i<roles.length; i++)
	{
		if(roles[i].checked)
		{
			role.push(roles[i].value);
		}
	}
	name = name.split(" ");
	firstName = name[0];
	lastName = name[1];
	if (username == "" || username == null || password == "" || password == null || name == "" || name == null || role == "")
	{
		alert("Please fill in all the fields!");
	}
	if (password!=password2)
	{
		alert("Passwords do not match. Please retype your password.");
		throw new Error("Passwords do not match");
	}
    var token = getCookie("token");
	var toSend = {"username": username, "session": token, "password": password, "firstName": firstName, "lastName": lastName, "role": role};
	//todo in later versions: add actual validation w/ tokens
	toSend.requestType = "addUser";
	$.post(                        
		"/cgi-bin/CSAssess/controller/request.py",                                                 
        toSend,
        "json",
        console.log("Executed.")
	);
}