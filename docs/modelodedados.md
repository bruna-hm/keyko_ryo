# Modelo de dados

## Visão geral
em desenvolvimento

## Tabela `alunos`
| Coluna | Tipo | Restrições | Descrição |
|--------|------|------------|-----------|
| id     | INTEGER | PRIMARY KEY AUTO INCREMENT | ... |
| nome   | TEXT    | obrigatório | ... |
| contato  | TEXT | ... | ... |
| ativo  | TEXT | ... | 1 = ativo, 0 = inativo |

## Tabela `aulas`
| Coluna | Tipo | Restrições | Descrição |
|--------|------|------------|-----------|
| id     | INTEGER | PRIMARY KEY AUTO INCREMET| ... |
| aluno_id   | INTEGER | FOREIGN KEY -> alunos| ... |
| data   | TEXT | PRIMARY KEY | formato YYYY-MM-DD |
| assunto   | TEXT | ... | ... |
| status    | TEXT | ... | realizada, agendada, cancelada e remarcada |

## Tabelas `aula_aluno`
| Coluna | Tipo | Restrições | Descrição |
|--------|------|------------|-----------|
| aula_id   | INTEGER | NOT NULL REFERENCES aulas(id) ON DELETE CASCADE | ... |
| aluno_id  | INTEGER | NOT NULL REFERENCES aulas(id) ON DELETE CASCADE | ... |

## Tabela `pagamentos`
| Coluna | Tipo | Restrições | Descrição |
|--------|------|------------|-----------|
| id     | INTEGER | PRIMARY KEY | ... |
| aluno_id  | INTEGER | FOREIGN KEY | ... |
| mes_referencia   | TEXT | ... | formato YYYY-MM |
| valor   | INTEGER | ... | dinheiro em centavos |
| data_pagamento   | TEXT | ... | formato YYYY-MM-DD |
| status   | TEXT | ... | pago, pendente |

## Convenções
- Dinheiro: inteiro em centavos
- Datas: YYYY-MM-DD ou YYYY-MM