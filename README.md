# spaCy


[modelos em pt-BR](https://spacy.io/models/pt)
```python
python -m venv .venv
source .venv/bin/activate
pip install spacy
python -m spacy download pt_core_news_sm
#python -m spacy download pt_core_news_lg
#python -m spacy download pt_core_news_md
```


## [Doc methods & properties](https://spacy.io/api/doc)  

A container for accessing linguistic annotations.  

**A Doc is a sequence of Token objects.** Access sentences and named entities, export annotations to numpy arrays, losslessly serialize to compressed binary strings. The Doc object holds an array of TokenC structs. The Python-level **Token and Span objects** are views of this array, i.e. they **don’t own the data themselves.**  

- [semantic similarity](https://spacy.io/api/doc#similarity)

- [ents](https://spacy.io/api/doc#ents)
Extrai e retorna uma tupla com as entidades nomeadas (NER) presentes no documento (*Span objects*), caso o reconhecimento de entidade possa ser aplicado. **Depende de modelo!**  

exemplo:
```python
import spacy

nlp = spacy.load('pt_core_news_lg')
doc = nlp('Felipe Barros, coordenador do projeto Viva a Feira, foi à feira. Voltou com muitas frutas. Se encontrou com o João, diretor do Google')
>>> doc.ents

(Felipe Barros, Viva a Feira, João, Google)

```
- [spans](https://spacy.io/api/doc#spans)
A dictionary of named span groups, to store and access additional span annotations. You can write to it by assigning a list of Span objects or a SpanGroup to a given key.

- [noun_chucnks](https://spacy.io/api/doc#noun_chunks)
Iterate over the base noun phrases in the document. Yields base noun-phrase Span objects, if the document has been syntactically parsed. A base noun phrase, or “NP chunk”, is a noun phrase that does not permit other NPs to be nested within it – so no NP-level coordination, no prepositional phrases, and no relative clauses.

`[Felipe Barros, coordenador do projeto Viva a Feira,, feira, muitas frutas, o João, , diretor, Google]`

- [sents](https://spacy.io/api/doc#sents) 
Iterate over the sentences in the document. Sentence spans have no label. This property is only available when sentence boundaries have been set on the document by the parser, senter, sentencizer or some custom function. It will raise an error otherwise.

# [Atributos](https://spacy.io/api/doc#attributes)  

# [Serialization](https://spacy.io/api/doc#serialization-fields)
During serialization, spaCy will export several data fields used to restore different aspects of the object. If needed, you can exclude them from serialization by passing in the string names via the exclude argument.


# [Span](https://spacy.io/api/span)

Slice of a doc

# [Token](https://spacy.io/api/token)

- [is_ancestor](https://spacy.io/api/token#is_ancestor)
Check whether this token is a parent, grandparent, etc. of another in the dependency tree.

- [conjuncts](https://spacy.io/api/token#conjuncts)
A tuple of coordinated tokens, not including the token itself.

- [subtree](https://spacy.io/api/token#subtree)
A sequence containing the token and all the token’s syntactic descendants.

