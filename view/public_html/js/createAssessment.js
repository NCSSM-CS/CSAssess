/* 
 This is the javacsript for the part of the file that will be incharge of adding
questions to the database.
 */

function assessmentOnLoad() {
    generateTopicCheckboxes();
    generateSectionCheckboxes();
}

}
function success() {
    alert("Your assessment was assigned.");
}

function error() {
    alert("Your assessment was not created.");
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
            input.setAttribute("type","checkbox");
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
 
//Called by an onload event in the body
function generateSectionCheckboxes() {
    var dataDef = {requestType:"getSections","session":checkCookie("token"),"username":checkCookie("username")};
    var urlDef = "/cgi-bin/request.py";
    var dataTypeDef = "json";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
    $.post(urlDef, dataDef, setSections, dataTypeDef);
}
//Will store the topics. Declared here so other functions can see it. 
var sections = [];
function setSections(sections) {
   //Create and append a new option to the option element.
    var sectionContainer = document.getElementByID("sectionSelect")
    for(i=0, i<Object.keys(sections).length, i++)
    {
        var name = sections[i].name;
        var span = document.createElement("span");
        span.className("addSection");
        var input = document.createElement("input");
        input.setAttribute("type","checkbox");
        input.id = name;
        input.innerHTML = name;
        span.appendChild(input);    
        document.getElementById("sectionSelect").appendChild(span);
        sections.push(sections[i]);
    }
 }


function reload() {
    location.reload();
}