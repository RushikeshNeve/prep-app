"""Structured content for the Movate AI Engineer Prep App."""

from dataclasses import dataclass, field
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
    kind: str
    tier: str
    description: str = ""


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
    importance_for_movate: str = ""
    role_relevance: List[str] = field(default_factory=list)
    learning_objectives: List[str] = field(default_factory=list)
    learn_sections: List[Dict[str, object]] = field(default_factory=list)
    use_cases: List[Dict[str, object]] = field(default_factory=list)
    techniques: List[Dict[str, object]] = field(default_factory=list)
    worked_examples: List[Dict[str, object]] = field(default_factory=list)
    debugging_sections: List[Dict[str, object]] = field(default_factory=list)
    operations: List[Dict[str, object]] = field(default_factory=list)
    cleaning_sections: List[Dict[str, object]] = field(default_factory=list)
    ai_workflow_examples: List[Dict[str, object]] = field(default_factory=list)
    sql_sections: List[Dict[str, object]] = field(default_factory=list)
    nosql_sections: List[Dict[str, object]] = field(default_factory=list)
    vector_db_sections: List[Dict[str, object]] = field(default_factory=list)
    ai_use_cases: List[Dict[str, object]] = field(default_factory=list)
    workflow_types: List[Dict[str, object]] = field(default_factory=list)
    system_design_sections: List[Dict[str, object]] = field(default_factory=list)
    evaluation_sections: List[Dict[str, object]] = field(default_factory=list)
    rest_sections: List[Dict[str, object]] = field(default_factory=list)
    ai_integration_examples: List[Dict[str, object]] = field(default_factory=list)
    architectures: List[Dict[str, object]] = field(default_factory=list)
    workflows: List[Dict[str, object]] = field(default_factory=list)
    patterns: List[Dict[str, object]] = field(default_factory=list)
    interview_questions_detailed: List[Dict[str, str]] = field(default_factory=list)
    interview_scenarios: List[Dict[str, object]] = field(default_factory=list)
    interview_rapid_fire: List[Dict[str, str]] = field(default_factory=list)
    interview_common_mistakes: List[str] = field(default_factory=list)
    resource_sections: Dict[str, List[ResourceLink]] = field(default_factory=dict)
    flow_diagrams: List[Dict[str, str]] = field(default_factory=list)


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


def _r(title: str, url: str, kind: str, tier: str, description: str) -> ResourceLink:
    return ResourceLink(title=title, url=url, kind=kind, tier=tier, description=description)


PYTHON_TOPIC = TopicContent(
    key="python",
    title="Python",
    icon="PY",
    difficulty="Beginner to Intermediate",
    priority="Very High",
    estimated_time="3 to 4 hours",
    importance_for_movate="Very High",
    why_it_matters=(
        "Python is the main execution language for campus AI Engineer work because it is easy to read, fast to prototype in, "
        "and supported by the strongest ecosystem for AI, automation, APIs, data handling, and backend scripting."
    ),
    role_relevance=[
        "AI experimentation and quick proof-of-concept building",
        "Prompt workflows and orchestration scripts",
        "Data handling with Pandas and NumPy",
        "Backend support and internal automation",
        "API integrations with model and business systems",
    ],
    learning_objectives=[
        "Learn Python from basics to interview-ready problem solving.",
        "Connect core syntax with AI engineering use cases.",
        "Revise common coding patterns asked in placement interviews.",
        "Practice short, clear explanations you can speak during interviews.",
    ],
    detailed_sections={
        "Python basics": "Python is an interpreted, high-level, readable language. Focus on syntax, variables, input/output, typing, and indentation.",
        "Collections and strings": "Lists, tuples, sets, dictionaries, and strings appear in almost every interview coding question.",
        "Control flow and functions": "Strong basics in loops, conditions, and functions help you write clean problem-solving code quickly.",
        "OOP, exceptions, and files": "These topics matter for practical engineering discussions and beginner backend tasks.",
        "Interview coding patterns": "Frequency maps, string operations, filtering, and common utility functions are high-value revision topics.",
    },
    common_mistakes=[
        "Treating list, tuple, set, and dict as if they behave the same.",
        "Forgetting that strings and tuples are immutable.",
        "Using `is` when `==` should be used for value comparison.",
        "Writing loops without thinking about edge cases like empty input.",
        "Explaining OOP in theory but failing to connect it to a simple class example.",
    ],
    code_examples={
        "Basic Types": """age = 21          # int
score = 88.5      # float
name = "Riya"     # str
is_selected = True  # bool

print(type(age))
print(int("42"))
print(float("3.14"))
print(str(100))
""",
        "Dictionary Frequency Count": """text = "movate"
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
""",
        "OOP Example": """class Student:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def introduce(self):
        return f"{self.name} is learning {self.skill}"

student = Student("Asha", "Python")
print(student.introduce())
""",
        "Exception Handling": """try:
    value = int("abc")
except ValueError:
    print("Please enter a valid integer")
finally:
    print("Program finished")
""",
    },
    learn_sections=[],
    patterns=[],
    interview_questions=[],
    interview_questions_detailed=[],
    interview_rapid_fire=[],
    interview_common_mistakes=[],
    quick_revision_points=[],
    quiz_questions=[],
    resources=[],
    resource_sections={},
)


