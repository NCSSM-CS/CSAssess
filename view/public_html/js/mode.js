//CEW 

//isCalled toggles on and off with call of returnValues
var isCalled = false;

//CodeMirror Editor in textarea
var editor;

//Bool to determine if all questions have answers
var isCompleted;

//Stores answers, initialized to number of questions on test
var answers;

//Stores number question in assessment
var numQuest;

function returnValues(val)
{
  //val - value of dropdown menu containing languages
  //result - updates textarea to be language specific
  
  //Basic json of default editor
  var languageArgs;

  languageArgs = {
    lineNumbers: true,
    matchBrackets: true
  }

  
  //Assigns arguments to the language object depending on val
  if (!isCalled)
  {
    if (val == "Python")
    {
      languageArgs["name"] = "python";
      languageArgs["version"] = 3;
      languageArgs["indentUnit"] = 4;
    }
    else if (val == "Java")
    {
      languageArgs["mode"] = "text/x-java";
    } 
    else if (val == "C")
    {
      languageArgs["mode"] = "text/x-csrc";
    }
    else if (val == "C++")
    {
      languageArgs["mode"] = "text/x-c++src";
    } 
    
     //Creates a CodeMirror editor in place of TextArea
    this.editor = CodeMirror.fromTextArea(
      document.getElementById('codingArea'),
      languageArgs);
      
    //Toggles isCalled
    isCalled = true;
    
    //If the option is changed, deletes CodeMirror and calls this function again to initialize a new one
    //This took 1.5 hours to figure out. I nearly cried.
  }   else {

    this.editor.toTextArea();
    isCalled=false;
    returnValues(val);
    
  }
  
  return;
}

//CEW
//Originally stores first button, then changes as buttons are clicked.
//This is used to update the previous button after it is deactivated
var prevButt = document.getElementById("currentQuest");

//Index of Question. Used to reference into answers
var indexQuest;

//Makes a string variable because CodeMirror be trippin
var newText;

//Changes style of button to reflect state of code in question
//Orange: Code in question
//Green: Current Question
//Gray: No code in question
function changeButtClass(that){
  
  //Stores previous button and deletes its id to avoid conflicts
  prevButt =  document.getElementById("currentQuest");
  prevButt.removeAttribute("id");
  
  //Takes content of button and decrements 1 so it can assess answers
  indexQuest = prevButt.textContent -1;
  
  //Saves answer in textarea to answers
  answers[indexQuest] = editor.getValue();
  
  //Updates current editor text to answer of current question
  editor.setValue(answers[that.textContent-1]);
  
  //Changes prevbutt color depending on whether or not text is in the textarea
  if (answers[prevButt.textContent-1] == ""){
  
    prevButt.setAttribute("class","btn btn-default");
    
  } else{
  
    prevButt.setAttribute("class","btn btn-default btn-warning");
    
  }
  
  //Updates look and id of buttons.
  that.setAttribute("class", "btn btn-default btn-success");
  that.setAttribute("id", "currentQuest");

}
          
//CEW
//submits data to database
//TODO: Submit data to database
function submitSubmission(){

  //result - Gets metadata and puts it into a JSON

  //Updates last answer so it is in answers
  answers[document.getElementById("currentQuest").textContent-1] = editor.getValue();
  
  isCompleted = true;
  
  
  for (var i =0; i<answers.length;i++){
    if (answers[i] == ""){
      isCompleted = false;
    }
  }
  if (!isCompleted){
    if (!confirm("You have not completed all problems. Are you sure that you want to submit?")){
      return;
    }
  }
  var submitData;
  submitData = {
    //language: document.getElementById('languageSelect').value,
    time: Date(),
    problem: "1.1",
    submissions: answers
  };

}

//CEW 
//Initializes editor to Python and makes all answers  = ""
function initialPython(){
  var urlDef = "/cgi-bin/CSAssess/controller/request.py";
  var token = getCookie("token");
  var dataDef = {"requestType":"getAssessment",
                  "session": token,
                  "name": "t0",
                  "user": "",
                  "section": "",
                  "course": "",
                  "question": 1
                 };
  
  console.log(dataDef);
  
  var dataTypeDef = "json";
  //Gets assessment
  $.post(urlDef, dataDef, makeTheTestPage, dataTypeDef);
  
  numQuests = 5;
  answers = new Array(numQuests);
  
  createProgress();
  for (var i = 0; i<answers.length;i++){
    answers[i] = "";
  }
  languageArgs = {
    lineNumbers: true,
    matchBrackets: true,
    indentUnit: 4,
    version: 3,
    name: "Python"
  };
  this.editor = CodeMirror.fromTextArea(
      document.getElementById('codingArea'),
      languageArgs);
   isCalled = true;
}

//CEW
//creates the progress buttons
function createProgress(){
  for (var i=0;i<numQuests;i++){
    var btn = document.createElement("BUTTON");
    var questNum = document.createTextNode(i+1);
    if (i==0){
      btn.setAttribute("class","btn btn-default btn-success");
      btn.setAttribute("id","currentQuest");
    }else{
      btn.setAttribute("class","btn btn-default");
    }
    btn.setAttribute("onclick","changeButtClass(this)");
    btn.appendChild(questNum);
    document.getElementById("progress").appendChild(btn);
  }
}


//CEW
 function makeTheTestPage(data){
  console.log(data["assessmentList"]);
  console.log(data["session"]);  
  console.log(data);
 }
