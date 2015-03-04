function submitCourse()
{
	var name = document.getElementById("courseNameArea").value;
	var id = document.getElementById("courseIDArea").value;
	if (name == "" || name == null || id == "" || id == null)
	{
		alert("Please fill in all the fields!");
	}
        var token = checkCookie("token");
	var toSend = {"name": name, "courseCode": id, "session": token};
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