//CEW 

//isCalled toggles on and off with call of returnValues
var isCalled = false;

//CodeMirror Editor in textarea
var editor;

//Bool to determine if all questions have answers
var isCompleted;

//Stores answers, initialized to number of questions on test
var answers = new Array(10);

function returnValues(val)
{
  //val - value of dropdown menu containing languages
  //result - updates textarea to be language specific
  var languageArgs;

  languageArgs = {
    lineNumbers: true,
    matchBrackets: true
  }

  
  //Assigns arguments to the language object.
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
     
    this.editor = CodeMirror.fromTextArea(
      document.getElementById('codingArea'),
      languageArgs);
    isCalled = true;
    //If the option is changed, deletes codemirror and initializes a new one
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
var prevButt;
//Index of Question. Used to reference into answers
var indexQuest;

//Makes a string variable because CodeMirror be trippin
var newText;

//Changes style of button
//TODO: Update textarea and store info.
function changeButtClass(that){
  

  prevButt =  document.getElementById("currentQuest");
  prevButt.removeAttribute("id");
  
  indexQuest = prevButt.textContent -1;
  
  //Saves answer to answers
  answers[indexQuest] = editor.getValue();
  
  //Updates current editor text
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
function submitSubmission(){
  //Updates last answer
  answers[document.getElementById("currentQuest").textContent-1] = editor.getValue();
  
  isCompleted = true;
  
  //result - Gets metadata and puts it into a JSON
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
    language: document.getElementById('languageSelect').value,
    time: Date(),
    problem: "1.1",
    submissions: answers
  };

}

//CEW 
//Initializes editor to Python and makes all answers  = ""
function initialPython(){

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
