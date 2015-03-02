function searchDatabase()
{
	var questions = parseJSON("/test/test.json");
	var topic = document.getElementById("topic");
	var difficulty = document.getElementById("difficulty");
	var keyword = document.getElementById("practiceKeyword");
	for (var i = 0; i < questions.length; i++)
	{
		var topic_id = questions[i].topic;
		if (topic != topic_id)
		{
			questions.splice(i, 1);
		}
	}
	if (difficulty != "")
	{
		for (i = 0; i < questions.length; i++)
		{
			var difficulty_id = questions[i].difficulty;
			if (difficulty != difficulty_id)
			{
				questions.splice(i, 1);
			}
		}
	}
	if (keyword != "" && keyword != null)
	{
		keyword = keyword.split(" ");
		if ((typeof keyword[1]) == "undefined")
		{
			document.getElementById("error").text = "Multiple keywords are not supported. Please enter 1 keyword";
			return 0;
		}
		keyword[0] = keyword;
		for (i = 0; i < questions.length; i++)
		{
			var question_content = questions[i].content;
			question_content = question_content.split(" ");
			var contains = 0;
			for (j = 0; j < question_content.length; j++)
			{
				if (question_content[j].indexOf(keyword) != -1)
				{
					contains = 1;
					break;
				}
			}
			if (contains != 1)
			{
				questions.splice(i, 1);
			}
		}
	}
	var data = ["language", "difficulty", "last_given", "content", "topic"]
	var database = document.createElement("TABLE");
	database.setAttribute("id","database"); //creates table to keep the database in
	for (i = 0; i < questions.length; i++) 
	{
		var tr = document.createElement("TR");
		for (var j = 0; j < 5; j++)
		{
			var td = document.createElement("TD");
			td.setAttribute("text", question[i].data[j])
			tr.appendChild(td);
		}
		database.appendChild(tr);
	}
	document.getElementById("database_container").appendChild(database);
}