TOPIC_DATA: Dict[str, TopicContent] = {"python": PYTHON_TOPIC}


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "learn_sections": [
            {
                "title": "A. Python Basics",
                "summary": "Build the mental model: what Python is, why it is popular, and how its syntax helps in interviews and fast development.",
                "points": [
                    "Python is a general-purpose programming language used for scripting, backend work, data analysis, automation, and AI.",
                    "It is popular because the syntax is readable, the learning curve is friendly, and the library ecosystem is very strong.",
                    "Python is interpreted. This means code is executed by an interpreter line by line at runtime instead of being fully compiled first in the way languages like C often are.",
                    "Dynamic typing means you do not declare the variable type explicitly. The type is decided from the value assigned at runtime.",
                    "Simple syntax reduces interview friction. You spend less time on boilerplate and more time explaining logic.",
                    "Indentation is part of Python syntax. It defines blocks for `if`, loops, functions, and classes.",
                    "Comments improve readability. Use `#` for single-line comments and docstrings for function/class descriptions.",
                    "Variable naming rules: names can include letters, digits, and `_`, cannot start with a digit, and should not use reserved keywords like `class` or `for`.",
                ],
                "examples": [
                    {
                        "label": "Input, output, and type conversion",
                        "code": """name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("Hello,", name)
print("Next year age:", age + 1)
print("Height:", height)
""",
                    },
                    {
                        "label": "Indentation and comments",
                        "code": """score = 78

# Check whether the student cleared the cutoff
if score >= 60:
    print("Qualified")
else:
    print("Not qualified")
""",
                    },
                ],
                "callouts": [
                    {"type": "info", "text": "Interview tip: when asked why Python is easy to use, mention readability, less boilerplate, and strong libraries."},
                    {"type": "warning", "text": "Common mistake: mixing tabs and spaces or forgetting indentation after `if`, `for`, `def`, or `class`."},
                ],
                "notes": [
                    "Dynamic typing helps speed but also means you should be careful about unexpected types.",
                    "Beginners often say Python is compiled. A cleaner answer is: Python code is typically interpreted, although it is first converted to bytecode internally.",
                ],
            },
            {
                "title": "B. Data Types and Collections",
                "summary": "This is one of the highest-value interview areas because almost every coding task uses built-in Python data types.",
                "points": [
                    "`int` stores whole numbers like `10` or `-3`.",
                    "`float` stores decimal numbers like `3.14`.",
                    "`str` stores text. Strings are immutable.",
                    "`bool` stores `True` or `False`.",
                    "`None` represents the absence of a value.",
                ],
                "subtopics": [
                    {
                        "title": "List",
                        "content": [
                            "Definition: ordered, mutable collection.",
                            "Use when: you need indexing and may add, remove, or update items.",
                            "Mutability: mutable.",
                            "Ordering: ordered.",
                            "Duplicates: allowed.",
                            "Common methods: `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`.",
                            "Interview note: lists are the default choice for array-like problems in Python.",
                        ],
                        "code": """nums = [10, 20, 30]
nums.append(40)
nums[1] = 99
print(nums)
""",
                    },
                    {
                        "title": "Tuple",
                        "content": [
                            "Definition: ordered, immutable collection.",
                            "Use when: data should stay fixed, such as coordinates or a record-like value.",
                            "Mutability: immutable.",
                            "Ordering: ordered.",
                            "Duplicates: allowed.",
                            "Common methods: `count`, `index`.",
                            "Interview note: tuples can be used as dictionary keys if their elements are hashable.",
                        ],
                        "code": """point = (4, 7)
print(point[0])
""",
                    },
                    {
                        "title": "Set",
                        "content": [
                            "Definition: unordered collection of unique elements.",
                            "Use when: you need fast membership tests or to remove duplicates.",
                            "Mutability: mutable set, immutable version is `frozenset`.",
                            "Ordering: unordered from an interview perspective.",
                            "Duplicates: not allowed.",
                            "Common methods: `add`, `remove`, `discard`, `union`, `intersection`.",
                            "Interview note: average membership lookup is O(1).",
                        ],
                        "code": """skills = {"python", "sql", "python"}
skills.add("pandas")
print(skills)
""",
                    },
                    {
                        "title": "Dictionary",
                        "content": [
                            "Definition: key-value mapping.",
                            "Use when: you need lookup by key, frequency counts, grouped data, or structured records.",
                            "Mutability: mutable.",
                            "Ordering: insertion order is preserved in modern Python.",
                            "Duplicates: keys must be unique, values can repeat.",
                            "Common methods: `get`, `keys`, `values`, `items`, `update`, `pop`.",
                            "Interview note: `dict.get(key, default)` avoids `KeyError` and is common in counting problems.",
                        ],
                        "code": """student = {"name": "Ravi", "score": 92}
print(student.get("name"))
print(student.get("city", "Not available"))
""",
                    },
                ],
                "tables": [
                    {
                        "title": "List vs Tuple vs Set",
                        "markdown": """| Type | Ordered | Mutable | Duplicates | Best use |
|---|---|---|---|---|
| List | Yes | Yes | Yes | Sequence that changes |
| Tuple | Yes | No | Yes | Fixed record |
| Set | No | Yes | No | Unique values and fast membership |""",
                    },
                    {
                        "title": "Dict vs Set",
                        "markdown": """| Feature | Dict | Set |
|---|---|---|
| Stores | Key-value pairs | Unique values only |
| Access | By key | Membership check |
| Example | `{"a": 1}` | `{"a", "b"}` |
| Best use | Mapping and counts | Deduplication and lookup |""",
                    },
                    {
                        "title": "Mutable vs Immutable",
                        "markdown": """| Category | Examples | Can change after creation? |
|---|---|---|
| Mutable | list, dict, set | Yes |
| Immutable | int, float, str, tuple, bool, None | No |""",
                    },
                ],
                "callouts": [
                    {"type": "success", "text": "Short interview answer: list is mutable, tuple is immutable, set stores unique values, dict stores key-value pairs."},
                    {"type": "warning", "text": "Common mistake: saying a set is just a dictionary without values. A set is its own type and only stores unique elements."},
                ],
            },
            {
                "title": "C. Strings",
                "summary": "Strings are heavily tested because they combine indexing, slicing, loops, conditionals, and immutability.",
                "points": [
                    "Strings are sequences of characters.",
                    "Indexing accesses one character, for example `s[0]`.",
                    "Slicing extracts a part of the string, for example `s[1:4]`.",
                    "Negative indexing starts from the end, for example `s[-1]` gives the last character.",
                    "Strings are immutable. You cannot change one character directly.",
                ],
                "examples": [
                    {
                        "label": "Indexing and slicing",
                        "code": """text = "python"
print(text[0])    # p
print(text[-1])   # n
print(text[1:4])  # yth
print(text[::-1]) # nohtyp
""",
                    },
                    {
                        "label": "Split, join, replace, strip",
                        "code": """line = "  ai engineer role  "
words = line.strip().split()
clean = "-".join(words)
updated = clean.replace("role", "prep")

print(words)
print(clean)
print(updated.upper())
""",
                    },
                    {
                        "label": "Palindrome check",
                        "code": """def is_palindrome(text):
    clean = text.lower()
    return clean == clean[::-1]

print(is_palindrome("madam"))
""",
                    },
                ],
                "notes": [
                    "To reverse a string, `s[::-1]` is the shortest solution.",
                    "To compare case-insensitively, convert both strings with `lower()` or `casefold()`.",
                    "To update a character, create a new string instead of trying `s[0] = 'a'`.",
                ],
                "mistakes": [
                    "Trying to modify a string using item assignment.",
                    "Using wrong slice boundaries and forgetting that end index is excluded.",
                    "Confusing `split()` and `join()`.",
                ],
            },
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC

TOPIC_DATA["generative_ai"] = TopicContent(
    key="generative_ai",
    title="Generative AI",
    icon="GAI",
    difficulty="Beginner-friendly",
    priority="High",
    estimated_time="3 hours",
    why_it_matters="Generative AI matters because modern AI products increasingly depend on model-generated content and workflows.",
    detailed_sections={},
    common_mistakes=[],
    code_examples={},
    interview_questions=[],
    quick_revision_points=[],
    quiz_questions=[],
    resources=[],
)


GENERATIVE_AI_TOPIC = TOPIC_DATA["generative_ai"].__class__(
    **{
        **TOPIC_DATA["generative_ai"].__dict__,
        "difficulty": "Beginner to Intermediate",
        "priority": "Very High",
        "estimated_time": "3 to 4 hours",
        "importance_for_movate": "Very High",
        "why_it_matters": (
            "Generative AI is the part of AI that creates new content such as text, code, images, summaries, answers, and workflows. "
            "For a campus AI Engineer role, it matters because modern enterprise products increasingly use copilots, prompt-based interfaces, "
            "retrieval systems, and agentic workflows to automate knowledge work."
        ),
        "role_relevance": [
            "Enterprise AI use cases such as support assistants and internal knowledge tools",
            "Prompt-based applications and copilots",
            "Agentic workflows that combine models, tools, and APIs",
            "Automation for knowledge work, ticket handling, and document processing",
            "Evaluation, experimentation, and safer deployment of AI features",
        ],
        "learning_objectives": [
            "Understand Generative AI from first principles without needing a deep math background.",
            "Explain LLMs, tokens, context, hallucination, embeddings, and RAG clearly in interviews.",
            "Connect theory to enterprise AI use cases expected in an AI Engineer role.",
            "Revise fast with crisp interview answers and compact notes before placement rounds.",
        ],
        "detailed_sections": {
            "Foundations": "Understand how AI, ML, deep learning, and Generative AI relate to each other.",
            "LLM basics": "Learn what a large language model does, how next-token prediction works, and what common misconceptions sound like.",
            "Prompting, context, and control": "Understand tokens, context windows, temperature, prompting basics, and output control.",
            "Grounding and retrieval": "Learn embeddings, semantic search, RAG, and why grounding matters in enterprise systems.",
            "Applications and risks": "Connect GenAI to enterprise use cases, limitations, safety, evaluation, and AI Engineer responsibilities.",
        },
        "common_mistakes": [
            "Confusing Generative AI with all of AI or with basic machine learning.",
            "Saying an LLM understands exactly like a human.",
            "Explaining hallucination vaguely without saying why it is risky in business systems.",
            "Not knowing RAG, embeddings, or grounding at a beginner level.",
            "Giving only theory and no practical use case examples.",
        ],
        "learn_sections": [
            {
                "title": "A. AI vs ML vs Deep Learning vs Generative AI",
                "summary": "This is the first distinction interviewers often test because it shows whether your mental model is layered and clear.",
                "points": [
                    "Artificial Intelligence is the broad field of making systems perform tasks that seem intelligent.",
                    "Machine Learning is a subset of AI where systems learn patterns from data.",
                    "Deep Learning is a subset of machine learning that uses multi-layer neural networks.",
                    "Generative AI is a subset of AI focused on creating new content such as text, code, images, audio, or video.",
                    "Predictive AI usually predicts a label, score, or next class. Generative AI produces a new output such as an answer, paragraph, or image.",
                ],
                "tables": [
                    {
                        "title": "Layered relationship",
                        "markdown": """| Layer | Simple meaning | Example |
|---|---|---|
| AI | Broad goal of intelligent behavior | Chess engine, chatbot, recommendation logic |
| ML | Learns patterns from data | Spam classifier |
| Deep Learning | Neural-network-based ML | Image recognition model |
| Generative AI | Creates new content | Text assistant, image generator, code copilot |""",
                    },
                    {
                        "title": "Predictive AI vs Generative AI",
                        "markdown": """| Type | Typical output | Example task |
|---|---|---|
| Predictive AI | Label, score, class | Fraud detection, demand prediction |
| Generative AI | New text, image, code, summary | Draft email, chatbot answer, generated image |""",
                    },
                ],
                "examples": [
                    {
                        "label": "Simple layered view",
                        "code": """AI
└── Machine Learning
    └── Deep Learning
        └── Generative AI (one important modern area)
""",
                    }
                ],
                "callouts": [
                    {"type": "info", "text": "Interview tip: say Generative AI is part of the wider AI landscape, not a replacement for all ML."},
                    {"type": "warning", "text": "Common confusion: every chatbot is not automatically Generative AI. Some are mainly rule-based or retrieval-based."},
                ],
                "notes": [
                    "A classifier predicts from known labels. A generative system creates a fresh output.",
                    "A good interview answer starts broad, then narrows down to Generative AI.",
                ],
            },
            {
                "title": "B. What is Generative AI",
                "summary": "Generative AI creates new content instead of only classifying or retrieving information.",
                "points": [
                    "Generative AI can create text, code, images, audio, video, and structured output.",
                    "It is different from simple retrieval. Retrieval finds existing information; generation creates a new response based on patterns plus provided context.",
                    "It became popular recently because model quality improved, compute became more available, and product interfaces made it easy for people to use natural language.",
                    "A simple analogy: retrieval is like finding a paragraph in a library; generation is like writing a new paragraph after reading many examples and the provided context.",
                ],
                "examples": [
                    {
                        "label": "Retrieval vs generation",
                        "code": """Question: "Summarize this support ticket"
Retrieval system: fetches similar past tickets
Generative system: writes a new summary in natural language
""",
                    }
                ],
                "notes": [
                    "Generation does not mean the output is always factual.",
                    "Most useful enterprise systems combine retrieval and generation.",
                ],
            },
            {
                "title": "C. What is an LLM",
                "summary": "A large language model is a model trained on large amounts of text to predict what token should come next.",
                "points": [
                    "LLM stands for Large Language Model.",
                    "In simple words, an LLM is a system trained to continue text in a useful way based on patterns learned from large text data.",
                    "It predicts the next token repeatedly, not the whole answer in one step.",
                    "It does not understand exactly like a human. It is very strong at language patterns, but that is different from human understanding.",
                    "LLMs are useful for chatbots, copilots, summarizers, Q&A systems, assistants, and code help.",
                ],
                "examples": [
                    {
                        "label": "Tiny next-token idea",
                        "code": """Prompt: "The capital of France is"
Likely next token: " Paris"

The model keeps doing this repeatedly:
prompt -> next token -> next token -> next token
""",
                    }
                ],
                "callouts": [
                    {"type": "success", "text": "Interview-ready line: an LLM is a next-token prediction model trained on large text corpora."},
                    {"type": "warning", "text": "Common confusion: strong text generation does not mean perfect reasoning or guaranteed truth."},
                ],
                "notes": [
                    "A model can sound confident even when it is wrong.",
                    "The output quality depends on prompt quality, context, and model capability.",
                ],
            },
            {
                "title": "D. Tokens",
                "summary": "Tokens are the units a language model reads and generates. They matter for cost, speed, and context size.",
                "points": [
                    "A token is a small chunk of text used internally by the model.",
                    "A token is not always equal to one word. One word can map to one token or multiple tokens depending on the tokenizer.",
                    "Token count affects cost because most APIs charge based on input and output tokens.",
                    "Token count affects latency because more tokens usually mean more processing time.",
                    "Prompt tokens and response tokens both matter in real applications.",
                ],
                "examples": [
                    {
                        "label": "Conceptual token idea",
                        "code": """Sentence: "I love AI"
Conceptually, it may become tokens like:
["I", " love", " AI"]

Sentence: "tokenization"
May split into smaller pieces depending on the model.
""",
                    }
                ],
                "notes": [
                    "You do not need tokenizer-level detail for most interviews.",
                    "You do need to know why token count affects context, cost, and latency.",
                ],
            },
            {
                "title": "E. Context Window",
                "summary": "The context window is the amount of text the model can consider at one time in a request.",
                "points": [
                    "A context window is the effective working memory available in a single model call.",
                    "If the input is too long, older information may be dropped, truncated, or summarized before the model sees it.",
                    "This matters in chatbots, document Q&A, and long enterprise conversations.",
                    "When context is too long, systems may use summarization, chunking, or retrieval to keep the most relevant information.",
                ],
                "examples": [
                    {
                        "label": "Simple flow",
                        "code": """Long history or large document
-> pick relevant pieces
-> fit inside context window
-> send to model
""",
                    }
                ],
                "callouts": [
                    {"type": "info", "text": "Interview tip: context window is not the same as permanent memory. It is request-time working memory."}
                ],
            },
            {
                "title": "F. Temperature and Output Control",
                "summary": "Temperature controls randomness in model output. Lower values usually make outputs more stable, while higher values allow more variation.",
                "points": [
                    "Low temperature is better when you want consistency, factual tone, or structured answers.",
                    "Higher temperature can be useful for brainstorming, creative writing, or generating multiple diverse ideas.",
                    "There is usually a trade-off between strictness and creativity.",
                    "Top-p is another sampling control. Beginner-friendly idea: it limits how much probability mass the model samples from.",
                ],
                "tables": [
                    {
                        "title": "Low vs high temperature",
                        "markdown": """| Setting | Tendency | Good for |
|---|---|---|
| Low temperature | More stable and focused | Q&A, extraction, enterprise workflows |
| Higher temperature | More varied and creative | Brainstorming, creative drafts |""",
                    }
                ],
                "notes": [
                    "Low temperature does not guarantee truth.",
                    "Sampling controls affect style and variability, not magical correctness.",
                ],
            },
            {
                "title": "G. Hallucination",
                "summary": "Hallucination means the model produces information that sounds plausible but is wrong, unsupported, or invented.",
                "points": [
                    "Hallucination happens because the model is generating the most likely continuation, not directly verifying facts like a database.",
                    "It may invent citations, product details, customer facts, or process steps if grounding is weak.",
                    "Hallucination is risky in enterprise systems because wrong answers can damage trust, create compliance issues, or lead to poor decisions.",
                ],
                "examples": [
                    {
                        "label": "Hallucination reduction flow",
                        "code": """User Query
-> Retrieve trusted company docs
-> Build constrained prompt
-> Model answer
-> Human review for sensitive cases
""",
                    }
                ],
                "callouts": [
                    {"type": "warning", "text": "Never present hallucination as only a rare bug. It is a core risk to manage in production GenAI systems."}
                ],
                "notes": [
                    "Ways to reduce hallucination: better prompts, grounding with retrieved data, output constraints, tool use, and human review.",
                    "Even strong models need system design around them.",
                ],
            },
            {
                "title": "H. Prompting Basics",
                "summary": "A prompt is the instruction and context given to the model. Good prompting improves relevance, structure, and reliability.",
                "points": [
                    "System-level instructions define behavior or boundaries at a high level.",
                    "User instructions describe the task and input.",
                    "Good prompts are clear, specific, and explicit about output format.",
                    "Role prompting can help frame the answer, such as asking the model to behave like a support assistant or recruiter assistant.",
                    "Structured prompts often include goal, context, constraints, and desired output format.",
                ],
                "examples": [
                    {
                        "label": "Basic structured prompt",
                        "code": """Task: Summarize the document
Audience: Support manager
Constraints: Use 5 bullet points, no extra facts
Output format: bullet list
""",
                    }
                ],
                "notes": [
                    "Prompt engineering has its own page, but you should still be able to explain why prompt clarity matters.",
                    "Asking for JSON, bullets, or a table is a simple but powerful control technique.",
                ],
            },
            {
                "title": "I. Embeddings and Semantic Search",
                "summary": "Embeddings convert text into vectors so systems can compare meaning, not just exact keyword overlap.",
                "points": [
                    "An embedding is a numeric vector representation of text.",
                    "Texts with similar meaning tend to have embeddings that are close together in vector space.",
                    "Semantic search uses this idea to find relevant content even when the exact words differ.",
                    "This matters in enterprise search, document retrieval, FAQ systems, and RAG pipelines.",
                ],
                "examples": [
                    {
                        "label": "Intuitive view",
                        "code": """'reset password'
'forgot login credentials'

Different words, similar meaning
-> embeddings help place them near each other
""",
                    }
                ],
                "callouts": [
                    {"type": "info", "text": "Common confusion: embeddings help find relevant information; they do not directly generate the final answer."}
                ],
            },
            {
                "title": "J. RAG (Retrieval-Augmented Generation)",
                "summary": "RAG combines retrieval with generation so the model answers using relevant external information.",
                "points": [
                    "RAG is useful when you want answers based on current or company-specific documents.",
                    "Basic flow: user query -> retrieve relevant documents -> send the relevant chunks to the model -> generate answer.",
                    "It reduces hallucination because the model is grounded in retrieved evidence.",
                    "It is common in enterprise knowledge assistants, document Q&A, internal copilots, and helpdesk systems.",
                ],
                "examples": [
                    {
                        "label": "ASCII flow",
                        "code": """User Query -> Retrieval -> Prompt -> Model -> Response
""",
                    }
                ],
                "notes": [
                    "RAG is often a better first step than fine-tuning for private knowledge use cases.",
                    "Good chunking, retrieval quality, and citation handling matter a lot.",
                ],
            },
            {
                "title": "K. Fine-tuning vs Prompting",
                "summary": "Interviewers often want to know when you would use prompt engineering, retrieval, or fine-tuning.",
                "points": [
                    "Prompting changes behavior through instructions and examples.",
                    "Retrieval adds relevant external knowledge at runtime.",
                    "Fine-tuning adjusts the model on task-specific data to shift style or task behavior more deeply.",
                    "In many real projects, teams start with good prompting plus retrieval before considering fine-tuning.",
                ],
                "tables": [
                    {
                        "title": "Prompting vs retrieval vs fine-tuning",
                        "markdown": """| Approach | Best when | Trade-off |
|---|---|---|
| Prompting | Fast iteration and instruction control | Limited by model's existing knowledge and behavior |
| Retrieval | Need current or private knowledge | Requires document pipeline and search quality |
| Fine-tuning | Need deeper behavior/style adaptation | Higher effort, data needs, and maintenance |""",
                    }
                ],
            },
            {
                "title": "L. GenAI Application Workflow",
                "summary": "A real GenAI application is more than one model call. It is a system with prompting, retrieval, checks, logging, and iteration.",
                "points": [
                    "User gives input.",
                    "Application builds the prompt and may add retrieved context or tool results.",
                    "Model is called through an API.",
                    "Optional retrieval or tool usage helps grounding and task completion.",
                    "Response is generated, validated, logged, and possibly sent for human review.",
                    "Evaluation and feedback improve prompts, retrieval, and system design over time.",
                ],
                "examples": [
                    {
                        "label": "Simple workflow",
                        "code": """User input
-> Prompt builder
-> Optional retrieval / tool calls
-> Model API
-> Response
-> Logging + evaluation + safety checks
""",
                    }
                ],
            },
            {
                "title": "M. Limitations and Risks",
                "summary": "Generative AI is powerful but not enough by itself for every business problem.",
                "points": [
                    "Hallucination can lead to wrong answers.",
                    "Bias in outputs can affect fairness and trust.",
                    "Model knowledge may be outdated or incomplete.",
                    "Privacy and security matter when business or customer data is involved.",
                    "Prompt injection is a risk when the model consumes untrusted external content.",
                    "Over-reliance can make people trust outputs without verification.",
                    "Cost and latency matter in production systems with high usage.",
                ],
                "callouts": [
                    {"type": "warning", "text": "Interview tip: strong answers about GenAI always mention both capability and risk."}
                ],
            },
            {
                "title": "N. Generative AI in Enterprise / AI Engineer Context",
                "summary": "This role-focused section connects Generative AI concepts with what an AI Engineer actually builds and maintains.",
                "points": [
                    "Chatbots and support assistants",
                    "Internal copilots for teams",
                    "Document summarization and Q&A",
                    "Ticket assistance and workflow automation",
                    "Code assistance and productivity tools",
                    "Enterprise search and knowledge assistants",
                    "Prompt pipelines, evaluation, and experimentation",
                    "Human-in-the-loop systems for quality control",
                ],
                "notes": [
                    "An AI Engineer is not only prompting a model. They are integrating APIs, retrieval, logging, guardrails, evaluation, and user experience.",
                    "Enterprise work values reliability, observability, and measurable impact as much as model output quality.",
                ],
            },
        ],
        "use_cases": [
            {
                "title": "Chatbots and assistants",
                "what_it_does": "Answers user questions in natural language and helps users complete tasks through conversation.",
                "why_businesses_use_it": "It improves accessibility, reduces response time, and creates a familiar interface for users.",
                "architecture": "User -> App UI -> Prompt builder -> Model -> Response",
                "risks": "Hallucination, inconsistent tone, and weak grounding when domain knowledge is missing.",
            },
            {
                "title": "Customer support automation",
                "what_it_does": "Drafts replies, summarizes tickets, suggests troubleshooting steps, and routes issues.",
                "why_businesses_use_it": "It reduces manual workload and speeds up support operations.",
                "architecture": "Ticket -> Retrieve KB articles -> Prompt -> Model -> Draft response",
                "risks": "Wrong support advice, privacy issues, and over-trusting auto-generated answers.",
            },
            {
                "title": "Content summarization",
                "what_it_does": "Condenses long documents, emails, or reports into short useful summaries.",
                "why_businesses_use_it": "It saves time and helps teams process information faster.",
                "architecture": "Document -> Chunk or summarize -> Model -> Summary",
                "risks": "Important details may be dropped or distorted.",
            },
            {
                "title": "Document Q&A",
                "what_it_does": "Lets users ask questions about uploaded or indexed documents.",
                "why_businesses_use_it": "It helps employees get answers from manuals, policies, contracts, or knowledge bases quickly.",
                "architecture": "User query -> Retrieval -> Prompt with docs -> Model answer",
                "risks": "Poor retrieval quality, hallucinated answers, and document permission issues.",
            },
            {
                "title": "Code generation",
                "what_it_does": "Helps generate code snippets, explain code, refactor logic, or draft tests.",
                "why_businesses_use_it": "It improves developer productivity and speeds up prototyping.",
                "architecture": "Developer request -> Prompt -> Model -> Suggested code",
                "risks": "Incorrect logic, insecure code, or hidden bugs if outputs are not reviewed.",
            },
            {
                "title": "Email drafting",
                "what_it_does": "Drafts or rewrites emails from short instructions or context.",
                "why_businesses_use_it": "It saves time in repetitive communication work.",
                "architecture": "Intent + context -> Prompt -> Model -> Draft email",
                "risks": "Wrong tone, privacy issues, or missing factual details.",
            },
            {
                "title": "Classification and extraction",
                "what_it_does": "Extracts fields, labels content, or converts unstructured text into structured output.",
                "why_businesses_use_it": "It helps automate document workflows and data entry tasks.",
                "architecture": "Raw text -> Prompt with schema -> Model -> Structured output",
                "risks": "Format inconsistency and extraction errors on edge cases.",
            },
            {
                "title": "Knowledge base assistants",
                "what_it_does": "Answers employee questions from internal policies, docs, and process guides.",
                "why_businesses_use_it": "It reduces search time and improves knowledge accessibility.",
                "architecture": "User query -> Embeddings search -> Retrieved docs -> Model answer",
                "risks": "Outdated content, access control issues, and weak citation behavior.",
            },
            {
                "title": "Internal enterprise copilots",
                "what_it_does": "Supports employees across tasks such as drafting, search, summarization, and workflow guidance.",
                "why_businesses_use_it": "It boosts productivity across multiple teams with one AI layer.",
                "architecture": "User task -> Context + tools + retrieval -> Model -> Checked response",
                "risks": "Governance complexity, tool misuse, and over-reliance on AI output.",
            },
        ],
    }
)


TOPIC_DATA["generative_ai"] = GENERATIVE_AI_TOPIC


GENERATIVE_AI_TOPIC = GENERATIVE_AI_TOPIC.__class__(
    **{
        **GENERATIVE_AI_TOPIC.__dict__,
        "interview_questions": [
            {"q": "What is Generative AI?", "a": "Generative AI creates new content such as text, code, or images rather than only predicting labels."},
            {"q": "What is an LLM?", "a": "An LLM is a large language model trained to predict the next token based on patterns in text."},
            {"q": "What is a token?", "a": "A token is a unit of text used internally by the model."},
            {"q": "What is RAG?", "a": "RAG combines retrieval with generation so answers can use relevant external documents."},
            {"q": "What is hallucination?", "a": "Hallucination is when a model gives a plausible but unsupported or incorrect answer."},
        ],
        "interview_questions_detailed": [
            {"question": "What is Generative AI?", "short_answer": "Generative AI is AI that creates new content such as text, code, images, audio, or summaries.", "spoken_answer": "Generative AI focuses on producing new outputs instead of only predicting a class or score. In practice, that means systems can draft emails, summarize documents, generate code, answer questions, and create images or other content."},
            {"question": "Difference between AI, ML, DL, and Generative AI?", "short_answer": "AI is the broad field, ML is a subset that learns from data, deep learning is neural-network-based ML, and Generative AI creates new content.", "spoken_answer": "I explain it as layers. AI is the broad umbrella of intelligent systems. Machine learning is when the system learns patterns from data. Deep learning is ML using deep neural networks. Generative AI is a modern area that uses these ideas to generate fresh outputs like text, code, and images."},
            {"question": "What is an LLM?", "short_answer": "An LLM is a Large Language Model trained on large amounts of text to predict the next token.", "spoken_answer": "In simple words, an LLM is a model that has learned language patterns from massive text data. At inference time, it predicts the next token repeatedly, which lets it generate answers, summaries, code, and conversations."},
            {"question": "What is a token?", "short_answer": "A token is a small unit of text used by the model while reading and generating language.", "spoken_answer": "Tokens are the units the model actually processes internally. They are not always the same as words. Token count matters because it affects cost, latency, and how much text fits inside the context window."},
            {"question": "What is a context window?", "short_answer": "A context window is the amount of text the model can consider in one request.", "spoken_answer": "I think of the context window as the model's working memory during a single interaction. If the conversation or document is too large, the system may need chunking, summarization, or retrieval so the most relevant information fits."},
            {"question": "What is temperature?", "short_answer": "Temperature controls output randomness. Lower values are more stable, higher values are more creative.", "spoken_answer": "Temperature changes how varied the model output can be. For enterprise tasks like extraction or support Q&A, lower temperature is usually better. For brainstorming or creative drafting, slightly higher temperature can help produce more variety."},
            {"question": "What is hallucination?", "short_answer": "Hallucination is when the model produces an answer that sounds believable but is wrong or unsupported.", "spoken_answer": "Hallucination happens because the model is generating likely text, not directly verifying facts the way a database would. In enterprise settings this is risky because wrong answers can affect users, compliance, or business trust."},
            {"question": "Why do LLMs hallucinate?", "short_answer": "Because they generate likely continuations from patterns and may not have enough grounded evidence for the answer.", "spoken_answer": "An LLM predicts likely next tokens based on learned patterns and whatever context we provide. If the prompt is vague, the retrieved evidence is weak, or the answer requires precise facts the model does not truly have, it can confidently produce unsupported content."},
            {"question": "How do you reduce hallucination?", "short_answer": "Use better prompts, grounding with retrieved data, output constraints, tools, and human review.", "spoken_answer": "I would reduce hallucination by grounding the model with trusted data, using structured prompts, constraining output format, allowing tools or retrieval where needed, and keeping a human in the loop for sensitive cases. System design matters as much as model choice."},
            {"question": "What is prompt engineering?", "short_answer": "Prompt engineering is the practice of designing instructions and context so the model gives better output.", "spoken_answer": "Prompt engineering is about making tasks clearer for the model. That includes defining the goal, context, constraints, output format, and examples when useful. It is one of the fastest ways to improve results without changing the underlying model."},
            {"question": "What is RAG?", "short_answer": "RAG stands for Retrieval-Augmented Generation and combines document retrieval with model generation.", "spoken_answer": "In RAG, the system first retrieves relevant information from a knowledge source and then sends that context with the user query to the model. This helps the answer stay grounded in trusted documents and is very common in enterprise assistants and document Q&A tools."},
            {"question": "What are embeddings?", "short_answer": "Embeddings are vector representations of text that capture semantic meaning.", "spoken_answer": "Embeddings convert text into numbers in a way that helps the system compare meaning. Similar meanings tend to be close in vector space, which makes embeddings useful for semantic search, clustering, recommendation, and retrieval pipelines."},
            {"question": "What is semantic search?", "short_answer": "Semantic search finds relevant content based on meaning, not just exact keyword matching.", "spoken_answer": "Instead of looking only for the exact same words, semantic search tries to find content with similar meaning. This is why embeddings are useful in enterprise knowledge assistants where users may ask the same question in different ways."},
            {"question": "Fine-tuning vs prompting?", "short_answer": "Prompting changes behavior through instructions, while fine-tuning changes the model more deeply using training data.", "spoken_answer": "Prompting is the faster and cheaper first step because it only changes the instructions and context. Fine-tuning is better when you need stronger behavior adaptation or style consistency, but it requires more data, effort, and maintenance. Many teams start with prompting plus retrieval before fine-tuning."},
            {"question": "What is the difference between a chatbot and an AI assistant?", "short_answer": "A chatbot mainly replies in conversation, while an AI assistant may also use tools, retrieval, memory, and workflows to complete tasks.", "spoken_answer": "A chatbot can be simple and conversational. An AI assistant is usually more capable because it may retrieve documents, call APIs, follow instructions, and help complete end-to-end tasks instead of only replying with text."},
            {"question": "Why is Python commonly used in AI?", "short_answer": "Python is readable, fast to prototype with, and has a strong AI ecosystem.", "spoken_answer": "Python is widely used because the syntax is simple and the ecosystem is rich with libraries for data handling, model development, APIs, and experimentation. It reduces idea-to-prototype time, which is valuable in AI engineering."},
            {"question": "What are enterprise uses of GenAI?", "short_answer": "Chatbots, copilots, document summarization, document Q&A, knowledge assistants, code help, extraction, and workflow automation.", "spoken_answer": "In enterprises, Generative AI is often used for support assistants, internal knowledge search, summarization, drafting, ticket workflows, coding help, and content extraction. The key is that the model is usually part of a larger system with data access, monitoring, and safeguards."},
            {"question": "What are risks of GenAI?", "short_answer": "Hallucination, bias, privacy issues, outdated knowledge, prompt injection, cost, latency, and over-reliance.", "spoken_answer": "A mature answer should mention both technical and business risks. Technical risks include hallucination and prompt injection. Business risks include privacy, compliance, cost, latency, and teams trusting model outputs too much without verification."},
            {"question": "How would you evaluate an AI-generated response?", "short_answer": "Check relevance, correctness, groundedness, format quality, safety, latency, and user usefulness.", "spoken_answer": "I would evaluate a response using both quality and system metrics. Quality includes correctness, relevance, completeness, and adherence to format. System metrics include latency, cost, and safety. In production, I would also compare against test cases or human review."},
            {"question": "What is an agentic workflow?", "short_answer": "An agentic workflow is a multi-step AI process where the model can plan, use tools, and iterate toward a goal.", "spoken_answer": "Instead of one prompt and one answer, agentic workflows involve multiple steps such as planning, retrieval, tool calling, checking outputs, and refining the result. They are useful for more complex enterprise automation tasks."},
            {"question": "Why does grounding matter?", "short_answer": "Grounding matters because it ties model output to trusted information and reduces unsupported answers.", "spoken_answer": "Grounding means giving the model reliable context from documents, databases, or tools. This is important because without grounding, the model may rely too much on general patterns and produce answers that sound good but are not actually supported."},
            {"question": "What is the role of APIs in GenAI applications?", "short_answer": "APIs connect the application to models, retrieval systems, tools, business data, and external services.", "spoken_answer": "APIs are how GenAI products become real systems. The model itself is only one component. APIs let the application call models, fetch documents, trigger workflows, access business systems, and return structured results to the user."},
            {"question": "What is human-in-the-loop?", "short_answer": "Human-in-the-loop means a person reviews, approves, or corrects model outputs where needed.", "spoken_answer": "Human-in-the-loop is important for higher-risk cases such as policy answers, customer messaging, financial content, or medical-like scenarios. It helps keep quality and trust high while the system is still improving."},
            {"question": "Why can’t we trust model outputs blindly?", "short_answer": "Because fluent output does not guarantee truth, grounding, or policy compliance.", "spoken_answer": "Generative models are optimized to produce likely text, not guaranteed truth. They can be persuasive even when wrong. That is why enterprise systems need evaluation, grounding, logging, and human review for important decisions."},
            {"question": "Explain a GenAI project you have worked on.", "short_answer": "Explain the problem, system flow, model usage, retrieval/tooling, evaluation, challenge, and business impact.", "spoken_answer": "A strong project answer should cover the problem statement, the data or knowledge source, prompt or retrieval design, APIs used, how you evaluated output quality, one challenge you faced, and the result. Interviewers want both technical flow and practical thinking."},
            {"question": "What is the difference between retrieving information and generating information?", "short_answer": "Retrieval finds existing information; generation creates a new response using patterns and context.", "spoken_answer": "A retrieval system searches and returns existing content from a source, like a database or document index. A generative model writes a fresh answer. The best enterprise systems often combine both so the generation stays grounded in real information."},
        ],
        "interview_rapid_fire": [
            {"question": "GenAI creates what?", "answer": "New content such as text, code, images, audio, or summaries."},
            {"question": "LLM core idea?", "answer": "Next-token prediction over language."},
            {"question": "Token matters for?", "answer": "Cost, latency, and context size."},
            {"question": "Context window means?", "answer": "How much text the model can consider in one call."},
            {"question": "Low temperature means?", "answer": "More stable and less random output."},
            {"question": "Hallucination means?", "answer": "Plausible but unsupported or incorrect output."},
            {"question": "Embeddings do what?", "answer": "Represent meaning as vectors."},
            {"question": "RAG is?", "answer": "Retrieval plus generation."},
            {"question": "Grounding helps with?", "answer": "Reducing unsupported answers."},
            {"question": "Human-in-the-loop means?", "answer": "A person reviews or approves outputs."},
        ],
        "interview_common_mistakes": [
            "Confusing Generative AI with all machine learning.",
            "Saying an LLM understands exactly like a human.",
            "Not being able to explain hallucination in simple language.",
            "Not knowing what embeddings or RAG are at a basic level.",
            "Talking only in theory without any real enterprise example.",
        ],
        "quick_revision_points": [
            "Generative AI creates new content such as text, code, images, audio, or summaries.",
            "AI is the broad field, ML is a subset, deep learning is neural-network-based ML, and Generative AI is one modern content-generation area.",
            "Predictive AI usually predicts labels or scores; Generative AI creates new outputs.",
            "LLM stands for Large Language Model.",
            "An LLM generates text by predicting the next token repeatedly.",
            "Strong language output does not mean human-like understanding.",
            "A token is a small unit of text used by the model.",
            "Tokens matter for cost, latency, and context limits.",
            "Prompt tokens and response tokens both count in real systems.",
            "A context window is the amount of text the model can consider in one request.",
            "Long inputs may need chunking, summarization, or retrieval.",
            "Temperature controls output randomness.",
            "Low temperature is usually better for enterprise Q&A and extraction.",
            "Higher temperature can help brainstorming and creative drafting.",
            "Hallucination means plausible but unsupported output.",
            "Hallucination is risky in enterprise systems because it can reduce trust and create business errors.",
            "Grounding means giving the model trusted context.",
            "Prompt quality strongly affects output quality.",
            "Structured prompts often include task, context, constraints, and output format.",
            "Embeddings convert text into vectors that capture meaning.",
            "Semantic search uses embeddings to find relevant content by meaning.",
            "RAG combines retrieval with generation.",
            "Basic RAG flow is query to retrieval to prompt to model to answer.",
            "RAG is useful for company-specific or current knowledge.",
            "Prompting changes behavior through instructions.",
            "Fine-tuning changes behavior more deeply using training data.",
            "Many real systems start with prompting plus retrieval before fine-tuning.",
            "Enterprise GenAI systems need logging, evaluation, and safety checks.",
            "APIs connect the model to apps, tools, databases, and workflows.",
            "Human-in-the-loop is important for sensitive or high-risk tasks.",
        ],
        "quiz_questions": [
            _q("Which statement best describes Generative AI?", ["It only predicts numeric labels", "It creates new content such as text or images", "It only stores data", "It is the same as a database"], 1, "Generative AI is focused on producing new outputs such as text, code, images, audio, or summaries."),
            _q("What is an LLM mainly doing during generation?", ["Sorting a database table", "Predicting the next token repeatedly", "Only retrieving documents", "Running a spreadsheet formula"], 1, "An LLM generates output by repeatedly predicting the next token."),
            _q("Why do tokens matter in GenAI systems?", ["They only matter for font size", "They affect cost, latency, and context usage", "They replace embeddings", "They are only used in training"], 1, "Token count affects how much text fits, how long calls take, and how much the API may cost."),
            _q("What does context window mean?", ["The size of the app screen", "The number of users in the system", "The amount of text the model can consider in one request", "The training dataset size"], 2, "Context window is the request-time text capacity available to the model."),
            _q("Which temperature choice is usually better for structured enterprise extraction?", ["Higher temperature", "Lower temperature", "Temperature does not matter", "The maximum possible temperature"], 1, "Lower temperature is usually better when you want stable, consistent output."),
            _q("What is hallucination?", ["A model refusing to answer", "A model generating unsupported or incorrect information", "A model using too many APIs", "A model compressing files"], 1, "Hallucination means the output sounds plausible but is wrong or unsupported."),
            _q("What are embeddings mainly used for?", ["Charging API bills", "Semantic similarity and retrieval", "Changing model temperature", "Encrypting passwords"], 1, "Embeddings help represent meaning so the system can find semantically relevant content."),
            _q("What is RAG?", ["A way to reduce file size", "Retrieval-Augmented Generation", "A neural network layer type", "A database backup process"], 1, "RAG retrieves relevant information first and then uses it while generating the answer."),
        ],
        "resource_sections": {
            "Must watch first": [
                _r("3Blue1Brown: But what is a Neural Network?", "https://www.youtube.com/watch?v=aircAruvnKk", "video", "must_watch", "Helpful background if you want deep learning intuition before GenAI."),
                _r("IBM Technology: Large Language Models Explained", "https://www.youtube.com/results?search_query=IBM+Technology+large+language+models+explained", "video", "must_watch", "Beginner-friendly LLM explainers from IBM Technology."),
                _r("DeepLearning.AI Generative AI for Everyone", "https://www.deeplearning.ai/courses/generative-ai-for-everyone/", "video", "must_watch", "A structured beginner-friendly introduction to Generative AI use cases and terminology."),
                _r("freeCodeCamp Generative AI Videos", "https://www.youtube.com/@freecodecamp/search?query=generative%20ai", "video", "must_watch", "Long-form beginner explainers and practical walkthroughs."),
            ],
            "Must read first": [
                _r("OpenAI Docs", "https://platform.openai.com/docs/overview", "article", "must_read", "Useful conceptual and API-adjacent reference for modern GenAI systems."),
                _r("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "must_read", "A strong learning path for LLM and GenAI concepts."),
                _r("IBM Think: Large Language Models", "https://www.ibm.com/think/topics/large-language-models", "article", "must_read", "Good conceptual enterprise-facing explainer."),
                _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Good reference for prompt design and related GenAI topics."),
            ],
            "Practice / explore": [
                _r("OpenAI Cookbook", "https://cookbook.openai.com/", "article", "practice", "Practical examples for building model-powered applications."),
                _r("Pinecone Learn: Retrieval-Augmented Generation", "https://www.pinecone.io/learn/retrieval-augmented-generation/", "article", "practice", "Beginner-friendly explainer for RAG systems."),
                _r("Hugging Face Tasks and Models", "https://huggingface.co/models", "article", "practice", "Explore tasks, models, and how different AI applications are built."),
            ],
            "Optional deep dive": [
                _r("Google Cloud: Generative AI Learning Path", "https://cloud.google.com/learn/training/generative-ai", "article", "optional_deep_dive", "Extra structured learning if you want a broader vendor view."),
                _r("Pinecone Learn: Vector Embeddings", "https://www.pinecone.io/learn/vector-embeddings/", "article", "optional_deep_dive", "Good intuitive explanation of embeddings and semantic similarity."),
                _r("Anthropic Prompt Engineering Overview", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview", "article", "optional_deep_dive", "Another useful conceptual reference for prompting and safe generation."),
            ],
        },
        "resources": [
            _r("OpenAI Docs", "https://platform.openai.com/docs/overview", "article", "must_read", "Useful conceptual and API-adjacent reference for modern GenAI systems."),
            _r("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "must_read", "A strong learning path for LLM and GenAI concepts."),
            _r("Pinecone Learn: Retrieval-Augmented Generation", "https://www.pinecone.io/learn/retrieval-augmented-generation/", "article", "practice", "Beginner-friendly explainer for RAG systems."),
            _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Good reference for prompt design and related GenAI topics."),
        ],
    }
)


TOPIC_DATA["generative_ai"] = GENERATIVE_AI_TOPIC


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "patterns": [
            *PYTHON_TOPIC.patterns,
            {
                "title": "Palindrome Check",
                "problem": "Check whether a string reads the same from both ends.",
                "intuition": "Compare the original string with its reversed version after normalization.",
                "solution": """def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("Level"))
""",
                "alternative": """def is_palindrome(text):
    text = text.lower()
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Not converting case when the interview expects case-insensitive comparison."],
                "variation": "Ignore spaces and punctuation.",
            },
            {
                "title": "Find Duplicates",
                "problem": "Find repeated elements in a list.",
                "intuition": "Track seen elements in a set and collect repeated values.",
                "solution": """def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
""",
                "alternative": """def find_duplicates(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [num for num, count in freq.items() if count > 1]
""",
                "time_complexity": "O(n) time on average.",
                "mistakes": ["Returning the same duplicate multiple times."],
                "variation": "Return only whether duplicates exist.",
            },
            {
                "title": "Count Vowels",
                "problem": "Count vowels in a string.",
                "intuition": "Loop once and count characters that belong to the vowel set.",
                "solution": """def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
""",
                "alternative": """def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Missing uppercase vowels when not using `lower()`."],
                "variation": "Return each vowel count separately.",
            },
            {
                "title": "List Comprehension Examples",
                "problem": "Create a new list with concise filtering or transformation logic.",
                "intuition": "Use list comprehension when the transformation is simple and readable.",
                "solution": """nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
squares = [num * num for num in nums]
""",
                "alternative": """nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda num: num % 2 == 0, nums))
""",
                "time_complexity": "Usually O(n) time.",
                "mistakes": ["Writing comprehension logic that is too complex to read quickly."],
                "variation": "Build a dictionary comprehension for squares.",
            },
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC
TOPIC_DATA["generative_ai"] = GENERATIVE_AI_TOPIC


TOPIC_DATA["dsa"] = TopicContent(
    key="dsa",
    title="DSA",
    icon="DSA",
    difficulty="Beginner to Intermediate",
    priority="High",
    estimated_time="4 hours",
    why_it_matters="DSA determines coding-round performance and shows structured problem-solving under time pressure.",
    detailed_sections={
        "Core patterns": "Arrays, strings, hashing, sliding window, two pointers, and recursion fundamentals cover a large share of campus coding rounds.",
        "Complexity mindset": "State brute force first, then optimize. Explain time and space trade-offs clearly.",
        "Interview approach": "Clarify input, discuss edge cases, write clean code, and dry-run with examples.",
    },
    common_mistakes=[
        "Jumping into code without discussing approach.",
        "Ignoring constraints and edge cases.",
        "Forgetting invariants in pointer-based problems.",
        "Writing recursion without a base case.",
    ],
    code_examples={
        "Sliding Window": """def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best
""",
        "Two Pointers": """def has_pair(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return True
        if current < target:
            left += 1
        else:
            right -= 1
    return False
""",
    },
    interview_questions=[
        {"q": "When should you use hashing?", "a": "When you need fast lookup, membership, or frequency counting."},
        {"q": "What is sliding window?", "a": "A technique for optimizing calculations on contiguous subarrays or substrings."},
        {"q": "Why discuss brute force first?", "a": "It shows correctness-first thinking before optimization."},
        {"q": "What is recursion overhead?", "a": "Extra call stack memory and function call cost."},
        {"q": "Why mention complexity out loud?", "a": "It shows algorithmic awareness and interviewer-level communication."},
    ],
    quick_revision_points=[
        "Arrays and hashing solve many easy-medium interview problems.",
        "Sliding window is for contiguous segments.",
        "Two pointers often benefit from sorting.",
        "Always discuss time and space complexity.",
        "Dry-run before finalizing your answer.",
    ],
    quiz_questions=[
        _q("Best for duplicate detection?", ["list", "set", "tuple", "heap"], 1, "Set gives O(1)-average membership checks."),
        _q("Sliding window is mainly for", ["Trees", "Contiguous segments", "Graphs", "Stacks"], 1, "Sliding window is ideal for contiguous ranges."),
        _q("Recursion must include", ["Loop", "Base case", "Class", "Exception"], 1, "Without a base case recursion will not terminate."),
        _q("Two pointers often benefit from", ["Sorting", "Randomization", "Memoization", "Binary tree"], 0, "Sorted order often enables linear pointer movement."),
        _q("Which complexity is better for large n?", ["O(n)", "O(n^2)", "O(n^3)", "O(2^n)"], 0, "O(n) scales better than the others listed."),
    ],
    resources=[
        _r("GeeksforGeeks DSA", "https://www.geeksforgeeks.org/data-structures/", "article", "must_read", "Broad DSA reference."),
        _r("NeetCode Roadmap", "https://neetcode.io/roadmap", "article", "must_read", "Popular structured roadmap."),
        _r("Abdul Bari Algorithms", "https://www.youtube.com/@abdul_bari", "video", "must_watch", "Strong conceptual algorithm explanations."),
        _r("LeetCode Study Plans", "https://leetcode.com/studyplan/", "practice", "practice", "Guided problem sets."),
    ],
)


_ADDITIONAL_TOPICS = {
    "generative_ai": ("Generative AI", "GAI", "High", "3 hours"),
    "prompt_engineering": ("Prompt Engineering", "PE", "High", "2 hours"),
    "agentic_ai": ("Agentic AI", "AA", "High", "2.5 hours"),
    "apis_backend": ("APIs and Backend", "API", "High", "2.5 hours"),
    "pandas_data_handling": ("Pandas and Data Handling", "PD", "High", "2.5 hours"),
    "databases": ("Databases", "DB", "Medium", "2 hours"),
    "ai_workflows": ("AI Workflows", "WF", "High", "2 hours"),
    "interview_prep": ("Interview Prep", "INT", "High", "3 hours"),
}


for key, (title, icon, priority, estimated_time) in _ADDITIONAL_TOPICS.items():
    TOPIC_DATA[key] = TopicContent(
        key=key,
        title=title,
        icon=icon,
        difficulty="Beginner-friendly",
        priority=priority,
        estimated_time=estimated_time,
        why_it_matters=f"{title} is important for Movate AI Engineer interviews because it connects theory with practical execution.",
        detailed_sections={
            "Core concepts": f"Understand the foundational definitions and workflow for {title}.",
            "Interview depth": "Move beyond definitions and speak about use cases, trade-offs, and limitations.",
            "Role connection": "Explain how the concept helps AI systems become more useful, reliable, and easier to deploy.",
        },
        common_mistakes=[
            "Memorizing terms without examples.",
            "Not connecting the concept to implementation.",
            "Ignoring limitations and monitoring concerns.",
            "Giving generic answers without project framing.",
        ],
        code_examples={
            "Starter snippet": """pipeline = ["ingest", "process", "model_call", "evaluate"]
for step in pipeline:
    print(step)
"""
        },
        interview_questions=[
            {"q": f"Explain {title} in one minute.", "a": "Start with definition, then workflow, then one practical example."},
            {"q": "What are common pitfalls?", "a": "Mention one technical pitfall and one process pitfall, then a mitigation."},
            {"q": "How would you debug an issue?", "a": "Use logs, reproducible cases, and step-by-step isolation."},
            {"q": "How does this affect AI product quality?", "a": "It impacts reliability, relevance, latency, cost, or trust."},
            {"q": "What would you improve next?", "a": "Suggest one measurable iteration and the metric you would track."},
        ],
        quick_revision_points=[
            "Definition plus use case plus limitation is a strong answer structure.",
            "Explain workflow, not just buzzwords.",
            "Mention evaluation and monitoring.",
            "Use simple language first, then add technical depth.",
            "Connect technical work to impact.",
        ],
        quiz_questions=[
            _q("Best interview answer style?", ["Only definition", "Definition plus example plus trade-off", "Only formula", "Only buzzwords"], 1, "Balanced, practical answers are strongest."),
            _q("Which improves clarity most?", ["Jargon", "Workflow explanation", "Long monologue", "Skipping examples"], 1, "Workflow explanation shows structure."),
            _q("A strong answer includes", ["No limitations", "Only benefits", "Benefits and limitations", "Random facts"], 2, "Balanced thinking improves credibility."),
            _q("Fastest way to revise before an interview?", ["Quick bullets", "Full textbook", "No notes", "Only videos"], 0, "Short revision bullets are high yield under time pressure."),
            _q("Technical communication should be", ["Confusing", "Structured", "Overly long", "Vague"], 1, "Structured communication is a core interview signal."),
        ],
        resources=[
            _r("Streamlit docs", "https://docs.streamlit.io/", "article", "must_read", "Useful app reference."),
            _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Solid prompt and GenAI reference."),
            _r("Hugging Face LLM Course", "https://huggingface.co/learn/llm-course", "article", "optional_deep_dive", "Good AI deep dive."),
            _r("freeCodeCamp", "https://www.youtube.com/@freecodecamp", "video", "must_watch", "Broad technical video coverage."),
        ],
    )


ALL_TOPICS_ORDER = [
    "python",
    "dsa",
    "generative_ai",
    "prompt_engineering",
    "agentic_ai",
    "apis_backend",
    "pandas_data_handling",
    "databases",
    "ai_workflows",
    "interview_prep",
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


FIVE_DAY_TIMETABLE = {
    "overview": {
        "goal_summary": [
            "This is a focused 5-day preparation plan for the Movate AI Engineer role.",
            "The plan emphasizes Python, Generative AI, Prompt Engineering, Agentic AI, APIs, Data Handling, Databases, and AI Workflows.",
            "Generative AI, Prompt Engineering, and Agentic AI are strong differentiators in this drive.",
        ],
        "daily_structure": [
            "9:30 AM – 12:00 PM -> Core Learning",
            "2:00 PM – 4:30 PM -> Practice + Deep Dive",
            "8:00 PM – 10:30 PM -> Revision + Interview Prep",
        ],
        "priority_order": [
            "1. Generative AI",
            "2. Prompt Engineering",
            "3. Agentic AI",
            "4. Python",
            "5. APIs & Backend",
            "6. Databases / Vector DB",
            "7. Pandas / Data Handling",
            "8. AI Workflows",
            "9. DSA",
        ],
        "outcome_goals": [
            "Strong conceptual clarity across the full role scope",
            "Fast interview revision ability before the placement drive",
            "Better answers for AI-related questions",
            "Confidence in project and system-design discussions",
            "Readiness for technical plus HR rounds",
        ],
        "flow_diagram": "Day 1 Foundation -> Day 2 Problem Solving + Data -> Day 3 GenAI Core -> Day 4 Agentic + APIs -> Day 5 Systems + Revision",
        "high_priority_topics": ["Generative AI", "Prompt Engineering", "Agentic AI", "Python", "APIs & Backend"],
    },
    "days": [
        {
            "day": "Day 1",
            "title": "Day 1 — Python + Core Coding Foundation",
            "goal": "Build strong coding and language fundamentals for AI and backend learning.",
            "priority": "High",
            "badge": "Foundation Day",
            "covered_topics": ["Python"],
            "blocks": {
                "morning": ["Python basics", "Variables and data types", "Lists, tuples, sets, dictionaries", "Strings", "Functions", "OOP basics"],
                "afternoon": ["Frequency count", "Anagram check", "Second largest element", "Reverse string", "Count vowels", "Revise `dict.get()`"],
                "night": ["Revise Python basics", "Review OOP", "Practice short interview answers on Python"],
            },
            "interview_focus": [
                "Why Python for AI?",
                "Difference between list and tuple",
                "What is a dictionary?",
                "Explain OOP basics",
            ],
            "expected_outcome": [
                "Comfort with Python fundamentals and common data structures",
                "Confidence in basic coding patterns asked in campus rounds",
                "Ability to answer Python basics clearly in interviews",
            ],
            "checklist": [
                "Finish Python Learn tab",
                "Solve 5 basic Python pattern questions",
                "Revise OOP with one example",
                "Speak 4 interview answers aloud",
            ],
        },
        {
            "day": "Day 2",
            "title": "Day 2 — DSA + Pandas / Data Handling",
            "goal": "Improve problem-solving basics and structured data handling.",
            "priority": "High",
            "badge": "Practice Day",
            "covered_topics": ["DSA", "Pandas / Data Handling"],
            "blocks": {
                "morning": ["Arrays", "Strings", "Hashing", "Sliding window basics", "Solve 4–5 basic coding questions"],
                "afternoon": ["Pandas basics", "DataFrame", "read_csv", "head, info, describe", "Filtering rows", "Creating columns", "groupby", "Missing values", "Duplicates"],
                "night": ["Revise DSA patterns", "Revise Pandas concepts", "Practice data handling interview answers"],
            },
            "interview_focus": [
                "What is DataFrame?",
                "Why does data cleaning matter?",
                "What is groupby?",
                "How do you handle missing values?",
            ],
            "expected_outcome": [
                "Better grip on beginner DSA patterns",
                "Comfort with Pandas basics and cleaning vocabulary",
                "Ability to connect data handling to AI preparation tasks",
            ],
            "checklist": [
                "Solve 4 DSA basics",
                "Finish Pandas Learn tab",
                "Practice groupby and null handling examples",
                "Revise 4 data interview questions",
            ],
        },
        {
            "day": "Day 3",
            "title": "Day 3 — Generative AI + Prompt Engineering",
            "goal": "Master the core differentiator topics for this role.",
            "priority": "Very High",
            "badge": "High Priority / High Impact",
            "covered_topics": ["Generative AI", "Prompt Engineering"],
            "blocks": {
                "morning": ["AI vs ML vs DL vs GenAI", "What is an LLM", "Tokens", "Context window", "Temperature", "Hallucination", "Embeddings", "RAG basics"],
                "afternoon": ["Prompt engineering basics", "Zero-shot vs few-shot", "Role prompting", "Structured prompting", "Constraint prompting", "Output formatting", "Prompt refinement", "Write prompts for explanation, summarization, extraction, and JSON output"],
                "night": ["Revise GenAI concepts", "Revise prompt engineering rules", "Practice high-probability interview answers"],
            },
            "interview_focus": [
                "What is Generative AI?",
                "What is an LLM?",
                "What is hallucination?",
                "What is prompt engineering?",
                "How do you reduce hallucination?",
            ],
            "expected_outcome": [
                "Strong conceptual clarity in the highest-impact AI topics",
                "Ability to explain prompting and LLM basics with confidence",
                "Better readiness for role-specific AI interview questions",
            ],
            "checklist": [
                "Finish GenAI Learn tab",
                "Finish Prompt Engineering Learn and Techniques tabs",
                "Write 4 strong example prompts",
                "Speak 5 top GenAI interview answers aloud",
            ],
        },
        {
            "day": "Day 4",
            "title": "Day 4 — Agentic AI + APIs / Backend",
            "goal": "Understand how AI systems take actions and how backend systems support them.",
            "priority": "Very High",
            "badge": "Differentiator Day",
            "covered_topics": ["Agentic AI", "APIs & Backend"],
            "diagram": "User Goal -> Agent -> Tool/API -> Result -> Final Response",
            "blocks": {
                "morning": ["What is an AI agent", "Chatbot vs assistant vs agent", "Planning", "Tool usage", "Memory", "Workflow orchestration", "Planner-executor idea", "Human-in-the-loop"],
                "afternoon": ["Backend basics", "What is an API", "Client-server architecture", "HTTP basics", "GET / POST / PUT / DELETE", "JSON", "Status codes", "Authentication basics", "External API integrations"],
                "night": ["Revise agentic AI", "Revise backend and API basics", "Practice mixed system-thinking interview questions"],
            },
            "interview_focus": [
                "What is an AI agent?",
                "Difference between chatbot and agent?",
                "What is tool calling?",
                "What is an API?",
                "Difference between GET and POST?",
                "Why is backend important in AI apps?",
            ],
            "expected_outcome": [
                "Ability to explain agents, tools, and backend support clearly",
                "Confidence in API and backend basics for AI workflows",
                "Stronger system-thinking answers than most candidates",
            ],
            "checklist": [
                "Finish Agentic AI Learn tab",
                "Finish APIs & Backend Learn tab",
                "Revise tool calling and status codes",
                "Speak 6 system-design style answers aloud",
            ],
        },
        {
            "day": "Day 5",
            "title": "Day 5 — Databases + Vector DB + AI Workflows + Full Revision",
            "goal": "Connect all system components and prepare for final interview discussion.",
            "priority": "Very High",
            "badge": "System Thinking Day",
            "covered_topics": ["Databases / Vector DB", "AI Workflows", "Interview Prep / Revision"],
            "diagram": "User -> Backend -> Retrieval/DB/Model -> Output -> Validation -> User",
            "blocks": {
                "morning": ["DBMS basics", "SQL vs NoSQL", "Tables, rows, columns", "Primary key, joins", "CRUD", "Vector database basics", "Embeddings", "Similarity search", "RAG flow"],
                "afternoon": ["AI workflow basics", "Preprocessing", "Prompt construction", "Retrieval", "Model call", "Tool usage", "Post-processing", "Validation", "Logging", "Human-in-the-loop", "Enterprise workflow examples"],
                "night": ["Full revision of all 5 days", "Project revision", "Mock interview practice", "Final quick notes preparation"],
            },
            "interview_focus": [
                "What is SQL vs NoSQL?",
                "What is a vector database?",
                "What is embedding?",
                "What is RAG?",
                "What is an AI workflow?",
                "Why does validation matter in AI systems?",
            ],
            "expected_outcome": [
                "Clear system-level understanding of AI products",
                "Confidence in vector DB, RAG, and workflow answers",
                "Readiness for final technical discussion and mock interviews",
            ],
            "checklist": [
                "Finish Databases Vector DB tab",
                "Finish AI Workflows Learn and Evaluation tabs",
                "Do one full mock interview round",
                "Prepare final 1-page quick notes",
            ],
        },
    ],
    "final_revision": {
        "summary": "Use this tab on the last night or on interview morning for a calm, high-yield revision pass.",
        "one_hour_plan": [
            "10 minutes: revise Python dict, list/tuple, and OOP basics",
            "10 minutes: revise LLM, tokens, hallucination, embeddings, and RAG",
            "10 minutes: revise Prompt Engineering rules and examples",
            "10 minutes: revise Agentic AI, tool use, APIs, and backend basics",
            "10 minutes: revise vector DB, AI workflow flow, and validation",
            "10 minutes: speak top interview answers aloud and review your project story",
        ],
        "important_concepts": [
            "Python dict / OOP",
            "LLM / tokens / hallucination",
            "Prompt Engineering",
            "Agentic AI",
            "APIs",
            "Vector DB / RAG",
            "AI workflow end-to-end",
        ],
        "top_questions": [
            "Why Python for AI?",
            "What is an LLM?",
            "What is hallucination?",
            "What is prompt engineering?",
            "How do you reduce hallucination?",
            "What is an AI agent?",
            "What is tool calling?",
            "What is an API?",
            "What is SQL vs NoSQL?",
            "What is a vector database?",
            "What is embedding?",
            "What is RAG?",
            "What is an AI workflow?",
            "Why does validation matter in AI systems?",
            "Explain one AI project end to end.",
        ],
        "final_night_strategy": [
            "Do not learn new heavy topics.",
            "Revise only.",
            "Explain your project clearly in simple language.",
            "Sleep properly.",
            "Stay calm and keep answers structured.",
        ],
        "confidence_reminders": [
            "You do not need perfect depth in everything; you need clear, structured answers.",
            "If you explain systems better than others, you will stand out.",
            "GenAI + Prompting + Agents + RAG is already a strong differentiator.",
            "Keep answers simple, practical, and confident.",
        ],
        "diagram": "Python/Foundation -> GenAI -> Prompting -> Agents -> APIs -> DB/Vector DB -> AI Workflow -> Interview Confidence",
    },
}


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "patterns": PYTHON_TOPIC.patterns
        + [
            {
                "title": "Palindrome Check",
                "problem": "Check whether a string reads the same from both ends.",
                "intuition": "Compare the original string with its reversed version after needed normalization.",
                "solution": """def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("Level"))
""",
                "alternative": """def is_palindrome(text):
    text = text.lower()
    left, right = 0, len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Not converting case when the interview expects case-insensitive comparison."],
                "variation": "Ignore spaces and special characters.",
            },
            {
                "title": "Find Duplicates",
                "problem": "Find repeated elements in a list.",
                "intuition": "Track seen elements in a set. If an item appears again, add it to duplicates.",
                "solution": """def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 1]))
""",
                "alternative": """def find_duplicates(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [num for num, count in freq.items() if count > 1]
""",
                "time_complexity": "O(n) time on average.",
                "mistakes": ["Returning duplicates multiple times instead of only once."],
                "variation": "Return whether any duplicate exists instead of returning the duplicate values.",
            },
            {
                "title": "Count Vowels",
                "problem": "Count vowels in a string.",
                "intuition": "Loop once through the string and increase the count when the character is in the vowel set.",
                "solution": """def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Artificial"))
""",
                "alternative": """def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Missing uppercase vowels when not using `lower()`."],
                "variation": "Return counts of each vowel separately using a dictionary.",
            },
            {
                "title": "List Comprehension Examples",
                "problem": "Create a new list using a concise expression.",
                "intuition": "Use list comprehension when you want to transform or filter data in a readable one-line pattern.",
                "solution": """nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
squares = [num * num for num in nums]

print(evens)
print(squares)
""",
                "alternative": """nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda num: num % 2 == 0, nums))
""",
                "time_complexity": "Usually O(n) time.",
                "mistakes": ["Writing very complex comprehensions that reduce readability."],
                "variation": "Build a dictionary comprehension for squares or a filtered mapping.",
            },
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "quick_revision_points": [
            "Python is widely used in AI because it is readable, fast to prototype in, and has a rich ecosystem.",
            "Python is dynamically typed, which means variable types are decided at runtime.",
            "Indentation is mandatory in Python and defines code blocks.",
            "Use `#` for comments and meaningful variable names for readability.",
            "`int`, `float`, `str`, `bool`, and `None` are core built-in data types.",
            "Lists are ordered and mutable.",
            "Tuples are ordered and immutable.",
            "Sets store unique values and support fast membership checks.",
            "Dictionaries store key-value pairs and are great for frequency counts.",
            "Strings are immutable sequences.",
            "Indexing accesses one element, slicing accesses a range.",
            "Negative indexing starts from the end.",
            "`split()` breaks a string into parts and `join()` combines items into a string.",
            "`strip()` removes extra spaces from the ends of a string.",
            "`replace()` returns a new string with substitutions.",
            "`if`, `elif`, and `else` control decisions.",
            "`for` is best for sequences; `while` is best for condition-based repetition.",
            "`break` exits a loop, `continue` skips an iteration, and `pass` is a placeholder.",
            "Functions improve reuse, readability, and testing.",
            "Parameters are in the definition; arguments are in the function call.",
            "`return` sends output back to the caller.",
            "A class is a blueprint and an object is its instance.",
            "`self` refers to the current object.",
            "Inheritance supports reuse; encapsulation organizes data and behavior together.",
            "Use `try`/`except` for runtime errors and `with open` for safe file handling.",
        ],
        "quiz_questions": [
            _q("Which Python collection is ordered, mutable, and allows duplicates?", ["tuple", "set", "list", "dict"], 2, "A list is ordered, mutable, and can contain duplicate values."),
            _q("What will `'python'[::-1]` return?", ["python", "nohtyp", "error", "py"], 1, "Slice with step `-1` reverses the string."),
            _q("Which statement about OOP is correct?", ["An object is a blueprint and a class is an instance", "A class is a blueprint and an object is an instance", "Inheritance means hiding data", "Encapsulation means multiple return values"], 1, "A class defines the structure and an object is created from that class."),
            _q("What does `continue` do inside a loop?", ["Stops the loop completely", "Skips the current iteration and moves to the next one", "Does nothing and ends the program", "Restarts the loop from the beginning"], 1, "The `continue` statement skips the current iteration only."),
            _q("Which block always runs whether an exception happens or not?", ["try", "except", "else", "finally"], 3, "The `finally` block is always executed."),
            _q("What is the main purpose of the `return` keyword in a function?", ["To print the answer", "To stop the Python interpreter", "To send a value back to the caller", "To define default arguments"], 2, "`return` gives the function result back to the caller."),
            _q("What is the benefit of `dict.get(key, 0)` in frequency counting?", ["It sorts the dictionary", "It avoids KeyError for missing keys", "It deletes duplicate keys", "It converts values to integers"], 1, "`get()` returns a default value when the key is missing, which is perfect for counting logic."),
            _q("Which of the following is immutable?", ["list", "dict", "set", "tuple"], 3, "Tuple is immutable. The others are mutable."),
        ],
        "resources": [
            _r("Programming with Mosh Python Tutorial", "https://www.youtube.com/watch?v=_uQrJ0TkZlc", "video", "must_watch", "Beginner-friendly full Python walkthrough with clear explanations."),
            _r("freeCodeCamp Python Full Course", "https://www.youtube.com/watch?v=rfscVS0vtbw", "video", "must_watch", "Long-form course useful for revising fundamentals in one sitting."),
            _r("Corey Schafer Python Playlist", "https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc", "video", "must_watch", "Excellent playlist for functions, OOP, files, and practical Python concepts."),
            _r("Python Official Tutorial", "https://docs.python.org/3/tutorial/", "article", "must_read", "Best primary reference for core syntax and standard Python behavior."),
            _r("Real Python Basics", "https://realpython.com/python-basics/", "article", "must_read", "Readable explanations with examples for beginners and interview revision."),
            _r("GeeksforGeeks Python Programming Language", "https://www.geeksforgeeks.org/python-programming-language/", "article", "must_read", "Good for quick topic lookup and revision examples."),
            _r("HackerRank Python Practice", "https://www.hackerrank.com/domains/python", "practice", "practice", "Topic-wise Python problems from beginner to intermediate."),
            _r("LeetCode Problemset", "https://leetcode.com/problemset/", "practice", "practice", "Use filters for easy array and string problems to build speed."),
            _r("GeeksforGeeks Practice", "https://practice.geeksforgeeks.org/", "practice", "practice", "Good for basic coding rounds and Python implementation practice."),
            _r("NumPy Quickstart", "https://numpy.org/doc/stable/user/quickstart.html", "article", "optional_deep_dive", "Useful to connect core Python with AI numerical computing."),
            _r("Pandas Getting Started", "https://pandas.pydata.org/docs/getting_started/index.html", "article", "optional_deep_dive", "Helpful when moving from Python basics to data handling for AI workflows."),
            _r("FastAPI Tutorial", "https://fastapi.tiangolo.com/tutorial/", "article", "optional_deep_dive", "Good next step to connect Python with backend APIs."),
        ],
        "resource_sections": {
            "Must watch first": [
                _r("Programming with Mosh Python Tutorial", "https://www.youtube.com/watch?v=_uQrJ0TkZlc", "video", "must_watch", "Start here if you want a single beginner-friendly video before reading."),
                _r("freeCodeCamp Python Full Course", "https://www.youtube.com/watch?v=rfscVS0vtbw", "video", "must_watch", "Use this for deep revision in one sitting."),
                _r("Corey Schafer Python Playlist", "https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc", "video", "must_watch", "Best playlist for revising specific Python topics."),
            ],
            "Must read first": [
                _r("Python Official Tutorial", "https://docs.python.org/3/tutorial/", "article", "must_read", "Primary source for Python syntax and behavior."),
                _r("Real Python Basics", "https://realpython.com/python-basics/", "article", "must_read", "Clear explanations with strong examples."),
                _r("GeeksforGeeks Python Programming Language", "https://www.geeksforgeeks.org/python-programming-language/", "article", "must_read", "Fast revision reference for many subtopics."),
            ],
            "Practice resources": [
                _r("HackerRank Python Practice", "https://www.hackerrank.com/domains/python", "practice", "practice", "Topic-focused practice for syntax and collections."),
                _r("LeetCode Problemset", "https://leetcode.com/problemset/", "practice", "practice", "Filter for easy array and string questions for interview prep."),
                _r("GeeksforGeeks Practice", "https://practice.geeksforgeeks.org/", "practice", "practice", "Good for beginner-friendly coding questions."),
            ],
            "Optional deep dive": [
                _r("NumPy Quickstart", "https://numpy.org/doc/stable/user/quickstart.html", "article", "optional_deep_dive", "Bridge Python basics with AI numerical work."),
                _r("Pandas Getting Started", "https://pandas.pydata.org/docs/getting_started/index.html", "article", "optional_deep_dive", "Useful for data cleaning and table operations."),
                _r("FastAPI Tutorial", "https://fastapi.tiangolo.com/tutorial/", "article", "optional_deep_dive", "Connect Python fundamentals with backend API development."),
            ],
        },
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "patterns": PYTHON_TOPIC.patterns
        + [
            {
                "title": "Palindrome Check",
                "problem": "Check whether a string reads the same from both ends.",
                "intuition": "Compare the original string with its reversed version after needed normalization.",
                "solution": """def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("Level"))
""",
                "alternative": """def is_palindrome(text):
    text = text.lower()
    left, right = 0, len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Not converting case when the interview expects case-insensitive comparison."],
                "variation": "Ignore spaces and special characters.",
            },
            {
                "title": "Find Duplicates",
                "problem": "Find repeated elements in a list.",
                "intuition": "Track seen elements in a set. If an item appears again, add it to duplicates.",
                "solution": """def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 1]))
""",
                "alternative": """def find_duplicates(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [num for num, count in freq.items() if count > 1]
""",
                "time_complexity": "O(n) time on average.",
                "mistakes": ["Returning duplicates multiple times instead of only once."],
                "variation": "Return whether any duplicate exists instead of returning the duplicate values.",
            },
            {
                "title": "Count Vowels",
                "problem": "Count vowels in a string.",
                "intuition": "Loop once through the string and increase the count when the character is in the vowel set.",
                "solution": """def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Artificial"))
""",
                "alternative": """def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Missing uppercase vowels when not using `lower()`."],
                "variation": "Return counts of each vowel separately using a dictionary.",
            },
            {
                "title": "List Comprehension Examples",
                "problem": "Create a new list using a concise expression.",
                "intuition": "Use list comprehension when you want to transform or filter data in a readable one-line pattern.",
                "solution": """nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
squares = [num * num for num in nums]

print(evens)
print(squares)
""",
                "alternative": """nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda num: num % 2 == 0, nums))
""",
                "time_complexity": "Usually O(n) time.",
                "mistakes": ["Writing very complex comprehensions that reduce readability."],
                "variation": "Build a dictionary comprehension for squares or a filtered mapping.",
            },
        ],
        "interview_questions": [
            {"q": "Why Python for AI?", "a": "Readable syntax, fast prototyping, and a huge AI/data ecosystem make Python the default AI language."},
            {"q": "What is dynamic typing?", "a": "Variable types are decided at runtime, so you do not declare them explicitly."},
            {"q": "Difference between list and tuple?", "a": "List is mutable, tuple is immutable."},
            {"q": "Difference between set and dict?", "a": "Set stores unique values, dict stores key-value pairs."},
            {"q": "What is a dictionary?", "a": "A mutable key-value mapping used for fast lookups and counts."},
        ],
        "interview_questions_detailed": [
            {
                "question": "Why Python for AI?",
                "short_answer": "Python is preferred in AI because it is easy to write, easy to read, and has strong libraries like NumPy, Pandas, PyTorch, and TensorFlow.",
                "spoken_answer": "In AI work, Python helps us move from idea to experiment quickly. Its syntax is simple, so teams can focus on logic instead of boilerplate, and the ecosystem for data processing, model training, APIs, and automation is already very mature.",
            },
            {
                "question": "What is dynamic typing?",
                "short_answer": "Dynamic typing means the type of a variable is determined at runtime based on the assigned value.",
                "spoken_answer": "In Python, I do not need to declare a type first. If I assign `x = 10`, Python treats it as an integer, and if I later assign text, the type changes at runtime. It improves development speed, but I still need to be careful about unexpected types.",
            },
            {
                "question": "Difference between list and tuple",
                "short_answer": "List is ordered and mutable. Tuple is ordered and immutable.",
                "spoken_answer": "I use a list when the data may change, such as adding or removing values. I use a tuple when the data should remain fixed, such as coordinates or a record-like value. That immutability can also make tuples safer in some cases.",
            },
            {
                "question": "Difference between set and dict",
                "short_answer": "A set stores unique values only. A dictionary stores key-value pairs.",
                "spoken_answer": "Both are hash-based structures, but they solve different problems. A set is useful for removing duplicates and checking membership quickly, while a dictionary is useful when each key should map to some value, such as a count, score, or record.",
            },
            {
                "question": "What is a dictionary?",
                "short_answer": "A dictionary is a mutable key-value data structure used for fast lookup.",
                "spoken_answer": "A dictionary stores data as `key: value` pairs. It is extremely useful in interviews for frequency counting, caching, grouping, and quick access by key. One big advantage is average O(1) lookup time.",
            },
            {
                "question": "What is the use of `get()` in dict?",
                "short_answer": "It safely returns the value for a key and can provide a default if the key is missing.",
                "spoken_answer": "I use `dict.get(key, default)` when a key may not already exist. It avoids `KeyError` and is especially helpful in counting problems, for example `freq[ch] = freq.get(ch, 0) + 1`.",
            },
            {
                "question": "What is slicing?",
                "short_answer": "Slicing extracts a portion of a sequence like a string or list using start, stop, and step.",
                "spoken_answer": "Slicing is a compact way to work with sequences. For example, `text[1:4]` gives elements from index 1 up to but not including index 4, and `text[::-1]` reverses the sequence.",
            },
            {
                "question": "What is the difference between `==` and `is`?",
                "short_answer": "`==` checks value equality, while `is` checks whether two references point to the same object.",
                "spoken_answer": "I use `==` when I want to compare values, like two strings with the same content. I use `is` mainly for identity checks, such as `value is None`. Confusing them is a common Python mistake.",
            },
            {
                "question": "What is mutability?",
                "short_answer": "Mutability means whether an object can be changed after creation.",
                "spoken_answer": "A mutable object like a list or dictionary can be modified in place. An immutable object like a string or tuple cannot be changed after it is created, so operations create a new object instead.",
            },
            {
                "question": "What is OOP?",
                "short_answer": "Object-oriented programming organizes code using classes and objects.",
                "spoken_answer": "OOP helps model real-world entities by combining data and behavior together. In Python, classes define the structure, objects are instances, and concepts like inheritance and encapsulation improve code organization and reuse.",
            },
            {
                "question": "What is inheritance?",
                "short_answer": "Inheritance allows one class to reuse and extend another class.",
                "spoken_answer": "With inheritance, a child class gets properties and methods from a parent class and can add or override behavior. It reduces repeated code and supports cleaner design when there is a natural hierarchy.",
            },
            {
                "question": "What is encapsulation?",
                "short_answer": "Encapsulation means bundling data and methods together and controlling how internal data is accessed.",
                "spoken_answer": "Encapsulation helps keep object state organized and prevents careless direct changes to internals. In simple interview language, it means putting related data and behavior inside one class and exposing only what is necessary.",
            },
            {
                "question": "What is abstraction?",
                "short_answer": "Abstraction means hiding internal complexity and showing only the essential interface.",
                "spoken_answer": "Abstraction helps users of a class focus on what an object does instead of how it is implemented internally. For example, a user may call a method without knowing all the internal steps behind it.",
            },
            {
                "question": "What is exception handling?",
                "short_answer": "Exception handling is the way Python manages runtime errors safely using `try`, `except`, `else`, and `finally`.",
                "spoken_answer": "Instead of letting the program crash, exception handling allows us to catch expected errors and respond properly. In real applications it improves reliability, debugging, and user experience.",
            },
            {
                "question": "Difference between `break`, `continue`, and `pass`",
                "short_answer": "`break` exits the loop, `continue` skips the current iteration, and `pass` does nothing.",
                "spoken_answer": "I use `break` when I want to stop the loop completely, `continue` when I want to skip one iteration but keep looping, and `pass` when syntax requires a block but I am leaving it empty for now.",
            },
            {
                "question": "What is list comprehension?",
                "short_answer": "List comprehension is a concise way to build a new list from an iterable with optional filtering.",
                "spoken_answer": "It helps write short and readable transformation logic, such as building squares or filtering even numbers in one expression. It is great for clean code, but I avoid making it too complex.",
            },
            {
                "question": "Why use `with open`?",
                "short_answer": "It automatically closes the file and makes file handling safer and cleaner.",
                "spoken_answer": "Using `with open(...)` creates a context manager that handles resource cleanup for me. Even if an exception occurs, the file is closed properly, which is why it is the preferred style.",
            },
            {
                "question": "What is `self`?",
                "short_answer": "`self` refers to the current object instance inside a class method.",
                "spoken_answer": "In Python, instance methods use `self` to access the current object's data and other methods. It lets each object keep its own values, such as `self.name` or `self.score`.",
            },
            {
                "question": "What are `*args` and `**kwargs`?",
                "short_answer": "`*args` collects extra positional arguments and `**kwargs` collects extra keyword arguments.",
                "spoken_answer": "These are useful when a function should accept a flexible number of inputs. `*args` gives a tuple of extra positional values, and `**kwargs` gives a dictionary of extra named values.",
            },
            {
                "question": "Difference between shallow copy and deep copy",
                "short_answer": "A shallow copy copies the outer object only, while a deep copy recursively copies nested objects too.",
                "spoken_answer": "If a list contains nested lists, a shallow copy still shares those inner lists. A deep copy creates fully independent nested data structures, so changes in one copy do not affect the other.",
            },
            {
                "question": "What is the role of `None` in Python?",
                "short_answer": "`None` represents the absence of a value.",
                "spoken_answer": "I use `None` when a variable has no meaningful value yet or when a function should indicate that nothing useful was returned. It is common in defaults, placeholders, and missing-result cases.",
            },
            {
                "question": "How do you loop through a dictionary?",
                "short_answer": "Use `.items()` to get both key and value, `.keys()` for keys, and `.values()` for values.",
                "spoken_answer": "The most common approach is `for key, value in my_dict.items():` because it gives both pieces directly and reads clearly during interviews.",
            },
        ],
        "interview_rapid_fire": [
            {"question": "Python is interpreted or compiled?", "answer": "Usually described as interpreted, though it also uses bytecode internally."},
            {"question": "Is string mutable?", "answer": "No, strings are immutable."},
            {"question": "Best use of set?", "answer": "Uniqueness and fast membership checks."},
            {"question": "Best use of dict?", "answer": "Mapping keys to values and frequency counting."},
            {"question": "What does `range(5)` give?", "answer": "0, 1, 2, 3, 4."},
            {"question": "What does `s[::-1]` do?", "answer": "Reverses the sequence."},
            {"question": "What is `self`?", "answer": "Reference to the current object."},
            {"question": "What does `return` do?", "answer": "Sends a value back to the caller."},
            {"question": "Why use `with open`?", "answer": "Automatic file closing and safer resource handling."},
            {"question": "What does `dict.get()` prevent?", "answer": "It avoids `KeyError` for missing keys."},
        ],
        "interview_common_mistakes": [
            "Confusing list, set, and dictionary use cases.",
            "Not clearly stating that tuples are immutable.",
            "Giving a memorized OOP definition without a simple class example.",
            "Not being able to explain `dict.get()` with a counting example.",
            "Forgetting that strings are immutable.",
            "Using `is` instead of `==` for normal value comparison.",
            "Ignoring edge cases such as empty list, one element, or mixed case strings.",
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "learn_sections": PYTHON_TOPIC.learn_sections
        + [
            {
                "title": "I. Python for Interview Coding",
                "summary": "These are the coding patterns that repeatedly appear in campus interviews and online assessments.",
                "points": [
                    "Frequency count with `dict.get()` is one of the most useful Python interview patterns.",
                    "Anagram check can be solved using sorting or frequency maps.",
                    "Second largest element tests loop logic and edge-case handling.",
                    "Duplicate detection often uses a set.",
                    "Reverse string and palindrome check are common string warm-up questions.",
                    "Built-ins like `max`, `min`, `sum`, `sorted`, and `set` help you code faster.",
                    "`enumerate` gives both index and value while looping.",
                    "`zip` helps iterate over two lists together.",
                    "List comprehensions give a concise way to build filtered or transformed lists.",
                ],
                "examples": [
                    {
                        "label": "enumerate, zip, and list comprehension",
                        "code": """names = ["A", "B", "C"]
scores = [80, 85, 90]

for index, name in enumerate(names):
    print(index, name)

for name, score in zip(names, scores):
    print(name, score)

even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)
""",
                    },
                ],
                "notes": [
                    "Always mention time complexity when the interviewer pauses after your solution.",
                    "Handle edge cases: empty list, one element, uppercase/lowercase, spaces, and duplicates.",
                ],
            },
            {
                "title": "J. Python in AI and Backend Context",
                "summary": "This section connects core Python to the exact skills expected from a campus AI Engineer role.",
                "points": [
                    "Python is heavily used in AI because experimentation is fast and the ML ecosystem is built around it.",
                    "Pandas helps clean, filter, transform, and inspect structured data before training or inference.",
                    "NumPy provides efficient array operations and numerical computing foundations used by many AI libraries.",
                    "Python is useful for quick APIs and automation scripts that connect models with real workflows.",
                    "Prompt pipelines often use Python scripts to prepare context, call APIs, parse responses, and save results.",
                    "Backend frameworks like FastAPI are popular for exposing model endpoints or internal tools.",
                    "Preprocessing and experimentation scripts help compare prompts, clean datasets, evaluate outputs, and automate repetitive tasks.",
                ],
                "callouts": [
                    {"type": "info", "text": "Good interview framing: Python is not only easy to code in; it reduces idea-to-experiment time in AI projects."},
                    {"type": "success", "text": "Role-ready answer: I would use Python for data cleaning, API orchestration, evaluation scripts, and lightweight backend services."},
                ],
                "examples": [
                    {
                        "label": "FastAPI taste",
                        "code": """from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
""",
                    },
                    {
                        "label": "Simple preprocessing idea",
                        "code": """rows = ["  Great output  ", "Bad Output", " average "]
cleaned = [row.strip().lower() for row in rows]
print(cleaned)
""",
                    },
                ],
                "notes": [
                    "For this role, Python is the bridge between AI models, business data, APIs, and automation.",
                    "If asked why Python over lower-level languages for campus AI work, say productivity and ecosystem first.",
                ],
            },
        ],
        "patterns": [
            {
                "title": "Frequency Count",
                "problem": "Count how many times each element appears in a string or list.",
                "intuition": "Store each item as a key in a dictionary and increment its count as you scan once from left to right.",
                "solution": """def frequency_count(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(frequency_count("banana"))
""",
                "alternative": """from collections import Counter

print(Counter("banana"))
""",
                "time_complexity": "O(n) time, O(k) space where k is the number of unique items.",
                "mistakes": [
                    "Using `freq[item] += 1` before the key exists.",
                    "Forgetting to normalize case when the problem is case-insensitive.",
                ],
                "variation": "Return the character with maximum frequency instead of the full dictionary.",
            },
            {
                "title": "Anagram Check",
                "problem": "Check whether two strings contain the same characters in a different order.",
                "intuition": "If the sorted characters match, or if both frequency maps match, the strings are anagrams.",
                "solution": """def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(is_anagram("listen", "silent"))
""",
                "alternative": """def is_anagram(a, b):
    if len(a) != len(b):
        return False

    freq = {}
    for ch in a.lower():
        freq[ch] = freq.get(ch, 0) + 1

    for ch in b.lower():
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True
""",
                "time_complexity": "Sorting version: O(n log n). Frequency-map version: O(n).",
                "mistakes": [
                    "Ignoring uppercase/lowercase or spaces if the question expects normalization.",
                    "Checking only character presence and not full counts.",
                ],
                "variation": "Ignore spaces and punctuation while checking anagrams.",
            },
            {
                "title": "Second Largest Element",
                "problem": "Find the second largest distinct element in a list.",
                "intuition": "Track the largest and second largest values in one scan.",
                "solution": """def second_largest(nums):
    first = float("-inf")
    second = float("-inf")

    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return None if second == float("-inf") else second

print(second_largest([10, 40, 20, 40, 30]))
""",
                "alternative": """def second_largest(nums):
    unique = sorted(set(nums))
    return unique[-2] if len(unique) >= 2 else None
""",
                "time_complexity": "One-pass version: O(n). Sorting version: O(n log n).",
                "mistakes": [
                    "Not handling duplicate maximum values correctly.",
                    "Failing on lists with fewer than two distinct values.",
                ],
                "variation": "Return the second smallest distinct element.",
            },
            {
                "title": "Reverse String",
                "problem": "Reverse a given string.",
                "intuition": "Strings support slicing, so reversing with step `-1` is the cleanest Python solution.",
                "solution": """def reverse_string(text):
    return text[::-1]

print(reverse_string("python"))
""",
                "alternative": """def reverse_string(text):
    result = ""
    for ch in text:
        result = ch + result
    return result
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Trying to swap characters in place even though strings are immutable."],
                "variation": "Reverse only the words in a sentence, not the full character sequence.",
            },
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "learn_sections": PYTHON_TOPIC.learn_sections
        + [
            {
                "title": "D. Conditional Statements and Loops",
                "summary": "Control flow decides how a program reacts to input and repeats logic. Interviewers expect confidence here.",
                "points": [
                    "`if`, `elif`, and `else` are used for decision making.",
                    "`for` loop is used when iterating over a sequence or range.",
                    "`while` loop is used when repetition should continue while a condition remains true.",
                    "`break` exits the loop, `continue` skips the current iteration, and `pass` is a placeholder that does nothing.",
                    "`range()` generates a sequence of numbers commonly used in loops.",
                ],
                "examples": [
                    {
                        "label": "Count vowels",
                        "code": """text = "artificial intelligence"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)
""",
                    },
                    {
                        "label": "Sum numbers",
                        "code": """nums = [4, 7, 2, 9]
total = 0

for num in nums:
    total += num

print(total)
""",
                    },
                    {
                        "label": "Frequency counting basics",
                        "code": """items = ["a", "b", "a", "c", "b", "a"]
freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

print(freq)
""",
                    },
                    {
                        "label": "Loop through dictionary items",
                        "code": """scores = {"math": 90, "python": 95}

for subject, score in scores.items():
    print(subject, score)
""",
                    },
                ],
                "notes": [
                    "Use `for` when the number of iterations is tied to a sequence.",
                    "Use `while` carefully. Always think about the update condition to avoid infinite loops.",
                    "In interviews, explain loop invariant or what each iteration is maintaining.",
                ],
            },
            {
                "title": "E. Functions",
                "summary": "Functions make code reusable, testable, and easier to explain during interviews.",
                "points": [
                    "A function groups related logic into one reusable block.",
                    "Parameters are the variables in the function definition. Arguments are the actual values passed during the call.",
                    "`return` sends a value back to the caller.",
                    "Default arguments give a fallback value when an argument is not passed.",
                    "Keyword arguments improve clarity by naming the parameter in the function call.",
                    "Scope basics: variables created inside a function are local unless explicitly handled otherwise.",
                    "Lambda is a short anonymous function useful for simple one-line expressions.",
                ],
                "examples": [
                    {
                        "label": "Parameters, arguments, and return",
                        "code": """def add(a, b):
    return a + b

result = add(10, 20)
print(result)
""",
                    },
                    {
                        "label": "Default and keyword arguments",
                        "code": """def greet(name, role="student"):
    return f"{name} is a {role}"

print(greet("Neha"))
print(greet(name="Kiran", role="intern"))
""",
                    },
                    {
                        "label": "Lambda basics",
                        "code": """square = lambda x: x * x
print(square(5))
""",
                    },
                ],
                "interview_questions": [
                    "What is the difference between parameter and argument?",
                    "Why do we use `return` instead of only `print`?",
                    "What is local scope?",
                    "When is a lambda function useful?",
                ],
                "notes": [
                    "A function that prints output is not the same as a function that returns output.",
                    "Avoid mutable default arguments like `def f(items=[])` in real projects.",
                ],
            },
            {
                "title": "F. Object-Oriented Programming",
                "summary": "OOP is often asked even in beginner interviews because it shows whether you can model real entities in code.",
                "points": [
                    "A class is a blueprint. An object is an instance created from that blueprint.",
                    "`__init__` is the constructor used to initialize object data.",
                    "`self` refers to the current object instance.",
                    "Instance variables store data specific to each object.",
                    "Methods are functions defined inside a class.",
                    "Inheritance allows one class to reuse and extend another class.",
                    "Encapsulation means bundling data and behavior together and controlling access where needed.",
                    "Polymorphism means the same method name can behave differently for different classes.",
                    "Abstraction means exposing only the important idea while hiding unnecessary implementation details.",
                ],
                "examples": [
                    {
                        "label": "Simple class example",
                        "code": """class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        return f"{self.brand} runs at {self.speed} km/h"

car = Car("Toyota", 120)
print(car.show())
""",
                    },
                    {
                        "label": "Inheritance example",
                        "code": """class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())
""",
                    },
                ],
                "notes": [
                    "Class vs object: class is the design, object is the real created entity.",
                    "Encapsulation vs abstraction: encapsulation protects and organizes internals, abstraction hides complexity and shows only the useful interface.",
                    "Beginner-friendly polymorphism answer: different classes can respond to the same method call in their own way.",
                ],
            },
            {
                "title": "G. Exception Handling",
                "summary": "Exceptions help programs fail safely instead of crashing unexpectedly.",
                "points": [
                    "Exceptions happen when runtime errors occur, such as dividing by zero or converting invalid text to an integer.",
                    "`try` contains risky code.",
                    "`except` handles the error.",
                    "`else` runs if no exception occurs.",
                    "`finally` runs whether an exception happens or not.",
                ],
                "examples": [
                    {
                        "label": "Division by zero",
                        "code": """try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
""",
                    },
                    {
                        "label": "Invalid integer conversion",
                        "code": """try:
    value = int("hello")
except ValueError:
    print("String cannot be converted to int")
""",
                    },
                    {
                        "label": "File not found",
                        "code": """try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")
""",
                    },
                ],
                "notes": [
                    "Use specific exceptions instead of a broad `except Exception` when possible.",
                    "In real applications, exception handling improves reliability, logging, and user experience.",
                ],
            },
            {
                "title": "H. File Handling",
                "summary": "File handling appears in practical coding rounds, backend tasks, and automation scripts.",
                "points": [
                    "`open()` is used to open a file.",
                    "Modes: `r` for read, `w` for write, `a` for append.",
                    "`with open(...) as f` is preferred because it closes the file automatically.",
                    "Context managers make code safer and cleaner, especially when exceptions occur.",
                ],
                "examples": [
                    {
                        "label": "Read a text file",
                        "code": """with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
""",
                    },
                    {
                        "label": "Write and append",
                        "code": """with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python basics\\n")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Interview revision\\n")
""",
                    },
                ],
                "notes": [
                    "If you forget to close files in manual handling, resources may leak.",
                    "Interview answer: `with open` is better because it automatically manages file closing.",
                ],
            },
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC


PYTHON_TOPIC = PYTHON_TOPIC.__class__(
    **{
        **PYTHON_TOPIC.__dict__,
        "patterns": PYTHON_TOPIC.patterns
        + [
            {
                "title": "Palindrome Check",
                "problem": "Check whether a string reads the same from both ends.",
                "intuition": "Compare the original string with its reversed version after normalization.",
                "solution": """def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
""",
                "alternative": """def is_palindrome(text):
    text = text.lower()
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Not converting case when the interview expects case-insensitive comparison."],
                "variation": "Ignore spaces and punctuation.",
            },
            {
                "title": "Find Duplicates",
                "problem": "Find repeated elements in a list.",
                "intuition": "Track seen elements in a set and collect repeated values.",
                "solution": """def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
""",
                "alternative": """def find_duplicates(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return [num for num, count in freq.items() if count > 1]
""",
                "time_complexity": "O(n) time on average.",
                "mistakes": ["Returning the same duplicate multiple times."],
                "variation": "Return only whether duplicates exist.",
            },
            {
                "title": "Count Vowels",
                "problem": "Count vowels in a string.",
                "intuition": "Loop once and count characters that belong to the vowel set.",
                "solution": """def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
""",
                "alternative": """def count_vowels(text):
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)
""",
                "time_complexity": "O(n) time.",
                "mistakes": ["Missing uppercase vowels when not using `lower()`."],
                "variation": "Return each vowel count separately.",
            },
            {
                "title": "List Comprehension Examples",
                "problem": "Create a new list with concise filtering or transformation logic.",
                "intuition": "Use list comprehension when the transformation is simple and readable.",
                "solution": """nums = [1, 2, 3, 4, 5, 6]
evens = [num for num in nums if num % 2 == 0]
squares = [num * num for num in nums]
""",
                "alternative": """nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda num: num % 2 == 0, nums))
""",
                "time_complexity": "Usually O(n) time.",
                "mistakes": ["Writing comprehension logic that is too complex to read quickly."],
                "variation": "Build a dictionary comprehension for squares.",
            },
        ],
    }
)


TOPIC_DATA["python"] = PYTHON_TOPIC
