function submitCourse()
{
	var name = document.getElementById("courseNameArea").value;
	var id = document.getElementById("courseIDArea").value;
	var topicList = document.getElementsByName("topics");
	var topics = "";
	for (var i=0; i<topicList.length; i++)
	{
		if(topicList[i].checked)
		{
			topics+=","+topicList[i].value;
		}
	}
	topics=topics.substring(1)
	if (name == "" || name == null || id == "" || id == null || topics == "")
	{
		alert("Please fill in all the fields!");
	}
        var token = checkCookie("token");
	var toSend = {"name": name, "ID": id, "topics": topics, "session": token};
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