-- Write your PostgreSQL query statement below
SELECT s.student_id, s.student_name, sub.subject_name, count(e.subject_name) as attended_exams FROM Students as s
CROSS JOIN Subjects AS sub
LEFT JOIN Examinations as e
ON s.student_id = e.student_id and sub.subject_name = e.subject_name
Group BY sub.subject_name, s.student_name, s.student_id
Order by s.student_id, sub.subject_name