--задание 1 

-- Сценарий 1: Обновление информации об аэропорте
1. Выберите конкретный аэропорт, для которого вы хотите обновить информацию.
2. В таблице "airport" найдите соответствующую запись по идентификатору аэропорта.

SELECT *
FROM postgres_air.airport
WHERE airport_code = 'ACC'

3. Внесите изменения в информацию об аэропорте, например, измените название или город.

UPDATE postgres_air.airport
SET city = 'chelyabinsk',
    airport_code = 'SUS'
WHERE airport_name = 'SUSU'


*. Исправление ошибки
ERROR: ОШИБКА:  UPDATE или DELETE в таблице "airport" нарушает ограничение внешнего ключа "departure_airport_fk" таблицы "flight"
DETAIL:  На ключ (airport_code)=(ACC) всё ещё есть ссылки в таблице "flight".

ALTER TABLE postgres_air.flight
DROP CONSTRAINT IF EXISTS departure_airport_fk,
ADD CONSTRAINT departure_airport_fk
    FOREIGN KEY (departure_airport)
    REFERENCES postgres_air.airport (airport_code)
    ON UPDATE CASCADE
    ON DELETE CASCADE;
   
4. Убедитесь, что изменения автоматически применяются ко всем связанным таблицам, например, в таблицe "flight", где используется внешний ключ на аэропорт.

SELECT *
FROM postgres_air.flight
WHERE flight.departure_airport = 'SUS' OR flight.arrival_airport = 'SUS'


--Сценарий 2: Удаление записи о пассажире
1. Выберите конкретного пассажира, запись о котором вы хотите удалить.

SELECT * FROM postgres_air.booking
ORDER BY booking_id ASC --мы здесь выбираем просто passenger_id

2. В таблице "passenger" найдите соответствующую запись по идентификатору пассажира.

SELECT *
FROM postgres_air.passenger
WHERE passenger_id = '10'

3. Удалите запись о пассажире из таблицы "passenger".

DELETE FROM postgres_air.passenger
WHERE passenger_id = 10;

*. Исправление ошибки
ERROR: ОШИБКА:  UPDATE или DELETE в таблице "passenger" нарушает ограничение внешнего ключа "passenger_id_fk" таблицы "boarding_pass"
DETAIL:  На ключ (passenger_id)=(10) всё ещё есть ссылки в таблице "boarding_pass".

ALTER TABLE postgres_air.boarding_pass
DROP CONSTRAINT IF EXISTS passenger_id_fk,
ADD CONSTRAINT passenger_id_fk
    FOREIGN KEY (passenger_id)
    REFERENCES postgres_air.passenger (passenger_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

4. Убедитесь, что связанные записи в других таблицах, например, в таблицах  "boarding_pass", также автоматически удаляются благодаря каскадному удалению по внешнему ключу.

SELECT *
FROM postgres_air.boarding_pass
WHERE boarding_pass.passenger_id = '10'



--Сценарий 3: Изменение информации об бронировании
1. В таблице "booking" найдите соответствующую запись по "booking_id"

SELECT *
FROM postgres_air.booking

2. отобразить данные

SELECT *
FROM postgres_air.booking
WHERE booking_ref = '1FYA12'

2. Измените информацию об бронировании

UPDATE postgres_air.booking
SET email = 'ascdedcewcdecwdc@mail.ru',
    booking_id = '10'
WHERE booking_ref = '1FYA12'

*. Исправление ошибки
ERROR: ОШИБКА:  UPDATE или DELETE в таблице "booking" нарушает ограничение внешнего ключа "booking_id_fk" таблицы "booking_leg"
DETAIL:  На ключ (booking_id)=(10) всё ещё есть ссылки в таблице "booking_leg". 

ALTER TABLE postgres_air.booking_leg
DROP CONSTRAINT IF EXISTS booking_id_fk,
ADD CONSTRAINT booking_id_fk
    FOREIGN KEY (booking_id)
    REFERENCES postgres_air.booking (booking_id)
    ON UPDATE CASCADE;

*. Исправление ошибки
ERROR: ОШИБКА:  UPDATE или DELETE в таблице "booking" нарушает ограничение внешнего ключа "pass_booking_id_fk" таблицы "passenger"
DETAIL:  На ключ (booking_id)=(10) всё ещё есть ссылки в таблице "passenger".

ALTER TABLE postgres_air.passenger
DROP CONSTRAINT IF EXISTS pass_booking_id_fk,
ADD CONSTRAINT pass_booking_id_fk
    FOREIGN KEY (booking_id)
    REFERENCES postgres_air.booking (booking_id)
    ON UPDATE CASCADE;

4. Убедитесь, что изменения автоматически применяются ко всем связанным таблицам, например, в таблицах "passenger" и "booking_leg", где используется внешний ключ на рейс.

SELECT *
FROM postgres_air.passenger
WHERE passenger.booking_id = '0' 

SELECT *
FROM postgres_air.booking_leg
WHERE booking_leg.booking_id = '0' 







--здание 2

Сценарий 1: Фильтрация по столбцу last_name в таблице account
-- До добавления индекса
EXPLAIN SELECT * FROM postgres_air.account WHERE last_name = 'Smith';
-- После добавления индекса
CREATE INDEX idx_account_last_name ON postgres_air.account(last_name);
EXPLAIN SELECT * FROM postgres_air.account WHERE last_name = 'Smith';
-- Удаление индекса
DROP INDEX postgres_air.idx_account_last_name;


Сценарий 2: Соединение таблицы account и frequent_flyer
EXPLAIN (ANALYZE TRUE) SELECT postgres_air.account.first_name, postgres_air.account.last_name, 	postgres_air.account.login, postgres_air.account.frequent_flyer_id,
 	postgres_air.frequent_flyer.card_num, postgres_air.frequent_flyer.level
 	FROM postgres_air.account
 	JOIN postgres_air.frequent_flyer
 	ON postgres_air.account.first_name = 'RYAN' AND
 	postgres_air.frequent_flyer.level = 2;
	
--CREATE INDEX index_2_1 ON postgres_air.account (first_name);
--CREATE INDEX index_2_2 ON postgres_air.frequent_flyer (level);

--DROP INDEX postgres_air.index_2_1;
--DROP INDEX postgres_air.index_2_2;


Сценарий 3: Фильтрация по столбцу flight_no в таблице flight с использованием JOIN
-- До добавления индекса
EXPLAIN SELECT * FROM flight f JOIN postgres_air.booking_leg bl ON f.flight_id = bl.flight_id WHERE f.flight_no = 'ABC123';
-- После добавления индекса
CREATE INDEX idx_flight_flight_no ON postgres_air.flight(flight_no);
EXPLAIN SELECT * FROM flight f JOIN postgres_air.booking_leg bl ON f.flight_id = bl.flight_id WHERE f.flight_no = 'ABC123';
-- Удаление индексов
DROP INDEX postgres_airidx_flight_flight_no;








--задание 3
--даем права
CREATE USER read_only_user WITH PASSWORD '1234';
GRANT CONNECT ON DATABASE airlines_new TO read_only_user;
GRANT USAGE ON SCHEMA postgres_air TO read_only_user;
GRANT SELECT ON ALL TABLES IN SCHEMA postgres_air TO read_only_user;
--проверяем доступ
SELECT * FROM postgres_air.aircraft WHERE code = 'NEW_aircraft';
UPDATE postgres_air.aircraft SET velocity = 1210 WHERE CODE = 'NEW_aircraft';