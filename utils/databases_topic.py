"""Structured content for the Databases and Vector Databases topic page."""

from utils.data import TopicContent, _q, _r


DATABASES_TOPIC = TopicContent(
    key="databases",
    title="Databases and Vector Databases",
    icon="DB",
    difficulty="Easy to Medium",
    priority="Very High",
    estimated_time="4 to 5 hours",
    importance_for_movate="Very High",
    why_it_matters=(
        "Databases are essential because software systems need reliable ways to store and retrieve information. Traditional SQL and NoSQL databases "
        "support backend systems, enterprise applications, and reporting. Vector databases are especially important for AI roles because they help "
        "retrieve semantically relevant information for search, RAG, copilots, and knowledge assistants."
    ),
    detailed_sections={
        "Database basics": "Understand what a database is, why persistent storage matters, and how backend systems use databases.",
        "SQL and NoSQL foundations": "Learn relational tables, basic queries, flexible-schema stores, and when each style is useful.",
        "Vector databases": "Understand embeddings, semantic similarity, vector storage, and why modern AI apps depend on vector retrieval.",
        "AI architecture connection": "Connect databases to search, RAG, hybrid retrieval, and enterprise knowledge systems.",
        "Interview depth": "Practice short, structured explanations for SQL, NoSQL, indexing, joins, vector search, and RAG.",
    },
    common_mistakes=[
        "Explaining databases only as storage and forgetting retrieval, structure, and query patterns.",
        "Confusing SQL with SQL databases and NoSQL with only one specific product.",
        "Saying vector databases store plain text instead of vector embeddings.",
        "Not understanding why vector retrieval is useful in RAG or AI assistants.",
        "Giving SQL theory answers without any workflow or real use case.",
    ],
    code_examples={
        "Simple SQL query": """SELECT name FROM users WHERE age > 20;""",
        "Join example": """SELECT u.name, o.order_id
FROM users u
INNER JOIN orders o ON u.id = o.user_id;""",
        "RAG flow": "User Query -> Embed Query -> Search Vector DB -> Retrieve Chunks -> Send to LLM -> Answer",
    },
    interview_questions=[
        {"q": "What is a database?", "a": "A database is an organized system for storing and retrieving data persistently."},
        {"q": "What is SQL vs NoSQL?", "a": "SQL databases are relational and structured, while NoSQL databases are more flexible and often used for semi-structured or large-scale use cases."},
        {"q": "What is a vector database?", "a": "A vector database stores embeddings and supports similarity search instead of only exact matching."},
        {"q": "Why are vector DBs important in AI?", "a": "Because they help retrieve semantically relevant context for search, RAG, and AI assistants."},
        {"q": "What is RAG?", "a": "RAG stands for Retrieval-Augmented Generation and combines retrieval with LLM generation."},
    ],
    role_relevance=[
        "Storing enterprise data for apps, workflows, and reporting",
        "Supporting backend services and structured query operations",
        "Handling structured and semi-structured data in AI systems",
        "Enabling search, retrieval, and RAG through vector databases",
        "Connecting business data, knowledge sources, and AI assistants",
    ],
    learning_objectives=[
        "Understand databases from SQL foundations to modern vector search use cases.",
        "Explain relational, NoSQL, and vector database concepts in simple interview-ready language.",
        "Connect database choices to backend systems, search, and AI workflows.",
        "Be comfortable discussing RAG, semantic search, and hybrid architectures.",
    ],
    learn_sections=[
        {
            "title": "1. What is a Database",
            "summary": "A database is an organized system for storing and retrieving data. It provides persistent storage, which means the data remains available after the program stops running.",
            "points": [
                "Databases are used when apps need reliable long-term storage.",
                "They make retrieval faster and more structured than keeping everything in memory or plain files.",
                "Examples include user data, product data, logs, transactions, and knowledge records.",
            ],
            "diagram": "User -> Backend -> Database -> Backend -> User",
        },
        {
            "title": "2. Why databases are needed",
            "summary": "Databases matter because most real applications need to save information, query it later, update it safely, and support multiple users or systems.",
            "points": [
                "Backend systems need a trusted place to store business data.",
                "Reports, analytics, and AI workflows often depend on stored records.",
                "Databases help with consistency, query speed, and controlled access.",
            ],
            "callouts": [
                {"type": "info", "text": "Interview tip: say databases are not just storage, they are queryable storage with structure and rules."}
            ],
        },
        {
            "title": "3. Types of Databases",
            "summary": "The two broad beginner-friendly categories are relational databases and non-relational databases.",
            "tables": [
                {
                    "title": "Relational vs non-relational overview",
                    "markdown": """| Type | Main idea | Example use |
|---|---|---|
| Relational (SQL) | Tables with rows, columns, and relationships | Users, orders, payments |
| Non-relational (NoSQL) | Flexible schemas such as documents or key-value | Logs, events, evolving app data |""",
                }
            ],
            "points": [
                "SQL databases are usually best for structured data and relationships.",
                "NoSQL databases are useful when data shape is flexible or scale patterns differ.",
            ],
            "diagram": "Application Data -> SQL or NoSQL decision -> Store and query",
        },
    ],
    sql_sections=[
        {
            "title": "1. Relational Database Basics",
            "summary": "Relational databases store data in tables. Tables have rows and columns, and relationships can be created between tables.",
            "points": [
                "A row represents one record.",
                "A column represents one field such as name, age, or email.",
                "A primary key uniquely identifies a row.",
                "A foreign key connects one table to another table.",
            ],
            "diagram": """Users Table                 Orders Table
user_id (PK)                order_id (PK)
name                        user_id (FK)
email                       amount

Users.user_id -> Orders.user_id""",
        },
        {
            "title": "2. SQL Queries",
            "summary": "SQL is the query language used to read and manipulate relational data.",
            "points": [
                "`SELECT` reads columns from a table.",
                "`WHERE` filters rows.",
                "`ORDER BY` sorts output.",
                "`LIMIT` restricts number of rows returned.",
            ],
            "examples": [
                {"label": "Basic SQL query", "code": "SELECT name FROM users WHERE age > 20;", "language": "sql"},
                {"label": "Sort and limit", "code": "SELECT name, score FROM students ORDER BY score DESC LIMIT 5;", "language": "sql"},
            ],
            "diagram": "SQL query -> DB engine -> filter / sort / retrieve -> results",
        },
        {
            "title": "3. Joins",
            "summary": "Joins combine data from multiple tables using a related key. This is a high-frequency interview topic.",
            "points": [
                "INNER JOIN returns only matching rows from both tables.",
                "LEFT JOIN returns all rows from the left table and matching rows from the right table.",
                "RIGHT JOIN is the opposite idea at a basic level.",
            ],
            "examples": [
                {
                    "label": "INNER JOIN example",
                    "code": """SELECT u.name, o.order_id
FROM users u
INNER JOIN orders o ON u.id = o.user_id;""",
                    "language": "sql",
                },
                {
                    "label": "LEFT JOIN example",
                    "code": """SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;""",
                    "language": "sql",
                },
            ],
            "diagram": """Users      Orders
  | match on user_id |
  -> join result table""",
        },
        {
            "title": "4. GROUP BY and Aggregation",
            "summary": "Aggregation helps summarize data, while GROUP BY lets you summarize per category or key.",
            "points": [
                "`COUNT` counts records.",
                "`SUM` adds numeric values.",
                "`AVG` computes average values.",
            ],
            "examples": [
                {"label": "Count orders by user", "code": "SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;", "language": "sql"},
                {"label": "Average score by department", "code": "SELECT department, AVG(score) FROM employees GROUP BY department;", "language": "sql"},
            ],
        },
        {
            "title": "5. Normalization",
            "summary": "Normalization means organizing relational data to reduce redundancy and improve consistency.",
            "points": [
                "Instead of repeating the same details in many rows, you split data into related tables.",
                "This reduces duplication and makes updates safer.",
                "At beginner level, explain it as reducing repeated information and improving structure.",
            ],
            "diagram": "Repeated data in one table -> split into related tables -> less redundancy",
        },
        {
            "title": "6. Indexing",
            "summary": "Indexes help the database find rows faster, especially for common searches.",
            "points": [
                "Indexes improve read speed.",
                "They can add overhead to writes because the index must also be updated.",
                "A simple interview answer is that indexing is a speed optimization for lookups.",
            ],
            "diagram": "Query on indexed column -> use index -> faster lookup",
        },
        {
            "title": "7. CRUD operations",
            "summary": "CRUD stands for Create, Read, Update, Delete and maps directly to core SQL actions.",
            "points": [
                "CREATE usually maps to `INSERT`.",
                "READ usually maps to `SELECT`.",
                "UPDATE maps to `UPDATE`.",
                "DELETE maps to `DELETE`.",
            ],
            "examples": [
                {"label": "INSERT", "code": "INSERT INTO users (name, age) VALUES ('Ravi', 22);", "language": "sql"},
                {"label": "UPDATE", "code": "UPDATE users SET age = 23 WHERE name = 'Ravi';", "language": "sql"},
                {"label": "DELETE", "code": "DELETE FROM users WHERE name = 'Ravi';", "language": "sql"},
            ],
            "diagram": "CREATE -> INSERT\nREAD -> SELECT\nUPDATE -> UPDATE\nDELETE -> DELETE",
        },
    ],
    nosql_sections=[
        {
            "title": "1. What is NoSQL",
            "summary": "NoSQL refers to non-relational databases that often use flexible schemas such as documents, key-value pairs, or wide-column structures.",
            "points": [
                "NoSQL databases do not require the same fixed table structure as relational systems.",
                "They are useful when data shape changes often or the system needs a different scaling style.",
                "Examples include MongoDB and DynamoDB.",
            ],
            "diagram": "App -> NoSQL document / key-value store -> flexible retrieval",
        },
        {
            "title": "2. When to use NoSQL",
            "summary": "NoSQL is useful when data is semi-structured, evolving, or needs a flexible schema.",
            "points": [
                "Useful for logs, event data, flexible app records, or document-heavy systems.",
                "Often chosen when schema changes frequently.",
                "Can be useful when scaling patterns are different from traditional relational workloads.",
            ],
        },
        {
            "title": "3. SQL vs NoSQL comparison",
            "summary": "Both styles are useful. The right choice depends on structure, queries, scale, and consistency needs.",
            "table": """| Feature | SQL | NoSQL |
|---|---|---|
| Structure | Tables | Documents / key-value / other models |
| Schema | Usually fixed and defined | Usually more flexible |
| Relationships | Strong relational support | Often weaker or handled differently |
| Common use cases | Transactions, structured business data | Flexible app data, logs, document-heavy data |""",
            "diagram": "Structured + relational -> SQL\nFlexible + evolving -> NoSQL",
        },
    ],
    vector_db_sections=[
        {
            "title": "1. What is a Vector Database",
            "summary": "A vector database stores embeddings, which are numerical vector representations of data. It is used for similarity search instead of only exact matching.",
            "points": [
                "Vector databases are important for semantic search.",
                "They help AI systems find content that is meaningfully similar, not just text that matches exactly.",
                "This is a major building block for RAG and AI assistants.",
            ],
            "callouts": [
                {"type": "success", "text": "High-impact interview point: vector databases help LLM applications retrieve relevant context based on meaning."}
            ],
        },
        {
            "title": "2. What is an Embedding",
            "summary": "An embedding is a numerical vector representation of text or another data item. Similar meaning tends to produce vectors that are close together.",
            "points": [
                "You can think of an embedding as converting meaning into numbers.",
                "Two texts with related meaning tend to be close in vector space.",
                "Embeddings are generated by embedding models, not by the vector database itself.",
            ],
            "diagram": "Text -> Embedding model -> numeric vector",
        },
        {
            "title": "3. Why Vector DB is needed",
            "summary": "LLMs often need external context. Vector databases help retrieve the most relevant chunks of information based on semantic similarity.",
            "points": [
                "Exact keyword search is sometimes not enough.",
                "Vector search helps when wording differs but meaning is similar.",
                "This is especially useful in knowledge assistants, search, and RAG systems.",
            ],
        },
        {
            "title": "4. Similarity Search",
            "summary": "Similarity search means finding vectors that are closest to the query vector. At a beginner level, think of it as finding the most meaningfully similar content.",
            "points": [
                "Cosine similarity is a common way to compare how close two vectors are in direction.",
                "Nearest neighbors means finding the most similar stored vectors to the query vector.",
                "The result is usually a set of relevant document chunks or items.",
            ],
            "diagram": "Text -> Embedding -> Store in Vector DB -> Query embedding -> Similar results",
        },
        {
            "title": "5. Vector DB Flow",
            "summary": "This is the full retrieval pipeline used in many AI applications.",
            "diagram": "User Query -> Convert to embedding -> Search vector DB -> retrieve relevant chunks -> send to LLM -> answer",
            "examples": [
                {"label": "Pipeline idea", "code": "User Query -> Embedding Model -> Vector Search -> Retrieved Chunks -> Prompt + LLM -> Response", "language": "text"}
            ],
        },
        {
            "title": "6. Examples of Vector DB tools",
            "summary": "There are several systems used for vector search in AI applications.",
            "points": [
                "Pinecone is a managed vector database service.",
                "Weaviate is a vector database with search and schema features.",
                "FAISS is a similarity search library commonly used for local or custom setups.",
            ],
        },
        {
            "title": "7. Database vs Vector Database",
            "summary": "Traditional databases and vector databases solve different retrieval problems.",
            "table": """| System | Best for |
|---|---|
| SQL DB | Exact matching, transactions, structured records |
| NoSQL DB | Flexible schema and document-style storage |
| Vector DB | Semantic similarity and nearest-neighbor retrieval |""",
            "diagram": "SQL DB -> exact lookup\nVector DB -> semantic similarity search",
        },
    ],
    ai_use_cases=[
        {
            "title": "1. RAG (Retrieval-Augmented Generation)",
            "business_purpose": "Use retrieval to ground an LLM answer in trusted information.",
            "responsibilities": [
                "Store document chunks and embeddings.",
                "Embed the user query.",
                "Retrieve relevant chunks from the vector database.",
                "Send retrieved context to the LLM before generating the answer.",
            ],
            "why_it_helps": "This reduces unsupported answers and makes responses more grounded in actual documents.",
            "risks": "Poor chunking, poor embeddings, irrelevant retrieval, and context overload can reduce answer quality.",
            "diagram": "User Query -> Vector DB -> Relevant Docs -> LLM -> Response",
        },
        {
            "title": "2. Chatbot with knowledge base",
            "business_purpose": "Answer user questions using company knowledge instead of only model memory.",
            "responsibilities": [
                "Store enterprise documents or FAQs.",
                "Index embeddings in a vector store.",
                "Retrieve relevant knowledge during conversation.",
                "Combine retrieval with LLM response generation.",
            ],
            "why_it_helps": "The chatbot becomes more useful for real business information and policy-aware answering.",
            "risks": "Outdated docs, retrieval misses, and hallucination if context is poor.",
            "diagram": "User Question -> Embed -> Vector DB search -> Relevant knowledge -> LLM answer",
        },
        {
            "title": "3. Document search system",
            "business_purpose": "Let users search documents by meaning, not only by exact words.",
            "responsibilities": [
                "Convert documents into embeddings.",
                "Store vectors with metadata.",
                "Embed user queries and retrieve similar chunks.",
                "Return ranked semantic search results.",
            ],
            "why_it_helps": "Users can find relevant content even when the wording differs from the document text.",
            "risks": "Bad chunking, weak metadata, and poor ranking can hurt search quality.",
            "diagram": "Documents -> Chunk + Embed -> Vector DB\nUser Query -> Embed -> Similarity Search -> Ranked Results",
        },
        {
            "title": "4. Enterprise support assistant",
            "business_purpose": "Support employees or agents with internal knowledge retrieval and guided answers.",
            "responsibilities": [
                "Combine structured enterprise DB records with knowledge retrieval.",
                "Use SQL/NoSQL for exact business data and vector DB for semantic knowledge search.",
                "Return grounded responses for internal help workflows.",
            ],
            "why_it_helps": "A hybrid architecture gives both exact business facts and semantically relevant knowledge.",
            "risks": "Joining multiple systems increases complexity, latency, and validation needs.",
            "diagram": "User -> Backend -> SQL/NoSQL for exact data + Vector DB for knowledge -> LLM -> Response",
        },
        {
            "title": "5. Product search and recommendation support",
            "business_purpose": "Improve search and matching by combining structured product filters with semantic similarity.",
            "responsibilities": [
                "Use SQL or NoSQL for product inventory, price, and structured metadata.",
                "Use embeddings and vector search for semantic matching of descriptions or queries.",
                "Combine both retrieval styles for better relevance.",
            ],
            "why_it_helps": "This supports hybrid search: exact filters plus semantic similarity.",
            "risks": "Need careful ranking logic and consistent metadata across systems.",
            "diagram": "Query -> Structured filters + vector similarity -> Combined ranking -> Results",
        },
    ],
    interview_questions_detailed=[
        {"question": "What is DBMS?", "short_answer": "A DBMS is a system used to store, manage, and retrieve data.", "spoken_answer": "DBMS stands for Database Management System. It is the software layer that helps applications store data, query it, update it, and manage access efficiently."},
        {"question": "What is a database?", "short_answer": "A database is an organized system for persistent data storage and retrieval.", "spoken_answer": "A database stores data in a structured way so that applications can retrieve, update, and manage it reliably over time."},
        {"question": "Why are databases needed?", "short_answer": "Because applications need reliable long-term storage, structured retrieval, and safe updates.", "spoken_answer": "Databases matter because real systems cannot depend only on in-memory data. They need persistent storage, query support, consistency, and controlled access."},
        {"question": "What is SQL?", "short_answer": "SQL is the language used to query and manipulate relational databases.", "spoken_answer": "SQL stands for Structured Query Language. It is used for reading, inserting, updating, and deleting data in relational database systems."},
        {"question": "What is a relational database?", "short_answer": "A relational database stores structured data in tables with relationships between tables.", "spoken_answer": "A relational database organizes data in tables made of rows and columns. Relationships between tables are usually created using keys such as primary keys and foreign keys."},
        {"question": "What is a primary key?", "short_answer": "A primary key uniquely identifies a row in a table.", "spoken_answer": "A primary key is a column or set of columns used to uniquely identify each row. It helps the database maintain uniqueness and reference records reliably."},
        {"question": "What is a foreign key?", "short_answer": "A foreign key links one table to another table.", "spoken_answer": "A foreign key is a column that references the primary key of another table. It is how relational databases represent relationships between data."},
        {"question": "What is SELECT?", "short_answer": "SELECT is used to read data from a table.", "spoken_answer": "The SELECT statement is used to retrieve data from one or more tables. It is one of the most common SQL operations."},
        {"question": "What is WHERE?", "short_answer": "WHERE filters rows based on a condition.", "spoken_answer": "The WHERE clause limits results to rows that match a condition, such as users above a certain age or orders from a specific customer."},
        {"question": "What is ORDER BY?", "short_answer": "ORDER BY sorts query results.", "spoken_answer": "ORDER BY is used when you want results sorted by one or more columns, either ascending or descending."},
        {"question": "What is LIMIT?", "short_answer": "LIMIT restricts the number of rows returned.", "spoken_answer": "LIMIT is helpful when you only want the top few results, such as the first 10 rows or the top 5 ranked items."},
        {"question": "What is a join?", "short_answer": "A join combines related data from multiple tables.", "spoken_answer": "A join is used when information is split across tables and you want one combined result. For example, joining users with orders based on user ID."},
        {"question": "Difference between INNER JOIN and LEFT JOIN?", "short_answer": "INNER JOIN returns matching rows only, while LEFT JOIN keeps all rows from the left table and adds matches from the right table when available.", "spoken_answer": "INNER JOIN gives only records that match in both tables. LEFT JOIN keeps every row from the left table and adds matching right-side data if it exists, otherwise it returns nulls for missing matches."},
        {"question": "What is GROUP BY?", "short_answer": "GROUP BY groups rows by a category so aggregate functions can be applied.", "spoken_answer": "GROUP BY is used when you want summaries per category, such as count of orders by customer or average salary by department."},
        {"question": "What is normalization?", "short_answer": "Normalization is organizing data to reduce redundancy and improve consistency.", "spoken_answer": "Normalization means structuring relational data so the same information is not repeated unnecessarily in multiple places. It helps reduce duplication and update problems."},
        {"question": "What is indexing?", "short_answer": "Indexing helps the database find rows faster.", "spoken_answer": "An index is a structure that improves lookup speed for queries on selected columns. It helps reads but can add overhead to writes because indexes must also be maintained."},
        {"question": "What is NoSQL?", "short_answer": "NoSQL refers to non-relational databases with flexible data models.", "spoken_answer": "NoSQL databases are non-relational systems that may use document, key-value, or other flexible storage models. They are often useful when schema flexibility is important."},
        {"question": "When would you use NoSQL?", "short_answer": "When schema is flexible, data is semi-structured, or the workload fits a non-relational model better.", "spoken_answer": "I would consider NoSQL when the data shape changes often, when the system is document-heavy, or when the access pattern fits a flexible non-relational model better than relational tables."},
        {"question": "SQL vs NoSQL?", "short_answer": "SQL is relational and structured, while NoSQL is more flexible in schema and storage style.", "spoken_answer": "SQL databases are best known for structured tables, relationships, and strong query patterns. NoSQL databases are more flexible and are often used for document-style or evolving data models."},
        {"question": "What is a vector database?", "short_answer": "A vector database stores embeddings and supports similarity search.", "spoken_answer": "A vector database is built to store high-dimensional vectors, often embeddings of text or other data, and retrieve the most similar vectors for a query."},
        {"question": "What is an embedding?", "short_answer": "An embedding is a numerical vector representation of data that captures semantic meaning.", "spoken_answer": "An embedding converts text or another item into numbers in a way that helps the system compare meaning. Similar meanings tend to produce nearby vectors."},
        {"question": "Why are vector DBs used in AI?", "short_answer": "Because they help retrieve semantically relevant context for search, RAG, and assistants.", "spoken_answer": "Vector databases are useful in AI because exact keyword matching is often not enough. AI systems need semantically relevant context, and vector search helps retrieve it."},
        {"question": "What is similarity search?", "short_answer": "Similarity search finds stored vectors that are closest to the query vector.", "spoken_answer": "Similarity search means converting the query into an embedding and then finding the most similar stored embeddings. This helps retrieve meaningfully related content."},
        {"question": "What is semantic search?", "short_answer": "Semantic search finds results based on meaning, not just exact keyword overlap.", "spoken_answer": "Semantic search tries to understand intent or meaning by using embeddings and similarity, so it can return relevant results even when the words do not exactly match."},
        {"question": "What is RAG?", "short_answer": "RAG stands for Retrieval-Augmented Generation and combines retrieval with LLM generation.", "spoken_answer": "RAG is a pattern where the system first retrieves relevant content, often from a vector database, and then gives that content to the LLM so the final answer is better grounded."},
        {"question": "How does AI retrieve knowledge?", "short_answer": "It often uses embeddings and vector search to retrieve relevant document chunks.", "spoken_answer": "A common pipeline is to embed documents, store them in a vector database, embed the user query, retrieve similar chunks, and pass those chunks into the model as context."},
        {"question": "Difference between traditional DB and vector DB?", "short_answer": "Traditional databases focus on exact structured retrieval, while vector DBs focus on semantic similarity retrieval.", "spoken_answer": "Traditional databases are strong for exact matches, structured queries, and transactions. Vector databases are designed for similarity search over embeddings, which is useful in AI retrieval workflows."},
        {"question": "Why not store everything in SQL only?", "short_answer": "Because SQL is great for exact structured data, but semantic retrieval over embeddings needs a different retrieval style.", "spoken_answer": "SQL databases are excellent for exact lookups and structured relationships, but they are not the natural tool for high-dimensional similarity search. AI retrieval often needs vector search for semantic matching."},
        {"question": "What is hybrid architecture with DB and vector DB?", "short_answer": "It combines structured databases for exact facts with vector databases for semantic retrieval.", "spoken_answer": "A hybrid architecture is common in AI systems. SQL or NoSQL stores structured business data, while a vector database stores embeddings for semantic search. Together they support both exact and meaning-based retrieval."},
        {"question": "How does indexing help?", "short_answer": "Indexing speeds up lookups by helping the database find rows faster.", "spoken_answer": "Indexing helps because the database does not need to scan every row for common lookup patterns. It improves read performance, though it adds some write cost."},
        {"question": "Explain a real use case for vector databases.", "short_answer": "A company knowledge assistant can store document embeddings in a vector database and retrieve relevant chunks for user questions.", "spoken_answer": "A strong real example is an enterprise knowledge assistant. Company documents are chunked, embedded, and stored in a vector database. When a user asks a question, the system retrieves relevant chunks and gives them to the LLM before answering."},
    ],
    interview_scenarios=[
        {
            "question": "How would you explain frontend, backend, and database flow?",
            "approach": "Start from user action and walk through request, processing, storage, and response.",
            "answer_points": [
                "The user interacts with the frontend.",
                "The frontend sends a request to the backend.",
                "The backend applies business logic and queries or updates the database.",
                "The database returns the needed data.",
                "The backend sends the result back to the frontend.",
            ],
            "diagram": "User -> Frontend -> Backend -> Database -> Backend -> Frontend",
        },
        {
            "question": "How would you explain RAG using a vector database?",
            "approach": "Explain retrieval first, then generation, and show why context helps.",
            "answer_points": [
                "Documents are split into chunks and converted into embeddings.",
                "Those embeddings are stored in a vector database.",
                "The user query is also embedded.",
                "The system retrieves the most similar chunks.",
                "The retrieved context is sent to the LLM to produce a grounded answer.",
            ],
            "diagram": "Docs -> Chunk + Embed -> Vector DB\nUser Query -> Embed -> Retrieve -> LLM -> Response",
        },
        {
            "question": "When would you choose SQL vs NoSQL vs vector DB?",
            "approach": "Compare them by retrieval style and data shape.",
            "answer_points": [
                "Choose SQL for structured relational data and exact queries.",
                "Choose NoSQL for flexible or document-style data models.",
                "Choose vector DB for semantic similarity retrieval over embeddings.",
                "In modern AI systems, you often use them together instead of choosing only one.",
            ],
            "diagram": "Structured exact data -> SQL\nFlexible schema -> NoSQL\nSemantic retrieval -> Vector DB",
        },
        {
            "question": "How would an AI app use both a normal DB and a vector DB?",
            "approach": "Explain hybrid retrieval with exact business data plus semantic knowledge search.",
            "answer_points": [
                "Use SQL or NoSQL to store exact user, order, or product records.",
                "Use a vector database to store document or description embeddings.",
                "At query time, fetch exact facts from the structured database and semantic context from the vector database.",
                "Combine both into the final response or prompt.",
            ],
            "diagram": "User Query -> Backend -> SQL/NoSQL exact data + Vector DB semantic context -> LLM/app response",
        },
    ],
    interview_rapid_fire=[
        {"question": "Database means?", "answer": "Persistent organized storage and retrieval of data."},
        {"question": "SQL means?", "answer": "Structured Query Language for relational databases."},
        {"question": "Primary key?", "answer": "Unique identifier for a row."},
        {"question": "Foreign key?", "answer": "Column linking one table to another."},
        {"question": "JOIN does?", "answer": "Combines related rows from multiple tables."},
        {"question": "NoSQL means?", "answer": "Non-relational flexible data storage style."},
        {"question": "Vector DB stores?", "answer": "Embeddings or vectors."},
        {"question": "Embedding is?", "answer": "A numeric representation of meaning."},
        {"question": "RAG means?", "answer": "Retrieve relevant context, then generate."},
        {"question": "Semantic search means?", "answer": "Search by meaning, not only exact words."},
    ],
    interview_common_mistakes=[
        "Confusing a database with the query language used on it.",
        "Not being able to explain keys and joins simply.",
        "Thinking NoSQL means no structure at all.",
        "Saying vector databases store plain text instead of embeddings.",
        "Failing to connect vector search to RAG and AI retrieval workflows.",
    ],
    quick_revision_points=[
        "A database stores and retrieves data persistently.",
        "Databases are used because applications need reliable long-term storage.",
        "SQL databases are relational and table-based.",
        "NoSQL databases are non-relational and often more flexible.",
        "A table has rows and columns.",
        "A primary key uniquely identifies a row.",
        "A foreign key connects related tables.",
        "SELECT reads data.",
        "WHERE filters rows.",
        "ORDER BY sorts results.",
        "LIMIT restricts result count.",
        "INNER JOIN returns matching rows from both tables.",
        "LEFT JOIN keeps all rows from the left table.",
        "GROUP BY is used for category-wise aggregation.",
        "COUNT, SUM, and AVG are common aggregate functions.",
        "Normalization reduces redundancy.",
        "Indexing helps faster reads.",
        "Indexes can add write overhead.",
        "CRUD maps to INSERT, SELECT, UPDATE, and DELETE.",
        "NoSQL is useful for flexible or evolving data models.",
        "Vector databases store embeddings.",
        "Embeddings represent semantic meaning as numbers.",
        "Similarity search finds nearby vectors.",
        "Semantic search finds meaningfully relevant content.",
        "Vector databases are important for RAG.",
        "RAG means retrieve first, then generate.",
        "SQL is strong for exact structured data retrieval.",
        "Vector DB is strong for semantic retrieval.",
        "Hybrid systems often use both structured DBs and vector DBs.",
        "Vector DB + RAG is a high-impact topic for AI interviews.",
    ],
    quiz_questions=[
        _q("What does a primary key do?", ["Sorts rows", "Uniquely identifies a row", "Deletes data", "Stores embeddings"], 1, "A primary key uniquely identifies a record in a table."),
        _q("What is the main use of INNER JOIN?", ["To remove duplicates", "To combine matching rows from two tables", "To create an index", "To export CSV"], 1, "INNER JOIN combines rows that match based on a join condition."),
        _q("Which is a NoSQL database example?", ["PostgreSQL", "MySQL", "MongoDB", "SQLite"], 2, "MongoDB is a common document-oriented NoSQL database."),
        _q("What does a vector database mainly store?", ["Only PDFs", "Embeddings or vectors", "Only SQL queries", "Only API keys"], 1, "Vector databases store numerical vectors used for similarity search."),
        _q("What is an embedding?", ["A CSS style", "A database backup", "A numeric representation of meaning", "A SQL join"], 2, "Embeddings convert content into vectors that capture semantic meaning."),
        _q("What is RAG?", ["Random Access Grid", "Retrieve And Group", "Retrieval-Augmented Generation", "Relational API Gateway"], 2, "RAG retrieves relevant context first and then uses it during generation."),
        _q("SQL is generally strongest for what?", ["Semantic similarity only", "Exact structured queries and relations", "Image editing", "Tokenization"], 1, "SQL databases are strongest for structured exact data and relational querying."),
        _q("Why use a vector DB in an AI app?", ["To make UI colorful", "To retrieve semantically relevant context", "To replace all backend code", "To avoid embeddings"], 1, "Vector databases are useful because they support semantic retrieval for AI applications."),
    ],
    resources=[
        _r("W3Schools SQL Tutorial", "https://www.w3schools.com/sql/", "article", "must_read", "Quick SQL basics reference."),
        _r("Pinecone Learn", "https://www.pinecone.io/learn/", "article", "must_read", "Good vector DB and RAG explainers."),
        _r("FAISS Getting Started", "https://github.com/facebookresearch/faiss/wiki/Getting-started", "article", "practice", "Basic local vector search introduction."),
        _r("freeCodeCamp SQL Videos", "https://www.youtube.com/results?search_query=freecodecamp+sql", "video", "must_watch", "Beginner-friendly SQL videos."),
    ],
    resource_sections={
        "Must watch first": [
            _r("freeCodeCamp SQL Videos", "https://www.youtube.com/results?search_query=freecodecamp+sql", "video", "must_watch", "Good beginner-friendly SQL tutorials."),
            _r("Vector DB Explainer Videos", "https://www.youtube.com/results?search_query=vector+database+explained", "video", "must_watch", "Helpful conceptual videos for vector search."),
            _r("RAG Tutorial Videos", "https://www.youtube.com/results?search_query=RAG+tutorial+beginner", "video", "must_watch", "Good walkthroughs of retrieval plus generation."),
        ],
        "Must read first": [
            _r("W3Schools SQL Tutorial", "https://www.w3schools.com/sql/", "article", "must_read", "Quick SQL basics reference."),
            _r("GeeksforGeeks DBMS Tutorial", "https://www.geeksforgeeks.org/dbms/", "article", "must_read", "Broad DBMS basics."),
            _r("Pinecone Learn", "https://www.pinecone.io/learn/", "article", "must_read", "Good intuitive explainers on embeddings, vector DBs, and RAG."),
            _r("MongoDB NoSQL Basics", "https://www.mongodb.com/nosql-explained", "article", "must_read", "Simple NoSQL explanation."),
        ],
        "Practice / explore": [
            _r("SQLBolt", "https://sqlbolt.com/", "article", "practice", "Interactive SQL practice."),
            _r("FAISS Getting Started", "https://github.com/facebookresearch/faiss/wiki/Getting-started", "article", "practice", "Basic local vector search introduction."),
            _r("Pinecone Learn: Vector Embeddings", "https://www.pinecone.io/learn/vector-embeddings/", "article", "practice", "Helpful embedding intuition."),
        ],
        "Optional deep dive": [
            _r("PostgreSQL Documentation", "https://www.postgresql.org/docs/", "article", "optional_deep_dive", "Useful if you want more SQL depth."),
            _r("Weaviate Concepts", "https://weaviate.io/developers/weaviate/concepts", "article", "optional_deep_dive", "Vector database and search concepts."),
            _r("Pinecone Learn: Retrieval-Augmented Generation", "https://www.pinecone.io/learn/retrieval-augmented-generation/", "article", "optional_deep_dive", "Clear RAG walkthrough."),
        ],
    },
    flow_diagrams=[
        {"title": "Frontend to DB flow", "diagram": "Frontend -> Backend -> Database -> Backend -> Frontend"},
        {"title": "SQL query execution flow", "diagram": "SQL Query -> DB Engine -> Parse / Plan / Execute -> Result"},
        {"title": "Vector retrieval flow", "diagram": "Text -> Embedding -> Store in Vector DB -> Query -> Similar Results"},
        {"title": "RAG flow", "diagram": "User Query -> Embed -> Vector DB -> Relevant Chunks -> LLM -> Response"},
        {"title": "Hybrid architecture", "diagram": "App -> Structured DB for exact data + Vector DB for semantic retrieval -> Final response"},
    ],
)
