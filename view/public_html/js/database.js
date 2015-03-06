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
	//var topic = document.getElementById("topic").value;
	var i = 0;
	var j = 0;
	var length = Object.keys(questions.questionlist).length; //gets length of associative array "questions"
	var container = document.getElementById("database_container"); //gets container to put table in
	while (container.firstChild) //removes old table if it exists
	{
  		container.removeChild(container.firstChild);
	}
	var data = ["difficulty", "language", "last_given", "topic", "content"]; //topics to get from request
	var data2 = ["Difficulty", "Language", "Last Given", "Topic", "Content"]; //labels for columns
	var database = document.createElement("TABLE"); //creates table
	database.setAttribute("id","database"); 		//identifies as database
	database.setAttribute("class","table table-bordered"); //adds bootstrap table classes
	var thead = document.createElement("THEAD"); //adds table head
	var tr = document.createElement("TR");
	for (j = 0; j < 5; j++) 				//adds elements in table head as labels
	{
    	var th = document.createElement("TH");
    	th.textContent = data2[j];
    	tr.appendChild(th);
    }
    thead.appendChild(tr);
    database.appendChild(thead);
    var tbody = document.createElement("TBODY"); //gets all questions and puts them in table 
	for (i = 0; i < length; i++) 
	{	
		var tr = document.createElement("TR");
		for (j = 0; j < 5; j++) 
		{
    		var td = document.createElement("TD");
    		td.textContent = questions.questionlist[i][data[j]];
    		tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    database.appendChild(tbody);
    document.getElementById("database_container").appendChild(database); //puts table on page
}
function submitQuery()
{
	var difficulty = document.getElementById("difficulty").value;
	var topic = document.getElementById("topicSelect").value;
	//var keyword = document.getElementById("practiceKeyword").value;
	var toSend = {};
	topic = [topic];
	if (difficulty != "")
	{
		toSend.difficulty = difficulty;
	}
	if (topic != "")
	{
		toSend.topic = topic;
	}
	//todo in later versions: add actual validation w/ tokens
    var token = getCookie("token");
	toSend.session = token;
	toSend.requestType = "getQuestion";
    $.post("/cgi-bin/CSAssess/controller/request.py", toSend, searchDatabase, "json");
}
