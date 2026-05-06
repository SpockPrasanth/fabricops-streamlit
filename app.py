import streamlit as st

st.set_page_config(
    page_title="Interview Question Portal",
    layout="wide"
)

st.title("📘 Miracle Recruitment Interview Assistant")

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
            },

            {
                "question": "What is a CTE in SQL?",
                "answer": """
CTE stands for Common Table Expression.

It is a temporary result set that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement.
"""
            },

            {
                "question": "Difference between UNION and UNION ALL?",
                "answer": """
UNION removes duplicates.

UNION ALL keeps duplicates and performs faster.
"""
            },

            {
                "question": "What are indexes in SQL?",
                "answer": """
Indexes improve query performance by allowing faster data retrieval.
"""
            },

            {
                "question": "What is normalization?",
                "answer": """
Normalization organizes data to reduce redundancy and improve integrity.
"""
            },

            {
                "question": "Explain primary key and foreign key.",
                "answer": """
Primary Key uniquely identifies records.

Foreign Key creates relationship between tables.
"""
            },

            {
                "question": "What is a stored procedure?",
                "answer": """
Stored Procedure is a precompiled collection of SQL statements stored in database.
"""
            },

            {
                "question": "What is partitioning in SQL?",
                "answer": """
Partitioning divides large tables into smaller manageable pieces.
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
            },

            {
                "question": "What are Linked Services in ADF?",
                "answer": """
Linked Services are connection strings used to connect to external systems.
"""
            },

            {
                "question": "What is a Dataset in ADF?",
                "answer": """
Dataset represents the structure of data within data stores.
"""
            },

            {
                "question": "Difference between pipeline and activity?",
                "answer": """
Pipeline is a logical grouping of activities.

Activity performs actual task execution.
"""
            },

            {
                "question": "What are triggers in ADF?",
                "answer": """
Triggers schedule or automate pipeline execution.
"""
            },

            {
                "question": "What is parameterization in ADF?",
                "answer": """
Parameterization allows dynamic values in pipelines and datasets.
"""
            },

            {
                "question": "What is Mapping Data Flow?",
                "answer": """
Mapping Data Flow is used for graphical data transformation in ADF.
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
            },

            {
                "question": "What is a Lakehouse?",
                "answer": """
Lakehouse combines Data Lake and Data Warehouse capabilities.
"""
            },

            {
                "question": "What is Direct Lake mode?",
                "answer": """
Direct Lake allows Power BI to query Fabric Lakehouse directly without import.
"""
            },

            {
                "question": "What are Fabric Workspaces?",
                "answer": """
Workspaces organize Fabric items and manage access/security.
"""
            },

            {
                "question": "What is Delta Table?",
                "answer": """
Delta Table supports ACID transactions and versioning in data lakes.
"""
            }

        ],

        "PySpark": [

            {
                "question": "What is lazy evaluation in PySpark?",
                "answer": """
Transformations are evaluated only when an action is triggered.
"""
            },

            {
                "question": "Difference between transformation and action?",
                "answer": """
Transformation creates new dataframe.

Action triggers execution.
"""
            },

            {
                "question": "What is repartition in PySpark?",
                "answer": """
Repartition increases or decreases partitions with shuffle.
"""
            },

            {
                "question": "What is cache in PySpark?",
                "answer": """
Cache stores dataframe in memory for faster access.
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
            },

            {
                "question": "What is FILTER function in DAX?",
                "answer": """
FILTER returns a filtered table based on conditions.
"""
            },

            {
                "question": "What is ALL function in DAX?",
                "answer": """
ALL removes filters from table or columns.
"""
            },

            {
                "question": "Difference between SUM and SUMX?",
                "answer": """
SUM adds column values directly.

SUMX iterates row by row.
"""
            },

            {
                "question": "What is context transition?",
                "answer": """
Context transition converts row context into filter context.
"""
            },

            {
                "question": "What is time intelligence in DAX?",
                "answer": """
Time intelligence functions help analyze date-based calculations.
"""
            }

        ],

        "Power Query": [

            {
                "question": "What is query folding?",
                "answer": """
Query folding pushes transformations back to source system.
"""
            },

            {
                "question": "What is M language?",
                "answer": """
M language is used in Power Query transformations.
"""
            },

            {
                "question": "What is append query?",
                "answer": """
Append combines rows from multiple tables.
"""
            },

            {
                "question": "What is merge query?",
                "answer": """
Merge joins tables based on matching columns.
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
            },

            {
                "question": "What is snowflake schema?",
                "answer": """
Snowflake schema contains normalized dimension tables.
"""
            },

            {
                "question": "What is cardinality?",
                "answer": """
Cardinality defines relationship type between tables.
"""
            },

            {
                "question": "What is role-playing dimension?",
                "answer": """
Role-playing dimension is reused multiple times for different purposes.
"""
            }

        ],

        "Performance Tuning": [

            {
                "question": "How do you optimize Power BI reports?",
                "answer": """
Methods:
- Reduce visuals
- Optimize DAX
- Remove unused columns
- Use star schema
- Use aggregations
"""
            },

            {
                "question": "What is incremental refresh?",
                "answer": """
Incremental refresh loads only new or changed partitions.
"""
            },

            {
                "question": "What is aggregation table?",
                "answer": """
Aggregation tables improve query performance.
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
    ["Fresher", "2-4 Years", "5-8 Years", "10+ Years"]
)

# -----------------------------
# SEARCH BAR
# -----------------------------

search = st.text_input(
    "🔍 Search Questions",
    placeholder="Search by keyword..."
)

# -----------------------------
# MAIN SCREEN
# -----------------------------

st.subheader(f"{role} - {technology} Questions")

questions = question_bank[role][technology]

filtered_questions = [
    q for q in questions
    if search.lower() in q["question"].lower()
]

for index, item in enumerate(filtered_questions):

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

st.caption("Developed for Miracle Software Systems Recruitment Team")
