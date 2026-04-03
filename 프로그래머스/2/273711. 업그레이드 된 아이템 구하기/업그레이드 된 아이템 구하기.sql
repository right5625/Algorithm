select A.ITEM_ID, A.ITEM_NAME, A.RARITY
from ITEM_INFO A join (
    select B.ITEM_ID
    from ITEM_INFO A, ITEM_TREE B
    where A.ITEM_ID = B.PARENT_ITEM_ID and A.RARITY = 'RARE'
) B on A.ITEM_ID = B.ITEM_ID
order by ITEM_ID desc;