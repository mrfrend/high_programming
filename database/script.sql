drop database if exists high_events;
create database if not exists high_events;
use high_events;

create table companies (
    id int primary key auto_increment,
    name varchar(255) not null,
	logo varchar(255),
	contribution_price decimal(10, 2) not null    
);

create table events (
    id int primary key auto_increment,
    company_id int not null,
    event_name varchar(255) not null,
    start_date date not null,
    end_date date not null,
    CONSTRAINT chk_dates CHECK (end_date >= start_date),
    foreign key (company_id) references companies(id) on delete cascade
);

create table services (
    id int primary key auto_increment,
    service_name varchar(255) not null,
    price decimal(10, 2) not null
);

create table event_services (
    id int primary key auto_increment,
    event_id int not null,
    service_id int not null,
    foreign key (event_id) references events(id) on delete cascade,
    foreign key (service_id) references services(id) on delete cascade
);

create table participants (
    id int primary key auto_increment,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    company_name varchar(255) not null,
    job_title varchar(255) not null
);

create table records (
    id int primary key auto_increment,
    participant_id int not null,
    event_id int not null,
    foreign key (participant_id) references participants(id) on delete cascade,
    foreign key (event_id) references events(id) on delete cascade,
    total decimal(10, 2) default 0
);

create table record_services (
    id int primary key auto_increment,
    record_id int not null,
    service_id int not null,
    foreign key (record_id) references records(id) on delete cascade,
    foreign key (service_id) references services(id) on delete cascade
);

INSERT INTO companies (name, logo, contribution_price) VALUES
('Postgres', 'postgres.png', 2500),
('1C', '1c.png', 1500),
('Astra Linux', 'astra.png', 2000),
('RED OS', 'redos.png', 1800),
('Alt Linux', 'alt.png', 1500),
('ClickHouse', 'clickhouse.png', 1500);


INSERT INTO events (company_id, event_name, start_date, end_date) VALUES
(1, 'Postgres Conf', '2025-06-01', '2025-06-03'),
(2, '1C Developer Day', '2025-06-05', '2025-06-06'),
(3, 'Astra Linux Security Summit', '2025-06-10', '2025-06-12'),
(4, 'RED OS Tech Forum', '2025-06-15', '2025-06-16'),
(5, 'Alt Linux Open Source Day', '2025-06-18', '2025-06-19'),
(6, 'Конференция "Анализ данных ClickHouse"', '2025-05-10', '2025-05-12');

INSERT INTO services (service_name, price) VALUES
('Проживание', 2000),
('Питание', 1200),
('VIP доступ', 3000),
('Стандартный пакет', 500);

INSERT INTO event_services (event_id, service_id) VALUES
(1,1),(1,2),(1,4),
(2,2),(2,4),
(3,1),(3,2),(3,3),
(4,2),(4,4),
(5,4),
(6,1),(6,2),(6,3);

INSERT INTO participants (first_name, last_name, company_name, job_title) VALUES
('Иван', 'Иванов', 'Astra Linux', 'Аналитик'),
('Петр', 'Петров', 'Postgres', 'Backend разработчик'),
('Анна', 'Сидорова', '1C', 'Системный аналитик');

INSERT INTO records (participant_id, event_id, total) VALUES
(1, 6, 4700), -- ClickHouse
(2, 1, 3700), -- Postgres
(3, 2, 1700); -- 1C

