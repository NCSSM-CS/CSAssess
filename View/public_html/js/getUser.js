/* 
 * This is a file to test the functionality of getting a user. 
 */

function generateUserInfo() {
    var token = getCookie("token");
    var dataDef = {"requestType":"getUser", "session": token, "firstName": "Morgan", "lastName": "Freeman"};
    var urlDef = "/cgi-bin/CSAssess/request.py";
    var dataTypeDef = "json";
    $.post(urlDef, dataDef, showUser, dataTypeDef);
}

function showUser(users) {
    var length = users.length;
     var tbody = document.createElement("TBODY"); //gets all questions and puts them in table 
	for (var i = 0; i < length; i++) 
	{	
		var tr = document.createElement("TR");
                data = Object.getKeys(users[i]);
		for (var j = 0; j < data.length; j++) 
		{
    		var td = document.createElement("TD");
    		td.textContent = users[i][j];
    		tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    database.appendChild(tbody);
    document.getElementById("database_container").appendChild(database);
}