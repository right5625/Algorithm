select concat('/home/grep/src/', A.BOARD_ID, '/', B.FILE_ID, B.FILE_NAME, B.FILE_EXT) as 'FILE_PATH'
from USED_GOODS_BOARD A join USED_GOODS_FILE B on A.BOARD_ID = B.BOARD_ID
where A.VIEWS = (
    select max(VIEWS)
    from USED_GOODS_BOARD
)
order by FILE_ID desc;