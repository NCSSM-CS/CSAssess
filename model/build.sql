DROP DATABASE IF EXISTS `csassess`;
CREATE DATABASE `csassess`;
USE csassess;

-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'answer'
-- a specific answer to a specific question. Also includes ''solutions'' which are teacher submitted answers to the question.
-- ---

DROP TABLE IF EXISTS `answer`;
		
CREATE TABLE `answer` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `question_id` INTEGER NOT NULL,
  `score` DECIMAL NULL DEFAULT NULL,
  `content` TEXT NOT NULL,
  `solution` BIT NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'a specific answer to a specific question. Also includes ''sol';

-- ---
-- Table 'question'
-- 
-- ---

DROP TABLE IF EXISTS `question`;
		
CREATE TABLE `question` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `language` ENUM('python', 'java', 'none') NOT NULL COMMENT 'c, c++, java...',
  `type` ENUM('all', 'test', 'quiz', 'practice', 'inactive') NOT NULL DEFAULT 'all' COMMENT 'all, test, quiz, practice, inactive',
  `difficulty` INTEGER NOT NULL COMMENT '1-10',
  `prev_question_id` INTEGER NULL DEFAULT NULL COMMENT 'references previous versions of the question',
  `version_number` INTEGER NOT NULL DEFAULT 1,
  `last_given` DATETIME NULL DEFAULT NULL,
  `content` MEDIUMTEXT NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  CHECK (difficulty>0 and difficulty<10) 
);

-- ---
-- Table 'user'
-- contains username, passwords, and permissions. Includes all roles: Admin, Teacher, TA, student
-- ---

DROP TABLE IF EXISTS `user`;
		
CREATE TABLE `user` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `last_login` DATETIME NOT NULL,
  `username` VARCHAR(32) NOT NULL,
  `password` VARCHAR(32) NOT NULL COMMENT 'username+password MD5',
  `first_name` VARCHAR(32) NOT NULL,
  `last_name` VARCHAR(32) NOT NULL,
  `role` ENUM('admin', 'teacher', 'student') NOT NULL COMMENT 'ADMIN, TEACHER, STUDENT',
  `add_assessment` bit NOT NULL,
  `edit_user` bit NOT NULL,
  `edit_question` bit NOT NULL,
  `edit_answer` bit NOT NULL,
  `edit_test_case` bit NOT NULL,
  `edit_permission` bit NOT NULL,
  `view_student_info` bit NOT NULL,
  `view_teacher_info` bit NOT NULL,
  `view_answer` bit NOT NULL,
  `view_test_case` bit NOT NULL,
  `view_question` bit NOT NULL,
  `view_all_question` bit NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'contain username, passwords, and permissions. Includes all ';

-- ---
-- Table 'course'
-- such as ''Databases''
-- ---

DROP TABLE IF EXISTS `course`;
		
CREATE TABLE `course` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `course_code` CHAR(6) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'such as ''Databases''';

-- ---
-- Table 'section'
-- A concrete example of a class including specific dates, times, and roster.
-- ---

DROP TABLE IF EXISTS `section`;
		
CREATE TABLE `section` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `course_id` INTEGER NOT NULL,
  `year` YEAR NOT NULL,
  `term` ENUM('Trimester 1 - Fall', 'Trimester 2 - Winter', 'Trimester 3 - Spring') NOT NULL COMMENT 'school dependant',
  `period` ENUM('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I') NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'A concrete example of a class including specific dates, time';

-- ---
-- Table 'assessment'
-- 
-- ---

DROP TABLE IF EXISTS `assessment`;
		
CREATE TABLE `assessment` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `type` ENUM('problem_set', 'test', 'quiz') NOT NULL COMMENT 'problem_set, test, quiz',
  `section_id` INTEGER NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'test_case'
-- cases specific to a question, weight signifies its relative importance to the problem
-- ---

DROP TABLE IF EXISTS `test_case`;
		
CREATE TABLE `test_case` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `question_id` INTEGER NOT NULL,
  `weight` INTEGER NOT NULL,
  `content` MEDIUMTEXT NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'cases specific to a question, weight signifies its relative ';

-- ---
-- Table 'topic'
-- such as ''normal forms''
-- ---

