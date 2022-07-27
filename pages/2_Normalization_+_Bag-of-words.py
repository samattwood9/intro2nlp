import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import nlp

st.markdown('# Normalization + Bag of words')

st.markdown("""
    Needing to identify topics from texts is a common occurence when doing NLP.
    A simple but effective approach known as bag-of-words achieves this by looking at the frequency of tokens.
    The underlying assumption being that the more times a word appears in a text, the more important it is likely to be.
""")

st.markdown("""
    Examine the examples below to see learn more about the bag-of-words approach.
    And use the text input widget below to change the value of `example_text` and experiment further.
""")

example_text = st.text_area('Enter some example text:', "The duck swam on the river. As it swam, the duck took great care of it's ducklings. After all, the duck didn't want anything bad to happen to them! Luckily, the duck and it's ducklings were able to cross the river unharmed.")

st.markdown('## Bag of words')

st.markdown("""
    Building on techniques like tokenization, we can implement a bag-of-words using `Counter`.
""")

with st.echo():
    from collections import Counter
    from nltk import word_tokenize

    tokens = word_tokenize(example_text)

    bag_of_words = Counter(tokens)

    st.pyplot(nlp.plot_bag_of_words(bag_of_words))

st.markdown('## Normalization (using stopwords)')

st.markdown("""
    Having experimented with the bag-of-words above, you may have noticed a problem...
    Words like *the* and punctuation occur frequently in many texts and can make our bag-of-words hard to interpret.
    To improve our bag-of-words we can filter out these common tokens that don't really tell us much using `string.punctuation` and a corpus of stopwords within `nltk`.
""")

with st.echo():
    from collections import Counter
    from nltk import word_tokenize
    from nltk.corpus import stopwords
    import string

    tokens = word_tokenize(example_text)

    filtered_tokens = [t for t in tokens if t not in stopwords.words('english') and t not in string.punctuation]

    bag_of_words = Counter(filtered_tokens)

    st.pyplot(nlp.plot_bag_of_words(bag_of_words))

st.markdown('## Advanced normalization')

st.markdown("""
    Using the text input widget below we can enter regex patterns to further remove unwanted features.
    We can do this by importing `re` and then passing `re.sub` a pattern followed by an empty string, followed by the text we want to process.
    Patterns like `\B@\w+` and `(http|https):\/\/\S+` can be applied to remove @ mentions and urls respectively.
""")

input_pattern = st.text_input('Enter a regex pattern for normalization:', '\B@\w+')

with st.echo():
    import re
    from nltk import word_tokenize
    from nltk.corpus import stopwords
    import string

     # append the input pattern with an r so that it is read as regex, so #\w+ -> r"#\w+"
    regex_pattern = r'%s'%(input_pattern) 

    example_text = re.sub(regex_pattern, "", example_text)

    tokens = word_tokenize(example_text)

    filtered_tokens = [t for t in tokens if t not in stopwords.words('english') and t not in string.punctuation]

    bag_of_words = Counter(filtered_tokens)

    st.pyplot(nlp.plot_bag_of_words(bag_of_words))








