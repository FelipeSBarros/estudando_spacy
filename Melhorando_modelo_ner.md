# 

Para melhorar o modelo `pt_core_news_lg`, utilizou-se o `quick start` para gerar o [`base_config`](base_config.cfg).

```
mkdir ner_from_scratch && cd ner_from_scratch
python -m spacy init fill-config base_config.cfg config.cfg
```

>✔ Auto-filled config with all values  
> ✔ Saved config config.cfg  
> You can now add your data and train your pipeline:
`python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./dev.spacy`
