select count(*) as FISH_COUNT, FISH_NAME
from FISH_INFO A, FISH_NAME_INFO B
where A.FISH_TYPE = B.FISH_TYPE
group by FISH_NAME
order by FISH_COUNT desc