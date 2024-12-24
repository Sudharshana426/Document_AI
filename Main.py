import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI-Powered Document Processing",
    page_icon="📄",
    layout="wide",
)

st.markdown("""
    <style>
        .css-1d391kg { 
            background-color: #f4f6f9; 
            border-radius: 8px;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .css-1v0mbdj { 
            color: white; 
            border-radius: 8px; 
            padding: 1rem;
        }
        .css-1v0mbdj .st-bq { 
            background-color: #3b3f44;
        }
        .sidebar-title {
            font-size: 28px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 20px;
        }
        .stRadio>label {
            font-size: 18px;
            font-weight: 500;
            color: #e4e4e4;
            cursor: pointer;
            padding: 8px 16px;
            border-radius: 6px;
            transition: background-color 0.3s, color 0.3s;
        }
        .stRadio div[role="radiogroup"] {
            background-color: #2f3136;
            padding:30px 10px;
            border-radius: 8px;
        }
        .stRadio div label:hover {
            background-color: transparent;
            color: inherit;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-size: 16px;
            border-radius: 6px;
            padding: 8px 16px;
        }
        .stButton>button:focus {
            background-color: #0056b3;
        }
        .main-content {
            margin-left: 0 !important;
            margin-right: 0 !important;
        }
        body {
            background-color: #f8f9fa;
            font-family: "Arial", sans-serif;
            color: #333;
        }
        .stMarkdown h1, .stMarkdown h2 {
            font-weight: 700;
            color: #333;
        }
        .stMarkdown {
            line-height: 1.6;
        }
        .stTooltip {
            background-color: #555;
            color: white;
            border-radius: 4px;
            padding: 5px;
        }
        .stTextInput>div {
            margin-bottom: 16px;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)
    selection = st.radio(
        "Go to", 
        ["Home", "Upload Document", "Query Insights", "Dashboard"], 
        label_visibility="collapsed"
    )

dummy_data = pd.DataFrame({
    'Category': ['Invoices', 'Purchase Orders', 'Shipping Orders', 'Reports'],
    'Documents Processed': [1200, 800, 600, 300],
    'Errors Detected': [50, 30, 20, 10],
})

if selection == "Home":
    st.title("📄 AI-Powered Document Processing")
    st.markdown(
        """
        Welcome to the **AI Document Processing Dashboard**! This tool automates the classification, 
        analysis, and extraction of actionable insights from unstructured financial documents. 
        
        ### Features:
        - **Document Upload:** Upload your financial documents for analysis.
        - **Query Insights:** Ask questions about document data for real-time answers.
        - **Interactive Dashboard:** Visualize processed documents and error trends.
        """
    )

if selection == "Upload Document":
    st.title("📤 Upload Document")
    uploaded_file = st.file_uploader("Upload your document (PDF or Image):", type=["pdf", "png", "jpg"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        st.info("Processing the document... Please wait.")
        st.markdown("✅ Document processed successfully!")

if selection == "Query Insights":
    st.title("🔍 Query Insights")
    user_query = st.text_input("Enter your query:")
    st.markdown("<span class='stTooltip'>Enter your question to retrieve document insights.</span>", unsafe_allow_html=True)

    if st.button("Submit Query"):
        if user_query.strip():
            st.info(f"Fetching results for your query: `{user_query}`...")
            st.success("Insights: The system found actionable trends for your query.")
        else:
            st.warning("Please enter a query before submitting.")

if selection == "Dashboard":
    st.title("📊 Insights Dashboard")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Documents Processed by Category")
        fig1 = px.bar(
            dummy_data, x="Category", y="Documents Processed", color="Category",
            title="Documents Processed by Category", labels={"Documents Processed": "Count"}
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Errors Detected by Category")
        fig2 = px.pie(
            dummy_data, names="Category", values="Errors Detected",
            title="Error Distribution by Category"
        )
        st.plotly_chart(fig2, use_container_width=True)
