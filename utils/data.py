"""Structured content for the Movate AI Engineer Prep App."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class QuizQuestion:
    question: str
    options: List[str]
    answer_index: int
    explanation: str


@dataclass(frozen=True)
class ResourceLink:
    title: str
    url: str
    kind: str  # article | video
    tier: str  # must_watch | must_read | deep_dive


@dataclass(frozen=True)
class TopicContent:
    key: str
    title: str
    icon: str
    difficulty: str
    priority: str
    estimated_time: str
    why_it_matters: str
    detailed_sections: Dict[str, str]
    common_mistakes: List[str]
    code_examples: Dict[str, str]
    interview_questions: List[Dict[str, str]]
    quick_revision_points: List[str]
    quiz_questions: List[QuizQuestion]
    resources: List[ResourceLink]


ROLE_SUMMARY = {
    "role": "AI Engineer",
    "location": "Pune",
    "ctc": "9 LPA",
    "focus_areas": [
        "Python",
        "GenAI",
        "Prompt Engineering",
        "Agentic AI",
        "APIs",
        "Data Handling",
        "Databases",
        "AI Workflows",
    ],
}


def _q(question: str, options: List[str], answer_index: int, explanation: str) -> QuizQuestion:
    return QuizQuestion(question, options, answer_index, explanation)


TOPIC_DATA: Dict[str, TopicContent] = {
    "python": TopicContent(
        key="python",
        title="Python",
        icon="🐍",
        difficulty="Beginner → Intermediate",
        priority="High",
        estimated_time="3.5 hours",
        why_it_matters=(
            "Python is the default language in AI engineering interviews because it tests coding clarity, data manipulation ability, and problem-solving speed."
        ),
        detailed_sections={
            "Variables, data types, and mutability": "Understand int/float/str/bool, plus mutable (list, dict, set) vs immutable (tuple, str). Interviewers often check if you can avoid accidental side effects while passing objects to functions.",
            "Collections and string operations": "Lists are ordered and mutable, tuples are ordered and immutable, sets remove duplicates and allow O(1)-average membership checks, dicts support key-value lookup. String slicing and methods are common in screening rounds.",
            "Functions and OOP": "Focus on clean function signatures, *args/**kwargs basics, class vs instance attributes, inheritance, and polymorphism. Explain where OOP helps readability in multi-module apps.",
            "Exceptions and file handling": "Use try/except for expected failures, not for hiding bugs. Prefer context managers (`with open(...)`) for file safety and readability.",
            "Coding patterns": "Practice frequency counting using dict/Counter, anagram checks via sorted/frequency map, second-largest in single pass, and reverse string using slicing/two pointers.",
        },
        common_mistakes=[
            "Using list operations where set/dict gives better complexity.",
            "Mutating default arguments in function definitions.",
            "Catching broad Exception without handling strategy.",
            "Ignoring edge cases like empty input or single-element arrays.",
        ],
        code_examples={
            "Frequency Count": """from collections import Counter\n\ntext = \"movate ai engineer\"\nfreq = Counter(text.replace(\" \", \"\"))\nprint(freq.most_common(3))""",
            "Anagram Check": """def is_anagram(a: str, b: str) -> bool:\n    return sorted(a.lower()) == sorted(b.lower())\n\nprint(is_anagram(\"listen\", \"silent\"))""",
            "Second Largest": """def second_largest(nums):\n    first = second = float(\"-inf\")\n    for n in nums:\n        if n > first:\n            second, first = first, n\n        elif first > n > second:\n            second = n\n    return None if second == float(\"-inf\") else second""",
            "Reverse String": """def reverse_string(s: str) -> str:\n    return s[::-1]""",
        },
        interview_questions=[
            {"q": "Why is Python preferred in AI stacks?", "a": "Fast prototyping, huge ecosystem (NumPy, Pandas, PyTorch), and readable syntax for collaboration."},
            {"q": "Difference between list and tuple?", "a": "Lists are mutable and better for changing data; tuples are immutable and safer for fixed records."},
            {"q": "What is duck typing?", "a": "Python cares about behavior (methods/attributes), not explicit type declarations."},
            {"q": "How do you handle file exceptions safely?", "a": "Use `with` context manager and catch specific exceptions like FileNotFoundError."},
            {"q": "What is the complexity of dictionary lookup?", "a": "Average O(1), worst-case O(n) in collision-heavy scenarios."},
        ],
        quick_revision_points=[
            "Prefer dict/set for lookup-heavy logic.",
            "Use specific exceptions and meaningful messages.",
            "Write functions with single responsibility.",
            "State time complexity while coding.",
            "Always test edge cases before finalizing answer.",
        ],
        quiz_questions=[
            _q("Which type is immutable?", ["list", "dict", "tuple", "set"], 2, "Tuple is immutable; list, dict, and set are mutable."),
            _q("Best structure for frequency counting?", ["tuple", "dict", "float", "str"], 1, "Dictionary or Counter gives direct key-based increments."),
            _q("Output of 'abc'[::-1]?", ["abc", "cba", "error", "bac"], 1, "Slice with -1 step reverses a sequence."),
            _q("Which block ensures file closure?", ["if", "for", "with", "class"], 2, "`with open(...)` guarantees close even on exception."),
            _q("Average complexity of set membership?", ["O(1)", "O(log n)", "O(n)", "O(n^2)"], 0, "Hashing gives O(1)-average membership checks."),
        ],
        resources=[
            ResourceLink("Official Python docs", "https://docs.python.org/3/tutorial/", "article", "must_read"),
            ResourceLink("Real Python learning paths", "https://realpython.com/", "article", "must_read"),
            ResourceLink("GeeksforGeeks Python", "https://www.geeksforgeeks.org/python-programming-language/", "article", "deep_dive"),
            ResourceLink("Corey Schafer Python playlist", "https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc", "video", "must_watch"),
        ],
    ),
    "dsa": TopicContent(
        key="dsa", title="DSA", icon="🧠", difficulty="Beginner → Intermediate", priority="High", estimated_time="4 hours",
        why_it_matters="DSA determines your coding-round performance and proves structured problem-solving under time pressure.",
        detailed_sections={
            "Core patterns": "Start with arrays/strings, then hashing, sliding window, two pointers, recursion fundamentals. These cover most campus screening questions.",
            "Complexity mindset": "Speak about time and space before coding. For each optimization, justify trade-offs.",
            "Interview approach": "Clarify input constraints, propose brute force, optimize, and dry-run with test cases.",
        },
        common_mistakes=["Jumping into code without discussing approach.", "Ignoring constraints and edge cases.", "Not tracking left/right boundaries in window problems.", "Recursion without base case."],
        code_examples={
            "Sliding Window Sum": """def max_sum_k(nums, k):\n    window = sum(nums[:k])\n    best = window\n    for i in range(k, len(nums)):\n        window += nums[i] - nums[i-k]\n        best = max(best, window)\n    return best""",
            "Two Pointers Pair": """def has_pair(nums, target):\n    nums.sort()\n    l, r = 0, len(nums)-1\n    while l < r:\n        s = nums[l] + nums[r]\n        if s == target: return True\n        if s < target: l += 1\n        else: r -= 1\n    return False""",
        },
        interview_questions=[
            {"q": "When to use hashing?", "a": "When you need fast membership/frequency checks."},
            {"q": "Sliding window vs two pointers?", "a": "Sliding window for contiguous ranges; two pointers for relative pointer movement across sorted/unstructured data."},
            {"q": "What is recursion overhead?", "a": "Call stack memory and function call cost."},
            {"q": "How do you explain O(n log n)?", "a": "Common in divide-and-conquer and sorting algorithms."},
            {"q": "Brute force then optimize—why?", "a": "Shows correctness-first thinking and systematic improvement."},
        ],
        quick_revision_points=["Arrays + hashing solve many easy-medium problems.", "Track invariants in two-pointer methods.", "For recursion: base case, transition, and return value.", "Mention complexity out loud.", "Practice 30-minute timed sets."],
        quiz_questions=[
            _q("Best for duplicate detection quickly?", ["list", "set", "tuple", "heap"], 1, "Set provides O(1)-average membership."),
            _q("Sliding window is mainly for", ["Trees", "Contiguous segments", "Graphs", "Stacks only"], 1, "It optimizes contiguous subarray/substring computations."),
            _q("Recursion must include", ["Loop", "Base case", "Class", "Exception"], 1, "Without base case recursion never terminates."),
            _q("Two pointers usually benefits from", ["Sorting", "Randomization", "Recursion only", "DP table"], 0, "Sorted order often enables linear pointer movement."),
            _q("O(n^2) is usually worse than", ["O(n)", "O(n^3)", "O(2^n)", "All same"], 0, "For large n, O(n) scales much better."),
        ],
        resources=[
            ResourceLink("GeeksforGeeks DSA", "https://www.geeksforgeeks.org/data-structures/", "article", "must_read"),
            ResourceLink("NeetCode roadmap", "https://neetcode.io/roadmap", "article", "must_read"),
            ResourceLink("Abdul Bari algorithms playlist", "https://www.youtube.com/@abdul_bari", "video", "must_watch"),
            ResourceLink("LeetCode patterns", "https://leetcode.com/studyplan/", "article", "deep_dive"),
        ],
    ),
}

