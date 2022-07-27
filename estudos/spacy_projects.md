## [spaCy projects](https://spacy.io/usage/projects)

*spaCy projects* permite gestionar e compartilhar fluxos de trabalho "end-to-end" para diferentes casos e domínios, organizar treinamento, empacotamento e servindo *pipelines* customizados. Para começar, basta clonar um modelo de projeto prédefinido, o ajustando às necessidaders, carregando dados específicos, treinando *pipeline*, exportando-o como um módulo python, subindo os resultados a um servidor de armazenamento remoto e compartilhando com a equipe. 

![spaCy projects](../img/img_3.png)

1. Clone project template
O comando `spacy project clone` clona um modeo de projeto prexistente e copia os arquivos para um diretório local. Tendo isso, pode-se executar o projeto (por exemplo, treinar um *pipeline*).

`python -m spacy project clone pipelines/tagger_parser_ud`

Por padrão, o projeto será clonado no diretório de trabalho. Pode-se especificar um segudno argumento que define o diretorio ao qual o mesmo deverá ser clonado. O `--repo` permite definir um repositório a partir do qual o modelo será clonado, caso o modelo não seja do repositório do spaCy.

2. Baixar os ativos do projeto

*Assets* são arquivos que o projeto necessita. Por exemplo, os dados de treinamento e avaliação ou vetores prétreinados e *embeddings* para iniciar o modelo. 
Cada modelo de projeto possui um `project.yml` que especifica os ativos a serem baixados e onde organizá-los. 

```commandline
python -m spacy project assets
```

Os URLs dos ativos podem ser diferentes protocolos: HTTP, HTTPS, FTP, SSH, e até *cloud storage* (GCS ou S3).

É possível que o projeto inclua ativos muito grandes que não precisem ser baixados necessariamente ao fazer o clone do projeto. É por isso que os ativos podem ser marcados como "extra". Por padrão, esses ativos não são baixados. 
Caso seja necessário baixá-los, basta adicionar a flag `--extra`: `spacy project assets --extra`.

3. Executar um comando

Um comando consiste em um ou mais passos que podem ser executados a partir do comando `run`  do spacy project. 

Por exemplo, o comando a seguir irá executar uma tarefa de pré processamento definido no `project.yml`:

`python -m spacy project run preprocess`

Comandos podem ter dependencias e *outputs* declarados usando chaves `deps` e `outputs`, permitindo ao projeto identificar mudanças e determinar quando o comando precisa ser executado novamente.

4. Executa o fluxo de trabalho

Fluxo de trabalho são definidos por um conjunto de comandos (ver ite anterior) executados em orem, onde um depende do outro. Por exemplo, para gerar um pacote de *pipeline*, é necessário inciar convertendo os dados para, então, executar o `spacy train`, caso a conversão seja realizada com sucesso, executa o `spacy package` para transformar o melhor modelo treinado em um Python package instalável. Esse fluxo de trabalho é definido no `project.yml`. 

No exemplo a seguir, se está executando um fluxo de trabalho definido como `all`:

`python -m spacy project run all`

5. Optional: enviar a um repositório remoto

Após treinar um *pipeline*, pode-se opcionalmente usar o comando `push` do `spacy project` para exportar o resultado a um servidor remoto (S3, Google Cloud Storage ou SSH).

`python -m spacy project push`

A seção `remotes` do arquivo `project.yml` permite definir os nomes de diferentes servidores. Para baixar os resultados de um `Remote`, bas usar o comando `pull`.
