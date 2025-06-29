import streamlit as st

# Initialize session state
if "show_hidden_ui" not in st.session_state:
    st.session_state.show_hidden_ui = False

# --- Title Banner ---
st.markdown("""
    <div style="
        background-color: #8b0000;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        width: 80%;
        margin: auto;
        font-size: 32px;">
        <strong>Welcome to Nerrarya's Krezi Website!</strong><br><br>
        Please enter your full name to continue.
    </div>
""", unsafe_allow_html=True)

# --- Expected Names ---
First = 'Rafa'
First1 = 'Nararya'
Last = 'Tanaya'
Full = f'{First} {Last}'
Full1 = f'{First1} {First}'

# --- Centered Input Label ---
st.markdown("""
    <div style="text-align: center; font-size: 20px; padding-top: 20px;">
        <strong>Enter your full name:</strong>
    </div>
""", unsafe_allow_html=True)

# --- Input Field ---
name = st.text_input("")

# --- Centered Submit Button using Columns ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    submit = st.button("Submit")

# --- Button Logic ---
if submit and name:
    st.session_state.show_hidden_ui = True

    if name == Full:
        st.success(f"Hello {name}, redirecting you to something special...")
        st.markdown("[Click here if you're not redirected automatically](https://x.com/kanyewest)", unsafe_allow_html=True)
        st.balloons()
    elif name == Full1:
        st.success(f"Hi {name}, ready for a little fun?")
        st.markdown("[Click here if you're brave enough](https://pranx.com/maze/)", unsafe_allow_html=True)
    else:
        st.success(f"Hello {name}, you may now proceed.")

# --- Hidden UI After Submit ---
if st.session_state.show_hidden_ui:
    st.subheader("🔥 Hello, I'm Nararya from 8C!")
    st.image(
        "https://i.pinimg.com/736x/bf/c7/2f/bfc72f7aac6c0290de0ddb30363de0f3.jpg",
        caption="100% A picture of Me",
        use_container_width=True
    )

    # --- Red Highlight Box ---
    st.markdown("""
        <div style="
            background-color: #8b0000;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 80%;
            margin: auto;
            font-size: 16px;">
            <strong>I'm that one nerdy guy that you all surely know and hate, and well this is the website for ya'll to see my routines.</strong>
        </div>
    """, unsafe_allow_html=True)

    # --- Dark Blue Highlighted Text Box ---
    st.markdown("""
        <div style="
            background-color: #002b36;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            width: 80%;
            margin: auto;
            font-size: 16px;">
            <strong>Well, first-thing-first</strong>, I'm a member of Olympus Kesatuan Bangsa.<br>
            I'm not a high-rank member but I'm a member at least.<br><br>
            <strong>Second thing</strong>, I love math, love it more than sleeping at 12am everyday.<br><br>
            <em>And that's all, for now at least. See you later!!!</em>
        </div>
    """, unsafe_allow_html=True)
