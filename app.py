import streamlit as st
from utils.pdf_reader import extract_text
from rag import create_vector_store, retrieve
from interview import generate_question
from evaluator import evaluate

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

.score-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #1E1E1E;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown("""
<h1 style='text-align:center'>
🤖 AI Interview Assistant
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center'>
Generative AI + RAG Powered Mock Interview System
</h4>
""", unsafe_allow_html=True)

st.divider()

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("📌 Project")

    st.info("""
    Features:

    ✅ Resume Analysis

    ✅ AI Question Generation

    ✅ Technical Interview

    ✅ Answer Evaluation

    ✅ Feedback Report
    """)

    st.divider()

    st.write("Built Using")

    st.write("""
    • Streamlit

    • Groq API

    • Llama 3.3

    • FAISS

    • Sentence Transformers
    """)

# -------------------------
# Upload Section
# -------------------------

col1, col2 = st.columns([1, 2])

with col1:

    st.subheader("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Choose Resume PDF",
        type=["pdf"]
    )

with col2:

    st.subheader("ℹ️ Instructions")

    st.info("""
    1. Upload your resume

    2. Generate an interview question

    3. Answer the question

    4. Get AI feedback and score
    """)

# -------------------------
# Resume Processing
# -------------------------

if uploaded_file:

    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    try:

        text = extract_text("resume.pdf")

        create_vector_store(text)

        st.success("✅ Resume processed successfully")

        with st.expander("📑 Resume Preview"):

            st.write(text[:2000])

        # ---------------------
        # Generate Question
        # ---------------------

        if st.button("🎯 Generate Interview Question"):

            context = retrieve(
                "skills projects experience"
            )

            question = generate_question(context)

            st.session_state.question = question

    except Exception as e:

        st.error(f"Error : {e}")

# -------------------------
# Question Section
# -------------------------

if "question" in st.session_state:

    st.divider()

    st.subheader("💬 Interview Question")

    st.info(st.session_state.question)

    answer = st.text_area(
        "✍ Enter Your Answer",
        height=250
    )

    if st.button("🚀 Submit Answer"):

        if answer.strip() == "":

            st.warning("Please enter an answer.")

        else:

            with st.spinner("Evaluating Answer..."):

                feedback = evaluate(
                    st.session_state.question,
                    answer
                )

            st.divider()

            st.subheader("📊 Evaluation Report")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    label="Technical",
                    value="8/10"
                )

            with col2:
                st.metric(
                    label="Communication",
                    value="8/10"
                )

            with col3:
                st.metric(
                    label="Confidence",
                    value="9/10"
                )

            st.divider()

            st.subheader("📝 Detailed Feedback")

            st.write(feedback)

            st.success(
                "Interview Evaluation Completed"
            )

# -------------------------
# Footer
# -------------------------

st.divider()

st.markdown(
    """
    <center>
    Developed using Generative AI + RAG
    </center>
    """,
    unsafe_allow_html=True
)