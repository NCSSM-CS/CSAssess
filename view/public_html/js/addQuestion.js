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
    var types = "";
    if($('#test').prop('checked')) types += "test" + " ";
    if($('#quiz').prop('checked')) types += "quiz" + " ";
    if($('#practice').prop('checked')) types += "quiz" + " ";
    var topics = getTopics();
    
    //Gets the token cookie, where the session data is stored. 
    var token = getCookie("token");
    //Defines the JSON to be returned
    var dataDef = {"requestType":"addQuestion","content": questionContent ,"session": token, "language": language, "topics": topics, "difficulty": difficulty, "answer": answerContent };
    //Checks to see if they typed a question, language, difficulty, topic
    if(questionContent == "") {
        alert("Please enter a question");
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
    if(types == "") {
        alert("Please enter a type");
        return false;
    }
    //Since deleting a question can't be done, it makes sure they want to add the question. 
    var keepGoing = prompt("Is this the question you want to add? \n\Type yes to submit it.");
    if(keepGoing.toUpperCase() !== "YES") 
    {
        alert("Your question was not added to the database.");
        return false;
    }
    var urlDef = "/cgi-bin/request.py";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
  //$.post(urlDef, dataDef, success);
    //Gives the question information to the database. 
    $.ajax({
        type: "POST",
        url: urlDef,
        data: dataDef,
        success: success,
        error: error
    }); 
}
function success() {
    alert("Your question has been added to the database.");
}

function error() {
    alert("There was an error. Your question was not added");
}

//Called by an onload event in the body
function generateTopicCheckboxes() {
    var token = getCookie("token");
    var dataDef = {"requestType":"getTopics" , "session": token};
    var urlDef = "/cgi-bin/request.py";
    var dataTypeDef = "json";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
    $.post(urlDef, dataDef, setTopics, dataTypeDef);
}
//Will store the topics. Declared here so other functions can see it. 
var numTopics = [];
//Called once the AJAX call is done. 
function setTopics(topics) {
    var keys = Object.keys(topics);
    // using this style of for loop, i is the index of each key in keys 
    for(var i in keys)
    {
        //check to make sure that the key is an actual, useful member of the JSON (not something added by jQuery)
        if(topics.hasOwnProperty(keys[i]))
        {
            //Create and append a new option to the option element.
            var span = document.createElement("span");
            span.className = "addTopic";
            var input = document.createElement("input");
            //<span class="addtopic"><input type="checkbox" id="searching" value="searching"> Searching</span>
            //gets the topic
            input.id = topics[keys[i]];
            input.innerHTML = topics[keys[i]];
            input.setAttribute("type","checkbox");
            span.appendChild(input);
            document.getElementById("topicSelect").appendChild(span);
            numTopics.push(topics[keys[i]]);
        }
    }
 }
 
 //I have a function that returns a global variable because the controller
//kept changing how they want to get the topics, so I am leaving a call to this method
//for if/when they decide to change their minds again.
 function getTopics() {
        return numTopics;
    }
 
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
        numTopics.push(text);
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
        document.getElementById("topicSelect").appendChild(span);
    }
}
function reload() {
    location.reload();
}