DROP TABLE IF EXISTS `topic`;
		
CREATE TABLE `topic` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'such as ''normal forms''';

-- ---
-- Table 'comment'
-- comments given by the teacher or TA specific to an answer
-- -- TABLE IF EXISTS `comment`;
		
CREATE TABLE `comment` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `answer_id` INTEGER NOT NULL,
  `content` VARCHAR(140) NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'comments given by the teacher or TA specific to an answer';

-- ---
-- Table 'job'
-- task for a user to complete. Assigned by teachers to students and TAs. The ''verb'' to an assessment.
-- ---

DROP TABLE IF EXISTS `job`;
		
CREATE TABLE `job` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `created_by` INTEGER NOT NULL,
  `section_id` INTEGER NOT NULL,
  `type` ENUM('Take Assessment', 'Grade Assessment') NOT NULL,
  `assessment_id` INTEGER NOT NULL,
  `assigned_to_id` INTEGER NOT NULL,
  `content` VARCHAR(140) NOT NULL,
  `taken_by_user_id` INTEGER NULL DEFAULT NULL COMMENT 'used when TA is grading, name of gradee',
  `active` BIT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) COMMENT 'task for a user to complete. Assigned by teachers to student';

-- ---
-- Table 'session'
-- keeps track of user sessions
-- ---

DROP TABLE IF EXISTS `session`;

CREATE TABLE `session` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `timestamp` TIMESTAMP NOT NULL,
  `token` CHAR(64) NOT NULL,
  `ip` VARCHAR(39) NOT NULL,
  `user_id` INT NOT NULL,
  `active` BIT NOT NULL DEFAULT 1,
  UNIQUE (`token`),
  PRIMARY KEY (`id`)
) COMMENT 'keeps track of user sessions';
-- ---
-- Table 'assessment_question'
-- 
-- ---

DROP TABLE IF EXISTS `assessment_question`;
		
CREATE TABLE `assessment_question` (
  `assessment_id` INTEGER NOT NULL,
  `question_id` INTEGER NOT NULL
);

-- ---
-- Table 'question_topic'
-- 
-- ---

DROP TABLE IF EXISTS `question_topic`;
		
CREATE TABLE `question_topic` (
  `question_id` INTEGER NOT NULL,
  `topic_id` INTEGER NOT NULL
);

-- ---
-- Table 'section_user'
-- 
-- ---

DROP TABLE IF EXISTS `section_user`;
		
CREATE TABLE `section_user` (
  `section_id` INTEGER NOT NULL,
  `user_id` INTEGER NOT NULL,
  `ta_flag` BIT NOT NULL DEFAULT 1
);

-- ---
-- Table 'user_assessment'
-- 
-- ---

DROP TABLE IF EXISTS `user_assessment`;
		
CREATE TABLE `user_assessment` (
  `user_id` INTEGER NOT NULL,
  `assessment_id` INTEGER NOT NULL
);

-- ---
-- Table 'assessment_topic'
-- 
-- ---

DROP TABLE IF EXISTS `assessment_topic`;
		
