import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import nlp
import st_helpers

if 'documents' not in st.session_state:
    st.session_state['documents'] = []

st.markdown('# Tf-idf + gensim')

st.markdown("""
    `gensim` is a powerful and versatile library that can be used for many NLP tasks.
    In this example we will start exploring `gensim` by using it develop an alternative to our bag-of-words, known as tf-idf.
""")

st.markdown('## Calculating the tf-idf')

st.markdown("""
    Tf-idf stands for: term frequency - inverse document frequency and is motivated by the observation that not all common words in a corpus are important (even excluding stopwords).
    The equation for calculating the tf-idf is as follows:
""")

st.latex('w_{i,j} = tf_{i,j}*log(N/df_{i})')

st.write(r'''
Where:
- $w_{i,j}$ is the calculated tf-idf for the $i^{th}$ token in the $j^{th}$ document,
- $tf_{i,j}$ is the frequency of the $i^{th}$ token in the $j^{th}$ document,
- $N$ is the total number of documents,
- $df_{i}$ is the number of documents that contain the $i_{th}$ token.
''')

st.markdown('## Tf-idf with gensim')

st.markdown("""
    Using the text input widget below create a corpus containing multiple documents (lines of text).
    Experiment by using certain words repeatedly across different documents and seeing how this impacts the tf-idf.
""")

document = st.text_input('Add a document:')

st.write('##### Documents')

if document != '':
    st.session_state['documents'].append(document)

st.write(st.session_state['documents'])

# assigning to documents makes for easier reading on dash via st.echo
documents = st.session_state['documents']

with st.echo():
    from nltk import word_tokenize
    from gensim.corpora.dictionary import Dictionary
    from gensim.models.tfidfmodel import TfidfModel
    import pandas as pd

    tokenized_documents = [word_tokenize(document) for document in documents]

    dictionary = Dictionary(tokenized_documents)

    corpus = [dictionary.doc2bow(document) for document in tokenized_documents] # in matrix market format

    tfidf = TfidfModel(corpus)

    tfidf_results = pd.DataFrame(columns=['token', 'document', 'tfidf'])
    for idx, document in enumerate(corpus):
        token_weights = tfidf[document]
        for token_weight in token_weights:
            tfidf_results.loc[len(tfidf_results.index)] = [
                dictionary[token_weight[0]],
                documents[idx],
                token_weight[1]
            ]

tfidf_results["tfidf"] = pd.to_numeric(tfidf_results["tfidf"])

st.dataframe(st_helpers.filter_dataframe(tfidf_results))

    







