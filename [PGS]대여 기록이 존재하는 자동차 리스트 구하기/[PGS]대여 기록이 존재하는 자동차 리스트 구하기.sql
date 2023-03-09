SELECT DIStinct(a.car_id)
from CAR_RENTAL_COMPANY_RENTAL_HISTORY a, CAR_RENTAL_COMPANY_CAR b
where a.car_id = b.car_id
and car_type = '세단'
and START_DATE BETWEEN '2022-10-01' and '2022-10-31'
order by a.car_id DESC
