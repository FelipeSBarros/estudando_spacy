# Passos para organização dos assets

O [*asset* de participantes](./assets/schedule_random_participants_1000.json) foram baixados em formato JSON usando a *query*:

```sql
select participants 
    from "agenda-transparente".schedule
     where participants is not null
      order by random() limit 1000;
```

O JSON é, então, transformado em JSON lines, usando o [script participants_data_organization.py](./participants_data_organization.py), gerando o [schedule_random_participants_1000.jsonl](./assets/schedule_random_participants_1000.jsonl).

A cada entrada, foi usado o [modelo pt-br]() para extrair as entdades, labels, inicio e fim do span e salva-la como [schedule_participants_100_train](./assets/schedule_participants_100_train.json). 
O objetivo é melhorar o identificação de NE, adicionando novas classes, corrigindo e incluindo aquelas que não foram identificadas corretamente.
