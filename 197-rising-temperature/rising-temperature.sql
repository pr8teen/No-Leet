-- Write your PostgreSQL query statement below
SELECT w1.id from Weather as w1
JOIN Weather as w2
ON w1.recordDate = w2.recordDate + 1
WHERE w1.temperature > w2.temperature
ORDER BY w1.recordDate