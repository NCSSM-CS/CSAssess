/* 
 This is the javacsript for the part of the file that will be incharge of adding
questions to the database.
 */

function assessmentOnLoad() {
    generateTopicCheckboxes();
    generateSectionCheckboxes();
}


function success() {
    alert("Your assessment was assigned.");
}

function error() {
    alert("Your assessment was not created.");
}

//Called by an onload event in the body
function generateTopicCheckboxes() {
    var token = checkCookie("token");
    var dataDef = {"requestType":"getTopics", "session": token};
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
 
function reload() {
    location.reload();
}