# Add remaining topic entries in compact form for maintainability
_ADDITIONAL_TOPICS = {
    "generative_ai": ("Generative AI", "✨", "High", "3 hours"),
    "prompt_engineering": ("Prompt Engineering", "📝", "High", "2 hours"),
    "agentic_ai": ("Agentic AI", "🤖", "High", "2.5 hours"),
    "apis_backend": ("APIs & Backend", "🌐", "High", "2.5 hours"),
    "pandas_data_handling": ("Pandas & Data Handling", "📊", "High", "2.5 hours"),
    "databases": ("Databases", "🗃️", "Medium", "2 hours"),
    "ai_workflows": ("AI Workflows", "🔁", "High", "2 hours"),
    "interview_prep": ("Interview Prep", "🎯", "High", "3 hours"),
}

for key, (title, icon, priority, est) in _ADDITIONAL_TOPICS.items():
    TOPIC_DATA[key] = TopicContent(
        key=key,
        title=title,
        icon=icon,
        difficulty="Beginner-friendly",
        priority=priority,
        estimated_time=est,
        why_it_matters=f"{title} is a frequent discussion area in Movate AI Engineer interviews and helps you explain real-world execution, not just theory.",
        detailed_sections={
            "Core concepts": f"Master the foundational definitions in {title} and explain them with simple analogies.",
            "Interview-level depth": "Move from definitions to trade-offs, implementation decisions, and practical limitations.",
            "Real-world framing": "Use one mini project story to connect this topic to business outcomes like time saved, quality improved, or user experience improved.",
        },
        common_mistakes=[
            "Memorizing definitions without examples.",
            "Not linking concept to implementation.",
            "Giving generic answers without interview context.",
            "Ignoring failure cases and monitoring considerations.",
        ],
        code_examples={
            "Starter Example": """# Explain this snippet in interview:\npipeline = [\"ingest\", \"process\", \"model_call\", \"evaluate\"]\nfor step in pipeline:\n    print(f\"Running: {step}\")"""
        },
        interview_questions=[
            {"q": f"Explain {title} in one minute.", "a": "Start with definition, then workflow, then a practical example."},
            {"q": "What are common pitfalls?", "a": "State one technical and one process pitfall, then mitigation."},
            {"q": "How would you debug issues?", "a": "Use logs, reproducible test cases, and incremental isolation."},
            {"q": "How does this connect to AI product quality?", "a": "It impacts accuracy, reliability, cost, and trust."},
            {"q": "What would you improve next?", "a": "Propose measurable iteration with success metrics."},
        ],
        quick_revision_points=[
            "Definition + use case + limitation = strong answer structure.",
            "Always mention evaluation and monitoring.",
            "Talk in workflow steps, not isolated buzzwords.",
            "Use beginner-friendly but precise language.",
            "End with business impact.",
        ],
        quiz_questions=[
            _q("Best interview answer style?", ["Only definition", "Definition + example + trade-off", "Only formula", "Only buzzwords"], 1, "Interviewers value depth and practical framing."),
            _q("Which improves clarity most?", ["Jargon", "Workflow explanation", "Long monologue", "Skipping examples"], 1, "Workflow explanation shows structured thinking."),
            _q("A good response includes", ["No limitations", "Only benefits", "Benefits and limitations", "Random facts"], 2, "Balanced thinking improves credibility."),
            _q("Best way to revise quickly", ["Quick bullets", "Full textbook", "No notes", "Only videos"], 0, "Condensed points improve retention under time pressure."),
            _q("In interviews, communication should be", ["Confusing", "Structured", "Overly long", "Silent"], 1, "Structured communication is a core evaluation criterion."),
        ],
        resources=[
            ResourceLink("Streamlit docs", "https://docs.streamlit.io/", "article", "must_read"),
            ResourceLink("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read"),
            ResourceLink("Hugging Face LLM course", "https://huggingface.co/learn/llm-course", "article", "deep_dive"),
            ResourceLink("freeCodeCamp AI videos", "https://www.youtube.com/@freecodecamp", "video", "must_watch"),
        ],
    )

