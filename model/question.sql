-- ---
-- QUESTION TEST DATA
-- inserts a selection of questions
-- ---

INSERT INTO question
    (
	created_by,
	language,
	type,
	difficulty,
	content,
	active
    )
VALUES
    (
	3,
	'none',
	'quiz',
	10,
	'Convert the number 1 into binary.',
	1
    ),
    (
	4,
	'none',
	'test',
	1,
	'What is 9 x F in hexadecimal?',
	1
    ),
    (
	3,
	'python',
	'quiz',
	5,
	'How would you define a class "Test" that inherits from object?',
	1
    ),
    (
	4,
	'java',
	'test',
	5,
	'What is the result of new String("Test") == new String("Test")',
	1
    ),
    (
	3,
	'none',
	'quiz',
	5,
	'What does Todd Robert\'s wife do for a living?',
	0
    ),
    (
	4,
	'java',
	'test',
	5,
	'Where does Java get it\'s name?',
	0
    ),
    (
	3,
	'python',
	'quiz',
	3,
	'To what biological phylum does the python belong?',
	1
    ),
    (
	4,
	'none',
	'test',
	3,
	'In 300 words or more, explain what "it" is.',
	1
    ),
    (
	4,
	'java',
	'quiz',
	10,
	'What is Java?',
	1
    ),
    (
	4,
	'python',
	'test',
	5,
	'To what biological subphylum does the python belong?',
	1
    ),
    (
	3,
	'python',
	'quiz',
	3,
	'How many coconuts can a swallow carry?',
	1
    ),
    (
	4,
	'java',
	'test',
	7,
	'Complete the following sentence: I love Monty ______.',
	0
    ),
    (
	4,
	'python',
	'quiz',
	7,
	'To what biological class does the python belong?',
	1
    ),
    (
	4,
	'java',
	'test',
	2,
	'In what century did Java coffee emerge?',
	1
    ),
    (
	3,
	'none',
	'quiz',
	6,
	'What is the answer to life, the universe, and everything?',
	1
    );
