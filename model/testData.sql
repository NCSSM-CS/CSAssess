use csassess;

insert into `user` (created, created_by, last_login, username, password, first_name, last_name, role, add_assessment, edit_user, edit_question, edit_answer, edit_test_case, edit_permission, view_student_info, view_teacher_info, view_answer, view_test_case, view_question, view_all_question) values ('2015-03-01 00:00:00', 1, '2015-03-01 00:00:00', 'god', 'password', 'Morgan', 'Freeman', 'admin', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

insert into topic (created, created_by, name) values ('2015-03-01 00:00:01', 1, 'testTopic1'), ('2015-03-01 00:00:02', 1, 'testTopic2'), ('2015-03-01 00:00:03', 1, 'testTopic3');

insert into question (created, created_by, language, difficulty, content) values ('2015-03-01 00:00:04', 1, 'python', '3', 'test1'), 
('2015-03-01 00:00:05', 1, 'python', '3', 'test2'), ('2015-03-06 00:00:06', 1, 'python', '3', 'test3'), ('2015-03-01 00:00:07', 1, 'python', '6', 'test4'), ('2015-03-01 00:00:08', 1, 'python', '6', 'test5'), ('2015-03-01 00:00:09', 1, 'python', '6', 'test6'), ('2015-03-01 00:00:10', 1, 'python', '9', 'test7'), ('2015-03-01 00:00:11', 1, 'python', '9', 'test8'), ('2015-03-01 00:00:12', 1, 'python', '9', 'test9');

insert into course (created, created_by, course_code, name) values ('2015-03-01 00:00:13', 1, 'CS420', 'SMOKE WEED EVERYDAY!!!');

insert into section (created, created_by, course_id, year, term, period) values ('2015-03-01 00:00:14', 1, 1, 2015, 'Trimester 1 - Fall', 'A'), ('2015-03-01 00:00:15', 1, 1, 2015, 'Trimester 2 - Winter', 'B'), ('2015-03-01 00:00:16', 1, 1, 2015, 'Trimester 3 - Spring', 'C');

insert into assessment (created, created_by, type, section_id, name) values ('2015-03-01 00:00:17', 1, 'test', 1, 'testTest1');

insert into assessment_question (assessment_id, question_id) values (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9);

insert into assessment_topic (assessment_id, topic_id) values (1, 1), (1, 2), (1, 3);
