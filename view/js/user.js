/* 
 * This is a file to test the functionality of getting a user. 
 */

function generateUserInfo() {
  showUser("hi");
  var firstName = $("#firstName").val();
  var lastName = $("lastName").val();
  if (firstName == "" || lastName == "") {
    alert("Please fill out the search criteria");
    return false;
  }
  var token = getCookie("token");
  var dataDef = {"requestType": "getUser", "session": token, "firstName": firstName, "lastName": lastName};
  var urlDef = "/cgi-bin/CSAssess/request.py";
  var dataTypeDef = "json";
  $.post(urlDef, dataDef, showUser, dataTypeDef);
}

//This is the form of the JSON i am expecting 
var json = [
  {
    "language": "Bash",
    "difficulty": "5",
    "last_given": "",
    "topic": "Loops",
    "content": "Find the word count of the servers system dictionary."
  },
  {
    "language": "Bash",
    "difficulty": "2",
    "last_given": "",
    "topic": "Recursion",
    "content": "Write a bash command to concatenate any two strings."
  },
  {
    "language": "C++",
    "difficulty": "4",
    "last_given": "",
    "topic": "Search",
    "content": "Write a bash command to add any two numbers and display the result."
  }
];
function showUser(users) {
  users = json;
  //gets all the users, the json links a key to a value user.
  var userTable = document.createElement("TABLE"); //creates table
  userTable.setAttribute("id", "userTable"); 		//identifies as userTable
  userTable.setAttribute("class", "table table-bordered");
  var tbody = document.createElement("TBODY"); //gets all questions and puts them in table
  //Iterates over each user, which is an array
  for (var i = 0; i < users.length; i++) {
    console.log(users[i]);
    var tr = document.createElement("TR");
    data = Object.keys(users[i]);
    console.log(data);
    //iterates over each element of userInfo, which is a string
    for (var j = 0; j < data.length; j++) {
      alert(data.length);
      console.log(data);
      var topic = data[j];
      console.log(topic + "hi");
      var userInfo = users[i].topic;
      console.log(userInfo);
      var td = document.createElement("TD");
      td.textContent = userInfo;
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  }
  userTable.appendChild(tbody);
  document.getElementById("userContainer").appendChild(tbody);
}