/* 
 * This is a file to test the functionality of getting a user. 
 */

function doOnLoad() {
    var token = getCookie("token");
    var dataDef = {"requestType":"getUser", "session": token, "firstName": "Morgan", "lastName": "Freeman"};
    var urlDef = "/cgi-bin/CSAssess/request.py";
    var dataTypeDef = "json";
    $.post(urlDef, dataDef, showUser, dataTypeDef);
}

function showUser(user) {
    alert(user.section);
}