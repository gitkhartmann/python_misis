create database air2;

create table departure
(
    airline   text,
    time_from timestamp,
    time_to   timestamp
);

copy departure from '/Users/sergo/Desktop/new.csv' delimiter ',' csv header;

select *
from departure;

select *
from departure
where airline = 'АЭРОФЛОТ';

select *
from departure
where airline != 'АЭРОФЛОТ';

copy departure to '/Users/sergo/Desktop/new2.csv' delimiter ',' csv header;

truncate departure;

copy departure from '/Users/sergo/Desktop/new.csv' delimiter ',' csv header;


update departure
set airline = 'АЭРОЛОТ2'
where airline = 'АЭРОФЛОТ';


select *
from departure;

delete
from departure
where airline = 'С СЕВЕН';

select *
from departure;