# Topic-specific refinements
TOPIC_DATA["generative_ai"] = TOPIC_DATA["generative_ai"].__class__(
    **{**TOPIC_DATA["generative_ai"].__dict__,
       "detailed_sections": {
           "AI vs ML vs DL vs GenAI": "AI is the broad field, ML learns patterns from data, DL uses deep neural networks, and GenAI creates new content (text, image, code).",
           "LLM basics": "LLMs are next-token predictors trained on huge corpora. They are strong language pattern engines, not factual databases.",
           "Tokens, context, temperature": "Token is the unit model reads/writes, context window is memory span per request, temperature controls randomness.",
           "Hallucination and embeddings": "Hallucination is plausible but wrong output. Embeddings convert text to vectors for semantic retrieval and RAG workflows.",
           "Enterprise use cases": "Support copilots, summarization, drafting emails, code assistants, and internal knowledge search with human validation.",
       }}
)

TOPIC_DATA["prompt_engineering"] = TOPIC_DATA["prompt_engineering"].__class__(
    **{**TOPIC_DATA["prompt_engineering"].__dict__,
       "detailed_sections": {
           "Prompting fundamentals": "A prompt is an instruction design problem. Clear goals, context, constraints, and output format improve reliability.",
           "Zero-shot and few-shot": "Zero-shot gives direct instruction; few-shot gives examples to teach response style.",
           "System and user prompts": "System prompts define behavior boundaries; user prompts contain task details.",
           "Structured prompting": "Use sections like Objective, Inputs, Constraints, Output format, Evaluation criteria.",
           "Refinement and hallucination control": "Iterate prompts with guardrails, ask for assumptions, cite sources, and request uncertainty when confidence is low.",
       }}
)

