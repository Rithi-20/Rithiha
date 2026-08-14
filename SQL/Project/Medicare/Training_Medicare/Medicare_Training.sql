CREATE DATABASE Medicare_Training;
USE Medicare_Training;

CREATE TABLE Hospitals (
    hospital_id VARCHAR(50),
    hospital_name VARCHAR(50),
    hospital_type VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    region VARCHAR(50),
    bed_capacity VARCHAR(50),
    established_year VARCHAR(50),
    contact_number VARCHAR(50),
    email VARCHAR(50),

    CONSTRAINT pk_hospitals PRIMARY KEY (hospital_id)
);

CREATE TABLE Departments (
    department_id VARCHAR(50),
    department_name VARCHAR(50),
    hospital_id VARCHAR(50),
    floor_number VARCHAR(50),
    head_doctor_id VARCHAR(50),

    CONSTRAINT pk_departments PRIMARY KEY (department_id)
);

CREATE TABLE Doctors (
    doctor_id VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(50),
    specialization VARCHAR(50),
    department_id VARCHAR(50),
    hospital_id VARCHAR(50),
    qualification VARCHAR(50),
    experience_years VARCHAR(50),
    consultation_fee VARCHAR(50),
    phone_number VARCHAR(50),
    email VARCHAR(50),
    joining_date VARCHAR(50),

    CONSTRAINT pk_doctors PRIMARY KEY (doctor_id)
);

CREATE TABLE Patients (
    patient_id VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(50),
    date_of_birth VARCHAR(50),
    age VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    phone_number VARCHAR(50),
    email VARCHAR(50),
    blood_group VARCHAR(50),
    registration_date VARCHAR(50),

    CONSTRAINT pk_patients PRIMARY KEY (patient_id)
);

CREATE TABLE Rooms (
    room_id VARCHAR(50),
    hospital_id VARCHAR(50),
    room_number VARCHAR(50),
    room_type VARCHAR(50),
    floor_number VARCHAR(50),
    daily_charge VARCHAR(50),
    room_status VARCHAR(50),

    CONSTRAINT pk_rooms PRIMARY KEY (room_id)
);

CREATE TABLE Appointments (
    appointment_id VARCHAR(50),
    patient_id VARCHAR(50),
    doctor_id VARCHAR(50),
    hospital_id VARCHAR(50),
    appointment_date VARCHAR(50),
    appointment_time VARCHAR(50),
    status VARCHAR(50),
    reason_for_visit VARCHAR(50),
    created_at VARCHAR(50),

    CONSTRAINT pk_appointments PRIMARY KEY (appointment_id)
);

CREATE TABLE Admissions (
    admission_id VARCHAR(50),
    patient_id VARCHAR(50),
    hospital_id VARCHAR(50),
    department_id VARCHAR(50),
    admitting_doctor_id VARCHAR(50),
    room_id VARCHAR(50),
    admission_date VARCHAR(50),
    discharge_date VARCHAR(50),
    admission_type VARCHAR(50),
    admission_status VARCHAR(50),

    CONSTRAINT pk_admissions PRIMARY KEY (admission_id)
);

CREATE TABLE Treatments (
    treatment_id VARCHAR(50),
    admission_id VARCHAR(50),
    patient_id VARCHAR(50),
    doctor_id VARCHAR(50),
    treatment_name VARCHAR(50),
    treatment_date VARCHAR(50),
    treatment_cost VARCHAR(50),
    treatment_status VARCHAR(50),

    CONSTRAINT pk_treatments PRIMARY KEY (treatment_id)
);

CREATE TABLE Insurance (
    insurance_id VARCHAR(50),
    patient_id VARCHAR(50),
    insurance_provider VARCHAR(50),
    policy_number VARCHAR(50),
    coverage_amount VARCHAR(50),
    policy_start_date VARCHAR(50),
    policy_end_date VARCHAR(50),
    claim_status VARCHAR(50),

    CONSTRAINT pk_insurance PRIMARY KEY (insurance_id)
);

CREATE TABLE Medicines (
    medicine_id VARCHAR(50),
    medicine_name VARCHAR(50),
    category VARCHAR(50),
    manufacturer VARCHAR(50),
    unit_price VARCHAR(50),
    stock_quantity VARCHAR(50),

    CONSTRAINT pk_medicines PRIMARY KEY (medicine_id)
);

CREATE TABLE Pharmacy (
    pharmacy_sale_id VARCHAR(50),
    patient_id VARCHAR(50),
    medicine_id VARCHAR(50),
    hospital_id VARCHAR(50),
    quantity VARCHAR(50),
    sale_date VARCHAR(50),
    total_price VARCHAR(50),

    CONSTRAINT pk_pharmacy PRIMARY KEY (pharmacy_sale_id)
);

CREATE TABLE Laboratory (
    lab_test_id VARCHAR(50),
    patient_id VARCHAR(50),
    doctor_id VARCHAR(50),
    hospital_id VARCHAR(50),
    test_name VARCHAR(50),
    test_date VARCHAR(50),
    test_result VARCHAR(50),
    test_cost VARCHAR(50),
    test_status VARCHAR(50),

    CONSTRAINT pk_laboratory PRIMARY KEY (lab_test_id)
);

CREATE TABLE Employees (
    employee_id VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(50),
    hospital_id VARCHAR(50),
    department_id VARCHAR(50),
    designation VARCHAR(50),
    employment_type VARCHAR(50),
    salary VARCHAR(50),
    joining_date VARCHAR(50),
    phone_number VARCHAR(50),
    email VARCHAR(50),

    CONSTRAINT pk_employees PRIMARY KEY (employee_id)
);

CREATE TABLE Billing (
    bill_id VARCHAR(50),
    patient_id VARCHAR(50),
    admission_id VARCHAR(50),
    appointment_id VARCHAR(50),
    bill_date VARCHAR(50),
    room_charges VARCHAR(50),
    doctor_charges VARCHAR(50),
    medicine_charges VARCHAR(50),
    lab_charges VARCHAR(50),
    other_charges VARCHAR(50),
    total_amount VARCHAR(50),
    bill_status VARCHAR(50),

    CONSTRAINT pk_billing PRIMARY KEY (bill_id)
);

CREATE TABLE Payments (
    payment_id VARCHAR(50),
    bill_id VARCHAR(50),
    patient_id VARCHAR(50),
    payment_date VARCHAR(50),
    payment_amount VARCHAR(50),
    payment_mode VARCHAR(50),
    payment_status VARCHAR(50),

    CONSTRAINT pk_payments PRIMARY KEY (payment_id)
);

"""Select Cleaned_gender FROM (
Select 
CASE 
WHEN LOWER(TRIM(gender)) IN ('male','m')
THEN 'Male'
WHEN LOWER(TRIM(gender)) IN ('female','f')
THEN 'Female'
ELSE gender
END AS Cleaned_gender
FROM Doctors
) AS D; """