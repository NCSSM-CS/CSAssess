/* 
 *This is a javascript file for setting the HTML content of various elements on the 
 * database view page. 
 */
$(function() {
  var getTopics = {"requestType":"getTopics"};
  $.post({
        url: "/cgi-bin/request.py",
        data: getTopics,
        dataType: "json",
        success: getTopics(data)
    }); 
});

/*  this function takes the list of topics from the ajax call and uses that
 * to generate the options for the select
 */
function getTopics(topics) {
    for(var i = 0; i <topics.length; i++)
    {
    var option = document.createElement("option");
    option.value = topics[i];
    option.textContent = topics[i];
    document.getElementById("topicSelect").appendChild(option);
    }
}