ALL_TOPICS_ORDER = [
    "python", "dsa", "generative_ai", "prompt_engineering", "agentic_ai",
    "apis_backend", "pandas_data_handling", "databases", "ai_workflows", "interview_prep",
]

PAGE_TO_TOPIC = {
    "2_Python": "python",
    "3_DSA": "dsa",
    "4_Generative_AI": "generative_ai",
    "5_Prompt_Engineering": "prompt_engineering",
    "6_Agentic_AI": "agentic_ai",
    "7_APIs_Backend": "apis_backend",
    "8_Pandas_Data_Handling": "pandas_data_handling",
    "9_Databases": "databases",
    "10_AI_Workflows": "ai_workflows",
    "11_Interview_Prep": "interview_prep",
}


# Topic-specific depth for required syllabus coverage
TOPIC_DATA["agentic_ai"] = TOPIC_DATA["agentic_ai"].__class__(
    **{**TOPIC_DATA["agentic_ai"].__dict__,
       "detailed_sections": {
           "What is an AI agent?": "An AI agent is a system that plans actions and calls tools to achieve goals beyond one-shot text generation.",
           "Chatbot vs agent": "A chatbot mostly responds in one turn. An agent can break tasks, decide tool usage, and iterate until completion.",
           "Tool calling and memory": "Tool calling lets an LLM use APIs/databases/calculators. Memory stores conversation or task context to avoid repeating steps.",
           "Multi-step orchestration": "Typical loop: Understand goal → Plan subtasks → Execute tools → Observe outputs → Refine → Return final answer.",
           "Real-world examples": "Ticket triage agent, invoice extraction agent, or sales-assistant agent that reads CRM and drafts next actions.",
       },
       "code_examples": {
           "Simple Agent Pipeline": """steps = ["plan", "retrieve_context", "call_tool", "evaluate", "respond"]
for step in steps:
    print(f"Agent step: {step}")"""
       }}
)

TOPIC_DATA["apis_backend"] = TOPIC_DATA["apis_backend"].__class__(
    **{**TOPIC_DATA["apis_backend"].__dict__,
       "detailed_sections": {
           "API and REST basics": "An API is a contract for software communication. REST commonly uses resources and HTTP verbs.",
           "HTTP methods": "GET reads data, POST creates, PUT updates entire resource, DELETE removes resource.",
           "JSON and status codes": "JSON is a lightweight data format. Key codes: 200 success, 201 created, 400 bad request, 401 unauthorized, 404 not found, 500 server error.",
           "Request/response flow": "Client sends URL + headers + payload. Server validates, processes, and returns status code + data.",
           "AI app integration": "AI apps call embedding APIs, model inference endpoints, vector DB APIs, and business-system APIs for context.",
       },
       "code_examples": {
           "Python requests example": """import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
print(resp.status_code)
print(resp.json()["title"])"""
       }}
)

