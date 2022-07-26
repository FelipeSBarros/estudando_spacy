# Criadndo um modelo de Relation Extraction

O processo de `Relation Extraction (RE)` é, em geral, a tarefa desenvolvida posterior `extração de entidades nomeadas de um texto, o qual irá classificar o tipo de relação entre as antidades nomeadas encontradas. Para isso, treina-se um modelo específico, como veremos a seguir.

![img.png](./img/img_re_1.png)

## Intro

Este projeto foi criado usando como template o projeto [NER-RE](https://github.com/AdirthaBorgohain/NER-RE) que, por sua vez, está baseado no [tutorial](https://www.youtube.com/watch?v=8HL-Ap5_Axo) da explosion sobre `Relation Extraction` component.

Este tipo de componente (RE) demanda, necessáriamente, a criação de um modelo (ou uma layer a ser usada numa rede neural). No caso do projeto usado como template e no tutorial, implementa-se o modelo usando o [thinc.ai](https://thinc.ai/). Contudo o mesmo poderia ser implementado usando modelos do [pytorch](https://pytorch.org/) ou [tensorflow](https://www.tensorflow.org/).

Usando o `thinc`, será implementada uma camada com *foward function* ([`instance_foward`](./RE/scripts/rel_model.py#L59)) e *backpropagation* ([implementado na mesma função do *foward function*](./RE/scripts/rel_model.py#L83)). Ao implementar com `thinc`, ganha-se em transparência e flexibilidade.

No *foward function* o texto será tokenizado e será processado até a sua redução em duas dimensões de vetores de entidade (tanto i->j como j->i). Dita função retorna uma matriz com um "tensor" para cada candidato por linha, assim como um callback de [`backpropagation`](./RE/scripts/rel_model.py#L83).

A implementação da função `get_instance` depende do caso de uso:
- Pode ser uma função que emparelha duas entidades em um texto (doc) desde que as entidades estejam a uma distância máxima (`max_length`) entre elas;
- Pode-se definir um conjunto de relações candidatas possíveis entre duas entidades que co-ocorrem na mesma frase. 

## Config.cfg

É no [`config.cfg`](./config.cfg) que devemos declarar as varíaveis e hiperparâmetros do modelo. As funções/modelos criados/declarados antes são indicadas para serem instancadas.

O primeiro ponto é o `NLP`. Dentre vários parâmetros de configuração, a `pipeline` é um a ser considerado. No exemplo, não adicionam o processo de NER antes do RE, por simplicidades e estarem considerando um padrão basico de entidades. Mas deixam claro no vídeo a importância em adicionar o processo de NER à pipeline para cenários realistas.

Para cada `component`, uma `factory` deverá ser informada para a criação da componente e a ela, uma modelo será configurado, com seus parâmetros passados pelo bloco em questão, evitando parâmtros escondidos. Aumentando transparência e reprodutibilidade. 

Em casos de `factory` customizadas, a `@architecture` informada é a função criada anteriormente (`foward function` e `backpropagation`) e suas sublayers (`tok2vec`, `pooling`).

`custom factory>model arquitecture>sublayers`

### initialize


`Exemple` é um objeto do spacy 3, e armazena tanto um docuemnto com as prediões como um documento chamado `reference` que possui as `annotations`.

A função `update` criado, primeiramente as predições com o modelo atual e, então, compara com a `gold=standard` dadta para calcular a perda, ajustar o modelo pelo `backpropagation`.

Com o modelo treinado o `predict` model irá... produzir as predições, delegando ao modelo de aprendizado de máquina e retornando os escores preditos. Caso haja interesse em salvar os escores produzidos, é importante que a função `set_annotations` seja chamada em seguida.

`TrainablePipe` executa em `batches` 