CREATE TABLE `assessment_topic` (
  `assessment_id` INTEGER NOT NULL,
  `topic_id` INTEGER NOT NULL
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `answer` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `answer` ADD FOREIGN KEY (question_id) REFERENCES `question` (`id`);
ALTER TABLE `question` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `question` ADD FOREIGN KEY (prev_question_id) REFERENCES `question` (`id`);
ALTER TABLE `user` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `user` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `course` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `section` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `section` ADD FOREIGN KEY (course_id) REFERENCES `course` (`id`);
ALTER TABLE `assessment` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `assessment` ADD FOREIGN KEY (section_id) REFERENCES `section` (`id`);
ALTER TABLE `test_case` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `test_case` ADD FOREIGN KEY (question_id) REFERENCES `question` (`id`);
ALTER TABLE `topic` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `comment` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `comment` ADD FOREIGN KEY (answer_id) REFERENCES `answer` (`id`);
ALTER TABLE `job` ADD FOREIGN KEY (created_by) REFERENCES `user` (`id`);
ALTER TABLE `job` ADD FOREIGN KEY (section_id) REFERENCES `section` (`id`);
ALTER TABLE `job` ADD FOREIGN KEY (assessment_id) REFERENCES `assessment` (`id`);
ALTER TABLE `job` ADD FOREIGN KEY (assigned_to_id) REFERENCES `user` (`id`);
ALTER TABLE `job` ADD FOREIGN KEY (taken_by_user_id) REFERENCES `user` (`id`);
ALTER TABLE `session` ADD FOREIGN KEY (user_id) REFERENCES `user` (`id`);
ALTER TABLE `assessment_question` ADD FOREIGN KEY (assessment_id) REFERENCES `assessment` (`id`);
ALTER TABLE `assessment_question` ADD FOREIGN KEY (question_id) REFERENCES `question` (`id`);
ALTER TABLE `question_topic` ADD FOREIGN KEY (question_id) REFERENCES `question` (`id`);
ALTER TABLE `question_topic` ADD FOREIGN KEY (topic_id) REFERENCES `topic` (`id`);
ALTER TABLE `section_user` ADD FOREIGN KEY (section_id) REFERENCES `section` (`id`);
ALTER TABLE `section_user` ADD FOREIGN KEY (user_id) REFERENCES `user` (`id`);
ALTER TABLE `user_assessment` ADD FOREIGN KEY (user_id) REFERENCES `user` (`id`);
ALTER TABLE `user_assessment` ADD FOREIGN KEY (assessment_id) REFERENCES `assessment` (`id`);
ALTER TABLE `assessment_topic` ADD FOREIGN KEY (assessment_id) REFERENCES `assessment` (`id`);
ALTER TABLE `assessment_topic` ADD FOREIGN KEY (topic_id) REFERENCES `topic` (`id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `answer` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `question` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `user` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `course` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `section` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `assessment` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `test_case` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `topic` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `comment` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `job` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `assessment_question` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `question_topic` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `section_user` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `user_assessment` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `assessment_topic` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `answer` (`id`,`created`,`created_by`,`question_id`,`score`,`answer_text`) VALUES
-- ('','','','','','');
-- INSERT INTO `question` (`id`,`created`,`created_by`,`language`,`type`,`difficulty`,`prev_question_id`,`version_number`,`last_given`,`question_text`) VALUES
-- ('','','','','','','','','','');
-- INSERT INTO `user` (`id`,`created`,`created_by`,`last_login`,`username`,`password`,`role`,`edit_user`,`edit_question`,`edit_answer`,`edit_test_case`,`add_assessment`,`edit_permission`,`view_student_info`,`view_teacher_info`,`view_answer`,`view_test_case`,`view_question`,`view_all_question`) VALUES
-- ('','','','','','','','','','','','','','','','','','','');
-- INSERT INTO `course` (`id`,`created`,`created_by`,`course_code`,`name`) VALUES
-- ('','','','','');
-- INSERT INTO `section` (`id`,`created`,`created_by`,`course_id`,`year`,`term`,`period`) VALUES
-- ('','','','','','','');
-- INSERT INTO `assessment` (`id`,`created`,`created_by`,`type`,`section_id`) VALUES
-- ('','','','','');
-- INSERT INTO `test_case` (`id`,`created`,`created_by`,`question_id`,`weight`,`content`) VALUES
-- ('','','','','','');
-- INSERT INTO `topic` (`id`,`created`,`created_by`,`name`) VALUES
-- ('','','','');
-- INSERT INTO `comment` (`id`,`created`,`created_by`,`answer_id`,`content`) VALUES
-- ('','','','','');
-- INSERT INTO `job` (`id`,`created`,`created_by`,`section_id`,`type`,`assessment_id`,`assigned_to_id`,`content`,`taken_by_user_id`) VALUES
-- ('','','','','','','','','');
-- INSERT INTO `assessment_question` (`assessment_id`,`question_id`) VALUES
-- ('','');
-- INSERT INTO `question_topic` (`question_id`,`topic_id`) VALUES
-- ('','');
-- INSERT INTO `section_user` (`section_id`,`user_id`) VALUES
-- ('','');
-- INSERT INTO `user_assessment` (`user_id`,`assessment_id`) VALUES
-- ('','');
-- INSERT INTO `assessment_topic` (`assessment_id`,`topic_id`) VALUES
-- ('','');


