-- ---
-- ANSWER TEST DATA
-- inserts answers connected to questions
-- ---

INSERT INTO answer
	(
		created_by, question_id, score, content, solution, active
	)
	VALUES
		( 3,  1, 1, '0001', 1, 1),
		( 6,  1, 0, '2', 0, 1),

		( 4,  2,  1, 'fleventy five', 1, 1),
		( 5,  2,  0, '32', 0, 1),

		( 3,  3,  1, 'class Test(object)', 1, 1),
		( 6,  3,  0, 'wealthy by inheritance', 0, 1),

		( 4,  4, 1, 'false', 1, 1),
		( 7,  4, 0, 'yes', 0, 1),

		( 3,  5, 1, 'watch cat videos', 1, 0),
		( 7,  5, 0, 'be awsome', 0, 0),

		( 4,  6,  1, 'coffee', 0, 0),
		( 3,  6,  0, 'the dude spilled coffee over his computer when thinking of a name', 0, 0),

		(3,  7,  1, 'cordata', 0, 1),
		(10,  7,  0, 'snakes r cool', 0, 1),

		( 4,  8,  1, 'yes', 1, 1),
		( 9,  8,  0, 'no', 0, 1),

		( 4,  9, 1, 'programming language', 1, 1),
		( 8,  9, 0, 'Java is a class oriented programming language', 0, 1),

		( 4, 10,  1, 'vertabrata', 1, 1),
		( 9, 10,  0, 'snakes r still c00l', 0, 1),

		( 3, 11,  1, 'An African or European Swallow?', 1, 1),
		( 9, 11,  0, '2', 0, 1),

		( 4, 12,  1, 'Java', 1, 1),
		( 9, 12,  0, 'Python', 0, 1),

		( 4, 13,  1, 'Reptilia', 1, 1),
		( 9, 13,  0, 'snakes', 0, 1),

		( 4, 14,  1, '17th century', 1, 1),
		( 6, 14,  0, 'enough', 0, 1),

		( 3,  15, 1, '42', 1, 1),
		( 8,  15, 0, '43', 0, 1);


