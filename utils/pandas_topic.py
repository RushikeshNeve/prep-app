"""Structured content for the Pandas and Data Handling topic page."""

from utils.data import TopicContent, _q, _r


PANDAS_DATA_HANDLING_TOPIC = TopicContent(
    key="pandas_data_handling",
    title="Pandas and Data Handling",
    icon="PD",
    difficulty="Easy to Medium",
    priority="High",
    estimated_time="3 to 4 hours",
    importance_for_movate="High",
    why_it_matters=(
        "Data handling means loading, cleaning, transforming, and analyzing data so it becomes useful. Pandas is the main beginner-friendly "
        "Python library for tabular data such as CSV, Excel-like sheets, and structured records. For a Movate AI Engineer role, this matters "
        "because AI workflows need clean inputs, enterprise datasets are often messy, prompt pipelines depend on organized context, and "
        "experimentation or evaluation is only reliable when the underlying data is usable."
    ),
    detailed_sections={
        "Data handling basics": "Understand what raw data looks like and why cleaning and transformation matter before analysis or AI usage.",
        "Pandas foundations": "Learn DataFrame, Series, rows, columns, indexing, loading data, and inspection basics.",
        "Operations and cleaning": "Practice filtering, grouping, creating columns, missing value handling, duplicate removal, and type conversion.",
        "AI workflow connection": "See how Pandas supports preprocessing, prompt preparation, backend file handling, and experimentation.",
        "Interview focus": "Use concise explanations, practical examples, and workflow language instead of only function names.",
    },
    common_mistakes=[
        "Jumping into analysis without first inspecting the dataset.",
        "Confusing `loc` and `iloc` or forgetting parentheses in filter conditions.",
        "Handling missing values without thinking about business context.",
        "Using cleaning steps mechanically without checking if the result still makes sense.",
        "Not connecting Pandas usage to real AI or backend workflows in interview answers.",
    ],
    code_examples={
        "Create DataFrame": """import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Neha"],
    "score": [82, 91, 76]
})

print(df.head())
""",
        "Inspect Missing Values": """print(df.info())
print(df.isnull().sum())""",
        "GroupBy Example": """summary = df.groupby("department")["salary"].mean()
print(summary)""",
    },
    interview_questions=[
        {"q": "What is Pandas?", "a": "Pandas is a Python library for working with structured or tabular data like CSV files and DataFrames."},
        {"q": "What is a DataFrame?", "a": "A DataFrame is a 2D labeled table with rows and columns."},
        {"q": "Why inspect data first?", "a": "Because you need to understand columns, data types, nulls, and obvious issues before cleaning or analysis."},
        {"q": "What is groupby?", "a": "It groups rows by a category and then applies aggregate operations such as sum or mean."},
        {"q": "Why does data handling matter in AI?", "a": "Because poor-quality input leads to poor prompts, poor features, poor retrieval, and poor outputs."},
    ],
    role_relevance=[
        "Preparing data before AI or model usage",
        "Cleaning enterprise data from CSV, Excel, logs, or exported reports",
        "Transforming structured data for prompts, analytics, and evaluation",
        "Analyzing CSV and Excel datasets quickly during experimentation",
        "Supporting backend file-processing or reporting flows",
    ],
    learning_objectives=[
        "Understand data handling from raw data to cleaned usable data.",
        "Learn beginner-friendly Pandas operations that appear often in interviews and projects.",
        "Explain data cleaning decisions clearly instead of only naming functions.",
        "Connect Pandas work to AI workflows, prompt preparation, and backend data pipelines.",
    ],
    learn_sections=[
        {
            "title": "1. What is Data Handling",
            "summary": "Data handling means collecting, loading, cleaning, transforming, and analyzing data so that it becomes useful for reporting, backend systems, and AI workflows.",
            "points": [
                "Raw data is often messy, incomplete, inconsistent, or badly formatted.",
                "Useful systems need structured and trustworthy data, not just data that exists.",
                "A good analogy is raw vegetables becoming a meal: you wash, cut, clean, and prepare before serving. Data follows a similar journey.",
            ],
            "diagram": "Raw Data -> Load -> Inspect -> Clean -> Transform -> Analyze -> Use",
            "callouts": [
                {"type": "info", "text": "Interview tip: say data handling is about making data usable, not just storing it."}
            ],
        },
        {
            "title": "2. What is Pandas",
            "summary": "Pandas is a Python library for working with tabular data such as CSV files, spreadsheet-like data, and structured records.",
            "points": [
                "It makes loading, filtering, grouping, cleaning, and exporting data much easier.",
                "A DataFrame is the main Pandas structure. It looks like a table with rows and columns.",
                "A Series is like a single labeled column.",
                "Rows are records, columns are fields, and the index is the label or position reference for rows.",
            ],
            "diagram": "CSV/Excel/JSON -> Pandas DataFrame -> Operations -> Output",
        },
        {
            "title": "3. DataFrame Basics",
            "summary": "A DataFrame is a 2D table-like data structure. This is the main object you work with in Pandas.",
            "examples": [
                {
                    "label": "Create a simple DataFrame",
                    "code": """import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Neha"],
    "score": [82, 91, 76],
    "department": ["AI", "Backend", "AI"]
})

print(df.head())
print(df.columns)
print(df.shape)
print(df.dtypes)
""",
                    "language": "python",
                }
            ],
            "points": [
                "Columns act like fields such as `name`, `score`, or `department`.",
                "Rows act like individual records.",
                "`head()` shows first rows, `columns` lists column names, `shape` gives row and column count, and `dtypes` shows data types.",
            ],
        },
        {
            "title": "4. Reading Data",
            "summary": "Pandas can load data from CSV, Excel, or Python dictionaries and lists.",
            "examples": [
                {
                    "label": "Read CSV and create from dictionary",
                    "code": """import pandas as pd

df_csv = pd.read_csv("students.csv")

df_dict = pd.DataFrame({
    "name": ["Asha", "Ravi"],
    "score": [82, 91]
})
""",
                    "language": "python",
                }
            ],
            "points": [
                "`pd.read_csv()` is the most common starting point.",
                "`pd.read_excel()` is also common conceptually when dealing with spreadsheet data.",
                "Common loading issues include wrong file path, wrong delimiter, and basic encoding problems.",
            ],
            "diagram": "File Path -> read_csv/read_excel -> DataFrame -> Inspect",
        },
        {
            "title": "5. Inspecting Data",
            "summary": "Always inspect a dataset before cleaning or analysis. This prevents bad assumptions.",
            "examples": [
                {
                    "label": "Inspection tools",
                    "code": """print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
""",
                    "language": "python",
                }
            ],
            "points": [
                "`head()` and `tail()` help you see sample rows.",
                "`info()` shows structure, non-null counts, and data types.",
                "`describe()` gives basic numeric summary statistics.",
                "`isnull().sum()` helps detect missing values quickly.",
            ],
            "callouts": [
                {"type": "warning", "text": "Do not clean blindly. First inspect what kinds of problems actually exist."}
            ],
        },
        {
            "title": "6. Selecting and Filtering Data",
            "summary": "Selection and filtering are core Pandas skills. You use them to focus on the data you actually need.",
            "examples": [
                {
                    "label": "Column selection and filtering",
                    "code": """df["name"]
df[["name", "score"]]

high_scores = df[df["score"] > 80]
ai_team = df[(df["department"] == "AI") & (df["score"] > 75)]

print(df.loc[0:2, ["name", "score"]])
print(df.iloc[0:2, 0:2])
""",
                    "language": "python",
                }
            ],
            "points": [
                "Use `df['col']` for one column and `df[['a', 'b']]` for multiple columns.",
                "Use conditions to filter rows.",
                "`loc` is label-based and `iloc` is position-based.",
            ],
            "mistakes": [
                "Forgetting parentheses when combining conditions with `&` or `|`.",
                "Confusing `loc` with `iloc`.",
            ],
        },
        {
            "title": "7. Creating and Modifying Columns",
            "summary": "You often create derived columns, rename columns, or remove unnecessary ones during cleaning and preprocessing.",
            "examples": [
                {
                    "label": "Create and modify columns",
                    "code": """df["total"] = df["price"] * df["quantity"]
df["category_clean"] = df["category"].str.strip().str.lower()
df = df.rename(columns={"old_name": "new_name"})
df = df.drop(columns=["unused_column"])
""",
                    "language": "python",
                }
            ],
            "points": [
                "Derived columns help convert raw fields into usable business values.",
                "Renaming improves readability and consistency.",
                "Dropping columns reduces noise before export or model use.",
            ],
        },
        {
            "title": "8. Sorting and Aggregation",
            "summary": "Sorting and quick aggregates help in basic reporting, inspection, and experiment analysis.",
            "examples": [
                {
                    "label": "Sort and aggregate",
                    "code": """df.sort_values("score", ascending=False)
df["department"].value_counts()
df["score"].mean()
df["score"].max()
df["score"].min()
df["score"].count()
""",
                    "language": "python",
                }
            ],
            "points": [
                "`sort_values()` orders data.",
                "`value_counts()` is useful for category frequency.",
                "`sum()`, `mean()`, `min()`, `max()`, and `count()` help quick analysis.",
            ],
        },
        {
            "title": "9. GroupBy Basics",
            "summary": "GroupBy means grouping rows by a category and then applying an aggregate to each group.",
            "examples": [
                {
                    "label": "Group by category",
                    "code": """sales_by_category = df.groupby("category")["sales"].sum()
avg_score_by_dept = df.groupby("department")["score"].mean()
print(sales_by_category)
print(avg_score_by_dept)
""",
                    "language": "python",
                }
            ],
            "points": [
                "This is useful for summary tables, dashboards, and reports.",
                "Common interview phrasing: group rows by a category, then calculate sum, mean, count, or max for each group.",
            ],
            "diagram": "Raw Table -> Group by Category -> Aggregate -> Summary Table",
        },
        {
            "title": "10. Handling Missing Values",
            "summary": "Missing values are common in real datasets and must be handled thoughtfully.",
            "examples": [
                {
                    "label": "Null handling basics",
                    "code": """df.isnull().sum()
df.dropna()
df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna("unknown")
""",
                    "language": "python",
                }
            ],
            "points": [
                "Missing values matter because they can break analysis, model input, or reporting.",
                "Common strategies are dropping rows, filling with defaults, or filling with mean, median, or mode.",
                "There is no single correct strategy. It depends on the field and business context.",
            ],
            "diagram": "Nulls detected -> Decide importance -> Drop / Fill / Investigate source -> Validate result",
        },
        {
            "title": "11. Handling Duplicates",
            "summary": "Duplicate rows can appear because of repeated ingestion, export issues, or user/system mistakes.",
            "examples": [
                {
                    "label": "Remove duplicates",
                    "code": """df.duplicated().sum()
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["email"], keep="first")
""",
                    "language": "python",
                }
            ],
            "points": [
                "Duplicates can distort counts, sums, and analysis.",
                "`drop_duplicates()` is the common fix.",
                "You may remove full duplicates or duplicates based on specific columns.",
            ],
        },
        {
            "title": "12. Basic String Cleaning in Data",
            "summary": "String cleanup is common when data has inconsistent casing, extra spaces, or messy categories.",
            "examples": [
                {
                    "label": "String cleaning with `.str`",
                    "code": """df["city"] = df["city"].str.strip().str.lower()
df["category"] = df["category"].str.replace("-", " ")
df["status"] = df["status"].str.strip().str.title()
""",
                    "language": "python",
                }
            ],
            "points": [
                "Use `.str.strip()` to remove extra spaces.",
                "Use lowercase or title case to standardize categories.",
                "Use replacement for simple text normalization.",
            ],
        },
        {
            "title": "13. Data Type Conversion",
            "summary": "Correct data types are important because calculations, sorting, dates, and model preprocessing depend on them.",
            "examples": [
                {
                    "label": "Convert types",
                    "code": """df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
""",
                    "language": "python",
                }
            ],
            "points": [
                "Numeric conversion is needed when numbers are loaded as text.",
                "Date conversion helps sorting, filtering by time, and reporting.",
                "Inconsistent formats or invalid values can produce errors or `NaN` values.",
            ],
        },
        {
            "title": "14. Exporting Data",
            "summary": "After cleaning and transforming data, you often export it for reporting, app usage, or the next processing step.",
            "examples": [
                {
                    "label": "Export CSV",
                    "code": """df.to_csv("cleaned_output.csv", index=False)""",
                    "language": "python",
                }
            ],
            "points": [
                "Exporting cleaned data helps preserve the usable result.",
                "Processed outputs are useful for apps, reports, experiments, and downstream pipelines.",
            ],
            "diagram": "Clean DataFrame -> Export CSV/Report -> Share / Reuse / Feed next step",
        },
        {
            "title": "15. NumPy Awareness",
            "summary": "NumPy is a Python library for numerical operations. It works well with Pandas but serves a slightly different purpose.",
            "points": [
                "Pandas is more table-focused and easier for labeled tabular data.",
                "NumPy is more array-focused and common for numerical computation.",
                "You do not need deep NumPy knowledge here, but interviewers may ask why Pandas and NumPy are often mentioned together.",
            ],
            "tables": [
                {
                    "title": "Pandas vs NumPy at a glance",
                    "markdown": """| Library | Best known for |
|---|---|
| Pandas | Tabular data, labeled columns, CSV and cleaning operations |
| NumPy | Fast numerical arrays and mathematical operations |""",
                }
            ],
        },
        {
            "title": "16. Why Data Handling Matters in AI Workflows",
            "summary": "AI systems depend on usable, clean, and structured input. Poor data quality leads to poor downstream results.",
            "points": [
                "Prompt inputs may need organized rows or cleaned text before being sent to a model.",
                "Document metadata often needs cleanup before retrieval or analysis.",
                "Experiment logs and evaluation tables need aggregation before comparison.",
                "Preprocessing often happens before embeddings, analytics, or model input preparation.",
            ],
            "diagram": "Raw Enterprise Data -> Clean/Transform -> Feature/Input Prep -> AI/Analytics -> Result",
            "callouts": [
                {"type": "success", "text": "Interview tip: data quality directly affects AI output quality, so preprocessing is part of responsible AI engineering."}
            ],
        },
    ],
    operations=[
        {
            "title": "1. Create DataFrame",
            "what_it_does": "Creates a table-like DataFrame from Python data such as dictionaries or lists.",
            "syntax": "pd.DataFrame(data)",
            "example": """import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi"],
    "score": [82, 91]
})""",
            "common_mistake": "Passing columns with unequal lengths.",
            "interview_tip": "Say a DataFrame is the main 2D labeled structure in Pandas.",
        },
        {
            "title": "2. Read CSV",
            "what_it_does": "Loads a CSV file into a DataFrame.",
            "syntax": "pd.read_csv('file.csv')",
            "example": """df = pd.read_csv("students.csv")""",
            "common_mistake": "Using the wrong file path or delimiter.",
            "interview_tip": "Mention that CSV loading is often the first step in practical data handling.",
        },
        {
            "title": "3. View first rows",
            "what_it_does": "Shows sample top rows for quick inspection.",
            "syntax": "df.head()",
            "example": """print(df.head())""",
            "common_mistake": "Skipping inspection and going straight into cleaning.",
            "interview_tip": "Say `head()` helps you quickly understand structure and sample values.",
        },
        {
            "title": "4. Select columns",
            "what_it_does": "Returns one column or multiple columns from a DataFrame.",
            "syntax": "df['col'] or df[['a', 'b']]",
            "example": """names = df["name"]
subset = df[["name", "score"]]""",
            "common_mistake": "Using single brackets for multiple columns.",
            "interview_tip": "Single bracket gives a Series, double bracket gives a DataFrame.",
        },
        {
            "title": "5. Filter rows",
            "what_it_does": "Keeps only rows that match a condition.",
            "syntax": "df[df['score'] > 80]",
            "example": """high_scores = df[df["score"] > 80]
ai_team = df[(df["department"] == "AI") & (df["score"] > 75)]""",
            "common_mistake": "Forgetting parentheses around each condition when using `&` or `|`.",
            "interview_tip": "Filtering is one of the most common Pandas interview basics.",
        },
        {
            "title": "6. Add new column",
            "what_it_does": "Creates a derived column based on existing data.",
            "syntax": "df['new_col'] = ...",
            "example": """df["total"] = df["price"] * df["quantity"]""",
            "common_mistake": "Using the wrong source column names.",
            "interview_tip": "Derived columns are useful for preprocessing and feature preparation.",
        },
        {
            "title": "7. Rename columns",
            "what_it_does": "Changes column names to cleaner or more consistent labels.",
            "syntax": "df.rename(columns={'old': 'new'})",
            "example": """df = df.rename(columns={"dept": "department"})""",
            "common_mistake": "Forgetting to assign the result back when not using `inplace`.",
            "interview_tip": "Renaming improves readability and consistency in real projects.",
        },
        {
            "title": "8. Drop columns",
            "what_it_does": "Removes unwanted columns.",
            "syntax": "df.drop(columns=['col'])",
            "example": """df = df.drop(columns=["temporary_notes"])""",
            "common_mistake": "Dropping the wrong axis or forgetting `columns=`.",
            "interview_tip": "Dropping unnecessary columns reduces noise before export or model use.",
        },
        {
            "title": "9. Sort data",
            "what_it_does": "Orders rows by one or more columns.",
            "syntax": "df.sort_values('col', ascending=False)",
            "example": """top_scores = df.sort_values("score", ascending=False)""",
            "common_mistake": "Assuming sorting changes the original DataFrame without reassignment.",
            "interview_tip": "Sorting is useful for ranking, reporting, and debugging unusual values.",
        },
        {
            "title": "10. GroupBy + aggregate",
            "what_it_does": "Groups data by category and calculates summary values.",
            "syntax": "df.groupby('category')['value'].sum()",
            "example": """sales_summary = df.groupby("category")["sales"].sum()""",
            "common_mistake": "Forgetting which column should be grouped and which should be aggregated.",
            "interview_tip": "GroupBy is one of the highest-value Pandas concepts for interviews.",
        },
        {
            "title": "11. Missing value count",
            "what_it_does": "Counts null values in each column.",
            "syntax": "df.isnull().sum()",
            "example": """null_counts = df.isnull().sum()""",
            "common_mistake": "Checking only one column and missing the overall picture.",
            "interview_tip": "Inspect nulls before deciding how to clean them.",
        },
        {
            "title": "12. Fill nulls",
            "what_it_does": "Replaces missing values with a chosen value or statistic.",
            "syntax": "df.fillna(value) or df['col'].fillna(...)",
            "example": """df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("unknown")""",
            "common_mistake": "Using one fill strategy for all columns without thinking about meaning.",
            "interview_tip": "Always say null strategy depends on context and business meaning.",
        },
        {
            "title": "13. Drop duplicates",
            "what_it_does": "Removes repeated rows.",
            "syntax": "df.drop_duplicates()",
            "example": """df = df.drop_duplicates(subset=["email"], keep="first")""",
            "common_mistake": "Dropping duplicates without deciding which columns define a duplicate.",
            "interview_tip": "Explain why duplicates are harmful for counts, metrics, and downstream decisions.",
        },
        {
            "title": "14. Export CSV",
            "what_it_does": "Writes the processed DataFrame to a CSV file.",
            "syntax": "df.to_csv('file.csv', index=False)",
            "example": """df.to_csv("cleaned_students.csv", index=False)""",
            "common_mistake": "Forgetting `index=False` when the index should not be saved as a column.",
            "interview_tip": "Exporting is common after cleaning, summarizing, or preparing data for another system.",
        },
    ],
    cleaning_sections=[
        {
            "title": "1. Why real-world data is messy",
            "problem": "Real datasets often come from forms, logs, exports, and manual entry, so they contain inconsistencies.",
            "detect": "Use inspection functions like `head()`, `info()`, `describe()`, and `isnull().sum()`.",
            "fix": "Inspect first, identify issue types, and clean step by step instead of guessing.",
            "why_it_matters": "Messy data creates bad analysis, poor reports, and weak AI inputs.",
            "diagram": "Load Data -> Inspect -> Find Issues -> Clean -> Validate -> Save / Use",
        },
        {
            "title": "2. Missing values",
            "problem": "Some rows have empty or null values in important columns.",
            "detect": "Use `df.isnull().sum()` and inspect important columns directly.",
            "fix": "Drop rows, fill defaults, or use mean/median/mode depending on context.",
            "why_it_matters": "Nulls can break model input, analysis logic, or summaries.",
            "example": """df.isnull().sum()
df["age"] = df["age"].fillna(df["age"].mean())""",
        },
        {
            "title": "3. Duplicates",
            "problem": "The same row or record appears multiple times.",
            "detect": "Use `df.duplicated().sum()` or inspect duplicate keys like email or ID.",
            "fix": "Use `drop_duplicates()` with the right subset definition.",
            "why_it_matters": "Duplicates distort totals, counts, and business conclusions.",
            "example": """df.duplicated().sum()
df = df.drop_duplicates(subset=["email"])""",
        },
        {
            "title": "4. Inconsistent text or casing",
            "problem": "Categories like `AI`, `ai`, and ` Ai ` are logically the same but stored differently.",
            "detect": "Use `value_counts()` to inspect category spread.",
            "fix": "Use `.str.strip()`, `.str.lower()`, or `.str.title()` to standardize text.",
            "why_it_matters": "Inconsistent text causes wrong grouping and poor prompt/context quality.",
            "example": """df["team"] = df["team"].str.strip().str.lower()""",
        },
        {
            "title": "5. Extra spaces",
            "problem": "Leading or trailing spaces make values look different when they should match.",
            "detect": "Inspect sample rows and suspicious categories.",
            "fix": "Use `.str.strip()` on text columns.",
            "why_it_matters": "Extra spaces silently create duplicate categories or failed matches.",
            "example": """df["city"] = df["city"].str.strip()""",
        },
        {
            "title": "6. Wrong data types",
            "problem": "Numbers may be stored as text, or dates may be stored as inconsistent strings.",
            "detect": "Check `df.dtypes` and inspect values that look suspicious.",
            "fix": "Use `pd.to_numeric()` or `pd.to_datetime()` with careful error handling.",
            "why_it_matters": "Wrong types break calculations, sorting, date analysis, and model preprocessing.",
            "example": """df["price"] = pd.to_numeric(df["price"], errors="coerce")""",
        },
        {
            "title": "7. Outlier awareness",
            "problem": "Some values are unusually high or low compared with the rest of the data.",
            "detect": "Use `describe()`, sorting, and basic plots or manual inspection.",
            "fix": "Investigate whether the value is valid, a typo, or a business exception before removing it.",
            "why_it_matters": "Outliers can distort averages and lead to misleading analysis or model features.",
        },
        {
            "title": "8. Invalid records or impossible values",
            "problem": "Some values are logically impossible, like negative quantity or impossible age.",
            "detect": "Use validation rules and filtering conditions.",
            "fix": "Correct, remove, or escalate based on business rules and source trust.",
            "why_it_matters": "Invalid records can break trust in the dataset and downstream systems.",
            "example": """invalid_rows = df[df["quantity"] < 0]""",
        },
        {
            "title": "9. Basic validation before use",
            "problem": "A dataset may seem clean but still fail simple sanity checks.",
            "detect": "Check row counts, key uniqueness, nulls in required fields, and value ranges.",
            "fix": "Run a final validation pass after cleaning before export or AI usage.",
            "why_it_matters": "Validation reduces the risk of feeding bad data into reports, models, or prompts.",
            "diagram": "Clean -> Validate required columns -> Check ranges/uniqueness -> Use or re-clean",
        },
    ],
    ai_workflow_examples=[
        {
            "title": "1. CSV to AI-ready input flow",
            "business_purpose": "Turn a raw CSV file into structured context that can be safely used in a prompt or model call.",
            "data_handling_responsibilities": [
                "Load the CSV into a DataFrame.",
                "Clean column names and fix missing or messy values.",
                "Select only useful fields for the model or prompt.",
                "Convert rows into structured prompt-ready text or JSON.",
            ],
            "why_pandas_helps": "Pandas makes it easy to clean columns, filter records, and build structured inputs from tabular data.",
            "risks": "Messy columns, nulls, token-heavy prompts, and irrelevant rows can reduce output quality.",
            "diagram": "CSV -> Pandas -> Clean columns -> Build prompt/context -> Send to model",
        },
        {
            "title": "2. Customer support dataset cleanup",
            "business_purpose": "Prepare support tickets for summarization, categorization, or analytics.",
            "data_handling_responsibilities": [
                "Standardize categories and priority fields.",
                "Remove null or invalid records in important columns.",
                "Clean ticket text and metadata for later analysis.",
                "Create summary tables for reporting or model support.",
            ],
            "why_pandas_helps": "It is good for text cleanup, null handling, value counts, and grouping by ticket category or team.",
            "risks": "Noisy text, inconsistent labels, and duplicate tickets can distort both reports and AI outputs.",
            "diagram": "Raw tickets -> Clean categories -> Remove nulls -> Summarize or classify",
        },
        {
            "title": "3. Product data cleanup",
            "business_purpose": "Standardize product sheets before using them in search, recommendations, or content optimization.",
            "data_handling_responsibilities": [
                "Clean titles and categories.",
                "Normalize price and stock fields.",
                "Remove duplicates and impossible rows.",
                "Prepare structured export for downstream AI or backend use.",
            ],
            "why_pandas_helps": "It handles tabular product data efficiently and supports consistent category cleanup and export.",
            "risks": "Inconsistent naming, missing prices, and duplicate SKUs can create wrong downstream results.",
            "diagram": "Raw product sheet -> Standardize titles/categories -> Clean values -> Use in AI optimization flow",
        },
        {
            "title": "4. Analytics / experimentation support",
            "business_purpose": "Analyze experiment logs or evaluation results and create quick summaries for comparison.",
            "data_handling_responsibilities": [
                "Load log data from CSV or exported results.",
                "Aggregate metrics by model, prompt, or version.",
                "Compare mean values, counts, and category-level outcomes.",
                "Export final summary for reporting.",
            ],
            "why_pandas_helps": "GroupBy, sorting, and aggregation make experiment comparison fast and readable.",
            "risks": "Mixed data types, duplicated runs, and missing metrics can lead to wrong conclusions.",
            "diagram": "Experiment logs -> Aggregate metrics -> Compare results -> Export summary",
        },
        {
            "title": "5. File upload processing flow",
            "business_purpose": "Support a backend flow where a user uploads a CSV and gets a cleaned summary or report back.",
            "data_handling_responsibilities": [
                "Parse the uploaded file into Pandas.",
                "Inspect nulls, duplicates, and invalid values.",
                "Apply cleaning and transformation logic.",
                "Return a summary or save an export for the user.",
            ],
            "why_pandas_helps": "It gives a simple backend-friendly way to process uploaded tabular data quickly.",
            "risks": "Bad file format, encoding issues, unexpected columns, or large files can create processing problems.",
            "diagram": "User uploads CSV -> Backend parses -> Pandas cleans -> System returns summary/report",
        },
    ],
    interview_questions_detailed=[
        {"question": "What is Pandas?", "short_answer": "Pandas is a Python library for working with structured and tabular data.", "spoken_answer": "Pandas is a Python library mainly used for loading, cleaning, transforming, and analyzing tabular data such as CSV files, Excel-like data, and structured records. It is popular because it makes common data handling tasks much easier."},
        {"question": "What is a DataFrame?", "short_answer": "A DataFrame is a 2D labeled table with rows and columns.", "spoken_answer": "A DataFrame is the main Pandas object. It looks like a table where columns represent fields, rows represent records, and labels help with selection and analysis."},
        {"question": "What is a Series?", "short_answer": "A Series is a one-dimensional labeled array, often like a single column.", "spoken_answer": "A Series is like one labeled column of data in Pandas. It stores values along with an index and is often returned when you select a single column from a DataFrame."},
        {"question": "Why is Pandas useful?", "short_answer": "Pandas makes loading, cleaning, filtering, grouping, and exporting data much easier.", "spoken_answer": "Pandas is useful because real-world structured data is rarely clean. It gives simple tools for inspecting data, handling nulls, filtering rows, grouping records, and preparing outputs for analytics or AI workflows."},
        {"question": "How do you read a CSV in Pandas?", "short_answer": "Use `pd.read_csv('file.csv')`.", "spoken_answer": "The common way is `pd.read_csv('file.csv')`. It loads the CSV into a DataFrame so you can inspect and clean it."},
        {"question": "What does `head()` do?", "short_answer": "It shows the first few rows of the DataFrame.", "spoken_answer": "The `head()` method helps you quickly inspect sample rows from the top of a dataset. It is useful when you first load data and want to understand structure and values."},
        {"question": "Difference between `loc` and `iloc`?", "short_answer": "`loc` is label-based and `iloc` is position-based.", "spoken_answer": "Use `loc` when selecting by labels, such as row labels or column names. Use `iloc` when selecting by integer positions."},
        {"question": "How do you filter rows?", "short_answer": "Use boolean conditions like `df[df['score'] > 80]`.", "spoken_answer": "Filtering means keeping only rows that match a condition. In Pandas, you usually create a boolean expression and use it inside square brackets."},
        {"question": "How do you create a new column?", "short_answer": "Assign to a new column name like `df['total'] = ...`.", "spoken_answer": "You create a new column by assigning values or an expression to a new column name. This is common when deriving business values or preparing features."},
        {"question": "How do you handle missing values?", "short_answer": "First inspect them, then decide whether to drop, fill, or investigate the source.", "spoken_answer": "The first step is to inspect missing values using methods like `isnull().sum()`. Then the strategy depends on context: you may drop rows, fill with a default or statistic, or go back to the source process if the missing data is important."},
        {"question": "What is `dropna()`?", "short_answer": "`dropna()` removes rows or columns with missing values.", "spoken_answer": "The `dropna()` method is used when you decide that rows or columns with missing values should be removed. It is useful when the missing data is limited or not critical, but you should use it carefully."},
        {"question": "What is `fillna()`?", "short_answer": "`fillna()` replaces missing values with a chosen value.", "spoken_answer": "The `fillna()` method is used when you want to keep the rows but replace missing values with something meaningful, such as zero, `unknown`, or a statistic like mean or median."},
        {"question": "How do you remove duplicates?", "short_answer": "Use `drop_duplicates()`.", "spoken_answer": "Duplicates can be removed with `drop_duplicates()`, either on the full row or based on selected columns such as email or order ID."},
        {"question": "What is `groupby()`?", "short_answer": "It groups rows by a category and applies an aggregate function to each group.", "spoken_answer": "The `groupby()` operation is used when you want summary values by category, such as total sales by region or average score by department."},
        {"question": "Why is data cleaning important?", "short_answer": "Because poor-quality data leads to poor analysis, reporting, and AI results.", "spoken_answer": "Data cleaning matters because raw data often contains nulls, duplicates, inconsistencies, and wrong types. If those issues are ignored, downstream analytics or AI outputs become unreliable."},
        {"question": "What is the use of `info()`?", "short_answer": "`info()` shows structure, column names, non-null counts, and data types.", "spoken_answer": "The `info()` method is useful for understanding the overall structure of a dataset. It helps you quickly spot null-heavy columns and data type issues."},
        {"question": "What does `describe()` show?", "short_answer": "It shows summary statistics for numeric columns by default.", "spoken_answer": "The `describe()` method gives quick statistics such as count, mean, standard deviation, minimum, maximum, and quartiles. It helps in basic inspection and outlier awareness."},
        {"question": "Why are data types important?", "short_answer": "Because calculations, sorting, and date operations depend on correct types.", "spoken_answer": "If numbers are stored as text or dates are badly formatted, analysis and preprocessing will be wrong or difficult. Correct data types are important for reliability."},
        {"question": "How do you rename columns?", "short_answer": "Use `df.rename(columns={'old': 'new'})`.", "spoken_answer": "Renaming columns is useful when you want clearer or more consistent column names. It improves readability and later processing."},
        {"question": "How do you export a DataFrame?", "short_answer": "Use methods like `to_csv()`.", "spoken_answer": "After cleaning or analysis, you can export a DataFrame using methods like `to_csv()`. This is common when you want to save cleaned data or share a summary with another system."},
        {"question": "What is sorting in Pandas?", "short_answer": "Sorting means ordering rows based on one or more columns using `sort_values()`.", "spoken_answer": "Sorting is useful when you want to rank rows, inspect top or bottom values, or prepare a cleaner report."},
        {"question": "Why is Pandas important in AI workflows?", "short_answer": "Because AI workflows often need clean, structured, and filtered input data.", "spoken_answer": "Pandas is important in AI workflows because raw data often needs cleanup and transformation before it is used in prompts, embeddings, evaluation, or analytics. Better data quality usually leads to better downstream output."},
        {"question": "What happens if raw data is poor quality?", "short_answer": "Poor data quality leads to unreliable analytics, prompts, and model results.", "spoken_answer": "If raw data is poor quality, you may get wrong reports, confusing prompts, bad retrieval context, or poor model input. The system may still run, but the output quality will be weak."},
        {"question": "What is the role of preprocessing before model usage?", "short_answer": "Preprocessing makes data structured, clean, and suitable for downstream model or analytics steps.", "spoken_answer": "Preprocessing is the stage where you clean missing values, standardize text, fix data types, remove duplicates, and prepare the exact format needed by the model or workflow."},
        {"question": "What is the difference between Pandas and NumPy?", "short_answer": "Pandas is table-focused and labeled, while NumPy is array-focused and numerical.", "spoken_answer": "Pandas is more convenient for tabular data with labeled rows and columns. NumPy is more focused on fast numerical arrays and lower-level numerical operations."},
        {"question": "How would you clean an uploaded CSV file?", "short_answer": "Load it, inspect it, check nulls and types, clean inconsistencies, validate, and then export or use it.", "spoken_answer": "I would first load the CSV, inspect columns and null counts, look for duplicates or wrong types, standardize text fields, handle missing values based on context, validate the cleaned result, and then use or export it."},
        {"question": "What problems do you check first in a dataset?", "short_answer": "I first check structure, column names, data types, nulls, duplicates, and obviously invalid values.", "spoken_answer": "After loading a dataset, I usually start with `head()`, `info()`, and `isnull().sum()`. Then I look for duplicates, wrong types, suspicious categories, and impossible values."},
        {"question": "How do you inspect null values?", "short_answer": "Use `df.isnull().sum()`.", "spoken_answer": "A simple and common way is `df.isnull().sum()`, which shows the count of missing values in each column. It helps you prioritize cleaning."},
        {"question": "How do you standardize text categories?", "short_answer": "Use string methods such as `.str.strip()`, `.str.lower()`, and replacements.", "spoken_answer": "To standardize categories, I usually remove extra spaces, convert to a common case such as lowercase, and replace inconsistent text so that logically similar values become identical."},
        {"question": "Explain a real use case where you would use Pandas.", "short_answer": "I would use Pandas to clean a CSV of customer tickets, standardize categories, remove nulls, and build a summary for analytics or AI classification.", "spoken_answer": "A practical example is customer support data. I would load the ticket CSV, inspect nulls and categories, clean inconsistent labels, remove duplicates, group by category or priority, and then export a cleaned version for reporting or AI-based classification."},
    ],
    interview_scenarios=[
        {
            "question": "How would you clean a CSV before using it in an AI workflow?",
            "approach": "Explain it as a step-by-step pipeline from loading to validation.",
            "answer_points": [
                "Load the CSV into Pandas.",
                "Inspect the structure with `head()`, `info()`, and `isnull().sum()`.",
                "Fix missing values, duplicates, inconsistent text, and wrong data types.",
                "Select only relevant columns for the AI workflow.",
                "Validate the cleaned result and then build the prompt, features, or export.",
            ],
            "diagram": "CSV -> Inspect -> Clean nulls/types/text -> Select useful fields -> Validate -> AI workflow",
        },
        {
            "question": "Why is data handling important before using AI?",
            "approach": "Connect input quality to downstream output quality.",
            "answer_points": [
                "AI systems depend on usable and structured input.",
                "Poor data quality leads to poor prompts, features, retrieval context, and analytics.",
                "Cleaning improves consistency, reliability, and trust in outputs.",
                "Preprocessing is part of making an AI workflow production-friendly.",
            ],
            "diagram": "Poor data -> poor downstream results\nClean data -> stronger downstream results",
        },
        {
            "question": "How would you analyze category-wise totals in a dataset?",
            "approach": "Mention inspection, grouping, aggregation, and validation of results.",
            "answer_points": [
                "Inspect the dataset and identify the category and numeric columns.",
                "Clean category labels if needed.",
                "Use `groupby()` on the category column and apply `sum()` or another aggregate.",
                "Sort the output for readability and export or report the summary.",
            ],
            "diagram": "Raw Table -> Clean category column -> groupby(category) -> sum(value) -> Summary Table",
        },
        {
            "question": "What steps would you take after loading a dataset?",
            "approach": "Show a disciplined inspection-first workflow.",
            "answer_points": [
                "Look at sample rows with `head()`.",
                "Check structure with `info()`, columns, shape, and data types.",
                "Inspect null counts and duplicates.",
                "Identify obvious invalid values or inconsistent text.",
                "Then begin cleaning or analysis based on what you found.",
            ],
            "diagram": "Load -> Sample rows -> Check structure -> Check nulls/duplicates -> Clean or analyze",
        },
    ],
    interview_rapid_fire=[
        {"question": "Pandas is?", "answer": "A Python library for tabular data handling."},
        {"question": "DataFrame is?", "answer": "A 2D labeled table."},
        {"question": "Series is?", "answer": "A 1D labeled array, often like one column."},
        {"question": "`head()` does?", "answer": "Shows top rows."},
        {"question": "`info()` does?", "answer": "Shows structure, non-null counts, and dtypes."},
        {"question": "`describe()` does?", "answer": "Shows summary statistics."},
        {"question": "`loc` vs `iloc`?", "answer": "Label-based vs position-based selection."},
        {"question": "`groupby()` helps with?", "answer": "Category-wise summaries."},
        {"question": "Null strategy depends on?", "answer": "Business context and column meaning."},
        {"question": "Why Pandas in AI?", "answer": "To prepare clean and structured input data."},
    ],
    interview_common_mistakes=[
        "Jumping into analysis without inspecting data first.",
        "Not knowing `head()`, `info()`, `describe()`, or `isnull().sum()`.",
        "Giving a weak answer on missing value strategy.",
        "Not being able to explain `groupby()` in simple language.",
        "Talking about Pandas without connecting it to real AI or backend use cases.",
    ],
    quick_revision_points=[
        "Data handling means loading, cleaning, transforming, and analyzing data.",
        "Raw data is often messy and needs preparation before use.",
        "Pandas is used for tabular data manipulation in Python.",
        "A DataFrame is a 2D labeled data structure.",
        "A Series is a 1D labeled structure.",
        "Rows are records and columns are fields.",
        "Always inspect data before cleaning it.",
        "`head()` shows top rows.",
        "`tail()` shows bottom rows.",
        "`info()` shows structure, non-null counts, and data types.",
        "`describe()` shows summary statistics for numeric columns by default.",
        "`shape` tells you row and column count.",
        "`columns` lists the column names.",
        "`dtypes` shows data types.",
        "`isnull().sum()` helps inspect missing values.",
        "Use `pd.read_csv()` to load CSV data.",
        "Use `df['col']` for one column and `df[['a', 'b']]` for multiple columns.",
        "Filtering rows uses boolean conditions.",
        "Use parentheses when combining conditions with `&` or `|`.",
        "`loc` is label-based and `iloc` is position-based.",
        "New columns can be created from existing columns.",
        "Use `.str.strip()` and `.str.lower()` for basic text cleanup.",
        "`sort_values()` sorts rows.",
        "`value_counts()` counts category frequency.",
        "`groupby()` is used for category-wise aggregation.",
        "Missing value strategy depends on context.",
        "`drop_duplicates()` removes repeated rows.",
        "Correct data types are important for reliable analysis.",
        "Use `to_csv()` to export cleaned data.",
        "Data quality directly affects AI output quality.",
    ],
    quiz_questions=[
        _q("What is a DataFrame?", ["A 2D labeled table", "A plotting library", "A database server", "A token format"], 0, "A DataFrame is a 2D labeled data structure in Pandas."),
        _q("Which function is commonly used to load a CSV file?", ["pd.to_csv()", "pd.read_csv()", "pd.describe()", "pd.group_by()"], 1, "`pd.read_csv()` is the common way to load CSV data into a DataFrame."),
        _q("What does `head()` do?", ["Deletes the first rows", "Shows the first few rows", "Shows column types only", "Groups the data"], 1, "`head()` is used for quick inspection of the top rows."),
        _q("Which is correct for filtering rows with score > 80?", ["df['score' > 80]", "df[df['score'] > 80]", "df.filter(score > 80)", "df.loc['score' > 80]"], 1, "Filtering rows usually uses a boolean condition like `df[df['score'] > 80]`."),
        _q("Which method helps inspect missing values column-wise?", ["df.groupby()", "df.isnull().sum()", "df.to_csv()", "df.rename()"], 1, "`isnull().sum()` is a quick way to see null counts per column."),
        _q("What is `groupby()` mainly used for?", ["Exporting files", "Category-wise aggregation", "Dropping duplicates only", "Changing file paths"], 1, "`groupby()` is used to group rows by a category and aggregate each group."),
        _q("What does `drop_duplicates()` do?", ["Converts data types", "Sorts rows", "Removes repeated rows", "Adds new columns"], 2, "`drop_duplicates()` removes duplicate records."),
        _q("What is a simple difference between Pandas and NumPy?", ["Pandas is for tabular labeled data, NumPy is for arrays and numerical work", "Pandas is only for plotting", "NumPy only works with CSV", "They are the same library"], 0, "Pandas is more table-focused, while NumPy is more array-focused and numerical."),
    ],
    resources=[
        _r("Pandas Getting Started", "https://pandas.pydata.org/docs/getting_started/index.html", "article", "must_read", "Official beginner entry point."),
        _r("Kaggle Pandas Micro-course", "https://www.kaggle.com/learn/pandas", "article", "must_read", "Hands-on beginner-friendly practice."),
        _r("Real Python Pandas Tutorials", "https://realpython.com/tutorials/pandas/", "article", "practice", "Readable practical Pandas guides."),
        _r("NumPy Quickstart", "https://numpy.org/doc/stable/user/quickstart.html", "article", "optional_deep_dive", "Useful if you want a simple NumPy comparison."),
    ],
    resource_sections={
        "Must watch first": [
            _r("Corey Schafer Pandas Videos", "https://www.youtube.com/results?search_query=Corey+Schafer+pandas", "video", "must_watch", "Clear beginner-friendly Pandas explanations."),
            _r("freeCodeCamp Pandas Videos", "https://www.youtube.com/results?search_query=freecodecamp+pandas", "video", "must_watch", "Good long-form beginner video content."),
            _r("Data Cleaning Tutorial Videos", "https://www.youtube.com/results?search_query=data+cleaning+pandas+beginner", "video", "must_watch", "Useful for seeing messy-data cleanup workflows."),
        ],
        "Must read first": [
            _r("Pandas Getting Started", "https://pandas.pydata.org/docs/getting_started/index.html", "article", "must_read", "Official getting started guide."),
            _r("Kaggle Pandas Micro-course", "https://www.kaggle.com/learn/pandas", "article", "must_read", "Simple hands-on learning path."),
            _r("GeeksforGeeks Pandas Tutorial", "https://www.geeksforgeeks.org/python-pandas-tutorial/", "article", "must_read", "Broad Pandas basics reference."),
            _r("Real Python Pandas Tutorials", "https://realpython.com/tutorials/pandas/", "article", "must_read", "Practical explanations with examples."),
        ],
        "Practice / explore": [
            _r("Kaggle Datasets", "https://www.kaggle.com/datasets", "article", "practice", "Useful place to find CSV datasets for practice."),
            _r("Pandas User Guide", "https://pandas.pydata.org/docs/user_guide/index.html", "article", "practice", "Helpful once basics are comfortable."),
            _r("Real Python Data Cleaning Articles", "https://realpython.com/python-data-cleaning-numpy-pandas/", "article", "practice", "Good practical data cleaning examples."),
        ],
        "Optional deep dive": [
            _r("NumPy Quickstart", "https://numpy.org/doc/stable/user/quickstart.html", "article", "optional_deep_dive", "Good for understanding the Pandas and NumPy connection."),
            _r("Pandas Missing Data Guide", "https://pandas.pydata.org/docs/user_guide/missing_data.html", "article", "optional_deep_dive", "Useful when you want deeper null handling details."),
            _r("Pandas GroupBy Guide", "https://pandas.pydata.org/docs/user_guide/groupby.html", "article", "optional_deep_dive", "Helpful for stronger aggregation understanding."),
        ],
    },
    flow_diagrams=[
        {"title": "Intro flow", "diagram": "Raw Data -> Load -> Clean -> Transform -> Analyze -> Use in App / AI Workflow"},
        {"title": "DataFrame flow", "diagram": "CSV/Excel/JSON -> Pandas DataFrame -> Inspect -> Clean -> Analyze"},
        {"title": "AI workflow flow", "diagram": "Raw Enterprise Data -> Clean/Transform -> Feature/Input Prep -> AI/Analytics -> Result"},
    ],
)
