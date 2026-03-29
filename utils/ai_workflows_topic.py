"""Structured content for the AI Workflows topic page."""

from utils.data import TopicContent, _q, _r


AI_WORKFLOWS_TOPIC = TopicContent(
    key="ai_workflows",
    title="AI Workflows",
    icon="WF",
    difficulty="Medium",
    priority="Very High",
    estimated_time="4 to 5 hours",
    importance_for_movate="Very High",
    why_it_matters=(
        "An AI workflow is the end-to-end sequence of steps around the model: data or user input, preprocessing, prompt creation, retrieval, "
        "tool usage, model calls, validation, storage, logging, and improvement. For a Movate AI Engineer role, this matters because real AI "
        "products are built as usable workflows, not isolated prompts."
    ),
    detailed_sections={
        "Workflow mindset": "Understand that AI systems are pipelines of connected steps, not just one model call.",
        "Workflow building blocks": "Learn the role of preprocessing, prompting, retrieval, tools, post-processing, validation, and logging.",
        "System design": "See how frontend, backend, models, databases, tools, and monitoring fit together.",
        "Evaluation and iteration": "Strong AI systems are tested, measured, improved, and monitored continuously.",
        "Interview communication": "Explain workflows as sequences, trade-offs, and reliability decisions, not just buzzwords.",
    },
    common_mistakes=[
        "Describing only the model and ignoring the full workflow around it.",
        "Skipping preprocessing, validation, and post-processing in interview answers.",
        "Confusing an AI workflow with just calling one API.",
        "Ignoring evaluation, logging, and feedback loops.",
        "Adding retrieval, tools, or agents without explaining when they are actually needed.",
    ],
    code_examples={
        "Basic workflow": "User Input -> Preprocess -> Prompt -> Model -> Post-process -> Validate -> Response",
        "RAG workflow": "User Query -> Retrieve Relevant Docs -> Build Prompt -> Model -> Answer",
        "Evaluation loop": "Design -> Test -> Review -> Improve -> Re-test",
    },
    interview_questions=[
        {"q": "What is an AI workflow?", "a": "It is the sequence of steps used to solve a problem using AI, including input, processing, model use, validation, and output handling."},
        {"q": "Why is AI workflow more than a prompt?", "a": "Because real systems also need preprocessing, retrieval, tools, validation, logging, and iteration."},
        {"q": "What is RAG in a workflow?", "a": "RAG retrieves relevant context before generation so the answer is better grounded."},
        {"q": "Why does evaluation matter?", "a": "Because AI outputs can look good but still be wrong, unsafe, or unhelpful."},
        {"q": "Why are logs important in AI systems?", "a": "Logs help debugging, monitoring, comparison, and workflow improvement."},
    ],
    role_relevance=[
        "Experimenting with AI solutions and prompt pipelines",
        "Integrating prompts, tools, APIs, retrieval, and data flows",
        "Building usable enterprise AI workflows rather than isolated demos",
        "Evaluating outputs and iterating on quality",
        "Supporting automation and business workflows with AI",
    ],
    learning_objectives=[
        "Understand AI workflows from input to evaluation and improvement.",
        "Explain how prompts, retrieval, tools, validation, and storage fit together.",
        "Describe real AI system architectures in interview-friendly language.",
        "Connect workflow design with reliability, monitoring, and enterprise use cases.",
    ],
    learn_sections=[
        {
            "title": "1. What is an AI Workflow",
            "summary": "An AI workflow is the sequence of steps used to solve a problem using AI. It includes data, prompts, models, logic, validation, and output handling.",
            "points": [
                "Real AI apps are systems, not single prompts.",
                "A good analogy is cooking: ingredients go in, steps happen, the dish is tasted, and then improved if needed.",
                "An AI workflow usually has both AI parts and normal software parts.",
            ],
            "diagram": "User Need -> Data/Input -> AI Processing -> Output -> Evaluation -> Improvement",
        },
        {
            "title": "2. Core Building Blocks of AI Workflows",
            "summary": "A practical AI workflow is made of connected blocks, each with a specific role.",
            "subtopics": [
                {"title": "User input", "content": ["The problem starts with a user message, document, file, or system event.", "Example: a user asks a support question or uploads a PDF."]},
                {"title": "Preprocessing", "content": ["Input may need cleaning, parsing, chunking, normalization, or metadata extraction.", "Example: extract text from a PDF before using it."]},
                {"title": "Prompt construction", "content": ["The final prompt may combine system rules, user question, format instructions, and retrieved context.", "Example: add company policy context before asking the model to answer."]},
                {"title": "Model/API call", "content": ["The workflow sends the prepared request to a model or AI API.", "The model call is only one step in the full workflow."]},
                {"title": "Retrieval", "content": ["Some workflows fetch external context from docs, search, or vector databases.", "This improves grounding."]},
                {"title": "Tool usage", "content": ["Some workflows call tools like search, calculators, DB queries, or external APIs.", "This expands what the system can do."]},
                {"title": "Post-processing", "content": ["The raw output may be reformatted, cleaned, or converted into structured fields.", "This makes the answer usable by the UI or backend."]},
                {"title": "Validation", "content": ["The system may check format, business rules, or safety before returning the output.", "This improves reliability."]},
                {"title": "Storage and logging", "content": ["Prompts, responses, scores, and errors may be stored for debugging and improvement.", "This supports monitoring and evaluation."]},
                {"title": "User-facing response", "content": ["The final result is shown to the user or sent to another system.", "This should be clear, safe, and useful."]},
            ],
            "diagram": """User Input
  ↓
Preprocessing
  ↓
Prompt / Context Builder
  ↓
Model / Tool / Retrieval
  ↓
Post-processing
  ↓
Validation / Guardrails
  ↓
Response / Storage / Logging""",
        },
        {
            "title": "3. Input and Preprocessing",
            "summary": "Raw user input is often not enough. Inputs may need cleanup, filtering, parsing, chunking, or metadata extraction first.",
            "points": [
                "Documents may need text extraction before the model can use them.",
                "Structured data may need normalization or column cleanup.",
                "Conversation input may need trimming or formatting before prompt construction.",
            ],
            "examples": [
                {"label": "Preprocessing examples", "code": "PDF -> parse text\nCSV -> clean columns\nUser query -> trim, classify intent, attach metadata", "language": "text"}
            ],
        },
        {
            "title": "4. Prompt Construction",
            "summary": "Prompt creation is often dynamic. The workflow may combine instructions, user content, retrieved context, formatting rules, and safety notes.",
            "points": [
                "Prompt quality affects output quality.",
                "Retrieved context often changes prompt content for each request.",
                "The workflow may add output format constraints such as JSON or bullet points.",
            ],
            "diagram": "System Instructions + User Question + Retrieved Context + Output Rules -> Final Prompt",
        },
        {
            "title": "5. Model Interaction",
            "summary": "The app sends the prepared request to a model or API and receives generated output.",
            "points": [
                "Model output is probabilistic, so the answer may be useful, wrong, incomplete, or hallucinated.",
                "This is why the model call should be treated as one part of the workflow, not the whole workflow.",
            ],
            "callouts": [
                {"type": "warning", "text": "Interview tip: never describe a real AI system as only 'send prompt to model and show answer'."}
            ],
        },
        {
            "title": "6. Retrieval in AI Workflows",
            "summary": "Retrieval brings in relevant external context such as document chunks, FAQs, or knowledge base items.",
            "points": [
                "Retrieval is commonly used in RAG systems.",
                "It reduces hallucination by grounding the answer in retrieved information.",
            ],
            "diagram": "User Query -> Retrieve Relevant Docs -> Build Prompt -> Model -> Answer",
        },
        {
            "title": "7. Tool Use in AI Workflows",
            "summary": "Some workflows need tools, not just text generation. Tools expand capability.",
            "points": [
                "Tools may include search, calculator, DB query, file parser, calendar API, or email API.",
                "Tool use is important when the model must act on the world or fetch exact data.",
            ],
            "diagram": "User Request -> Model decides tool -> Tool/API call -> Result -> Final response",
        },
        {
            "title": "8. Post-processing",
            "summary": "Post-processing turns raw model output into something more usable and reliable.",
            "points": [
                "This can include cleaning text, formatting sections, extracting structured fields, or applying business rules.",
                "It hides raw model noise and makes the response UI-ready or system-ready.",
            ],
        },
        {
            "title": "9. Validation and Guardrails",
            "summary": "AI output should not always be trusted directly. Validation checks whether the output is acceptable before use.",
            "points": [
                "Guardrails may include format checks, business rule checks, source requirements, safety filters, or human review.",
                "Validation improves reliability and helps reduce risky output.",
            ],
            "diagram": "Model Output -> Format / Rule / Safety Checks -> Accept or Revise / Escalate",
        },
        {
            "title": "10. Logging, Feedback, and Storage",
            "summary": "Logs and stored results help debugging, comparison, and improvement.",
            "points": [
                "Store prompts, responses, scores, errors, latency, and user feedback when appropriate.",
                "Logs help identify failure patterns and compare workflow versions.",
                "Feedback helps improve prompts, retrieval, validation, and business value.",
            ],
        },
        {
            "title": "11. Human-in-the-Loop",
            "summary": "Some outputs need human approval before final action. This is common in business-critical systems.",
            "points": [
                "Useful for high-risk actions such as finance, customer communication, or compliance-heavy content.",
                "Human review improves trust and safety.",
            ],
            "diagram": "Input -> AI Draft -> Human Review -> Approve/Edit -> Final Output",
        },
        {
            "title": "12. End-to-End AI Workflow Example",
            "summary": "Enterprise document Q&A assistant: user asks a question, system retrieves document chunks, builds prompt, gets answer, validates it, logs the result, and shows the response.",
            "diagram": "User Question -> Retrieve Doc Chunks -> Build Prompt -> Model Answer -> Validate/Format -> Log -> Show Answer",
            "examples": [
                {"label": "Enterprise document Q&A flow", "code": "User asks question\n-> system retrieves relevant chunks\n-> prompt is built\n-> model answers\n-> response is validated and formatted\n-> logs stored\n-> answer shown to user", "language": "text"}
            ],
        },
        {
            "title": "13. Why AI Workflows Matter for AI Engineers",
            "summary": "AI Engineers work on the whole workflow: prompt pipelines, retrieval, APIs, agents, validation, testing, monitoring, and iteration.",
            "points": [
                "They design prompt pipelines and structured output flows.",
                "They connect models with APIs, tools, vector databases, and business logic.",
                "They improve workflow reliability through evaluation and iteration.",
            ],
            "callouts": [
                {"type": "success", "text": "High-value interview framing: AI Engineers build systems around models, not just prompts to models."}
            ],
        },
    ],
    workflow_types=[
        {
            "title": "1. Prompt-Only Workflow",
            "summary": "This is the simplest workflow: user input goes directly into a prompt, then the model returns a response.",
            "points": [
                "Simple and fast to build.",
                "Good for prototypes or low-risk use cases.",
                "Limited grounding and lower reliability if the task needs external facts.",
            ],
            "diagram": "User Input -> Prompt -> Model -> Response",
        },
        {
            "title": "2. Prompt + Backend Logic Workflow",
            "summary": "The backend transforms input, constructs the prompt programmatically, and post-processes the model result.",
            "points": [
                "Useful when app logic or formatting rules matter.",
                "The backend can enrich the prompt and validate the output.",
            ],
            "diagram": "User Input -> Backend Logic -> Prompt Builder -> Model -> Post-process -> Response",
        },
        {
            "title": "3. RAG Workflow",
            "summary": "RAG retrieves relevant documents or chunks and injects them into the prompt before generation.",
            "points": [
                "Useful when answers should come from trusted documents.",
                "Improves grounding and reduces hallucination.",
            ],
            "diagram": "User Query -> Retrieve Relevant Docs -> Build Prompt -> Model -> Answer",
        },
        {
            "title": "4. Document Processing Workflow",
            "summary": "This workflow handles uploaded or stored documents and runs extraction, summarization, or classification.",
            "points": [
                "Often used for reports, contracts, tickets, or enterprise files.",
                "Needs parsing, chunking, and validation steps.",
            ],
            "diagram": "Upload File -> Extract Text -> Clean/Chunk -> Summarize/Classify/Extract -> Output",
        },
        {
            "title": "5. Chatbot Workflow",
            "summary": "A chatbot workflow combines user message, conversation history, instructions, and sometimes retrieval or memory.",
            "points": [
                "History and system instructions influence answer quality.",
                "May include grounding from knowledge sources.",
            ],
            "diagram": "User Message + History + Instructions -> Prompt -> Model -> Response",
        },
        {
            "title": "6. Agentic Workflow",
            "summary": "An agentic workflow may plan steps, call tools, observe results, and continue until the task is complete.",
            "points": [
                "Useful when multi-step action is needed.",
                "More powerful, but also more complex and risky than simpler workflows.",
            ],
            "diagram": "Goal -> Plan -> Tool Call -> Observe -> Next Step -> Final Output",
        },
        {
            "title": "7. Human-in-the-Loop Workflow",
            "summary": "AI drafts the output, but a human reviews before final action is taken.",
            "points": [
                "Useful for high-risk outputs.",
                "Improves trust and control.",
            ],
            "diagram": "Input -> AI Draft -> Human Review -> Final Action",
        },
        {
            "title": "8. Batch vs Real-time AI Workflow",
            "summary": "Some workflows run immediately for each user request, while others process data in batches.",
            "table": """| Type | Meaning | Good for |
|---|---|---|
| Batch | Process many items together later | Bulk summarization, nightly analytics |
| Real-time | Process one request quickly as it comes | Chatbots, assistants, user-facing tools |""",
            "points": [
                "Batch workflows optimize throughput.",
                "Real-time workflows optimize responsiveness.",
            ],
        },
        {
            "title": "9. When a Simple Workflow Is Better Than a Complex One",
            "summary": "Do not add retrieval, agents, or tools unless the problem truly needs them.",
            "points": [
                "Start simple and add complexity only when needed.",
                "A simpler workflow is often easier to test, explain, and maintain.",
            ],
        },
    ],
    system_design_sections=[
        {
            "title": "1. AI App Architecture Components",
            "summary": "A practical AI system often includes frontend, backend, model API, database, vector database, storage, logging, and monitoring.",
            "points": [
                "Frontend handles user interaction.",
                "Backend orchestrates logic, prompts, retrieval, and tool calls.",
                "Model API performs generation or prediction.",
                "Databases and vector databases store exact and semantic data.",
                "Logging and monitoring help reliability and improvement.",
            ],
            "diagram": "Frontend -> Backend -> Model API / DB / Vector DB / Tools -> Backend -> Frontend",
        },
        {
            "title": "2. Example Architecture: AI Q&A Assistant",
            "summary": "A Q&A assistant usually combines frontend, backend, vector retrieval, model call, and logging.",
            "diagram": "User -> Frontend -> Backend -> Vector DB retrieval -> Prompt Builder -> Model -> Response + Logs",
        },
        {
            "title": "3. Example Architecture: Meeting Scheduler AI",
            "summary": "A meeting scheduler combines natural language understanding with calendar APIs and business rules.",
            "diagram": "User -> Frontend -> Backend -> Calendar API + Rules + AI component -> Response",
        },
        {
            "title": "4. Example Architecture: Document Analyzer",
            "summary": "A document analyzer handles upload, storage, parsing, AI processing, result storage, and response rendering.",
            "diagram": "Upload -> Storage -> Parser -> AI Processor -> Result Store -> UI Response",
        },
        {
            "title": "5. Data Flow Thinking",
            "summary": "Good system design means knowing where data enters, where context is added, where validation happens, and where outputs are stored.",
            "points": [
                "Track where the workflow adds context.",
                "Know where the system makes decisions.",
                "Know which parts are exact logic and which parts are probabilistic AI steps.",
            ],
        },
        {
            "title": "6. Failure Points in AI Systems",
            "summary": "AI systems can fail at many points, not just at the model.",
            "points": [
                "Bad input",
                "Retrieval failure",
                "Model hallucination",
                "Tool or API failure",
                "Bad formatting",
                "Latency",
                "Missing validation",
            ],
            "diagram": "Input issue / Retrieval miss / Model error / Tool failure -> Bad output unless checks exist",
        },
    ],
    evaluation_sections=[
        {
            "title": "1. Why Evaluation Matters",
            "summary": "AI outputs can look good but still be wrong, unsafe, or unhelpful. Evaluation helps measure usefulness instead of trusting appearances.",
            "points": [
                "A fluent answer is not always a correct answer.",
                "Evaluation helps compare workflow versions.",
            ],
        },
        {
            "title": "2. Types of Evaluation",
            "summary": "There are several beginner-friendly ways to evaluate AI workflows.",
            "points": [
                "Manual review",
                "Correctness checks",
                "Format checks",
                "Relevance",
                "Helpfulness",
                "Latency",
                "Consistency",
            ],
        },
        {
            "title": "3. Experimentation Cycle",
            "summary": "A workflow is rarely perfect on the first attempt. You build, test, compare, refine, deploy, monitor, and improve.",
            "diagram": "Design -> Test -> Review -> Improve -> Re-test",
        },
        {
            "title": "4. Prompt Iteration",
            "summary": "Prompt iteration means refining wording, constraints, output format, and context quality to improve results.",
            "points": [
                "Improve instructions when output is vague.",
                "Improve constraints when output is inconsistent.",
                "Improve context when retrieval is weak.",
            ],
        },
        {
            "title": "5. Retrieval Evaluation",
            "summary": "Retrieved documents must be relevant. If retrieval quality is poor, answer quality will usually also be poor.",
            "points": [
                "Check whether the retrieved chunks actually support the answer.",
                "Poor retrieval often causes grounded systems to still fail.",
            ],
            "diagram": "Query -> Retrieval -> Relevant or irrelevant context -> Answer quality changes",
        },
        {
            "title": "6. Workflow Improvement Strategies",
            "summary": "There are several ways to improve an AI workflow beyond only changing the model.",
            "points": [
                "Improve prompts",
                "Improve context quality",
                "Add validation",
                "Simplify unnecessary steps",
                "Add human review for risky outputs",
                "Reduce unnecessary complexity",
            ],
        },
        {
            "title": "7. Logging and Monitoring",
            "summary": "Monitoring helps teams watch response quality, latency, failure rate, and user feedback after deployment.",
            "points": [
                "Track quality and failure patterns over time.",
                "Use logs to debug bad responses or workflow breaks.",
                "Changing business needs and user behavior may require workflow updates.",
            ],
            "diagram": "Deploy -> Monitor quality/latency/failures -> Identify issues -> Improve workflow",
        },
    ],
    interview_questions_detailed=[
        {"question": "What is an AI workflow?", "short_answer": "An AI workflow is the end-to-end sequence of steps used to solve a problem using AI.", "spoken_answer": "An AI workflow is the full sequence around the model, including input handling, preprocessing, prompt building, retrieval or tools if needed, model interaction, validation, logging, and response delivery."},
        {"question": "Why is an AI workflow more than just a prompt?", "short_answer": "Because real systems also need preprocessing, logic, validation, retrieval, logging, and iteration.", "spoken_answer": "A prompt is only one part of a real AI system. Real workflows also manage context, tool access, validation, formatting, storage, evaluation, and improvement over time."},
        {"question": "What are the core components of an AI workflow?", "short_answer": "Input, preprocessing, prompt or context building, model interaction, retrieval or tools, post-processing, validation, logging, and response handling.", "spoken_answer": "A useful way to explain it is as a pipeline: input comes in, it is prepared, the prompt or context is built, the model or tools are called, the result is cleaned and validated, then logs are stored and the final answer is returned."},
        {"question": "What is preprocessing?", "short_answer": "Preprocessing is the step where raw input is cleaned, formatted, or transformed before AI processing.", "spoken_answer": "Preprocessing prepares raw input so the workflow can use it properly. That might mean parsing a document, cleaning text, chunking content, extracting metadata, or normalizing structured data."},
        {"question": "Why is prompt construction important?", "short_answer": "Because prompt structure affects output quality, clarity, and reliability.", "spoken_answer": "Prompt construction matters because the workflow often needs to combine instructions, the user question, retrieved context, and output constraints. Better prompt design usually improves output quality."},
        {"question": "What is post-processing?", "short_answer": "Post-processing converts raw model output into a cleaner or more usable result.", "spoken_answer": "Post-processing may format the answer, extract structured fields, remove noise, apply business rules, or transform the result into something the UI or backend can actually use."},
        {"question": "What is validation in AI workflows?", "short_answer": "Validation checks whether the AI output meets expected rules before it is used.", "spoken_answer": "Validation is important because model output is not always trustworthy. The system may check format, required fields, safety, business rules, or source support before returning the final answer."},
        {"question": "Why are guardrails important?", "short_answer": "Guardrails improve reliability and reduce harmful, invalid, or unsafe outputs.", "spoken_answer": "Guardrails matter because AI systems are probabilistic. Without checks, they may return bad formatting, unsupported answers, or risky content. Guardrails help control that risk."},
        {"question": "What is retrieval?", "short_answer": "Retrieval means fetching relevant external context to support the AI workflow.", "spoken_answer": "Retrieval usually means searching documents, a vector database, or another source to bring relevant information into the workflow before or during generation."},
        {"question": "What is a RAG workflow?", "short_answer": "RAG is Retrieval-Augmented Generation, where relevant context is retrieved and then used during generation.", "spoken_answer": "In a RAG workflow, the system first retrieves relevant content, often through vector search, and then includes that content in the prompt so the model can answer with better grounding."},
        {"question": "What is a prompt-only workflow?", "short_answer": "It is the simplest workflow where user input goes directly to the model through a prompt.", "spoken_answer": "A prompt-only workflow is simple and fast, but it has limited grounding and may be weaker when the task needs external facts, exact data, or validation."},
        {"question": "What is an agentic workflow?", "short_answer": "An agentic workflow is a multi-step workflow where the system may plan, use tools, observe results, and continue.", "spoken_answer": "Agentic workflows go beyond one-shot generation. The system may reason about what to do next, call tools, inspect results, and keep working until the task is complete."},
        {"question": "What is human-in-the-loop?", "short_answer": "It means a human reviews or approves AI output before final action.", "spoken_answer": "Human-in-the-loop is used when AI output is useful but should not be trusted automatically, especially in business-critical or risky workflows."},
        {"question": "Why does evaluation matter?", "short_answer": "Because AI outputs can sound good while still being wrong or unhelpful.", "spoken_answer": "Evaluation matters because fluent output is not enough. Teams need ways to measure correctness, relevance, formatting, safety, latency, and overall usefulness."},
        {"question": "How do you improve an AI workflow?", "short_answer": "Improve prompts, context, validation, logging, workflow design, and sometimes human review.", "spoken_answer": "Workflow improvement often comes from multiple changes: refining prompts, improving retrieval quality, adding validation, simplifying unnecessary steps, and monitoring failures more carefully."},
        {"question": "What are common failure points in AI systems?", "short_answer": "Bad input, retrieval failure, hallucination, tool failure, bad formatting, latency, and missing validation.", "spoken_answer": "AI systems can fail at many points, not only the model. Inputs may be messy, retrieval may miss useful context, tools may fail, outputs may be badly formatted, or latency may become too high."},
        {"question": "How would you build a document Q&A assistant?", "short_answer": "Parse documents, chunk them, retrieve relevant chunks for the query, build a prompt, generate an answer, validate it, and log results.", "spoken_answer": "A common workflow is to ingest documents, split them into chunks, create embeddings, store them for retrieval, then at query time retrieve relevant chunks, build a grounded prompt, generate an answer, validate and log it, and return the result."},
        {"question": "How would you build a chatbot workflow?", "short_answer": "Combine user input, conversation history, system instructions, optional retrieval, model call, and response handling.", "spoken_answer": "A chatbot workflow usually includes the latest user message, prior conversation context, system instructions, and sometimes retrieval or tool calls. Then it generates the response, formats it, and stores logs if needed."},
        {"question": "Why are logs important in AI systems?", "short_answer": "Logs help debugging, monitoring, evaluation, and iteration.", "spoken_answer": "Without logs it is hard to understand why a workflow failed or improved. Logs help track prompts, outputs, latency, errors, and feedback across versions."},
        {"question": "What is the role of backend in AI workflows?", "short_answer": "The backend orchestrates prompts, retrieval, tools, validation, storage, and model calls.", "spoken_answer": "The backend is usually the workflow engine. It receives input, prepares prompts, handles API calls, retrieval, validation, logging, and then returns a cleaned response to the frontend."},
        {"question": "Why use a vector database?", "short_answer": "To retrieve semantically relevant information using embeddings.", "spoken_answer": "A vector database is useful when the workflow needs semantic retrieval. It helps find relevant chunks by meaning instead of only exact keyword matching."},
        {"question": "Why use APIs in AI workflows?", "short_answer": "APIs connect the workflow to models, tools, data sources, and enterprise systems.", "spoken_answer": "AI workflows often depend on model APIs, search APIs, calendar APIs, databases, and other services. APIs are the way those parts communicate."},
        {"question": "What is the difference between workflow and model?", "short_answer": "The model is one component; the workflow is the full sequence around it.", "spoken_answer": "A model produces output, but a workflow includes everything around the model such as input preparation, retrieval, validation, post-processing, logging, and delivery."},
        {"question": "Why not trust raw model output directly?", "short_answer": "Because it may be wrong, unsafe, incomplete, or badly formatted.", "spoken_answer": "Model output is probabilistic and not always reliable. That is why validation, guardrails, and sometimes human review are needed."},
        {"question": "What is prompt iteration?", "short_answer": "Prompt iteration means improving prompt wording, structure, and constraints over time.", "spoken_answer": "Prompt iteration is part of workflow improvement. You test outputs, adjust instructions or format rules, and compare results to improve quality."},
        {"question": "What is retrieval evaluation?", "short_answer": "It checks whether the retrieved context is actually relevant and useful.", "spoken_answer": "Retrieval evaluation matters because poor retrieval leads to poor grounded answers. Even a strong model will struggle if the retrieved documents are irrelevant."},
        {"question": "What is structured output validation?", "short_answer": "It checks whether output follows the required schema or format.", "spoken_answer": "If a workflow expects JSON, fields, or a specific format, structured output validation checks that the result matches the expected structure before it is used."},
        {"question": "What is monitoring in AI systems?", "short_answer": "Monitoring tracks quality, latency, failures, and other workflow signals after deployment.", "spoken_answer": "Monitoring helps teams see whether the workflow is still working well in production. It tracks things like error rate, response quality, latency, and user feedback."},
        {"question": "What is the difference between batch and real-time AI workflows?", "short_answer": "Batch workflows process many items together later, while real-time workflows respond immediately to user requests.", "spoken_answer": "Batch workflows are useful for offline or scheduled processing, while real-time workflows are useful when the user expects a quick response such as in chat or assistants."},
        {"question": "When is a simple workflow enough?", "short_answer": "When the task is low-risk, narrow, and does not need retrieval, tools, or complex orchestration.", "spoken_answer": "A simple workflow is often enough when the task is straightforward and the system does not need external context or multi-step behavior. Starting simple is usually a good engineering approach."},
        {"question": "How does an AI Engineer contribute to workflow design?", "short_answer": "By designing prompts, retrieval, integrations, validation, evaluation, and iteration loops.", "spoken_answer": "AI Engineers work across the workflow: they connect data, prompts, APIs, vector search, model calls, validation rules, logging, and evaluation so the system becomes useful and reliable."},
        {"question": "What enterprise use cases can use AI workflows?", "short_answer": "Chatbots, document assistants, ticket helpers, internal copilots, report generation, and workflow automation.", "spoken_answer": "Enterprise AI workflows are used in support assistants, document Q&A, internal knowledge search, meeting scheduling, report generation, and many productivity or automation tools."},
        {"question": "What is grounding?", "short_answer": "Grounding means tying the output to trusted context or sources.", "spoken_answer": "Grounding means giving the workflow reliable context from documents, databases, or tools so the final answer is based on real information rather than only the model's general patterns."},
        {"question": "What is output post-processing?", "short_answer": "It is the step where raw model output is cleaned, reformatted, or transformed before final use.", "spoken_answer": "Post-processing helps convert raw model output into something usable for the UI, the backend, or another system. It may involve formatting, field extraction, or applying business logic."},
        {"question": "How do you reduce hallucination in workflows?", "short_answer": "Improve prompts, add retrieval, use validation, apply guardrails, and use human review where needed.", "spoken_answer": "Reducing hallucination often requires multiple steps: stronger prompts, better grounding through retrieval, output validation, source-aware policies, and human review in sensitive cases."},
        {"question": "Why is preprocessing important in real AI systems?", "short_answer": "Because raw input is often messy or incomplete and needs preparation before use.", "spoken_answer": "Preprocessing matters because models work better when the workflow sends clean, structured, and relevant input. Many workflow problems begin earlier than the model step."},
        {"question": "Why is a workflow mindset important for interviews?", "short_answer": "Because it shows you understand real AI systems, not just isolated model calls.", "spoken_answer": "Interviewers want to see whether you can think in systems. A workflow mindset shows that you understand how data, prompts, retrieval, APIs, tools, validation, and feedback all work together."},
    ],
    interview_scenarios=[
        {
            "question": "Design an AI workflow for document Q&A.",
            "approach": "Explain ingestion, retrieval, prompting, validation, logging, and user response in order.",
            "answer_points": [
                "Ingest and parse the documents.",
                "Split them into chunks and create embeddings if retrieval is needed.",
                "Store chunks in a searchable index or vector database.",
                "Embed the user query and retrieve relevant chunks.",
                "Build a prompt with the retrieved context and user question.",
                "Generate the answer, validate it, log the result, and return it to the user.",
            ],
            "diagram": "Docs -> Parse/Chunk -> Vector Store\nUser Query -> Retrieve -> Prompt -> Model -> Validate -> Response",
        },
        {
            "question": "Explain how an AI chatbot works end to end.",
            "approach": "Start from user message, then explain context, prompt building, model call, post-processing, and logging.",
            "answer_points": [
                "The user sends a message from the frontend.",
                "The backend collects conversation history and instructions.",
                "If needed, the system retrieves external context or tools.",
                "A final prompt is built and sent to the model.",
                "The result is cleaned, validated, logged, and returned to the user.",
            ],
            "diagram": "User Message -> Backend -> History/Context -> Prompt -> Model -> Post-process -> Response",
        },
        {
            "question": "How would you improve a low-quality AI workflow?",
            "approach": "Explain diagnosis first, then targeted improvements, then re-evaluation.",
            "answer_points": [
                "Check logs and failure patterns first.",
                "See whether the issue is prompt quality, retrieval quality, tool failure, or missing validation.",
                "Improve the weak component instead of changing everything at once.",
                "Test again, compare results, and monitor after deployment.",
            ],
            "diagram": "Observe failures -> Diagnose weak step -> Improve -> Re-test -> Monitor",
        },
        {
            "question": "What are the components of a real enterprise AI workflow?",
            "approach": "Name the system blocks from input to monitoring, and mention trust/reliability layers.",
            "answer_points": [
                "User input or file input",
                "Preprocessing and prompt/context building",
                "Model and optional retrieval or tools",
                "Post-processing and validation",
                "Response delivery",
                "Logging, evaluation, monitoring, and iteration",
            ],
            "diagram": "Input -> Prep -> Prompt/Context -> Model/Tools -> Validation -> Response -> Logs/Monitoring",
        },
    ],
    interview_rapid_fire=[
        {"question": "AI workflow means?", "answer": "The end-to-end sequence of steps around an AI task."},
        {"question": "Prompt-only workflow?", "answer": "User input goes straight to prompt and model."},
        {"question": "RAG means?", "answer": "Retrieve relevant context, then generate."},
        {"question": "Preprocessing does?", "answer": "Cleans or transforms raw input before AI use."},
        {"question": "Post-processing does?", "answer": "Cleans and formats raw output."},
        {"question": "Validation does?", "answer": "Checks whether output meets rules."},
        {"question": "Guardrails help with?", "answer": "Reliability and safety."},
        {"question": "Logs are for?", "answer": "Debugging, monitoring, and improvement."},
        {"question": "Human-in-the-loop means?", "answer": "Human review before final action."},
        {"question": "Workflow vs model?", "answer": "The model is one step; the workflow is the whole system."},
    ],
    interview_common_mistakes=[
        "Describing only the model and not the full workflow.",
        "Ignoring preprocessing, validation, and post-processing.",
        "Forgetting retrieval, guardrails, or logging.",
        "Not knowing how evaluation and iteration work.",
        "Confusing AI workflow with just calling one API.",
    ],
    quick_revision_points=[
        "AI workflow means the end-to-end sequence around an AI task.",
        "Real AI apps are systems, not just prompts.",
        "User input is only the starting point.",
        "Preprocessing makes raw input usable.",
        "Prompt construction is often dynamic.",
        "Prompt quality affects output quality.",
        "The model call is only one workflow step.",
        "Retrieval adds external context.",
        "RAG means retrieve first, then generate.",
        "Tools expand the workflow beyond text generation.",
        "Tool use can fetch exact data or perform actions.",
        "Post-processing cleans and formats output.",
        "Validation checks whether output is acceptable.",
        "Guardrails improve reliability and safety.",
        "You should not trust raw model output directly.",
        "Storage and logging help debugging and improvement.",
        "User feedback helps refine workflows.",
        "Human review is useful for high-risk outputs.",
        "A document Q&A assistant is a classic AI workflow example.",
        "A chatbot workflow often includes history and instructions.",
        "An agentic workflow may plan, act, observe, and continue.",
        "Batch workflows process many items together.",
        "Real-time workflows respond to live requests.",
        "Start simple before adding complexity.",
        "Frontend handles interaction, backend handles orchestration.",
        "Vector databases support semantic retrieval in workflows.",
        "Databases and APIs support exact data and integrations.",
        "Failure can happen at input, retrieval, model, tool, or validation layers.",
        "Evaluation matters because fluent output can still be wrong.",
        "Manual review is one evaluation method.",
        "Correctness, relevance, format, latency, and consistency all matter.",
        "Prompt iteration is part of workflow improvement.",
        "Retrieval quality directly affects grounded answers.",
        "Monitoring tracks quality, latency, and failure rate.",
        "AI Engineers build and improve workflows, not just model calls.",
    ],
    quiz_questions=[
        _q("What is the best definition of an AI workflow?", ["Only the model API call", "The end-to-end sequence of steps around an AI task", "Only a training loop", "Only a UI screen"], 1, "An AI workflow includes the full sequence around the model, not just one step."),
        _q("What is preprocessing mainly for?", ["Making the UI blue", "Preparing raw input before AI use", "Replacing the database", "Skipping validation"], 1, "Preprocessing prepares raw input so the workflow can use it effectively."),
        _q("What is the main idea of RAG?", ["Retrieve relevant context before generation", "Generate without input", "Only store logs", "Only use SQL joins"], 0, "RAG retrieves relevant information first and then uses it during generation."),
        _q("Why are tools used in AI workflows?", ["To reduce all prompts to zero", "To expand capability beyond pure text generation", "To avoid APIs", "To replace users"], 1, "Tools let the workflow search, calculate, query systems, or act on external services."),
        _q("What does post-processing do?", ["Only trains the model", "Cleans and formats raw output", "Deletes all logs", "Creates embeddings only"], 1, "Post-processing makes the raw output more usable and controlled."),
        _q("Why is validation important?", ["Because model output can be wrong or unsafe", "Because databases dislike prompts", "Because UI needs more tabs", "Because retrieval always fails"], 0, "Validation is needed because model output is not always reliable."),
        _q("What is human-in-the-loop?", ["The model reviewing itself", "A human reviewing AI output before final action", "Only batch processing", "Only vector search"], 1, "Human review is useful for risky or business-critical outputs."),
        _q("Why does evaluation matter in AI workflows?", ["Because fluent answers are always correct", "Because AI outputs can look good but still be wrong", "Because evaluation replaces prompts", "Because latency does not matter"], 1, "Evaluation matters because surface quality is not enough."),
    ],
    resources=[
        _r("OpenAI Docs Overview", "https://platform.openai.com/docs/overview", "article", "must_read", "Helpful conceptual reference for modern AI application building."),
        _r("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "must_read", "Broad educational reference for LLM systems and workflows."),
        _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Good prompt and workflow reference."),
        _r("Pinecone Learn: RAG", "https://www.pinecone.io/learn/retrieval-augmented-generation/", "article", "practice", "Useful beginner-friendly RAG explanation."),
    ],
    resource_sections={
        "Must watch first": [
            _r("DeepLearning.AI GenAI System Videos", "https://www.youtube.com/results?search_query=DeepLearning.AI+RAG+workflow", "video", "must_watch", "Good beginner-friendly workflow videos."),
            _r("IBM Technology AI Workflow Videos", "https://www.youtube.com/@IBMTechnology/search?query=AI%20workflow", "video", "must_watch", "Short explainers on AI systems and components."),
            _r("RAG Tutorial Videos", "https://www.youtube.com/results?search_query=RAG+tutorial+beginner", "video", "must_watch", "Helpful walkthroughs of retrieval workflows."),
        ],
        "Must read first": [
            _r("OpenAI Docs Overview", "https://platform.openai.com/docs/overview", "article", "must_read", "Useful conceptual AI app reference."),
            _r("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "must_read", "Strong educational overview."),
            _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Good practical reference."),
            _r("Pinecone Learn: RAG", "https://www.pinecone.io/learn/retrieval-augmented-generation/", "article", "must_read", "Clear retrieval-augmented generation explainer."),
        ],
        "Practice / explore": [
            _r("LangChain Concepts", "https://python.langchain.com/docs/concepts/", "article", "practice", "Helpful workflow and orchestration concepts."),
            _r("LlamaIndex Use Cases", "https://docs.llamaindex.ai/en/stable/use_cases/", "article", "practice", "Useful examples of document and retrieval workflows."),
            _r("Pinecone Learn", "https://www.pinecone.io/learn/", "article", "practice", "Helpful retrieval and vector search articles."),
        ],
        "Optional deep dive": [
            _r("LangChain Expression Language Concepts", "https://python.langchain.com/docs/concepts/lcel/", "article", "optional_deep_dive", "Useful if you want deeper workflow orchestration patterns."),
            _r("LlamaIndex Concepts", "https://docs.llamaindex.ai/en/stable/getting_started/concepts/", "article", "optional_deep_dive", "Helpful for stronger retrieval and indexing understanding."),
            _r("OpenAI Responses Guide", "https://platform.openai.com/docs/guides/text", "article", "optional_deep_dive", "Good model interaction reference."),
        ],
    },
    flow_diagrams=[
        {"title": "Basic AI lifecycle", "diagram": "User Need -> Data/Input -> AI Processing -> Output -> Evaluation -> Improvement"},
        {"title": "Prompt-based workflow", "diagram": "User Input -> Prompt Builder -> Model -> Response"},
        {"title": "RAG workflow", "diagram": "User Query -> Retrieve Relevant Docs -> Build Prompt -> Model -> Answer"},
        {"title": "Human-in-the-loop", "diagram": "Input -> AI Draft -> Human Review -> Approve/Edit -> Final Output"},
        {"title": "Deployment and monitoring", "diagram": "Deploy Workflow -> Monitor Quality/Latency -> Review Logs/Feedback -> Improve -> Re-deploy"},
    ],
)
