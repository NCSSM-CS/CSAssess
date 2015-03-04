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
    topics = getTopics();
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
   // $.post(urlDef, dataDef, success);
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

function generateTopicDropdowns() {
    var dataDef = {requestType:"getTopics"};
    var urlDef = "/cgi-bin/request.py";
    var dataTypeDef = "json";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
    $.post(urlDef, dataDef, getTopics, dataTypeDef);
}
function getTopics() {
    var keys = Object.keys(topics);

    // using this style of for loop, i is the index of each key in keys 
    for(var i in keys)
    {
        //check to make sure that the key is an actual, useful member of the JSON (not something added by jQuery)
        if(topics.hasOwnProperty(keys[i]))
        {
            //Create and append a new option to the option element.
            var span = document.createElement("span");
            span.className = "addtopic";
            var input = document.creatElement("input");
            //<span class="addtopic"><input type="checkbox" id="searching" value="searching"> Searching</span>
            input.id = topics[keys[i]];
            input.innerHTML = topics[keys[i]];
            span.appendChild(input);
            document.getElementById("topicSelect").appendChild(span);
        }
    }
}