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
    //Defines the JSON to be returned
    var dataDef = {requestType:"addQuestion", language: language, topic: topics, difficulty: difficulty, answer: answerContent };
    //Checks to see if they typed a question
    if(questionContent == "") {
        alert("Please enter a question");
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
    //TODO: Need to make sure this works, figure out how validation is going to be done.
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
    var dataDef = {requestType:"getTopics"};
    var urlDef = "/cgi-bin/request.py";
    var dataTypeDef = "json";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
    $.post(urlDef, dataDef, setTopics, dataTypeDef);
}
//Will store the topics. Declared here so other functions can see it. 
var numTopics = [];
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
            span.appendChild(input);
            document.getElementById("topicSelect").appendChild(span);
            numTopics.push(topics[keys[i]]);
        }
    }
    function getTopics() {
        topics = "";
        for(var i = 0; i < numTopics.length; i++) {
            if($('#'+numTopics[i]).prop('checked')) topics += numTopics[i] + " ";
        }
        return topics;
    }
 }
 
function newTopicSelect(e)
{
    if (e.keyCode == 13) 
    {
        numTopics.push(document.getElementById("topic").value);
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