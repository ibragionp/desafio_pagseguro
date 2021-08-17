SELECT merchant AS id_merchant, fullDate AS data, CAST(SUM(amount) AS DECIMAL(18,2))  AS tpv, COUNT(DISTINCT id) AS qtd_transacoes
FROM transactions
GROUP BY fullDate, merchant