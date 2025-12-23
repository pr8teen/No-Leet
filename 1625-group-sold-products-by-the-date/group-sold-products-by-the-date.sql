
SELECT sell_date, count(DISTINCT product) as num_sold,
STRING_AGG(DISTINCT product, ',') AS products
from Activities
group by sell_date
ORDER BY sell_date