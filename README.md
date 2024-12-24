# Document_AI
AI-Driven Document Chatbot for Sales Data Automation
Developed an AI-powered chatbot leveraging NLP and embedding-based models to analyze and extract insights from 2,677+ company documents, including invoices, purchase orders, inventory reports, and shipping orders. Utilized Pinecone for vector similarity, HuggingFace for embeddings, and LangChain for contextual query answering, enabling automated data extraction, rapid document processing, error reduction, and easy access to key insights.

# Financial Document Classification and Business Intelligence

## **Overview**
This project is developed as part of the Appian AI Application Challenge. It focuses on automating the classification and processing of unstructured financial documents, such as:

- Applications for bank accounts (e.g., credit card, savings account)
- Identity documents (e.g., driver’s licenses, passports)
- Supporting financial documents (e.g., income statements, tax returns)
- Receipts

Additionally, the project provides **business intelligence (BI) insights**, offering actionable trends and operational efficiencies derived from document data.

---

## **Features**

1. **Document Classification**
   - Automatically categorizes financial documents based on content.
   - Hierarchical classification:
     - **Person Association:** Associates documents with individuals using metadata (e.g., names, government IDs).
     - **Document Type Identification:** Groups documents of the same type together (e.g., applications, receipts).

2. **Business Intelligence (BI) Insights**
   - Extracts trends from document submissions.
   - Provides operational analytics, such as:
     - Most frequent document types.
     - Processing time insights.
     - Error detection and categorization.

3. **Interactive UI**
   - Built with **Streamlit** for real-time interaction:
     - Upload financial documents.
     - View classification results instantly.
     - Analyze BI visualizations and summaries.

---

## **Technology Stack**

- **Python**: Core language for processing and machine learning.
- **Streamlit**: UI development for interactivity.
- **Machine Learning**: Used for document classification and hierarchical categorization.
- **Libraries and Tools:**
  - **Hugging Face Transformers**: Text embeddings for document understanding.
  - **Pandas, NumPy**: Data processing and analytics.
  - **Matplotlib, Seaborn**: Visualization of BI insights.

---

## **Installation and Setup**

### Prerequisites
1. Python 3.8 or higher installed on your machine.
2. Install required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

### Steps to Run
1. Clone the repository:
   ```bash
   git clone <repository-link>
   ```
2. Navigate to the project directory:
   ```bash
   cd financial-document-classification
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Upload financial documents and view results in your browser.

---

## **Usage**

1. **Document Upload:**
   - Upload a single PDF or batch of PDFs for classification.

2. **View Classification Results:**
   - Hierarchical categorization by person and document type.

3. **Analyze BI Insights:**
   - Visualize document trends, anomalies, and actionable recommendations.

---


## **Contributing**
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to your fork and submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contact**
For questions or feedback, contact:
- **Name:** Sudharshana B
- **Email:** [sudharshana426@gmail.com]
- **GitHub:** [https://github.com/Sudharshana426]

