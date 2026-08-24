CREATE DATABASE SQL_LMS_Practice;
USE SQL_LMS_Practice;


CREATE TABLE Clinics(
clinic_id varchar(6) not null,
clinic_name varchar(50) not null,
clinic_type varchar(50) not null,
city varchar(50) not null,
state varchar(50) not null,
established_year int not null,
contact_number varchar(15) not null,

CONSTRAINT pk_clinic_id PRIMARY KEY(clinic_id)

);

INSERT INTO `Clinics` (`clinic_id`, `clinic_name`, `clinic_type`, `city`, `state`, `established_year`, `contact_number`) VALUES
('C001', 'HealthPlus Diagnostic Clinic - Kozhikode', 'Diagnostic', 'Kozhikode', 'Kerala', 2018, 8039233214),
('C002', 'HealthPlus Wellness Clinic - Kozhikode', 'Wellness', 'Kozhikode', 'Kerala', 2020, 8081973699),
('C003', 'HealthPlus Telemedicine Hub Clinic - Hyderabad', 'Telemedicine Hub', 'Hyderabad', 'Telangana', 2017, 8063272951),
('C004', 'HealthPlus Primary Care Clinic - Delhi', 'Primary Care', 'Delhi', 'Delhi', 2022, 8017560480),
('C005', 'HealthPlus Diagnostic Clinic - Pune', 'Diagnostic', 'Pune', 'Maharashtra', 2015, 8058178397),
('C006', 'HealthPlus Wellness Clinic - Coimbatore', 'Wellness', 'Coimbatore', 'Tamil Nadu', 2017, 8023279282),
('C007', 'HealthPlus Telemedicine Hub Clinic - Coimbatore', 'Telemedicine Hub', 'Coimbatore', 'Tamil Nadu', 2013, 8002761612),
('C008', 'HealthPlus Primary Care Clinic - Vijayawada', 'Primary Care', 'Vijayawada', 'Andhra Pradesh', 2021, 8006528630),
('C009', 'HealthPlus Diagnostic Clinic - Hyderabad', 'Diagnostic', 'Hyderabad', 'Telangana', 2019, 8048625702),
('C010', 'HealthPlus Wellness Clinic - Mysuru', 'Wellness', 'Mysuru', 'Karnataka', 2021, 8061112422),
('C011', 'HealthPlus Telemedicine Hub Clinic - Pune', 'Telemedicine Hub', 'Pune', 'Maharashtra', 2014, 8038573415),
('C012', 'HealthPlus Primary Care Clinic - Mangaluru', 'Primary Care', 'Mangaluru', 'Karnataka', 2022, 8018409053),
('C013', 'HealthPlus Diagnostic Clinic - Kozhikode', 'Diagnostic', 'Kozhikode', 'Kerala', 2018, 8056665812),
('C014', 'HealthPlus Wellness Clinic - Coimbatore', 'Wellness', 'Coimbatore', 'Tamil Nadu', 2017, 8067343415),
('C015', 'HealthPlus Telemedicine Hub Clinic - Hyderabad', 'Telemedicine Hub', 'Hyderabad', 'Telangana', 2023, 8036471764),
('C016', 'HealthPlus Primary Care Clinic - Madurai', 'Primary Care', 'Madurai', 'Tamil Nadu', 2020, 8045782464),
('C017', 'HealthPlus Diagnostic Clinic - Pune', 'Diagnostic', 'Pune', 'Maharashtra', 2022, 8092469973),
('C018', 'HealthPlus Wellness Clinic - Kozhikode', 'Wellness', 'Kozhikode', 'Kerala', 2017, 8035054324);

# Limit 
SELECT * from Clinics limit 5 offset 10; # this is helpful for pagination

# DISTINCT 	- displays only the unique values
SELECT DISTINCT clinic_name from Clinics;
# Multiple distict 
SELECT DISTINCT clinic_name,city from Clinics;

# order by - sort the data
SELECT * FROM Clinics
ORDER BY established_year DESC; 

# orderby using multiple columns
SELECT * FROM Clinics
ORDER BY established_year DESC, clinic_id ASC; # here yr will be sorted first then within that yr clinic_id will be sorted

# group by and having
SELECT established_year, COUNT(*)  # Aggregate functions includes sum.avg,min,max 
from clinics
group by established_year
having count(*) >1;

# SET OPERATORS         SET OPERATIONS-SELECT
# 1. UNION
# 2. INTERSECT
# 3. EXCEPT

# Union - this combines two select statement and remove duplicates 
SELECT clinic_id FROM Clinics 
UNION
SELECT established_year from Clinics; # we also use where condition

# union all - same syntax , combine both select statment but keep duplicates


# CONDITION FOR UNION 
# the columns selected in both queries should be same in number

# INTERSECT same synatx of union , it will retrun thecommon rows in both queries.
# Intersect is binary so can only compare with two select statementts only


# EXCEPT -WE dont haeve except keyword instaed we use not in . this will return rows exist in first query but not the second query 
# eg A=(1,2,3) B=(3,4,5)  -> res: (1,2)
# eg for except :  select * from order_details where customer_id not in (select customer_name from customer where city = "Sydney");
# UNION,UNION ALL,EXCEPT - we can use this with multiple select statement and even we can mis everything and work

use Medicare;

# Show doctors in Cardiology, Neurology or Orthopedics
Select first_name,specialization from Doctors 
where specialization in ('Cardiology', 'Neurology','Orthopedics');

# Find hospital names containing 'Care'
SELECT hospital_name
FROM Hospitals
WHERE hospital_name LIKE '%Care%';

# or

Select hospital_name from Hospitals 
where 
contains(hospital_name,'Care');

# between
select * from Employees where experience_years between 5 and 10;
select * from Employees where experience_years not between 5 and 10;
select * from Employees where experience_years between 'A' and 'P';

# subqueries in
select * from order_details where customer_id in (select customer_name from customer where city = "Sydney");

# not in
select * from order_details where customer_id not in('c0001','c002');


# Note:
#1. Aggregate functions ignore null values by default, i null values needs to be included use IFNULL() OR COALESCE() function to replace null values with default values.
# IFNULL - Check for null values and replace with 0 
# COALESCE() - Check for null values and replace but it can replace multiple values  
#MODIFY in alter table is used to change datatype of existing column

# Transaction
# A sequence of one or more SQL Statements that are executed as a single unit of work.

#Qualifiers:
# It is used to specify the origin of column
#Two types: Table Qualifier , Database qualifier
# Table qualifier : eg SELECT Employee.employee_id . It is used when it involves multiple tables.
# Database qualifier : eg database1.Employee.employee_id . It is used when same table name exist in multiple data base

