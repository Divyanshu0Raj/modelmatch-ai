# # import streamlit as st
# # from models import MODELS
# # from models import ask_model
# # from votes import *
# # import pandas as pd
# #
# # st.title("AI Arena")
# # prompt=st.text_input("Ask Anything....")
# # generate=st.button("Generate")
# #
# # responses={}
# #
# # for name, model in MODELS.items():
# #     responses[name]=ask_model(model,prompt)
# #
# # # if generate:
# # #     for name, response in responses.items():
# # #         st.subheader(name)
# # #         st.write(response)
# #
# # for col,model in zip(cols,responses):
# #     with col:
# #         st.subheader(model)
# #         st.write(responses[model])
# #
# # winner=st.radio("best response",list(responses.keys()))
# #
# # if st.button("vote"):
# #
# #     save_votes(prompt,winner)
# #
# #     st.success(f"You voted for {winner}\n Votes are Saved Now!!!")
# #
# # df=pd.read_csv("votes.csv")
# #
# # scores=df['Winner'].value_counts()
# #
# # st.bar_chart(scores)
#
# # ai-arena/app.py
# import streamlit as st
# from models import MODELS, ask_model
# from votes import save_votes  # import only what's needed
# import pandas as pd
# import os
#
# st.title("AI Arena")
#
# prompt = st.text_input("Ask anything...")
# generate = st.button("Generate")
#
# # store responses in session_state so UI persists across reruns
# if "responses" not in st.session_state:
#     st.session_state.responses = {}
#
# # Run model queries only when the user clicks Generate
# if generate:
#     if not prompt:
#         st.warning("Please enter a prompt before generating.")
#     else:
#         st.session_state.responses = {}  # reset previous responses
#         # Create columns equal to number of models
#         cols = st.columns(len(MODELS))
#         # For each model, call ask_model and show the response in its column
#         for idx, (name, model_id) in enumerate(MODELS.items()):
#             col = cols[idx]
#             with col:
#                 st.subheader(name)
#                 # show spinner while calling API
#                 with st.spinner(f"Generating from {name}..."):
#                     try:
#                         # ask_model accepts friendly name or model id; pass friendly name
#                         resp = ask_model(name, prompt)
#                     except Exception as e:
#                         resp = f"Error: {e}"
#                     st.write(resp)
#                     st.session_state.responses[name] = resp
#
# # If we already have responses from a previous run, show them in columns
# if st.session_state.responses:
#     cols = st.columns(len(st.session_state.responses))
#     for idx, (name, resp) in enumerate(st.session_state.responses.items()):
#         with cols[idx]:
#             st.subheader(name)
#             st.write(resp)
#
# # Voting UI
# if st.session_state.responses:
#     winner = st.radio("Best response", list(st.session_state.responses.keys()))
#     if st.button("Vote"):
#         try:
#             save_votes(prompt, winner)
#             st.success(f"You voted for {winner} — vote saved.")
#         except Exception as e:
#             st.error(f"Failed to save vote: {e}")
#
# # Show aggregated votes chart (if file exists)
# VOTES_FILE = os.path.join(os.path.dirname(__file__), "votes.csv")
# if os.path.exists(VOTES_FILE):
#     try:
#         df = pd.read_csv(VOTES_FILE)
#         if "Winner" in df.columns:
#             scores = df["Winner"].value_counts()
#             st.bar_chart(scores)
#         else:
#             st.info("votes.csv found but has no 'Winner' column.")
#     except Exception as e:
#         st.error(f"Could not read votes.csv: {e}")
# else:
#     st.info("No votes.csv found yet — vote to create one.")

import streamlit as st
from models import MODELS, ask_model
from votes import save_votes
import pandas as pd
import os

st.set_page_config(page_title="AI Arena", layout="wide")
st.title("🎓 AI Arena")
st.markdown("Compare AI model responses side-by-side and vote for the best!")

prompt = st.text_input("Ask anything...", placeholder="Type your question here...")
generate = st.button("⚡ Generate Responses", use_container_width=True)

if "responses" not in st.session_state:
    st.session_state.responses = {}

if generate:
    if not prompt:
        st.warning("⚠️ Please enter a prompt before generating.")
    else:
        st.session_state.responses = {}
        cols = st.columns(len(MODELS))

        for idx, (name, model_id) in enumerate(MODELS.items()):
            col = cols[idx]
            with col:
                with st.spinner(f"🤖 Generating from {name}..."):
                    try:
                        resp = ask_model(name, prompt)
                    except Exception as e:
                        resp = f"❌ Error: {str(e)[:100]}"
                    st.session_state.responses[name] = resp

# Display responses with borders and formatting
if st.session_state.responses:
    st.divider()
    st.subheader("📊 Responses")

    cols = st.columns(len(st.session_state.responses), gap="large")

    for idx, (name, resp) in enumerate(st.session_state.responses.items()):
        with cols[idx]:
        # Create a nice bordered box with theme-aware styling
            st.markdown(f"""
            <div style="
            border: 2px solid #1f77b4;
            border-radius: 10px;
            padding: 20px;
            background-color: #ffffff;
            margin: 10px 0;
            min-height: 300px;
            max-height: 500px;
            overflow-y: auto;
        ">
            <h3 style="color: #1f77b4; margin-top: 0;">🤖 {name}</h3>
            <hr style="border: 1px solid #1f77b4;">
            <p style="
                color: #000000;
                line-height: 1.6;
                font-size: 14px;
                word-wrap: break-word;
                white-space: pre-wrap;
            ">{resp}</p>
        </div>
        """, unsafe_allow_html=True)

# Voting section
if st.session_state.responses:
    st.divider()
    st.subheader("🏆 Vote for the Best Response")

    col1, col2 = st.columns([3, 1])

    with col1:
        winner = st.radio(
            "Select the best response:",
            list(st.session_state.responses.keys()),
            horizontal=True,
            label_visibility="collapsed"
        )

    with col2:
        if st.button("✅ Vote", use_container_width=True):
            try:
                save_votes(prompt, winner)
                st.success(f"✅ Voted for {winner}!")
            except Exception as e:
                st.error(f"Vote failed: {e}")

# Voting statistics
st.divider()
st.subheader("📈 Voting Statistics")

VOTES_FILE = os.path.join(os.path.dirname(__file__), "votes.csv")
if os.path.exists(VOTES_FILE):
    try:
        df = pd.read_csv(VOTES_FILE)
        if "Winner" in df.columns and not df.empty:
            scores = df["Winner"].value_counts()

            col1, col2 = st.columns([2, 1])
            with col1:
                st.bar_chart(scores)
            with col2:
                st.markdown("### Vote Count")
                for model, count in scores.items():
                    st.metric(model, count)
        else:
            st.info("📝 No votes yet. Be the first to vote!")
    except Exception as e:
        st.error(f"Could not read votes: {e}")
else:
    st.info("📝 No votes yet. Generate responses and vote to see statistics!")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 12px;">
    <p>AI Arena • Compare and vote for your favorite AI responses</p>
</div>
""", unsafe_allow_html=True)