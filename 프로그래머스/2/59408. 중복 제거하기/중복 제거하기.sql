select count(*) as 'count'
from (
    select distinct NAME
    from ANIMAL_INS
    where NAME is not null
) A;