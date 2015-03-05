/* 
 *This is a javascript file for setting the HTML content of the topic dropdown
 *on the database view page
 */ 

//Run by an onload event in the body tag. 
function doOnLoad() {
    var token = getCookie("token");
    var dataDef = {"requestType":"getTopics", "session": token};
    var urlDef = "/cgi-bin/CSAssess/request.py";
    var dataTypeDef = "json";
    $.post(urlDef, dataDef, getTopics, dataTypeDef);
}

/*  this function takes the list of topics from the ajax call and uses that
 * to generate the options for the select
 */
function getTopics(topics) {
    //This is the dumb way to get the keys of the JSON
    var keys = Object.keys(topics);

    // using this style of for loop, i is the index of each key in keys 
    for(var i in keys)
    {
        //check to make sure that the key is an actual, useful member of the JSON (not something added by jQuery)
        if(topics.hasOwnProperty(keys[i]))
        {
            //Create and append a new option to the option element.
            var option = document.createElement("option");
            option.value = topics[keys[i]];
            option.textContent = topics[keys[i]];
            document.getElementById("topicSelect").appendChild(option);
        }
    }
}

