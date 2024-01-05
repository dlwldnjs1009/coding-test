select car_type, count(*) as cars
    from car_rental_company_car
    WHERE options LIKE '%시트%' 
    group by car_type
    order by car_type;