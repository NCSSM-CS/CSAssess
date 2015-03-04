/* 
 *This is a javascript file for setting the HTML content of various elements on the 
 * database view page. 
 */ 

//Run by an onload event in the body tag. 
function doOnLoad() {
    var dataDef = {requestType:"getTopics"};
    var urlDef = "/cgi-bin/request.py";
    var dataTypeDef = "json";
  //$.post(urlToSubmitTo, dataToSubmit, successFunctionToRunOnReturn, expectedReturnType)
    $.post(urlDef, dataDef, getTopics, dataTypeDef);

  //$.ajax({
    //    type: "POST",
      //  url: urlDef,
        //data: dataDef,
        //dataType: dataTypeDef,
        //success: getTopics
    //}); 
}

/*  this function takes the list of topics from the ajax call and uses that
 * to generate the options for the select
 */
function getTopics(topics) {
    //This is the dumb way to get the keys of the JSON
    keys = Object.keys(topics);

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

