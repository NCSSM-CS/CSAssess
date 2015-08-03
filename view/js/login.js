function startLogin() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var md5hash = CryptoJS.MD5(username + password);
  var token = getCookie("token");
  var loginInfo = {"requestType": "login", "session": token, "username": username, "password": md5hash};
  $.post(
    "/cgi-bin/request.py",
    loginInfo,
    loginFunction,
    "json"
  );
}
function loginFunction(data) {
  if (data.success == true) {
    addCookie("username", document.getElementById("username").value);
    addCookie("token", data.session);
    window.location.replace("index.html");
  }
  document.getElementById("error").textContent = "Invalid login!";
}