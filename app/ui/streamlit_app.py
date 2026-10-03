import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="RepoPilot",
    page_icon="🤖",
    layout="wide",
)


st.title("🤖 RepoPilot")
st.caption("AI Codebase Understanding & Debugging Assistant")


query = st.text_area(
    "Ask a question about your codebase",
    placeholder="Example: How does user authentication work?",
    height=120,
)


top_k = st.slider(
    "Number of code chunks to retrieve",
    min_value=1,
    max_value=10,
    value=3,
)


if st.button("Ask RepoPilot", type="primary"):

    if not query.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Analyzing the codebase..."):

            try:

                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "query": query,
                        "top_k": top_k,
                    },
                    timeout=120,
                )

                response.raise_for_status()

                data = response.json()

            except requests.RequestException as error:

                st.error(
                    f"Could not connect to RepoPilot API: {error}"
                )

            else:

                st.subheader("Answer")

                st.write(data["answer"])

                st.subheader("Sources")

                for source in data["sources"]:

                    st.markdown(
                        f"""
**{source['file_path']}**

`{source['symbol_name']}`  
Lines `{source['start_line']}-{source['end_line']}`  
Relevance: `{source['score']:.4f}`
"""
                    )