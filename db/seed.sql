INSERT INTO hospitals(id, name, location_region, capacity, supervisor_id) VALUES
    (1, 'hospital 1', 'LA', 50, 10),
    (2, 'hospital 2', 'SG', 50, 20),
    (3, 'hospital 3', 'COM', 50, 30),
    (4, 'hospital 4', 'ELM', 50, 40);

INSERT INTO workers(id, name, hospital_id) VALUES
    (10, 'Susan',1),
    (11, 'Leon',1),
    (20, 'Barry',2),
    (21, 'Chloe',2),
    (30, 'Serine',3),
    (31, 'Grace',3),
    (40, 'Billy',4),
    (41, 'James',4),
    (90, 'Cyntia',1);    

INSERT INTO equipments(id, serial_number, model, status, charge_level, hospital_id, worker_id) VALUES
    (11, 89454, 'chaseatm', 'Operational', 19, 1, 11),
    (12, 89455, 'chaseatm', 'Operational', 100, 1, 21),
    (21, 22222, 'wellsatm', 'Operational', 50, 2, 21),
    (22, 22223, 'wellsatm', 'Operational', 15, 2, 21),
    (31, 3331, 'americaatm', 'Maintenance',100, 3, 31),
    (32, 3332, 'americaatm', 'Offline', 0, 3, 31),
    (41, 4441, 'eastatm', 'Operational', 19, 4, 41); 


INSERT INTO work_orders(id, title, priority, status, equipment_id, worker_id) VALUES
     (1, ' sensor not working','Critical', 'In-Progress', 31, 31),
     (2, ' sensor not working','Critical', 'In-Progress', 32, 31);


SELECT setval('hospitals_id_seq', (SELECT MAX(id) FROM hospitals));
SELECT setval('workers_id_seq', (SELECT MAX(id) FROM workers));
SELECT setval('equipments_id_seq', (SELECT MAX(id) FROM equipments));
SELECT setval('work_orders_id_seq', (SELECT MAX(id) FROM work_orders));