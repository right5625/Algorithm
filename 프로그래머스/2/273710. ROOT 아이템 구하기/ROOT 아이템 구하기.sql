select A.ITEM_ID, A.ITEM_NAME
from ITEM_INFO A join ITEM_TREE B on A.ITEM_ID = B.ITEM_ID
where B.PARENT_ITEM_ID is null
order by ITEM_ID;