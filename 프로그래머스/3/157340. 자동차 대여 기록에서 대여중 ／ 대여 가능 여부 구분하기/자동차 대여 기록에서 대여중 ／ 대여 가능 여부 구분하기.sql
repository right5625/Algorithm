select distinct A.CAR_ID, ifnull(B.AVAILABILITY, '대여 가능') as 'AVAILABILITY'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY A left outer join (
    select CAR_ID, '대여중' as AVAILABILITY
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where datediff(START_DATE, '2022-10-16') <= 0 and datediff(END_DATE, '2022-10-16') >= 0
) B on A.CAR_ID = B.CAR_ID
order by CAR_ID desc;