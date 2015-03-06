/* 
 This is the javacsript for the part of the file that will be incharge of adding
questions to the database.

 */


function submitQuestion() {
    //Gets the content of the input fields
    var questionContent = $("#questionSubmit").val();
    var language = $("#language").val();
    var difficulty = $("#difficulty").val();
    var answerContent = $("#answerSubmit").val();
    //Adds types if they are selected.
    var type = "";
    if($('#test').is(':checked')) type += "test" + " ";
    else if($('#quiz').is(':checked')) type += "quiz" + " ";
    else if($('#practice').is(':checked')) type += "quiz" + " ";
    //var topics = getTopics();
    var topics= ["search"];
    //Gets the token cookie, where the session data is stored. 
    var token = getCookie("token");
    //Defines the JSON to be returned
    var dataDef = {"requestType":"addQuestion","content": questionContent ,"session": token, "language": language, "topics": topics, "difficulty": difficulty, "answer": answerContent, "qType": type};
    //Checks to see if they typed a question, language, difficulty, topic
    if(questionContent == "") {
        alert("Please enter a question");
        return false;
    }
    if(type == "") {
        alert("Please select a type");
        return false;
    }
     if(language == "") {
        alert("Please enter a language");
        return false;
    }
    if(difficulty == "default") {
        alert("Please enter a difficulty");
        return false;
    }
    //Since deleting a question can't be done, it makes sure they want to add the question. 
    var keepGoing = prompt("Is this the question you want to add? \n\Type yes to submit it.");
    if(keepGoing.toUpperCase() !== "YES") 
    {
        alert("Your question was not added to the database.");
        return false;
    }
    var urlDef = "/cgi-bin/CSAssess/controller/request.py";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
  //$.post(urlDef, dataDef, success);
    //Gives the question information to the database. 
    $.ajax({
       // type: "POST",
        type: "GET",
        url: urlDef,
        data: dataDef,
        success: doOnSuccess,
        error: doOnError
    }); 
}
function doOnSuccess() {
    alert("Your question has been added to the database.");
}

function doOnError() {
    alert("There was an error. Your question was not added");
}

//Called by an onload event in the body
function generateTopicCheckboxes() {
    var token = getCookie("token");
    var dataDef = {"requestType":"getTopics" , "session": token};
    var urlDef = "/cgi-bin/CSAssess/controller/request.py";
    var dataTypeDef = "json";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
    $.post(urlDef, dataDef, setTopics, dataTypeDef);
}
//Will store the topics. Declared here so other functions can see it. 
var topicList = [];
var topicIds = {"topicList":
    [{"id": 3, "name": "sorting" },{"id": 4, "name": "searching" }
    ]};
//Called once the AJAX call is done. 
function setTopics(topics) {
    // using this style of for loop, i is the index of each key in keys 
    for(var i = 0; i < topics.topicList.length; i++ )
    {
            //Create and append a new option to the option element.
            var span = document.createElement("span");
            span.className = "addTopic";
            var input = document.createElement("input");
            topicIds[topics.topicList[i].name] = topics.topicList[i].id;
            //<span class="addtopic"><input type="checkbox" id="searching" value="searching"> Searching</span>
            //gets the topic
            input.id = topics.topicList[i].name;
            input.setAttribute("type","checkbox");
            //creates a label with the text of the question
            var label = document.createElement('label');
            label.appendChild(document.createTextNode(input.id));
            label.className = "addTopic";
            span.className = "addTopic";
            span.appendChild(input);
            span.appendChild(label);
            document.getElementById("topicSelect").appendChild(span);
            topicList.push(topics.topicList[i].name);
    }
 }
 
 //I have a function that returns a global variable because the controller
//kept changing how they want to get the topics, so I am leaving a call to this method
//for if/when they decide to change their minds again.
 function getTopics() {
        return topicList;
    }
 
 
 //Makes a new text box where the user can add topics. 
function newTopicSelect(e)
{
    if (e.keyCode == 13) 
    {
        //Gets the value of the question.
        var text = document.getElementById("topic").value;
        if(text=="") 
        {
           return false;
        }
        topicList.push(text);
        var span = document.createElement("span");
        span.className = "addTopic";
        //Takes the old text area and makes it so that enter won't do anything anymore.
        var oldTextArea = document.getElementById("topic");
        oldTextArea.setAttribute("id","");
        oldTextArea.setAttribute("onkeydown","");
        var textArea = document.createElement("input");
        textArea.id = "topic";
        textArea.type = "text";
        textArea.className = "addTopic";
        textArea.placeholder="Enter another topic.";
        textArea.setAttribute("onkeydown","newTopicSelect(event)");
        span.appendChild(textArea);
        //<span class="addtopic"><input type="text" class="addtopic" placeholder="Add new topic." id="topic"></span>
        console.log(span);
        document.getElementById("newTopic").appendChild(span);
    }
}
function reload() {
    location.reload();
}