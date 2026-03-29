"""Structured content for the Agentic AI topic page."""

from utils.data import TopicContent, _q, _r


AGENTIC_AI_TOPIC = TopicContent(
    key="agentic_ai",
    title="Agentic AI",
    icon="AA",
    difficulty="Medium",
    priority="Very High",
    estimated_time="3 to 4 hours",
    importance_for_movate="Very High",
    why_it_matters=(
        "Agentic AI is the idea of building AI systems that do more than give one answer. They can break work into steps, "
        "choose actions, use tools, keep state, and move toward a goal. This matters for Movate-style AI Engineer roles because "
        "modern enterprise assistants, workflow copilots, and automation systems increasingly depend on agentic behavior."
    ),
    detailed_sections={
        "Agent foundations": "Understand what makes a system agentic instead of just conversational.",
        "Planning and tools": "Agents often plan, call tools, and react to intermediate results.",
        "Memory and state": "Memory helps continuity, personalization, and multi-step task completion.",
        "Orchestration": "Agent workflows coordinate multiple steps, tools, and validations.",
        "Enterprise execution": "Real agent systems need safety, validation, logging, and human approval paths.",
    },
    common_mistakes=[
        "Saying every chatbot is automatically an AI agent.",
        "Using buzzwords like agent or orchestration without explaining the workflow.",
        "Ignoring tool use, memory, and planning when defining an agent.",
        "Confusing RAG with agentic AI as if they are the same thing.",
        "Explaining enterprise agents without mentioning risk control and validation.",
    ],
    code_examples={
        "Agent Intro Flow": """User Goal -> AI decides steps -> uses tools -> collects results -> returns final response""",
        "Tool Calling Flow": """User Request -> LLM decides tool -> Tool call -> Tool result -> LLM response""",
    },
    interview_questions=[
        {"q": "What is Agentic AI?", "a": "Agentic AI refers to AI systems that can pursue goals using planning, tools, memory, and multi-step execution."},
        {"q": "How is an agent different from a chatbot?", "a": "A chatbot mainly answers, while an agent can act, plan, and use tools."},
        {"q": "What is tool calling?", "a": "Tool calling means the model decides to use an external capability like search, APIs, or a calculator."},
        {"q": "Why does memory matter in agents?", "a": "Memory helps continuity, personalization, and multi-step task completion."},
        {"q": "What is planner-executor architecture?", "a": "One part plans the steps and another part executes them."},
    ],
    quick_revision_points=[],
    quiz_questions=[],
    resources=[],
    role_relevance=[
        "Agentic workflows for enterprise automation",
        "Tool-based AI systems that connect with APIs and business software",
        "Task orchestration across multiple steps and tools",
        "Copilots and assistants that do more than answer once",
        "AI productivity tools with validation and workflow control",
    ],
    learning_objectives=[
        "Understand agentic AI from scratch in simple language.",
        "Explain how agents plan, use tools, update memory, and complete tasks.",
        "Compare chatbot, assistant, and agent behavior confidently in interviews.",
        "Connect agentic AI with enterprise systems, risk controls, and AI Engineer work.",
    ],
    learn_sections=[],
    architectures=[],
    workflows=[],
    interview_questions_detailed=[],
    interview_rapid_fire=[],
    interview_common_mistakes=[],
    resource_sections={},
)


