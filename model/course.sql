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
