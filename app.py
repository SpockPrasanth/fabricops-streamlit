import streamlit as st

st.set_page_config(
    page_title="Interview Question Portal",
    layout="wide"
)

st.title("📘 Recruitment Interview Assistant")

# -----------------------------
# HARDCODED QUESTION BANK
# -----------------------------

question_bank = {

    "Data Engineer": {

        "SQL": [

            {
                "question": "What is the difference between DELETE, TRUNCATE, and DROP?",
                "answer": """
DELETE removes rows and can be rolled back.

TRUNCATE removes all rows and resets identity.

DROP removes the entire table structure.
"""
            },

            {
                "question": "Explain window functions in SQL.",
                "answer": """
Window functions perform calculations across rows related to the current row.

Examples:
ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
"""
            },

            {
                "question": "What is incremental loading?",
                "answer": """
Incremental loading loads only new or changed records instead of full load.
Usually implemented using:
- Timestamp
- CDC
- Watermark columns
"""
            }

        ],

        "ADF": [

            {
                "question": "What is Integration Runtime in ADF?",
                "answer": """
Integration Runtime is the compute infrastructure used by Azure Data Factory
to move and transform data.
"""
            },

            {
                "question": "Explain Copy Activity.",
                "answer": """
Copy Activity is used to move data from source to destination.
"""
            }

        ],

        "Fabric": [

            {
                "question": "What is Medallion Architecture?",
                "answer": """
Medallion Architecture consists of:
- Bronze Layer
- Silver Layer
- Gold Layer
"""
            },

            {
                "question": "What is OneLake?",
                "answer": """
OneLake is Microsoft Fabric's unified data lake storage.
"""
            }

        ]
    },

    "Power BI Developer": {

        "DAX": [

            {
                "question": "What is CALCULATE function?",
                "answer": """
CALCULATE modifies filter context in DAX.
"""
            },

            {
                "question": "Difference between calculated column and measure?",
                "answer": """
Calculated Column:
Stored physically in model.

Measure:
Calculated dynamically during query execution.
"""
            }

        ],

        "Power Query": [

            {
                "question": "What is query folding?",
                "answer": """
Query folding pushes transformations back to source system.
"""
            }

        ],

        "Data Modeling": [

            {
                "question": "What is star schema?",
                "answer": """
Star schema contains:
- Fact table
- Dimension tables
"""
            }

        ]
    }
}

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header("Interview Setup")

role = st.sidebar.selectbox(
    "Select Role",
    list(question_bank.keys())
)

technology = st.sidebar.selectbox(
    "Select Technology",
    list(question_bank[role].keys())
)

experience = st.sidebar.selectbox(
    "Experience Level",
    ["Fresher", "2-4 Years", "5-8 Years"]
)

# -----------------------------
# MAIN SCREEN
# -----------------------------

st.subheader(f"{role} - {technology} Questions")

questions = question_bank[role][technology]

for index, item in enumerate(questions):

    with st.expander(f"Question {index + 1}"):

        st.markdown(f"### ❓ {item['question']}")

        if st.button(
            f"Show Answer {index}",
            key=index
        ):
            st.success(item['answer'])

        st.checkbox(
            "Question Asked",
            key=f"asked_{index}"
        )

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption("Developed for Recruitment Team")
