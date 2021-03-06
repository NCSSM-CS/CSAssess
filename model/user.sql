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
    ),
	(
		1,
		'2015-03-05 09:53:01',
		'bent15m',
		MD5('bent15mbear'),
		'Matthew',
		'Bent',
		'student',
		0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0,
		1
	);
