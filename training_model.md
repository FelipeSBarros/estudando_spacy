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

Contudo, antes de começar a treinar o modelo é necessário definir tais configurações.

### Configurações

Para facilitar a definição de tais arquivos de configurações, existe o [quick start](https://spacy.io/usage/training#quickstart), e também o [init config](https://spacy.io/api/cli#init-config).

`init config`
> Initialize and save a config.cfg file using the recommended settings for your use case. It works just like the quickstart widget, only that it also auto-fills all default values and exports a training-ready config.

:1st_place_medal: `quick start`
> This quickstart widget helps you generate a starter config with the recommended settings for your specific use case. It’s also available in spaCy as the init config command.

O `quick start` demanda que as configurações [pré-definidas](https://spacy.io/usage/training#quickstart) sejam salvar num arquivo [`base_config.cfg`](./base_config.cfg) para então serem usadas no `init config`, com o parâmetro `fill-config`. ao usar o *quick start*, garantiomos que as configurações de treinamento estejam completas e sem *hidden defaults*, garantindo a reproducibilidade do experimento.

```python
python -m spacy init fill-config base_config.cfg config.cfg
```
>✔ Auto-filled config with all values  
✔ Saved config config.cfg  
You can now add your data and train your pipeline:
`python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./dev.spacy`

A configuração das `paths` podem estar definidas no `config.cfg`.  

> Some of the main advantages and features of spaCy’s training config are:
> * **Structured sections.** The config is grouped into sections, and nested sections are defined using the . notation. For example, [components.ner] defines the settings for the pipeline’s named entity recognizer. The config can be loaded as a Python dict.
> * **References to registered functions.** Sections can refer to registered functions like model architectures, optimizers or schedules and define arguments that are passed into them. You can also register your own functions to define custom architectures or methods, reference them in your config and tweak their parameters.
> * **Interpolation.** If you have hyperparameters or other settings used by multiple components, define them once and reference them as variables.
> * **Reproducibility with no hidden defaults.** The config file is the “single source of truth” and includes all settings.
> * **Automated checks and validation.** When you load a config, spaCy checks if the settings are complete and if all values have the correct types. This lets you catch potential mistakes early. In your custom architectures, you can use Python type hints to tell the config which types of data to expect.

> Under the hood, the config is parsed into a dictionary. It’s divided into sections and subsections, indicated by the square brackets and dot notation. For example, [training] is a section and [training.batch_size] a subsection. Subsections can define values, just like a dictionary, or use the @ syntax to refer to registered functions. This allows the config to not just define static settings, but also construct objects like architectures, schedules, optimizers or any other custom components.

### [Dados de treinamento](https://spacy.io/usage/training#training-data)

O spaCy já disponibiliza um comando ([`spacy convert`](https://spacy.io/api/cli#convert)) para converter os dados de treinamento ao formato binário (`.spacy`) requerido pelo sistema. O conversor pode ser definido na linha de comando ou [escolhido dentre as opções predefinidas](https://spacy.io/api/cli#converters) a partir da extensão do arquivo de entrada.
