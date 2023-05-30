распределение баллов:
    SELECT 1
    UPDATE 1
    INSERT 1
    DELETE 1

Сценарий 1: 
Авиакомпания сменила самолет и поставила на него новый двигатель
Авиакомпания купила новый самолет и необходимо добавить его описание в базу данных, а 
также удалить старый списаный самолет, потом обновить данные о скорости и двигателе, представить отчет о самолетах начальству
1. добавляем новый самолет
INSERT INTO postgres_air.aircraft (code, model, range, class, velocity) 
VALUES ('NEW_aircraft', 'Boeing777', 2000, 3, 1110);
2. проверка добавления самолета в бд 
SELECT * FROM postgres_air.aircraft WHERE code = 'NEW_aircraft';
3. новый движок и измененение данных и скорости
UPDATE postgres_air.aircraft SET velocity = 1210 WHERE CODE = 'NEW_aircraft';
SELECT * FROM postgres_air.aircraft WHERE code = 'NEW_aircraft'; --проверка что данные поменялись
4. удаление старого самолета
DELETE FROM postgres_air.aircraft WHERE code = 'CR2';
5. проверка удаления старого самолета
SELECT * FROM postgres_air.aircraft WHERE code = 'CR2';
6. формирование отчета о всех имеющихся самолетах
SELECT * FROM postgres_air.aircraft

сценарий 2:
ошибка регистрации и измененение данных о регистрации
1. обновляем время у неправильных бронирований
UPDATE postgres_air.flight 
SET scheduled_departure = '2023-04-10 10:00:00' WHERE flight_id IN (SELECT flight_id FROM postgres_air.booking_leg WHERE booking_id BETWEEN 1240000 AND 2054000);
2. добавим жену DEREK к таблице пассажиров с booking_id = 1241188
INSERT INTO postgres_air.passenger (booking_id, booking_ref, first_name, last_name, age)
VALUES (1241188, '74K122', 'BONNEY', 'MEYER', 50)
3. удаляем бронирование позвонившего пассажира, которому новое время не подходит booking_id = 2053883
DELETE FROM postgres_air.passenger
WHERE booking_id = 2053883;
4. оформляем отчёт начальству, что бронирования с 1240000 по 2054000 в порядке
SELECT * FROM postgres_air.booking
WHERE booking_id BETWEEN 1240000 AND 2054000;


сценарий 3:
отчет о самых исспользуемых аэропортах  
1. Мы выводим список всех рейсов и использованных аэропортов прилета и отправления
UPDATE postgres_air.airport
SET city = 'Los santos', airport_tz = 'Random/Random' WHERE postgres_air.airport.airport_code = 'ATL';
2. Подсчитать количество использований каждого аэропорта в списке и вывести топ-10 самых 
часто используемых аэропортов.
SELECT postgres_air.airport.airport_code, 
COUNT(postgres_air.flight.departure_airport) AS departures,
COUNT(postgres_air.flight.arrival_airport) AS arrivals,
(COUNT(postgres_air.flight.departure_airport) + COUNT(postgres_air.flight.arrival_airport)) AS total
FROM postgres_air.airport, postgres_air.flight
WHERE postgres_air.airport.airport_code = postgres_air.flight.departure_airport OR postgres_air.airport.airport_code = postgres_air.flight.arrival_airport
GROUP BY postgres_air.airport.airport_code
ORDER BY total DESC
LIMIT 10;
3. Обновить название города и географическое положение для одного из самых часто 
используемых аэропортов в топ-10. Вследствие ошибки системы.
UPDATE postgres_air.airport
SET city = 'Los santos', airport_tz = 'Random/Random'
WHERE postgres_air.airport.airport_code = 'ATL';
4. Вставить новую строку с информацией об аэропорте, которая был недавно открыт.
INSERT INTO postgres_air.airport (airport_code, airport_name, city, airport_tz, continent, iso_country, 
iso_region, intnl, update_ts)
VALUES ('AAB', 'New Airport', 'Los angeles', 'Random/Random', 'AA', 'AA', 'AA-AA', 'false', null);
5. Удалить информацию об аэропорте, который был закрыт.
DELETE FROM postgres_air.airport WHERE airport_code = 'XYZ';
SELECT from postgres_air.airport WHERE airport_code = 'XYZ';


* сценарий: 
авиакомпания продала слишком много билетов на один самолет, все пассажиры не влезли, нужно отправить пассажиров ближайшим рейсом и возместить убытки
1. сменить рейс у 3 человек кто не попал на свой рейс
2. удалить с рейса их
3. повысить уровень бонусной программы для этих пассажиров
4. вывести сводку по этим пассажирам (как было как стало)