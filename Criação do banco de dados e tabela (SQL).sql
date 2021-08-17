CREATE DATABASE db;

USE db;

CREATE TABLE transactions(
	step int,
	customer varchar(30),
	age varchar(3),
	gender varchar(30),
	zipcodeOri varchar(30),
	merchant varchar(50),
	zipMerchant varchar(30),
	category varchar(50),
	amount float,
	fraud int
);