SELECT tipo_erro, AVG(tempo_tratativa)
FROM tratativas
GROUP BY tipo_erro;