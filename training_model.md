# [Training Pipelines & Models](https://spacy.io/usage/training)

>spaCy’s tagger, parser, text categorizer and many other components are powered by statistical models. ... -> prediction

Essa predição é baseada nos pesos atribuidos no modelo. Por sua vez, tais pesos são estimados a partir de exemplos observados pelo modelo no processzo de treinamento do mesmo.

> Training is an iterative process in which the model’s predictions are compared against the reference annotations in order to estimate the gradient of the loss.

O gradiente de perda é usado para calcular o gradiente de pesos a partir de ["Baclpropagation"](https://thinc.ai/docs/backprop101). Este último gradiente indica como o peso deve mudar para que as prições sejam mais próximas (similares) às etiquetas de referência através do tempo.

![img_1.png](img/img_1.png)

> When training a model, we don’t just want it to memorize our examples – we want it to come up with a theory that can be generalized across unseen data. 

Não queremos que o modelo "memorize" que "Amazon" representa sempre uma empresa, mas que "Amazon" em determinados contextos, sim representa a empresa.

> :warining: That’s why the training data should always be representative of the data we want to process.

Além de ter o modelo criado, é necessário pode avaliar a "performance" do modelo, a sua acurácia. Por isso, além dos dados de treinamento, são necessários dados de avaliação (teste)

## Mão na massa: dados de treinamento

O [`spaCy`](https://spacy.io/) possui um comando para processar e executar o fluxo de trabalho de treinamento de uma modelo: [`spacy train`](https://spacy.io/api/cli#train). O mesmo depende de um [`config.cfg`](https://spacy.io/usage/training#config) com toda as informações de configurações/hiperparâmetros, e [os dados de treinamento num formato binário](https://spacy.io/api/data-formats#training).

Contudo, antes de começar a treinar o modelo é necessário definir tais configurações e para facilitar, existe o [quick start](https://spacy.io/usage/training#quickstart), e também o [init config](https://spacy.io/api/cli#init-config).

`init config`
> Initialize and save a config.cfg file using the recommended settings for your use case. It works just like the quickstart widget, only that it also auto-fills all default values and exports a training-ready config.

`quick start`
> This quickstart widget helps you generate a starter config with the recommended settings for your specific use case. It’s also available in spaCy as the init config command.
