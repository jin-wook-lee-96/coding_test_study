SELECT DISTINCT(a.car_id)
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY a, CAR_RENTAL_COMPANY_CAR b
WHERE a.car_id = b.car_id
AND car_type = '세단'
AND START_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY a.car_id DESC
