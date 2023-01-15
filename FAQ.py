import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.set_page_config(page_title="My Webpage", page_icon=":sunny:",layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_3rwasyjy.json")
with st.container():
    st.subheader("Hey, Welcome to Global Hack Week :wave:")
    st.title("Challenge: Design a FAQ Page for your Guild")
    st.write("[DISCORD>](https://discord.com/invite/mlh)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Frequently Asked Questions:")
        st.write("OCRA SQUAD")
        st.write(
            """
            Q: How do I find challenges at GHW?

            A: Head to https://ghw.mlh.io/challneges to view the list of challenges currently active at GHW, these are usually updated at the time of each day's 'Today at GHW' event. Each challenge should also list how it should be submitted. If you have any issues with this, feel free to ask in 💻｜hack-help or if something seems to be missing, please notify the MLH team in the #ask-ghw-* channel.
            """
        )
        st.write("[DISCORD >](https://discord.com/channels/1020027288764567622/1020348182414233710)")
    with right_column:
        st_lottie(coding)
