function submitCourse()
{
	var name = document.getElementById("courseNameArea").value;
	var id = document.getElementById("courseIDArea").value;
	if (name == "" || name == null || id == "" || id == null)
	{
		alert("Please fill in all the fields!");
	}
        var token = checkCookie("token");
<<<<<<< HEAD
	var toSend = {"name": name, "courseCode": id, "session": token};
	toSend.requestType = "addUser";
=======
	var toSend = {"name": name, "ID": id, "topics": topics, "session": token};
	toSend.requestType = "addCourse";
>>>>>>> origin/master
	console.log(toSend);
        //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
        $.post("/cgi-bin/request.py", toSend, console.log("done"), "json");
}

function showSelectedValues()
{
$("input[name=roleField]:checked").map(function(){return this.value;}).get().join(",");
}