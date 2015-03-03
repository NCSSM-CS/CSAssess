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
function searchDatabase(text)
{
	//todo: find out how topic will be gotten and figure out how to parse it
	var questions = JSON.parse(text);
	//var topic = document.getElementById("topic").value;
	var difficulty = document.getElementById("difficulty").value;
	var keyword = document.getElementById("practiceKeyword").value;
	var i = 0;
	var j = 0;
	//for (var i = 0; i < questions; i++)
	//{
	//	var topic_id = questions[i].topic;
	//	if (topic != topic_id)
	//	{
	//		questions.splice(i, 1);
	//	}
	//}
	var length = Object.keys(questions).length;
	if (difficulty != "")
	{
		console.log("Difficulty check running!");
		for (i = 0; i < length; i++)
		{
			var difficulty_id = questions[i].difficulty;
			if (difficulty != difficulty_id)
			{
				delete questions[i];
			}
		}
	}
	if (keyword != "" && keyword != null)
	{
		keyword = keyword.split(" ");
		if ((typeof keyword[1]) != "undefined")
		{
			document.getElementById("error").textContent = "Multiple keywords are not supported. Please enter 1 keyword";
			return 0;
		}
		keyword = keyword[0];
		//todo: implement partial string matching
		for (i = 0; i < length; i++)
		{
			if ((typeof questions[i]) == 'undefined')
			{
				continue;
			}
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
				delete questions[i];
			}
		}
	}
	document.getElementById("error").textContent = "";
	var container = document.getElementById("database_container");
	while (container.firstChild) 
	{
  		container.removeChild(container.firstChild);
	}
	var data = ["difficulty", "language", "last_given", "topic", "content"];
	var data2 = ["Difficulty", "Language", "Last Given", "Topic", "Content"];
	var database = document.createElement("TABLE");
	database.setAttribute("id","database"); //creates table to keep the database in
	database.setAttribute("class","table table-bordered");
	var thead = document.createElement("THEAD");
	var tr = document.createElement("TR");
	for (j = 0; j < 5; j++) 
	{
    	var th = document.createElement("TH");
    	th.textContent = data2[j];
    	tr.appendChild(th);
    }
    thead.appendChild(tr);
    database.appendChild(thead);
    var tbody = document.createElement("TBODY");
	for (i = 0; i < length; i++) 
	{
		if ((typeof questions[i]) == 'undefined')
		{
			continue;
		}
		var tr = document.createElement("TR");
		for (j = 0; j < 5; j++) 
		{
    		var td = document.createElement("TD");
    		td.textContent = questions[i][data[j]];
    		tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    database.appendChild(tbody);
    document.getElementById("database_container").appendChild(database);
}
function submitQuery(e)
{
	if (e.keycode == 13)
	{
		getExternal('/view/public_html/js/test/test.json', searchDatabase); 
		return false;
	}
}
