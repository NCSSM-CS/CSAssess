function submitCourse()
{
	var name = document.getElementById("courseNameArea").value;
	var id = document.getElementById("courseIDArea").value;
	if (name == "" || name == null || id == "" || id == null)
	{
		alert("Please fill in all the fields!");
	}
    var token = getCookie("token");
	var toSend = {"name": name, "courseCode": id, "session": token};
	toSend.requestType = "addUser";
	toSend = {"name": name, "ID": id, "session": token};
	toSend.requestType = "addCourse";
	console.log(toSend);
    $.post("/cgi-bin/CSAssess/controller/request.py", toSend, console.log("done"), "json");
}