-- Criar ID único incremental para cada transação
ALTER TABLE transactions ADD id BIGINT IDENTITY(1,1);

-- Em Age alterar valores 'U' para NULL antes de converter coluna para inteiro
UPDATE transactions
SET age = NULL
WHERE age = 'U';

-- Transformar coluna Age em inteiro
ALTER TABLE transactions
ALTER COLUMN age INT;

-- Deixar coluna Gender apenas com M e F (Feminino)
UPDATE transactions
SET gender = 'F'
WHERE TRIM(gender) LIKE 'Feminino' COLLATE SQL_Latin1_General_CP1_CI_AS;

-- Deixar coluna Gender apenas com M e F (Masculino)
UPDATE transactions
SET gender = 'M'
WHERE TRIM(gender) LIKE 'Masculino' COLLATE SQL_Latin1_General_CP1_CI_AS;

-- Em Gender alterar valores 'U' e 'E' para NULL
UPDATE transactions
SET gender = NULL
WHERE gender = 'U' OR gender = 'E';

-- Deixar NULL onde coluna Amount for zero
UPDATE transactions
SET amount = NULL
WHERE amount = 0;

-- Criar coluna mês
ALTER TABLE transactions ADD month INT;

-- Popular coluna mês com base na coluna step
UPDATE transactions
SET month = (CASE WHEN step BETWEEN 0 AND 30 Then 1
				  WHEN step BETWEEN 31 AND 60 Then 2
				  WHEN step BETWEEN 61 AND 90 Then 3
				  WHEN step BETWEEN 91 AND 120 Then 4
				  WHEN step BETWEEN 121 AND 150 Then 5
				  WHEN step BETWEEN 151 AND 180 Then 6
			END)

-- Criar coluna ano: 2021
ALTER TABLE transactions 
ADD year INT NULL
CONSTRAINT default_year_2021 DEFAULT 2021
WITH VALUES

-- Criar coluna data: sempre dia 1
ALTER TABLE transactions ADD fullDate Date;

UPDATE transactions
SET fullDate = DATEFROMPARTS (year, month, 1)





