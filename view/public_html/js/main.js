function getExternal(filepath, callback) //ajax request function
{	//filepath - path of file to be fetched
	//callback - function to be executed with file gotten
	//doesn't return, callback should be executed and return
	var ajax = new XMLHttpRequest(); 
	ajax.onreadystatechange = function () {
		if (ajax.readyState === 4 && ajax.status === 200) {
			callback(ajax.responseText);
		}
	};
	ajax.open("GET", filepath, "true");
	ajax.send();
}
function parseJSON(filepath) //parses JSON output
{	//filepath - path of JSON file to be fetched
	//returns javascript object
	getExternal(filepath, function(text) 
	{
		var obj = JSON.parse(text);
		return obj;
	});
}