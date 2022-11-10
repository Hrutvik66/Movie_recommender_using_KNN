import pandas as pd
import streamlit as st


@st.cache(suppress_st_warning=True)
def read_data(path):
    return pd.read_csv(path)


def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Movie Recommender
        </h1>
    """, unsafe_allow_html=True
                )

    st.caption("""
        <p style='text-align: center'>
        by   <span style="color:red"> Hrutvik </span>
        </p>
    """, unsafe_allow_html=True
               )


def body(sample):
    name = sample.iloc[0, 2]
    link = sample.iloc[0, 3]
    prob = sample.iloc[0, 4]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')
