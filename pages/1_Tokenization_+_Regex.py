import streamlit as st
import nltk
nltk.download('punkt')

st.markdown('# Tokenization + Regex')

st.markdown("""
    Tokenization and regular expressions (Regex) are essential to many NLP methods:
    - Tokenization is the the process of turning a string of text or a document into smaller chunks.
    - Regex allows you to search text for sequences and patterns.
""")

st.markdown("""
    Tokenization may involve breaking a text up into sentences, or break a sentence up into words. Common forms
    of tokenization like this can be implemented with ease using a library like `nltk`. However, you can also use
    regex to create custom patterns for tokenization.
""")

example_text = "This is some example text. Don't think it isn't! "

st.markdown('## Sentence tokenization')

with st.echo():
    from nltk.tokenize import sent_tokenize
    example_sentences = sent_tokenize(example_text)
    st.write(example_sentences)

st.markdown('## Word tokenization')

with st.echo():
    from nltk.tokenize import word_tokenize
    example_words = word_tokenize(example_text)
    st.write(example_words)

st.markdown('## Advanced tokenization with regex')

st.markdown("""
    Use the text input widgets below to change the value of `example_text` and experiment with different regex patterns.
""")

example_text = st.text_input('Enter some example text:', 'This is some example text with a #tag.')

input_pattern = st.text_input('Enter a regex pattern for tokenization:', '#\w+')

with st.echo():
    from nltk.tokenize import regexp_tokenize
    regex_pattern = r'%s'%(input_pattern) # append the input pattern with an r so that it is read as regex, so #\w+ -> r"#\w+"
    example_tokens = regexp_tokenize(example_text, regex_pattern)
    st.write(example_tokens)

    


