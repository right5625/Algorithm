select sum(B.SCORE) as 'SCORE', A.EMP_NO, A.EMP_NAME, A.POSITION, A.EMAIL
from HR_EMPLOYEES A, HR_GRADE B
where A.EMP_NO = B.EMP_NO
group by EMP_NO
order by SCORE desc
limit 1;