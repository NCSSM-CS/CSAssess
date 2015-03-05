-- ---
-- ANSWER TEST DATA
-- inserts answers connected to questions
-- ---

INSERT INTO answer
	(
		created_by, question_id, score, content, solution, active
	)
	VALUES
		(1, 1, 10, '0001', 1, 1),
		(5, 2, 0, '32', 0, 1),
		(6, 3, 0, 'wealthy by inheritance', 0, 1),
		(1, 4, 10, 'false', 1, 1),
		(56, 5, 10, 'be awsome', 1, 0),
		(1, 6, 3, 'the dude spilled coffee over his computer when thinking of a name', 0, 0)
		(89, 7, 2, 'snakes r cool', 0, 1),
		(2, 8, 0, 'no', 0, 1),
		(45, 9, 10, 'Java is a class oriented programming language', 0, 1),
		(15, 10, 2, 'snakes r still c00l', 0, 1),
		(16, 11, 5, 'enough', 0, 1),
		(2, 12, 10, 'Python', 1, 1);
