//CEW 
var isCalled=false;
var editor;
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

function submitSubmission(){
  //result - Gets metadata and puts it into a JSON or list. Not sure yet
  var submitData;
  submitData = {
    language: document.getElementById('languageSelect').value,
    time: Date(),
    problem: "1.1",
    code: document.getElementById('codingArea').value
  };

  console.log(submitData);
}