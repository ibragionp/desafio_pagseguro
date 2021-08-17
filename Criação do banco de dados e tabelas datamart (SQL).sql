CREATE DATABASE analytic;

USE analytic;

CREATE TABLE dim_merchant_category(
	id_merchant VARCHAR(50),
	category VARCHAR(50),
	CONSTRAINT PK_DIM_MERCHANT PRIMARY KEY (id_merchant)
)


CREATE TABLE fact_customer_kpi(
	id_customer VARCHAR(30),
	data DATE,
	tpv FLOAT,
	qtd_transacoes INT,
	CONSTRAINT PK_FACT_CUSTOMER PRIMARY KEY (id_customer, data)
)


CREATE TABLE fact_merchant_kpi(
	id_merchant VARCHAR(50),
	data DATE,
	tpv FLOAT,
	qtd_transacoes INT,
	CONSTRAINT PK_FACT_MERCHANT PRIMARY KEY (id_merchant, data),
	CONSTRAINT FK_MERCHANT FOREIGN KEY (id_merchant) REFERENCES dim_merchant_category (id_merchant)
)