select A.DEPT_ID, A.DEPT_NAME_EN, round(avg(B.SAL)) as 'AVG_SAL'
from HR_DEPARTMENT A, HR_EMPLOYEES B
where A.DEPT_ID = B.DEPT_ID
group by DEPT_ID
order by AVG_SAL desc;