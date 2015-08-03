function submitCourse() {
  var name = document.getElementById("courseNameArea").value;
  var courseCode = document.getElementById("courseIDArea").value;
  if (courseCode == "" || courseCode == null || name == "" || name == null) {
    alert("Please fill in all the fields!");
  }
  var token = getCookie("token");
  var toSend = {"requestType": "addCourse", "courseCode": courseCode, "session": token, "name": name};
  //todo in later versions: add actual validation w/ tokens
  $.post(
    "/cgi-bin/CSAssess/controller/request.py",
    toSend,
    "json",
    console.log("Executed.")
  );
}