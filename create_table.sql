-- create import imed

CREATE TABLE export_employee
(
   id serial,
   employee_login character varying(255), 
   employee_password character varying(255),
   employee_active character varying(255), 
   employee_firstname character varying(255),
   employee_lastname character varying(255),
   employee_authentication_id character varying(255)
);

INSERT INTO public.export_employee (employee_login, employee_password, employee_active, employee_firstname, employee_lastname, employee_authentication_id) VALUES('admin', 'demo', 'admin', 'admin', '1', '1');
INSERT INTO public.export_employee (employee_login, employee_password, employee_active, employee_firstname, employee_lastname, employee_authentication_id) VALUES('test', 'test', 'ทดสอบ', 'ทดสอบ', '1', '2');


CREATE TABLE export_employee_authentication (
    employee_authentication_id character varying(255) NOT NULL,
    employee_authentication_description character varying(255)
);
INSERT INTO public.export_employee_authentication (employee_authentication_id, employee_authentication_description) VALUES('1', 'ผู้ดูแลระบบ');
INSERT INTO public.export_employee_authentication (employee_authentication_id, employee_authentication_description) VALUES('2', 'ผู้ใช้งานทั่วไป');