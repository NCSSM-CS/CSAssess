function returnValues(val){
	if (val == 0){
		return {
            lineNumbers: true,
            name: "python",
            version: 3,
            indentUnit: 4,
            matchBrackets: true
          });
	} else if (val == 1){
		return {
        lineNumbers: true,
        matchBrackets: true,
        mode: "text/x-java"
      });
	} else if (val == 2){
		return {
        lineNumbers: true,
        matchBrackets: true,
        mode: "text/x-csrc"
      });
	} else if (val == 3){
		return {
        lineNumbers: true,
        matchBrackets: true,
        mode: "text/x-c++src"
      });
	} else {
		return {
			lineNumbers: true,
			matchBrackets: true;
		}
	}
}