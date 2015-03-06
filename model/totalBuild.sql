-- ---
-- Build all source files
-- ---

SOURCE db.sql
SOURCE user.sql
SOURCE course.sql
SOURCE section.sql
SOURCE topic.sql
SOURCE question.sql
SOURCE answer.sql
SOURCE assessment.sql
SOURCE assessment_question.sql
SOURCE assessment_section.sql

INSERT INTO `session` (token, ip, user_id, active) values ('morganfreemanmorganfreemanmorganfreemanmorganfreemanmorganfreema', '127.0.0.1', 1, 1);
