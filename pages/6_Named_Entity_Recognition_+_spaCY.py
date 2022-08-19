import streamlit as st

st.markdown('# Named Entity Recognition + spaCY')

# using spacy becuase it makes this very easy + has nice visualisation features

text = st.text_area("Enter some example text:", "BBC News is an operational business division of the British Broadcasting Corporation responsible for the gathering and broadcasting of news and current affairs in the UK and around the world")

colors = {"ORG": "#8dd3c7", "PERSON": "#ffffb3", "DATE": "#bebada", "GPE": "#fb8072", "MONEY": "#80b1d3"}
options = {"colors": colors}

with st.echo():
    import spacy
    from spacy import displacy

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    ent_html = displacy.render(doc, style="ent", jupyter=False, options=options)

st.markdown(ent_html, unsafe_allow_html=True)