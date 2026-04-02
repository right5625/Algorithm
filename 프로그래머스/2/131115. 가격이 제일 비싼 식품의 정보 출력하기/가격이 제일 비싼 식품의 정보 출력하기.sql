select *
from FOOD_PRODUCT
where PRICE = (
    select max(PRICE)
    from FOOD_PRODUCT
);