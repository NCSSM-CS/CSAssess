-- ---
-- SECTION TEST DATA
-- inserts a selection of sections for the courses offered
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
