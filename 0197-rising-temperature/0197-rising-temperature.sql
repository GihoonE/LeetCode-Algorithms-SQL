# Write your MySQL query statement below
Select w1.id
from Weather as w1
join Weather as w2
on DATEDIFF(w1.recordDate,w2.recordDate) = 1 where w1.temperature > w2.temperature