TOPIC_DATA["pandas_data_handling"] = TOPIC_DATA["pandas_data_handling"].__class__(
    **{**TOPIC_DATA["pandas_data_handling"].__dict__,
       "detailed_sections": {
           "What is Pandas?": "Pandas is a Python library for structured data analysis using DataFrame and Series objects.",
           "DataFrame operations": "Load CSV, inspect schema (`head`, `info`), select columns, filter rows, aggregate, and clean missing values.",
           "Null handling": "Use `isna`, `fillna`, and `dropna` intentionally; document why missing data is filled or removed.",
           "Why this matters for AI": "Model quality depends on input quality. Poorly cleaned data leads to poor model behavior and unreliable outputs.",
       },
       "code_examples": {
           "CSV + Filtering": """import pandas as pd

df = pd.read_csv("data.csv")
clean = df[df["score"] > 70][["name", "score"]]
clean["score"] = clean["score"].fillna(clean["score"].mean())"""
       }}
)

TOPIC_DATA["databases"] = TOPIC_DATA["databases"].__class__(
    **{**TOPIC_DATA["databases"].__dict__,
       "detailed_sections": {
           "DBMS basics": "A DBMS stores and retrieves data reliably with rules around consistency, concurrency, and security.",
           "SQL vs NoSQL": "SQL databases are relational and schema-driven. NoSQL systems offer flexible models for scale and variable structures.",
           "Tables and keys": "Tables contain rows and columns. Primary key uniquely identifies each row.",
           "CRUD and joins": "CRUD = create/read/update/delete. Joins combine data across tables (INNER, LEFT, etc.).",
           "Normalization and AI apps": "Normalization reduces redundancy in transactional systems; AI apps often combine relational data with vector stores for retrieval.",
       },
       "code_examples": {
           "Basic SQL": """SELECT u.name, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.total > 100;"""
       }}
)

TOPIC_DATA["ai_workflows"] = TOPIC_DATA["ai_workflows"].__class__(
    **{**TOPIC_DATA["ai_workflows"].__dict__,
       "detailed_sections": {
           "End-to-end workflow": "Define problem → gather data/context → process inputs → prompt/model call → evaluate output → iterate.",
           "Evaluation": "Use accuracy, relevance, latency, and cost metrics. Add human feedback for qualitative assessment.",
           "Testing and debugging": "Log prompts, model versions, and outputs to reproduce failures. Build small regression test sets.",
           "Human-in-the-loop": "Critical decisions should include user confirmation or reviewer approval.",
           "Deployment thinking": "Start with internal pilot, measure impact, then scale with monitoring and fallback logic.",
       }
    }
)

TOPIC_DATA["interview_prep"] = TOPIC_DATA["interview_prep"].__class__(
    **{**TOPIC_DATA["interview_prep"].__dict__,
       "detailed_sections": {
           "Tell me about yourself": "Present in 60-90 seconds: background, relevant projects, AI skills, and why this role fits your growth path.",
           "Why Movate / why AI Engineer": "Connect company context to your interest in practical AI solutions and customer impact.",
           "Strengths and weaknesses": "Use honest, role-relevant examples and show improvement plan.",
           "Project explanation": "Use Problem → Approach → Stack → Challenges → Outcome structure with measurable result.",
           "HR + technical rounds": "Prepare concise stories for teamwork, conflict, deadlines, and ownership plus domain-specific technical questions.",
           "STAR method": "Situation, Task, Action, Result helps structure behavioral answers clearly.",
       },
       "code_examples": {
           "STAR Template": """Situation: Final-year team had delayed model baseline.
Task: Deliver a demo in 5 days.
Action: Reduced scope, built clean data pipeline, tested prompt variants.
Result: Delivered working demo and improved response relevance by 18%."""
       }
    }
)