AGENTIC_AI_TOPIC = AGENTIC_AI_TOPIC.__class__(
    **{
        **AGENTIC_AI_TOPIC.__dict__,
        "learn_sections": [
            {
                "title": "1. What is Agentic AI",
                "summary": "An AI agent is not just a text generator. It behaves more like a task performer that can reason about the goal, choose actions, use tools, and continue through multiple steps.",
                "points": [
                    "A chatbot usually gives a response. An agent tries to complete a task.",
                    "Agentic AI is goal-driven rather than only response-driven.",
                    "Agents can choose actions, gather information, use tools, and update their next step based on what happened before.",
                ],
                "tables": [
                    {
                        "title": "Traditional chatbot vs assistant vs agent",
                        "markdown": """| System | Main behavior | Typical example |
|---|---|---|
| Traditional chatbot | Replies to user queries | FAQ bot |
| AI assistant | Replies with more context and sometimes retrieval | Knowledge assistant |
| AI agent | Plans, uses tools, and executes multi-step tasks | Scheduling agent |""",
                    }
                ],
                "examples": [
                    {"label": "Chatbot flow", "code": "User -> Prompt -> LLM -> Response"},
                    {"label": "Agent flow", "code": "User -> Goal -> LLM/Planner -> Tool/Action -> Result -> Next Step -> Final Output"},
                ],
                "callouts": [
                    {"type": "info", "text": "Simple analogy: chatbot answers one question, agent completes a task through multiple steps."},
                    {"type": "warning", "text": "Common confusion: if a system only responds once with text, that alone does not make it agentic."},
                ],
            },
            {
                "title": "2. Core Characteristics of an AI Agent",
                "summary": "These are the traits that make an AI system feel agentic instead of just conversational.",
                "subtopics": [
                    {"title": "Goal-driven behavior", "content": ["Definition: the system works toward a user goal, not just a single reply.", "Why it matters: enterprise workflows often require task completion, not only explanation.", "Example: 'book a meeting' instead of 'what is a meeting?'"]},
                    {"title": "Planning", "content": ["Definition: the agent can break a task into smaller steps.", "Why it matters: complex tasks are easier to solve step by step.", "Example: retrieve calendar -> check conflicts -> suggest slot -> create event."]},
                    {"title": "Tool usage", "content": ["Definition: the agent can call external tools such as APIs, search, or calculators.", "Why it matters: the LLM alone cannot always fetch fresh or exact information.", "Example: use a calendar API instead of guessing availability."]},
                    {"title": "State awareness", "content": ["Definition: the system knows where it is in the current task or session.", "Why it matters: multi-step workflows need progress tracking.", "Example: it remembers that step 2 is complete and moves to step 3."]},
                    {"title": "Memory and context", "content": ["Definition: the agent can use current context and sometimes stored preferences.", "Why it matters: continuity and personalization improve task completion.", "Example: it remembers the user's preferred meeting hours."]},
                    {"title": "Multi-step execution", "content": ["Definition: the agent may need several actions before the final answer.", "Why it matters: many enterprise tasks are not solvable in one response.", "Example: read a file, summarize it, extract actions, and draft an email."]},
                    {"title": "Iteration", "content": ["Definition: the agent can use intermediate results to decide the next move.", "Why it matters: real workflows often need re-evaluation after each step.", "Example: if a tool returns no slot, the agent tries a different day."]},
                ],
            },
            {
                "title": "3. Agent vs Chatbot",
                "summary": "This is one of the most common interview distinctions.",
                "points": [
                    "A chatbot is usually response-only.",
                    "An agent can act, plan, call tools, and continue execution based on results.",
                    "A chatbot answers. An agent executes.",
                ],
                "examples": [
                    {"label": "Visual comparison", "code": """Chatbot:
User -> Prompt -> Model -> Response

Agent:
User -> Goal -> Planner -> Tool -> Observation -> Next Step -> Final Output
"""}
                ],
            },
            {
                "title": "4. Components of an Agentic AI System",
                "summary": "An agent is usually built from several cooperating pieces, not one model call.",
                "subtopics": [
                    {"title": "User input / goal", "content": ["What it does: captures what the user wants.", "Why it matters: poor goal understanding leads to poor plans.", "Interview view: the goal is the starting point of the workflow."]},
                    {"title": "LLM / reasoning engine", "content": ["What it does: interprets tasks, reasons, and decides the next action.", "Why it matters: it provides flexible decision-making.", "Interview view: the LLM is often the planner or controller."]},
                    {"title": "Planner", "content": ["What it does: breaks work into steps.", "Why it matters: complex tasks become manageable.", "Interview view: planners improve structure in multi-step problems."]},
                    {"title": "Tools", "content": ["What they do: connect the agent to APIs, DBs, search, files, or calculators.", "Why they matter: agents need external capabilities for real work.", "Interview view: tools extend the power of LLMs."]},
                    {"title": "Memory", "content": ["What it does: stores useful state, preferences, or prior steps.", "Why it matters: multi-step tasks need continuity.", "Interview view: memory improves personalization and task tracking."]},
                    {"title": "State / session context", "content": ["What it does: tracks current workflow status.", "Why it matters: prevents losing track of progress.", "Interview view: state awareness is important for reliable execution."]},
                    {"title": "Execution loop", "content": ["What it does: repeats reason -> act -> observe cycles.", "Why it matters: agents often need several iterations.", "Interview view: this loop is the heart of agent behavior."]},
                    {"title": "Output formatter", "content": ["What it does: shapes the final output for humans or systems.", "Why it matters: output must be usable.", "Interview view: formatting matters for downstream workflows."]},
                    {"title": "Safety / validation layer", "content": ["What it does: checks results, permissions, or policy constraints.", "Why it matters: enterprise systems need guardrails.", "Interview view: validation is essential for production trust."]},
                ],
                "examples": [
                    {"label": "Full architecture diagram", "code": """User
  ↓
Goal Interpreter
  ↓
Planner / LLM
  ↓
Tool Selector
  ↓
Tool Calls / APIs / DB / Search
  ↓
Intermediate Results
  ↓
Memory / Context Update
  ↓
Final Response
"""}
                ],
            },
            {
                "title": "5. Planning in Agentic AI",
                "summary": "Planning means breaking a big goal into smaller actions and re-checking progress after each step.",
                "points": [
                    "Explicit planning means the system creates visible task steps.",
                    "Implicit planning means the model internally decides actions without showing a full plan.",
                    "Planner-executor design is a common architecture where one unit plans and another carries out steps.",
                ],
                "examples": [{"label": "Planner flow", "code": "User Goal -> Planner -> Step 1 / Step 2 / Step 3 -> Executor -> Final Output"}],
            },
            {
                "title": "6. Tool Use / Tool Calling",
                "summary": "Tool calling is one of the biggest reasons agentic systems are more powerful than plain chat systems.",
                "points": [
                    "A tool is an external capability such as search, calculator, database query, calendar API, code executor, or file reader.",
                    "Tools matter because the LLM alone should not guess fresh facts, exact values, or live system state.",
                    "LLM alone is good at language; LLM plus tools is better at action and retrieval.",
                ],
                "examples": [
                    {
                        "label": "Scheduling example",
                        "code": """Request: "Schedule a meeting tomorrow"
Agent steps:
1. Read calendar
2. Check conflicts
3. Find free slot
4. Create event
""",
                    },
                    {"label": "Tool-calling flow", "code": "User Request -> LLM decides tool -> Tool call -> Tool result -> LLM response"},
                ],
            },
            {
                "title": "7. Memory in Agents",
                "summary": "Memory helps agents stay coherent across tasks and steps.",
                "points": [
                    "Short-term memory means current conversation or recent context.",
                    "Long-term memory means stored preferences or useful historical information.",
                    "Task memory means intermediate progress in the current workflow.",
                    "Memory matters for continuity, personalization, and multi-step execution.",
                ],
                "examples": [{"label": "Memory loop", "code": "Input -> Reasoning -> Tool -> Result -> Memory Update -> Next Step"}],
            },
            {
                "title": "8. Multi-step Reasoning and Execution",
                "summary": "Agents often need to gather data, inspect results, and decide what to do next instead of answering in one shot.",
                "points": [
                    "Multi-step reasoning is useful for automation, enterprise assistants, and task workflows.",
                    "The system may need to parse data, call tools, validate results, and continue.",
                ],
                "examples": [
                    {
                        "label": "Document to email workflow",
                        "code": """Task: "Summarize this document and email action items to manager"
1. Read file
2. Summarize content
3. Extract action items
4. Draft email
""",
                    }
                ],
            },
        ],
        "architectures": [
            {
                "title": "Single-Agent Architecture",
                "what_it_is": "One agent handles interpretation, planning, tool use, and final response.",
                "when_to_use": "Use it for simpler workflows or early prototypes.",
                "diagram": "User Goal -> Single Agent -> Tools / Memory -> Final Answer",
                "pros": "Simple to build, easy to understand, fast to prototype.",
                "limitations": "Can become hard to scale or specialize as tasks grow.",
                "interview_note": "A single-agent design is easiest to explain and is often enough for smaller workflows.",
            },
            {
                "title": "Planner-Executor Architecture",
                "what_it_is": "One component creates the plan and another component executes the steps.",
                "when_to_use": "Use it when tasks are complex enough to benefit from clear decomposition.",
                "diagram": "User Goal -> Planner -> Step List -> Executor -> Tool Calls -> Final Output",
                "pros": "Clear separation of planning and execution.",
                "limitations": "More moving parts and coordination overhead.",
                "interview_note": "Good answer structure: planner decides what to do, executor carries it out.",
            },
            {
                "title": "ReAct-style Loop",
                "what_it_is": "A high-level think -> act -> observe -> repeat loop.",
                "when_to_use": "Use it when the system needs iterative decision-making and tool use.",
                "diagram": "Goal -> Reason -> Act -> Observe -> Repeat -> Final Answer",
                "pros": "Flexible and intuitive for iterative tasks.",
                "limitations": "Can drift, loop too much, or become expensive without control.",
                "interview_note": "Explain it simply as a repeating cycle of reasoning, acting, and updating based on observations.",
            },
            {
                "title": "Multi-Agent System",
                "what_it_is": "Multiple agents handle different specialized roles.",
                "when_to_use": "Use it when tasks benefit from specialization such as research, writing, validation, or routing.",
                "diagram": "User Goal -> Coordinator -> Research Agent / Analysis Agent / Writer Agent -> Final Merge",
                "pros": "Specialization and clearer role separation.",
                "limitations": "Higher coordination complexity and more cost.",
                "interview_note": "Good for explaining how roles can be separated across a complex AI workflow.",
            },
            {
                "title": "Agent + RAG Architecture",
                "what_it_is": "An agent retrieves relevant documents and uses them while reasoning and acting.",
                "when_to_use": "Use it when grounded answers from company or current knowledge are required.",
                "diagram": "User Query -> Retriever -> Relevant Docs -> Agent -> Final Answer",
                "pros": "Improves grounding and reduces unsupported answers.",
                "limitations": "Depends heavily on retrieval quality and document freshness.",
                "interview_note": "RAG is not the same as an agent, but agents often use RAG as one part of the workflow.",
            },
        ],
        "workflows": [
            {
                "title": "Meeting Scheduling Agent",
                "business_purpose": "Automate scheduling while checking real calendar constraints.",
                "diagram": "User Request -> Calendar Check -> Conflict Detection -> Slot Suggestion -> Event Creation",
                "steps": [
                    "Read the user's scheduling request.",
                    "Query the calendar API for availability.",
                    "Detect conflicts and available windows.",
                    "Suggest one or more slots.",
                    "Create the event once a slot is selected.",
                ],
                "tools_involved": "Calendar API, time parser, scheduling rules.",
                "risks": "Wrong time zone, permission issues, double booking, unclear meeting preferences.",
                "why_agentic_ai_helps": "The workflow has multiple dependent steps and tool calls, so a one-shot answer is not enough.",
            },
            {
                "title": "Customer Support Knowledge Agent",
                "business_purpose": "Answer support queries using company knowledge while following policy.",
                "diagram": "User Query -> Knowledge Retrieval -> Answer Draft -> Policy Check -> Final Response",
                "steps": [
                    "Interpret the support question.",
                    "Retrieve relevant KB documents.",
                    "Draft an answer using the retrieved context.",
                    "Run a policy or safety check.",
                    "Return the final response or escalate if needed.",
                ],
                "tools_involved": "Retriever, KB index, policy checker, escalation rules.",
                "risks": "Weak retrieval, hallucination, outdated content, unsafe replies.",
                "why_agentic_ai_helps": "The system must combine retrieval, reasoning, validation, and escalation logic.",
            },
            {
                "title": "Document Analysis Agent",
                "business_purpose": "Help users quickly understand uploaded business documents.",
                "diagram": "Upload Document -> Parse -> Extract Key Info -> Summarize -> Return Insights",
                "steps": [
                    "Read and parse the uploaded document.",
                    "Extract key entities or sections.",
                    "Summarize the important content.",
                    "Return insights or a structured summary.",
                ],
                "tools_involved": "File parser, OCR if needed, summarization logic, extraction prompts.",
                "risks": "Parsing failures, missing content, unsupported summaries.",
                "why_agentic_ai_helps": "The workflow includes sequential processing and may need different tools for different document types.",
            },
            {
                "title": "Internal Enterprise Copilot",
                "business_purpose": "Help employees answer internal questions and complete small tasks faster.",
                "diagram": "Question -> Search Internal Docs -> Call Tools -> Draft Response -> Human Review if needed",
                "steps": [
                    "Understand the employee question.",
                    "Search internal documents and systems.",
                    "Use tools or APIs if the task requires action.",
                    "Draft a grounded response.",
                    "Route for human review when confidence or policy requires it.",
                ],
                "tools_involved": "Internal search, APIs, document store, approval flow.",
                "risks": "Permission leakage, wrong internal guidance, weak access control.",
                "why_agentic_ai_helps": "The copilot needs both knowledge retrieval and task-oriented actions.",
            },
            {
                "title": "Data Extraction and Reporting Agent",
                "business_purpose": "Turn raw files into summarized business reports with less manual work.",
                "diagram": "Input File -> Extract Data -> Clean Data -> Generate Summary -> Export Report",
                "steps": [
                    "Read the input file.",
                    "Extract relevant fields or values.",
                    "Clean and validate the data.",
                    "Generate a summary or report.",
                    "Export the final output.",
                ],
                "tools_involved": "File reader, parser, validator, report generator.",
                "risks": "Extraction errors, dirty data, bad formatting, false summary conclusions.",
                "why_agentic_ai_helps": "The task combines multiple dependent stages rather than one direct answer.",
            },
        ],
        "interview_questions_detailed": [
            {"question": "What is Agentic AI?", "short_answer": "Agentic AI refers to AI systems that can pursue goals using planning, tools, memory, and multi-step execution.", "spoken_answer": "Agentic AI is the idea of building AI systems that do more than give one response. An agent can work toward a goal by planning steps, calling tools, updating memory, and continuing until it reaches a useful result."},
            {"question": "Difference between chatbot and AI agent?", "short_answer": "A chatbot mainly answers, while an agent can plan, act, and use tools to complete tasks.", "spoken_answer": "A chatbot is usually response-focused. An agent is task-focused. It can break work into steps, use APIs or tools, check intermediate results, and continue until the task is done or it needs human approval."},
            {"question": "What makes an AI system agentic?", "short_answer": "Goal-driven behavior, planning, tool use, memory, and multi-step execution.", "spoken_answer": "I would call a system agentic when it behaves like a task performer instead of just a text responder. That usually means it can understand the goal, decide what to do next, use external tools, and adjust based on intermediate results."},
            {"question": "What is tool calling?", "short_answer": "Tool calling means the model decides to use an external capability such as search, APIs, a calculator, or a database.", "spoken_answer": "Tool calling extends the agent beyond language generation. Instead of guessing, the system can use a search API, database query, or calculator and then continue reasoning based on the real result."},
            {"question": "Why do agents need tools?", "short_answer": "Because the LLM alone should not rely only on memory for live data, exact values, or actions.", "spoken_answer": "Tools matter because the model alone is strong at language but weak at exact live interactions. Agents need tools to search, calculate, query systems, read files, update calendars, and interact with business software."},
            {"question": "What is planning in agentic AI?", "short_answer": "Planning means breaking a big task into smaller steps and deciding what to do first.", "spoken_answer": "Planning helps an agent turn a broad goal into manageable actions. It may decide to retrieve information first, then call a tool, then validate the result, and finally produce the answer or take an action."},
            {"question": "What is memory in AI agents?", "short_answer": "Memory is the stored context that helps the agent stay consistent across steps or conversations.", "spoken_answer": "Memory can include recent conversation context, stored user preferences, or progress in the current task. It matters because multi-step workflows need continuity and users often expect personalization."},
            {"question": "What is a planner-executor architecture?", "short_answer": "It is an architecture where one component plans the steps and another executes them.", "spoken_answer": "Planner-executor is a useful design because it separates decision-making from action-taking. The planner creates a sequence of actions, and the executor carries them out through tools or system calls."},
            {"question": "What is a multi-step AI workflow?", "short_answer": "It is a workflow where the agent performs several linked actions before producing the final result.", "spoken_answer": "Many useful AI tasks are not single-shot. For example, the system may need to read a document, summarize it, extract action items, and then draft an email. That kind of sequence is a multi-step AI workflow."},
            {"question": "What are risks of AI agents?", "short_answer": "Wrong tool selection, hallucination, loops, irrelevant actions, privacy issues, and excessive cost or latency.", "spoken_answer": "Agents are powerful because they can act, but that also increases risk. They may choose the wrong tool, get stuck in loops, make unsupported assumptions, expose sensitive data, or create unnecessary cost without good controls."},
            {"question": "How do you control or validate an AI agent?", "short_answer": "Use guardrails, validation, step limits, scoped tools, human approval, logging, and monitoring.", "spoken_answer": "I would control an agent by limiting tool permissions, validating outputs, adding safety rules, setting step limits, using human review for risky actions, and logging behavior so the system can be monitored and improved."},
            {"question": "What is human-in-the-loop?", "short_answer": "It means a person reviews or approves the agent's output or action before it is finalized.", "spoken_answer": "Human-in-the-loop is important when the workflow has high business or compliance risk. The agent can draft, suggest, or prepare the next step, but a person confirms before the system acts."},
            {"question": "What is the difference between RAG and an agent?", "short_answer": "RAG is a retrieval-plus-generation pattern, while an agent is a broader task-oriented system that may use RAG as one component.", "spoken_answer": "RAG focuses on retrieving useful documents and grounding the answer with them. An agent is broader: it may retrieve documents, call tools, plan steps, update memory, and decide what to do next. So RAG can be part of an agent, but they are not the same thing."},
            {"question": "Can an agent work without memory?", "short_answer": "Yes, but it will usually be weaker at continuity, personalization, and multi-step tracking.", "spoken_answer": "A memory-less agent is possible, but it is less capable in longer workflows. Without memory, it may forget progress, lose context, or fail to maintain continuity across steps."},
            {"question": "What is orchestration in AI workflows?", "short_answer": "Orchestration is coordinating the sequence of actions, tools, and next-step decisions in the workflow.", "spoken_answer": "Orchestration is about controlling how the whole workflow runs, including what happens first, how outputs are validated, when tools are called, and when the system should stop or ask for help."},
            {"question": "What enterprise use cases exist for AI agents?", "short_answer": "Support assistants, internal knowledge tools, document agents, ticket helpers, scheduling agents, data extraction agents, and workflow copilots.", "spoken_answer": "Enterprise use cases include internal knowledge assistants, support automation, scheduling, document analysis, ticket routing, report generation, and workflow copilots. The common idea is that the system does more than talk; it helps complete work."},
            {"question": "Why are APIs important for agents?", "short_answer": "APIs are how agents connect with tools, business systems, search, calendars, files, and external services.", "spoken_answer": "An agent becomes useful in the real world only when it can interact with systems outside the model. APIs let it fetch information, take actions, and integrate with enterprise workflows."},
            {"question": "How would you design a meeting scheduling agent?", "short_answer": "Interpret the request, check the calendar, find available slots, suggest options, and create the event.", "spoken_answer": "I would design it as a goal-driven workflow: understand the meeting request, call the calendar API, check conflicts, identify free slots, confirm a choice, and then create the event. I would also handle time zones, permissions, and human confirmation."},
            {"question": "What can go wrong in an agentic workflow?", "short_answer": "The agent may use the wrong tool, misread results, take irrelevant steps, or act without enough validation.", "spoken_answer": "Agentic workflows can fail through bad planning, wrong tool use, unsupported assumptions, loops, or missing safety checks. That is why validation and monitoring matter as much as the model itself."},
            {"question": "How would you reduce hallucination in agents?", "short_answer": "Use grounding, retrieval, tool validation, constraints, and human review for high-risk actions.", "spoken_answer": "I would not rely on prompting alone. I would ground the system with trusted sources, validate tool outputs, narrow scope, require structured outputs, and add human review where the consequences of error are high."},
            {"question": "How would you test an AI agent?", "short_answer": "Test the full workflow across normal cases, edge cases, tool failures, and risky scenarios.", "spoken_answer": "Agent testing should include functional workflow tests, edge cases, tool failure cases, security cases, and quality evaluation. I would also check latency, cost, output correctness, and whether the agent stops safely when it is uncertain."},
            {"question": "Why is agentic AI useful for automation?", "short_answer": "Because it can handle dynamic multi-step tasks that are too flexible for simple rule-based systems.", "spoken_answer": "Agentic AI is useful when the task path is not fully fixed. The system can adapt, retrieve missing context, call tools, and choose next steps based on what happened before. That makes it powerful for knowledge work and workflow support."},
            {"question": "What is the difference between a workflow and an agent?", "short_answer": "A workflow is the sequence of steps; an agent is the decision-making system that may operate inside that workflow.", "spoken_answer": "A workflow describes how tasks move from step to step. An agent is one type of intelligent component that can make decisions inside that workflow. Some workflows are deterministic and need no agent, while others benefit from agentic reasoning."},
            {"question": "What is a multi-agent system?", "short_answer": "A multi-agent system uses multiple specialized agents instead of one general agent.", "spoken_answer": "In a multi-agent system, different agents can handle roles like research, writing, validation, or coordination. This can improve specialization, but it also increases complexity and coordination overhead."},
            {"question": "How would an AI Engineer contribute to an agentic AI project?", "short_answer": "By designing prompts, integrating APIs and tools, building workflows, testing reliability, and improving behavior.", "spoken_answer": "An AI Engineer often connects the model to tools and business systems, designs prompts and constraints, handles workflow orchestration, adds validation and safety, tests behavior, and improves the system over time based on failures and metrics."},
        ],
        "interview_rapid_fire": [
            {"question": "Agent means?", "answer": "Goal-driven AI system that can plan and act."},
            {"question": "Chatbot vs agent?", "answer": "Chatbot answers; agent executes tasks."},
            {"question": "Why tools?", "answer": "Tools extend LLM capability with real actions and exact data."},
            {"question": "Planning means?", "answer": "Breaking a task into steps."},
            {"question": "Memory helps with?", "answer": "Continuity, personalization, and progress tracking."},
            {"question": "Planner-executor?", "answer": "One plans, one executes."},
            {"question": "Human-in-the-loop?", "answer": "A person reviews before final action."},
            {"question": "RAG vs agent?", "answer": "RAG is retrieval plus generation; an agent is a broader task system."},
            {"question": "Orchestration means?", "answer": "Coordinating the workflow across steps and tools."},
            {"question": "Not every workflow needs?", "answer": "An agent."},
        ],
        "interview_common_mistakes": [
            "Saying every chatbot is an agent.",
            "Not explaining tool usage clearly.",
            "Ignoring memory and planning.",
            "Confusing RAG with agentic AI.",
            "Using only buzzwords without a workflow explanation.",
        ],
        "quick_revision_points": [
            "Agent means a goal-driven AI system that can plan and act.",
            "A chatbot mainly answers; an agent can execute tasks.",
            "Not every assistant is fully agentic.",
            "Planning breaks a task into smaller actions.",
            "Tool calling lets the model use APIs, search, calculators, files, and databases.",
            "Tools extend the capabilities of LLMs.",
            "Memory helps continuity and personalization.",
            "Task memory helps track intermediate progress.",
            "Agents often work in multi-step loops, not one-shot replies.",
            "A planner-executor architecture separates planning from execution.",
            "ReAct-style loops follow reason -> act -> observe -> repeat.",
            "Multi-agent systems use specialized roles.",
            "RAG can be part of an agent, but it is not the same thing as an agent.",
            "State awareness helps the agent know where it is in the workflow.",
            "Orchestration means sequencing steps and coordinating actions.",
            "Rule-based automation is still better for some deterministic workflows.",
            "Human approval reduces enterprise risk.",
            "Common tools include search, DB query, calendar API, calculator, and file reader.",
            "A good agent should not guess when a tool can verify the answer.",
            "Wrong tool selection is a common failure mode.",
            "Infinite loops are an agent risk.",
            "Privacy and permission control matter in enterprise agents.",
            "Guardrails, validation, and step limits improve safety.",
            "Scoped tool access reduces risk.",
            "Logging and monitoring help debug agent behavior.",
            "Testing agents requires workflow and edge-case coverage.",
            "Agentic AI is useful when task paths are dynamic.",
            "Not every problem needs an agent; sometimes a simple workflow is enough.",
            "APIs are essential because they connect agents to real systems.",
            "An AI Engineer contributes by integrating tools, prompts, workflows, and evaluation.",
        ],
        "quiz_questions": [
            _q("What best describes an AI agent?", ["A system that only gives one text reply", "A goal-driven system that can plan and act", "A static dashboard", "A simple database query"], 1, "An AI agent is goal-driven and can plan, act, and use tools."),
            _q("What is a key difference between a chatbot and an agent?", ["Chatbots use text and agents use images", "Chatbots answer while agents can execute multi-step tasks", "Agents cannot use tools", "Chatbots always have memory"], 1, "A chatbot is usually response-focused, while an agent can execute multi-step workflows."),
            _q("What is tool calling?", ["Training a model from scratch", "Letting the model decide to use an external tool or API", "Storing prompts in a file", "Compressing context"], 1, "Tool calling means the model uses an external capability like search, a calculator, or an API."),
            _q("Why does memory matter in agents?", ["It improves screen brightness", "It helps continuity and progress tracking", "It removes the need for tools", "It replaces planning"], 1, "Memory helps the agent maintain context, preferences, and workflow progress."),
            _q("Planner-executor architecture means", ["One component plans and another executes", "Two databases run together", "The user manually plans every step", "Only one answer is allowed"], 0, "Planner-executor separates planning from execution."),
            _q("What is human-in-the-loop?", ["An infinite loop bug", "A person reviewing or approving agent output or actions", "A memory cache", "A kind of prompt"], 1, "Human review is used when risk or compliance matters."),
            _q("Which architecture matches reason -> act -> observe -> repeat?", ["RAG only", "ReAct-style loop", "Simple FAQ bot", "Static ETL pipeline"], 1, "That loop describes a high-level ReAct-style pattern."),
            _q("Which is a common agent risk?", ["Wrong tool selection", "Perfect certainty", "Zero latency always", "No need for validation"], 0, "Agents can fail through wrong tools, loops, hallucination, and unsafe actions."),
        ],
        "resource_sections": {
            "Must watch first": [
                _r("IBM Technology AI Agent Videos", "https://www.youtube.com/@IBMTechnology/search?query=AI%20agents", "video", "must_watch", "Short explainers on agents, tool use, and enterprise AI ideas."),
                _r("DeepLearning.AI Agentic AI Videos", "https://www.deeplearning.ai/short-courses/", "video", "must_watch", "Beginner-friendly AI workflow and agent learning content."),
                _r("LangChain Intro Videos", "https://www.youtube.com/results?search_query=LangChain+agents+intro", "video", "must_watch", "Helpful for understanding practical agent frameworks at a high level."),
            ],
            "Must read first": [
                _r("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "must_read", "Useful background for agents, RAG, and model-driven workflows."),
                _r("LangChain Docs", "https://python.langchain.com/docs/introduction/", "article", "must_read", "Conceptual and framework-level introduction to agents and chains."),
                _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Good reference for related prompting, agents, and workflow ideas."),
                _r("Microsoft AI Agents Search", "https://learn.microsoft.com/en-us/search/?terms=AI%20agents", "article", "must_read", "Enterprise educational material around agent patterns and responsible AI."),
            ],
            "Practice / explore": [
                _r("LlamaIndex Docs", "https://docs.llamaindex.ai/", "article", "practice", "Good for understanding retrieval and agentic application building."),
                _r("LangChain Agent Concepts", "https://python.langchain.com/docs/concepts/", "article", "practice", "Explore agent concepts and workflow structures."),
                _r("Hugging Face Spaces", "https://huggingface.co/spaces", "article", "practice", "Explore practical GenAI demos and workflows."),
            ],
            "Optional deep dive": [
                _r("Google Cloud Generative AI Training", "https://cloud.google.com/learn/training/generative-ai", "article", "optional_deep_dive", "Broader enterprise AI and agent-adjacent learning path."),
                _r("Anthropic Docs", "https://docs.anthropic.com/", "article", "optional_deep_dive", "Useful for tool use and model workflow concepts."),
                _r("OpenAI Cookbook", "https://cookbook.openai.com/", "article", "optional_deep_dive", "Hands-on references for model-powered workflows and tool usage."),
            ],
        },
        "resources": [
            _r("LangChain Docs", "https://python.langchain.com/docs/introduction/", "article", "must_read", "Conceptual intro to agents and chains."),
            _r("LlamaIndex Docs", "https://docs.llamaindex.ai/", "article", "practice", "Useful for retrieval and agentic building blocks."),
            _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Related prompting and workflow knowledge."),
            _r("OpenAI Cookbook", "https://cookbook.openai.com/", "article", "optional_deep_dive", "Practical examples for model-powered workflows."),
        ],
    }
)
