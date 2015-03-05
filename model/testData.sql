-- ---
-- Build the databases.
-- ---
SOURCE db.sql;

-- ---
-- USER TEST DATA
-- inserts a god user, an admin user, two teachers, and many students
-- ---

INSERT INTO user
    (
        created_by,
        last_login,
        username,
        password,
        first_name,
        last_name,
        role,
        add_assessment,
        edit_user,
        edit_question,
        edit_answer,
        edit_test_case,
        edit_permission,
        view_student_info,
        view_teacher_info,
        view_answer,
        view_test_case,
        view_question,
        view_all_question,
        active
    )
    VALUES
    (
        1,
        '2015-03-04 12:00:00',
        'god',
        MD5('goddog'),
        'Morgan',
        'Freeman',
        'admin',
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1
    ),
    (
        1,
        '2015-03-04 12:00:01',
        'admin',
        MD5('adminpassword'),
        'Paul',
        'Menchini',
        'admin',
        0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:02',
        'morrison',
        MD5('morrisonfecalexcrement'),
        'John',
        'Morrison',
        'teacher',
        1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1,
        1
    ),
    (
        1,
        '2015-03-04 12:00:03',
        'boyarskys',
        MD5('boyarskysquercus'),
        'Sam',
        'Boyarsky',
        'teacher',
        1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1,
        1
    ),
    (
        1,
        '2015-03-04 12:00:04',
        'ezhilarasan15a',
        MD5('ezhilarasan15aletmein!'),
        'Aravind',
        'Ezhilarasan',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:05',
        'mehalter',
        MD5('halter15mruprecht'),
        'Micah',
        'Halter',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:06',
        'toombs15t',
        MD5('toombs15ccaveman'),
        'Caeman',
        'Toombs',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:07',
        'chuba15e',
        MD5('chuba15eebbedcuba'),
        'Ebube',
        'Chuba',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:08',
        'patel15k',
        MD5('patel15kpassword'),
        'Keshav',
        'Patel',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:09',
        'manocha15a',
        MD5('manocha15accrunner'),
        'Aninda',
        'Manocha',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:10',
        'fang15j',
        MD5('fang15jrin4ever'),
        'John',
        'Fang',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:11',
        'paul16r',
        MD5('paul16rogrelord'),
        'Randolph',
        'Paul',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:12',
        'ranjan16v',
        MD5('ranjan16vmathematics'),
        'Vinit',
        'Ranjan',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:13',
        'zeller16l',
        MD5('zeller16liamyourfather'),
        'Luke',
        'Zeller',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:14',
        'zheng16m',
        MD5('zheng16mnocookies'),
        'Matthew',
        'Zheng',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:15',
        'lang16r',
        MD5('lang16rsister'),
        'Richard',
        'Lang',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        1
    ),
    (
        1,
        '2015-03-04 12:00:12',
        'walker14g',
        MD5('walker14gneverforget'),
        'Gibrael',
        'Walker',
        'student',
        0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
        0
    );

-- ---
-- COURSE TEST DATA
-- inserts a selection of compsci classes offered here
-- ---

INSERT INTO course
    (
        created_by, course_code, name, active
    )
    VALUES  
        (1, 'CS402', 'AP Computer Science - I', 1),
        (1, 'CS404', 'AP Computer Science - II', 1),
        (1, 'CS406', 'Advanced Programming', 1),
        (1, 'CS412', 'Data Structures', 1),
        (1, 'CS000', 'Obsolete Programming Class', 0);

-- ---
-- SECTION TEST DATA
-- inserts a selection sections for the courses offered
-- ---

INSERT INTO section
    (
        created_by,
        course_id,
        year,
        term,
        period,
        active
    )
    VALUES
    (
        1, 1, '2014',
        'Trimester 1 - Fall', 'D',
        1
    ),
    (
        1, 1, '2014',
        'Trimester 2 - Winter', 'G',
        1
    ),
    (
        1, 2, '2014',
        'Trimester 2 - Winter', 'D',
        1
    ),
    (
        1, 2, '2015',
        'Trimester 3 - Spring', 'G',
        1
    ),
    (
        1, 3, '2014',
        'Trimester 1 - Fall', 'A',
        1
    ),
    (
        1, 3, '2015',
        'Trimester 3 - Spring', 'A',
        1
    ),
    (
        1, 4, '2014',
        'Trimester 1 - Fall', 'F',
        1
    ),
    (
        1, 4, '2014',
        'Trimester 2 - Winter', 'F',
        1
    ),
    (
        1, 4, '2014',
        'Trimester 2 - Spring', 'F',
        1
    ),
    (
        1, 5, '1982',
        'Trimester 1 - Fall', 'A',
        0
    );

-- QUESTION AND ANSWER

-- ---
-- ASSESSMENT TEST DATA
-- inserts a selection of assessments
-- ---
/*
INSERT INTO assessment
    (
        created_by, type, section_id, name, active
    )
    VALUES
    (1, 'problem_set', '1', 'ps0', 1),
    (1, 'problem_set', '2', 'ps0', 1),*/
