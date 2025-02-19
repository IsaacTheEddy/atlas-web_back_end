-- Creates a need_meeting if its been a month from the last one
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
    AND (
        last_meeting IS NULL
        OR last_meeting <= CURDATE() - INTERVAL 1 MONTH
    );