TOPIC_DATA["apis_backend"] = TOPIC_DATA["apis_backend"].__class__(
    **{**TOPIC_DATA["apis_backend"].__dict__,
       "resources": [
           ResourceLink("MDN REST APIs intro", "https://developer.mozilla.org/en-US/docs/Glossary/REST", "article", "must_read"),
           ResourceLink("REST API tutorial", "https://restfulapi.net/", "article", "must_read"),
           ResourceLink("Postman API fundamentals", "https://learning.postman.com/docs/getting-started/introduction/", "article", "deep_dive"),
           ResourceLink("freeCodeCamp REST API course", "https://www.youtube.com/watch?v=-MTSQjw5DrM", "video", "must_watch"),
       ]}
)

TOPIC_DATA["pandas_data_handling"] = TOPIC_DATA["pandas_data_handling"].__class__(
    **{**TOPIC_DATA["pandas_data_handling"].__dict__,
       "resources": [
           ResourceLink("Official Pandas docs", "https://pandas.pydata.org/docs/", "article", "must_read"),
           ResourceLink("Kaggle Pandas course", "https://www.kaggle.com/learn/pandas", "article", "must_read"),
           ResourceLink("NumPy quickstart", "https://numpy.org/doc/stable/user/quickstart.html", "article", "deep_dive"),
           ResourceLink("Keith Galli Pandas video", "https://www.youtube.com/watch?v=vmEHCJofslg", "video", "must_watch"),
       ]}
)

TOPIC_DATA["databases"] = TOPIC_DATA["databases"].__class__(
    **{**TOPIC_DATA["databases"].__dict__,
       "resources": [
           ResourceLink("SQLBolt interactive SQL", "https://sqlbolt.com/", "article", "must_read"),
           ResourceLink("W3Schools SQL tutorial", "https://www.w3schools.com/sql/", "article", "must_read"),
           ResourceLink("LeetCode database problems", "https://leetcode.com/problemset/database/", "article", "deep_dive"),
           ResourceLink("freeCodeCamp SQL full course", "https://www.youtube.com/watch?v=HXV3zeQKqGY", "video", "must_watch"),
       ]}
)

TOPIC_DATA["generative_ai"] = TOPIC_DATA["generative_ai"].__class__(
    **{**TOPIC_DATA["generative_ai"].__dict__,
       "resources": [
           ResourceLink("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "must_read"),
           ResourceLink("Google prompt engineering whitepaper", "https://www.kaggle.com/whitepaper-prompt-engineering", "article", "must_read"),
           ResourceLink("OpenAI cookbook", "https://cookbook.openai.com/", "article", "deep_dive"),
           ResourceLink("Andrej Karpathy LLM talk", "https://www.youtube.com/watch?v=zjkBMFhNj_g", "video", "must_watch"),
       ]}
)

TOPIC_DATA["prompt_engineering"] = TOPIC_DATA["prompt_engineering"].__class__(
    **{**TOPIC_DATA["prompt_engineering"].__dict__,
       "resources": [
           ResourceLink("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read"),
           ResourceLink("OpenAI prompt engineering guide", "https://platform.openai.com/docs/guides/prompt-engineering", "article", "must_read"),
           ResourceLink("Anthropic prompt library", "https://docs.anthropic.com/en/prompt-library/library", "article", "deep_dive"),
           ResourceLink("DeepLearning.AI Prompt Engineering intro", "https://www.youtube.com/watch?v=dOxUroR57xs", "video", "must_watch"),
       ]}
)


TOPIC_DATA["interview_prep"] = TOPIC_DATA["interview_prep"].__class__(
    **{**TOPIC_DATA["interview_prep"].__dict__,
       "interview_questions": [
           {"q": "Tell me about yourself for this AI Engineer role.", "a": "Use a 3-part pitch: current profile, relevant AI projects, and what you want to contribute at Movate."},
           {"q": "Why Movate?", "a": "Mention customer-facing technology, global delivery exposure, and your excitement for practical AI impact."},
           {"q": "Why AI Engineer and not generic software role?", "a": "You enjoy building intelligent workflows that combine coding, data understanding, and user-centric iteration."},
           {"q": "Explain one project end-to-end.", "a": "Share architecture, API/data flow, evaluation metric, challenge, and result."},
           {"q": "Give one STAR example for teamwork/conflict.", "a": "Pick a real event, keep action-focused, and include measurable result."},
       ],
       "quick_revision_points": [
           "Prepare a 90-second intro and practice aloud.",
           "Keep two strong project stories ready with metrics.",
           "For strengths/weaknesses: be honest + improvement plan.",
           "Use STAR for HR and behavior-based questions.",
           "End every answer with impact and learning.",
       ]}
)
