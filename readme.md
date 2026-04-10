# 📊 Análise de Tratativas Logísticas

## 🎯 Objetivo

Este projeto simula a análise de erros operacionais em um fluxo logístico, com foco em identificar padrões de falhas e tempo de resolução.

---

## 📦 Contexto

Baseado em processos reais de logística, como:

* Avarias
* Duplicidade de pedidos
* Problemas de etiquetagem
* Fluxo de devoluções (returns)

---

## 🗂 Estrutura dos Dados

Tabela: `tratativas`

| Coluna          | Descrição                      |
| --------------- | ------------------------------ |
| pacote_id       | Identificador do pacote        |
| tipo_erro       | Tipo de erro ocorrido          |
| tempo_tratativa | Tempo para resolução (minutos) |

---

## 🔍 Perguntas de Negócio

* Qual tipo de erro ocorre com mais frequência?
* Qual erro demora mais para ser resolvido?
* Existe padrão de ineficiência operacional?

---

## 🛠 Tecnologias Utilizadas

* SQLite
* SQL
* Git & GitHub

---

## 📈 Exemplo de Análise

```sql
SELECT tipo_erro, AVG(tempo_tratativa) AS tempo_medio
FROM tratativas
GROUP BY tipo_erro;
```

---

## 🚀 Próximos Passos

* Adicionar mais dados simulados
* Criar análises mais complexas (JOIN, filtros)
* Evoluir para Python e automação

---

## 📌 Autor

Joh
