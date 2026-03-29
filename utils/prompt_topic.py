"""Structured content for the Prompt Engineering topic page."""

from utils.data import TopicContent, _q, _r


PROMPT_ENGINEERING_TOPIC = TopicContent(
    key="prompt_engineering",
    title="Prompt Engineering",
    icon="PE",
    difficulty="Easy to Medium",
    priority="Very High",
    estimated_time="2 to 3 hours",
    importance_for_movate="Very High",
    why_it_matters=(
        "Prompt engineering is the practice of designing model inputs so outputs become more accurate, structured, useful, "
        "and reliable. For an AI Engineer, prompt quality often decides whether a chatbot, copilot, summarizer, or automation "
        "workflow feels helpful or unusable."
    ),
    detailed_sections={
        "Prompt basics": "A prompt is the instruction given to an LLM. Better prompts usually produce better outputs.",
        "Prompt anatomy": "Good prompts usually include instruction, context, input data, output format, and constraints.",
        "Technique selection": "Zero-shot, few-shot, role prompting, structured prompting, and constraints are practical tools.",
        "Prompt debugging": "Weak prompts can be improved systematically by tightening scope, format, and context.",
        "Workflow thinking": "Prompt engineering is not just wording. It connects with retrieval, APIs, evaluation, and automation.",
    },
    common_mistakes=[
        "Writing vague prompts and expecting precise results.",
        "Giving too much context without structure.",
        "Asking for a format but not specifying the exact schema.",
        "Treating prompting like magic instead of an iterative engineering task.",
        "Not testing prompts against edge cases or realistic user inputs.",
    ],
    code_examples={
        "Anatomy of a Prompt": """You are a backend engineer.
Explain JWT in simple terms.
Output in bullet points.
""",
        "Structured Prompt": """Task: Summarize the support ticket
Audience: Support manager
Constraints: 5 bullets, no extra facts
Output format: bullet list
Input: <ticket text>
""",
    },
    interview_questions=[
        {"q": "What is prompt engineering?", "a": "It is the practice of designing prompts so LLM outputs become more useful, accurate, and controlled."},
        {"q": "Why does prompt quality matter?", "a": "Small prompt changes can change output quality, structure, and hallucination risk."},
        {"q": "What is zero-shot prompting?", "a": "It means asking the model to do a task directly without examples."},
        {"q": "What is few-shot prompting?", "a": "It means giving a few examples so the model follows a pattern."},
        {"q": "How do you debug a bad prompt?", "a": "Make the task clearer, reduce ambiguity, tighten constraints, and test variations."},
    ],
    quick_revision_points=[],
    quiz_questions=[],
    resources=[],
    role_relevance=[
        "AI copilots and assistants",
        "Enterprise automation workflows",
        "Knowledge assistants and chatbot systems",
        "Reducing hallucination through clearer instructions",
        "Standardizing outputs for downstream systems",
    ],
    learning_objectives=[
        "Understand prompting from scratch.",
        "Write higher-quality prompts for real AI tasks.",
        "Debug and improve prompts systematically.",
        "Explain prompt engineering confidently in interviews.",
        "Connect prompting with enterprise AI workflows.",
    ],
    learn_sections=[],
    techniques=[],
    worked_examples=[],
    debugging_sections=[],
    interview_questions_detailed=[],
    interview_rapid_fire=[],
    interview_common_mistakes=[],
    resource_sections={},
)


PROMPT_ENGINEERING_TOPIC = PROMPT_ENGINEERING_TOPIC.__class__(
    **{
        **PROMPT_ENGINEERING_TOPIC.__dict__,
        "learn_sections": [
            {
                "title": "1. What is Prompt Engineering",
                "summary": "A prompt is the instruction given to a language model. Prompt engineering is the practice of designing those instructions carefully so the output becomes more useful and controllable.",
                "points": [
                    "Prompt quality has a major impact on model output quality.",
                    "A vague prompt is like asking a human a vague question and expecting a perfect answer.",
                    "A clear prompt is like giving a teammate a precise task, enough context, and a clear format.",
                    "LLM behavior is not fully deterministic, so small wording changes can lead to noticeable output changes.",
                ],
                "examples": [
                    {
                        "label": "Vague vs clear analogy",
                        "code": """Vague: "Explain JWT"
Clear: "Explain JWT in simple terms for a beginner backend intern. Use 4 bullet points and one real-world analogy."
""",
                    }
                ],
                "callouts": [
                    {"type": "info", "text": "Interview tip: prompt engineering is not only wording. It is about controlling task framing, context, and output structure."},
                    {"type": "warning", "text": "Common confusion: a better prompt improves output quality, but it does not remove all model limitations."},
                ],
            },
            {
                "title": "2. Why It Matters for Movate AI Engineer",
                "summary": "In AI Engineer work, prompt engineering is a practical skill used in product behavior, not just a theoretical topic.",
                "points": [
                    "Prompting is used in AI copilots, enterprise automation, knowledge assistants, and chatbot systems.",
                    "Good prompts reduce hallucination by narrowing the task and making the model less ambiguous.",
                    "Good prompts improve accuracy by giving the model relevant role, task, and format information.",
                    "Good prompts standardize outputs so downstream systems can parse or store them more reliably.",
                    "Prompting helps automate workflows where the output needs to be consistent enough for review or next-step logic.",
                ],
                "examples": [{"label": "Workflow impact", "code": "User request -> Prompt builder -> Model response -> Validation / parsing -> Workflow action"}],
            },
            {
                "title": "3. Anatomy of a Prompt",
                "summary": "Strong prompts usually include a few repeatable components.",
                "points": [
                    "Instruction: what the model should do.",
                    "Context: background information that helps the model answer correctly.",
                    "Input data: the actual user data, text, or content to work on.",
                    "Output format: bullets, JSON, table, short answer, email draft, etc.",
                    "Constraints: limits such as length, tone, allowed sources, or no extra assumptions.",
                ],
                "examples": [
                    {
                        "label": "Prompt anatomy example",
                        "code": """You are a backend engineer.
Explain JWT in simple terms.
Output in bullet points.
""",
                    },
                    {
                        "label": "More complete anatomy",
                        "code": """Role: You are a support assistant.
Task: Summarize the ticket.
Context: This is for an internal escalation team.
Constraints: Maximum 5 bullet points. Do not invent facts.
Output format: bullet list
Input: <ticket text>
""",
                    },
                ],
            },
            {
                "title": "4. Prompting Styles",
                "summary": "Different prompt styles are useful for different tasks.",
                "points": [
                    "Zero-shot prompting means asking directly without examples.",
                    "Few-shot prompting means showing a few examples so the model copies the pattern.",
                    "Role prompting means telling the model what perspective to take, like recruiter, tutor, or support assistant.",
                    "Structured prompting means organizing prompt sections clearly instead of writing one long paragraph.",
                ],
                "tables": [
                    {
                        "title": "Style comparison",
                        "markdown": """| Style | Best for | Example |
|---|---|---|
| Zero-shot | Simple direct tasks | "Summarize this email" |
| Few-shot | Pattern-following tasks | Classification with examples |
| Role prompting | Tone and perspective control | "You are a recruiter..." |
| Structured prompting | Complex tasks | Task + context + constraints + format |""",
                    }
                ],
            },
            {
                "title": "5. Output Control and Formatting",
                "summary": "One of the easiest prompt improvements is asking for the exact format you want.",
                "points": [
                    "If the output will be read by a human, specify bullets, steps, tone, and length.",
                    "If the output will be used by code, specify JSON keys, fields, or table columns clearly.",
                    "Format control reduces post-processing effort and often reduces ambiguity.",
                ],
                "examples": [
                    {
                        "label": "Format-specific prompt",
                        "code": """Extract the issue summary from the ticket.
Return valid JSON with keys: category, priority, summary
Do not include any extra text.
""",
                    }
                ],
                "callouts": [{"type": "success", "text": "Simple rule: if you know the desired format, ask for it explicitly."}],
            },
            {
                "title": "6. Constraints and Guardrails",
                "summary": "Constraints help narrow the task and make the model output more reliable.",
                "points": [
                    "Common constraints include word limit, no extra assumptions, use only provided context, fixed tone, or specific output schema.",
                    "Guardrails are especially important when the model should not fabricate facts or go outside policy.",
                    "Constraints do not make the model perfect, but they often reduce noise and inconsistency.",
                ],
            },
            {
                "title": "7. Prompt Iteration and Optimization",
                "summary": "Prompting is an engineering loop: write, test, inspect output, revise, and compare.",
                "points": [
                    "Start with a simple prompt, then improve one thing at a time.",
                    "Change task clarity, context, format, or constraints systematically instead of rewriting everything randomly.",
                    "Compare outputs across realistic test cases, not only one ideal example.",
                    "Keep a prompt version history when working on real products.",
                ],
                "examples": [{"label": "Optimization loop", "code": "Prompt v1 -> Test outputs -> Identify failure -> Improve one variable -> Re-test"}],
            },
            {
                "title": "8. Prompt Engineering in Real AI Workflows",
                "summary": "In production apps, prompts live inside systems, not in isolation.",
                "points": [
                    "Prompts may be built dynamically from user input, retrieved context, and business rules.",
                    "Prompts often work together with APIs, retrieval layers, validation steps, and logging.",
                    "A strong AI Engineer thinks about prompt quality together with system behavior, not only wording.",
                ],
                "examples": [{"label": "ASCII flow", "code": "User Input -> Prompt Builder -> Optional Retrieval -> Model -> Output Check -> Final Response"}],
            },
        ],
        "techniques": [
            {
                "title": "Zero-shot prompting",
                "what_it_is": "Ask the model to perform the task directly without examples.",
                "why_it_helps": "Fastest option for simple, well-defined tasks.",
                "when_to_use": "Use it when the task is straightforward and the expected format is easy to specify.",
                "prompt": """Summarize the following customer complaint in 3 bullet points.
Do not add information that is not present in the complaint.
Complaint: <text>
""",
                "mistakes": ["Using zero-shot for pattern-heavy tasks that really need examples."],
            },
            {
                "title": "Few-shot prompting",
                "what_it_is": "Give a few example inputs and outputs before the real task.",
                "why_it_helps": "Helps the model copy a target pattern, style, or classification scheme.",
                "when_to_use": "Use it for extraction, classification, rewriting, and structured response tasks.",
                "prompt": """Example 1
Input: Ticket says login page crashes after password reset.
Output: category=authentication

Example 2
Input: User cannot download invoice PDF.
Output: category=billing

Now classify:
Input: Customer says OTP is not arriving.
Output:
""",
                "mistakes": ["Using examples that are inconsistent with each other."],
            },
            {
                "title": "Role prompting",
                "what_it_is": "Assign the model a role or perspective to shape tone and focus.",
                "why_it_helps": "Useful for tailoring the style of response for a target audience.",
                "when_to_use": "Use it when output needs a specific voice, level, or professional framing.",
                "prompt": """You are a customer support lead.
Rewrite the reply politely and professionally.
Input: <draft reply>
""",
                "mistakes": ["Thinking role prompting alone is enough without task clarity."],
            },
            {
                "title": "Structured prompting",
                "what_it_is": "Break the prompt into clear sections such as task, context, constraints, and output format.",
                "why_it_helps": "Reduces ambiguity and makes prompts easier to debug and maintain.",
                "when_to_use": "Use it for any medium-complexity or production-like prompt.",
                "prompt": """Task: Summarize the bug report
Context: For an engineering manager
Constraints: Max 4 bullets, no speculation
Output format: bullet list
Input: <bug report>
""",
                "mistakes": ["Putting all sections together in an unstructured paragraph."],
            },
            {
                "title": "Constraint prompting",
                "what_it_is": "Tell the model what it must not do and what limits it must follow.",
                "why_it_helps": "Improves consistency and reduces unwanted behavior.",
                "when_to_use": "Use it when hallucination, verbosity, or format drift is a problem.",
                "prompt": """Answer only from the provided policy text.
If the answer is not present, say "Not found in provided context."
Use exactly 2 bullet points.
Context: <policy text>
Question: <user question>
""",
                "mistakes": ["Adding constraints but forgetting to provide enough context to succeed."],
            },
            {
                "title": "Format-first prompting",
                "what_it_is": "Specify the exact response schema before the task.",
                "why_it_helps": "Very useful when outputs feed into downstream code or workflows.",
                "when_to_use": "Use it in extraction, classification, and structured automation tasks.",
                "prompt": """Return valid JSON only with keys:
issue_type, urgency, short_summary
Input: <ticket text>
""",
                "mistakes": ["Not defining required keys or allowed values clearly."],
            },
        ],
        "worked_examples": [
            {
                "title": "Example 1: Better explanation prompt",
                "problem": "The user wants a clear beginner-friendly explanation.",
                "bad_prompt": "Explain JWT.",
                "better_prompt": """Explain JWT to a beginner backend intern.
Use simple language.
Output in 4 bullet points.
Add one real-world analogy.
""",
                "why_better": "The improved prompt gives audience, style, structure, and depth constraints.",
                "workflow": "User need -> clarify audience -> ask for structure -> get more useful output",
            },
            {
                "title": "Example 2: Enterprise summarization prompt",
                "problem": "A team needs reliable ticket summaries for escalation workflows.",
                "bad_prompt": "Summarize this ticket.",
                "better_prompt": """You are a support operations assistant.
Summarize the ticket for an escalation engineer.
Use maximum 5 bullet points.
Include issue, impact, steps already tried, and urgency.
Do not invent facts.
Ticket: <ticket text>
""",
                "why_better": "The prompt makes the business context, audience, format, and constraints explicit.",
                "workflow": "Ticket -> prompt builder -> model summary -> review / store",
            },
            {
                "title": "Example 3: Structured extraction prompt",
                "problem": "The output must be machine-readable.",
                "bad_prompt": "Extract the key info from this email.",
                "better_prompt": """Extract the following fields from the email.
Return valid JSON only.
Fields: customer_name, issue_type, product, urgency
If a field is missing, use null.
Email: <email text>
""",
                "why_better": "The better prompt tells the model exactly what fields to return and how to handle missing values.",
                "workflow": "Email -> prompt -> JSON output -> downstream parser",
            },
            {
                "title": "Example 4: Classification with few-shot examples",
                "problem": "The model should follow a fixed label set consistently.",
                "bad_prompt": "Classify this support ticket.",
                "better_prompt": """Allowed labels: authentication, billing, bug, account_access

Example:
Input: I reset my password but still cannot sign in.
Output: authentication

Example:
Input: My invoice amount is incorrect.
Output: billing

Now classify:
Input: The app crashes when I upload a file.
Output:
""",
                "why_better": "The examples teach the label pattern and reduce inconsistent label naming.",
                "workflow": "Prompt with examples -> model classification -> workflow routing",
            },
        ],
        "debugging_sections": [
            {
                "title": "When the output is too vague",
                "problem": "The response is generic and not useful enough.",
                "why_it_happens": "The prompt does not specify audience, detail level, or output format.",
                "fix": "Add target audience, desired depth, and structure requirements.",
                "example": """Bad: Explain APIs.
Better: Explain REST APIs to a first-year engineering student in 5 simple bullet points with one example.
""",
                "checklist": ["Did I specify the audience?", "Did I ask for the format?", "Did I define the desired depth?"],
            },
            {
                "title": "When the model invents facts",
                "problem": "The output contains unsupported information.",
                "why_it_happens": "The prompt allows open-ended generation without grounding or constraints.",
                "fix": "Tell the model to answer only from provided context and say when information is missing.",
                "example": """Use only the provided context.
If the answer is not present, say "Not available in context."
""",
                "checklist": ["Did I provide trusted context?", "Did I forbid extra assumptions?", "Do I need retrieval?"],
            },
            {
                "title": "When the format keeps changing",
                "problem": "The model returns paragraphs when you need JSON, bullets, or a table.",
                "why_it_happens": "The output format was not specified tightly enough.",
                "fix": "Specify exact format, fields, and if needed say 'return only valid JSON'.",
                "example": """Return valid JSON only with keys: category, priority, summary
""",
                "checklist": ["Did I name the keys?", "Did I ask for extra text to be removed?", "Do I need a schema example?"],
            },
            {
                "title": "When prompts work for one case but fail on others",
                "problem": "The prompt looks good on one sample but breaks on realistic inputs.",
                "why_it_happens": "The prompt was not tested on enough edge cases.",
                "fix": "Build a small prompt test set and compare outputs across normal, short, noisy, and ambiguous inputs.",
                "example": """Test set:
- normal ticket
- very short ticket
- noisy customer email
- missing information case
""",
                "checklist": ["Did I test edge cases?", "Did I compare versions?", "Am I optimizing for one example only?"],
            },
        ],
        "interview_questions_detailed": [
            {"question": "What is prompt engineering?", "short_answer": "Prompt engineering is the practice of designing model inputs so the output becomes more useful, accurate, and controlled.", "spoken_answer": "Prompt engineering means writing prompts in a deliberate way so a language model gives better results. That includes deciding the instruction, context, format, constraints, and examples when needed. It is a practical engineering skill because small prompt changes can significantly change output quality."},
            {"question": "Why does prompt quality matter so much?", "short_answer": "Because the model depends heavily on prompt clarity to understand the task, format, and boundaries.", "spoken_answer": "The model does not automatically know our exact intent. If the prompt is vague, the model may answer in the wrong format, too generally, or with extra assumptions. A better prompt reduces ambiguity and often improves accuracy, consistency, and usefulness."},
            {"question": "What is the anatomy of a good prompt?", "short_answer": "A good prompt often includes instruction, context, input data, output format, and constraints.", "spoken_answer": "I usually think of prompt anatomy as five parts: what the model should do, the context it needs, the actual input data, the format expected in the output, and the constraints such as length or no extra assumptions. This structure makes prompts easier to build and debug."},
            {"question": "What is zero-shot prompting?", "short_answer": "Zero-shot prompting means asking the model to do the task directly without examples.", "spoken_answer": "In zero-shot prompting, we simply describe the task and ask the model to do it. This works well for straightforward tasks where the instruction is already clear and the behavior does not depend on a special pattern."},
            {"question": "What is few-shot prompting?", "short_answer": "Few-shot prompting means giving a few examples before the actual task so the model follows the pattern.", "spoken_answer": "Few-shot prompting is useful when we want the model to copy a specific output style, label set, or structure. By showing a few examples, we reduce ambiguity and often get more consistent outputs."},
            {"question": "What is role prompting?", "short_answer": "Role prompting tells the model what perspective or role it should take.", "spoken_answer": "Role prompting is when we ask the model to behave like a tutor, recruiter, support agent, or another role. It is useful for controlling tone, focus, and audience fit, but it still needs clear task instructions."},
            {"question": "What is structured prompting?", "short_answer": "Structured prompting means organizing the prompt into clear sections instead of one long paragraph.", "spoken_answer": "Structured prompting improves readability and reliability by separating task, context, constraints, and output format. It is especially useful in production systems because it is easier to maintain and debug."},
            {"question": "How do prompts reduce hallucination?", "short_answer": "Prompts reduce hallucination by narrowing the task, constraining the answer, and grounding the model in context.", "spoken_answer": "A prompt can reduce hallucination by telling the model to use only provided information, avoid unsupported assumptions, and follow a narrow scope. It does not fully eliminate hallucination, but it can reduce it significantly."},
            {"question": "How do you improve a weak prompt?", "short_answer": "Make the task clearer, add context, define the output format, and tighten constraints.", "spoken_answer": "I improve weak prompts systematically instead of rewriting them randomly. First I identify the failure mode, such as vague output or wrong format. Then I add specificity, audience, context, constraints, or examples depending on what is missing."},
            {"question": "How do you debug a prompt that gives inconsistent output?", "short_answer": "Reduce ambiguity, add a tighter format, and test the prompt across multiple inputs.", "spoken_answer": "If a prompt behaves inconsistently, I look at whether the task is under-specified, whether the format is unclear, or whether the prompt was only tested on one sample. I usually tighten the instructions and build a small prompt test set."},
            {"question": "Why specify output format explicitly?", "short_answer": "Because the model is more likely to return usable and consistent output when the expected format is explicit.", "spoken_answer": "If I know the output should be bullet points, JSON, or a table, I ask for that directly. This reduces post-processing effort and makes the output more reliable for users or downstream systems."},
            {"question": "What is the difference between prompting and fine-tuning?", "short_answer": "Prompting changes behavior through input design, while fine-tuning changes the model behavior more deeply using data.", "spoken_answer": "Prompting is usually the faster and cheaper option because it only changes what we send to the model. Fine-tuning changes the model itself and is more expensive and maintenance-heavy. In many workflows, teams try better prompting first."},
            {"question": "When should you use few-shot instead of zero-shot?", "short_answer": "Use few-shot when the task needs a specific pattern, label set, or output style.", "spoken_answer": "If the model needs help learning the exact pattern we want, few-shot prompting is often better. This is common in classification, extraction, and transformation tasks where consistency matters."},
            {"question": "What are common prompt engineering techniques?", "short_answer": "Zero-shot, few-shot, role prompting, structured prompting, constraints, and format control.", "spoken_answer": "The most common practical techniques are zero-shot prompting for direct tasks, few-shot prompting for patterned outputs, role prompting for tone and perspective, structured prompting for clarity, and explicit format or constraints for consistency."},
            {"question": "How does prompt engineering connect to real AI applications?", "short_answer": "Prompt engineering shapes how copilots, chatbots, summarizers, and automation systems behave in production.", "spoken_answer": "In a real AI system, prompt engineering is part of product behavior. It affects accuracy, structure, hallucination risk, and workflow fit. For example, a support summarizer, internal copilot, or document extractor depends heavily on prompt quality."},
            {"question": "What is a prompt template?", "short_answer": "A prompt template is a reusable prompt structure with placeholders for dynamic inputs.", "spoken_answer": "In production systems, prompts are often templates rather than static text. We keep a reusable structure and fill in user input, retrieved content, or workflow-specific values dynamically."},
            {"question": "How do constraints help in prompting?", "short_answer": "Constraints narrow the task and reduce unwanted behavior.", "spoken_answer": "Constraints tell the model what limits to follow, such as no extra assumptions, use only provided context, keep the answer short, or return a fixed schema. They are useful for improving reliability."},
            {"question": "What is prompt iteration?", "short_answer": "Prompt iteration is the process of testing and refining prompts based on output behavior.", "spoken_answer": "Prompt iteration is like debugging any other system component. You test the prompt, inspect where it fails, improve one variable at a time, and compare results across multiple examples."},
            {"question": "Why is prompt engineering important for enterprise AI?", "short_answer": "Because enterprise systems need controlled, consistent, and workflow-safe output.", "spoken_answer": "Enterprise AI systems cannot rely on vague output. They need prompts that produce predictable formats, reduce hallucination, and fit workflow requirements such as summaries, extraction, routing, or reporting."},
            {"question": "How would you evaluate whether a prompt is good?", "short_answer": "Check relevance, correctness, consistency, format adherence, and usefulness across multiple cases.", "spoken_answer": "A good prompt should not be judged on one lucky example. I would test it on several realistic inputs and check output quality, consistency, format compliance, and whether it actually helps the workflow."},
            {"question": "What is the difference between a prompt and a prompt template?", "short_answer": "A prompt is one instruction set, while a prompt template is a reusable structure with placeholders.", "spoken_answer": "In simple terms, a prompt is the actual text we send to the model, while a prompt template is the reusable pattern behind it. In production systems, templates are more common because they let us insert user data, retrieved context, and workflow values dynamically."},
            {"question": "Why do small prompt changes sometimes cause big output differences?", "short_answer": "Because prompt wording changes the task framing, context interpretation, and output constraints the model follows.", "spoken_answer": "A small wording change can shift the model's interpretation of the task, the level of detail, the assumed audience, or the output style. Since models respond to patterns in text, those small changes can create large output differences."},
            {"question": "When should you ask the model to say 'I don't know'?", "short_answer": "When factual reliability matters and the model should avoid unsupported answers.", "spoken_answer": "In enterprise systems, it is often safer to tell the model to admit missing information rather than guess. This is useful in policy Q&A, knowledge assistants, or any workflow where unsupported output is risky."},
            {"question": "How does prompt engineering connect with RAG?", "short_answer": "Prompt engineering tells the model how to use the retrieved context properly.", "spoken_answer": "Retrieval alone is not enough. The prompt still has to tell the model how to use the retrieved documents, what to do if the answer is missing, and what format to return. Good prompt design is a major part of a strong RAG system."},
            {"question": "What is one practical sign that a prompt needs improvement?", "short_answer": "The output is inconsistent, too vague, hallucinates, or does not follow the required format.", "spoken_answer": "If the same prompt behaves differently across similar inputs, or if the output is too generic, unsupported, or format-breaking, that usually means the prompt is under-specified. That is when I tighten clarity, constraints, and examples."},
        ],
        "interview_rapid_fire": [
            {"question": "Prompt means?", "answer": "Instruction and context given to the model."},
            {"question": "Prompt engineering means?", "answer": "Designing inputs to control outputs."},
            {"question": "Zero-shot?", "answer": "No examples, direct instruction."},
            {"question": "Few-shot?", "answer": "A few examples before the task."},
            {"question": "Role prompting?", "answer": "Assigning a perspective like tutor or support agent."},
            {"question": "Structured prompting?", "answer": "Task plus context plus constraints plus format."},
            {"question": "Format control helps with?", "answer": "Consistency and easier downstream use."},
            {"question": "Prompt debugging starts with?", "answer": "Identifying the exact failure mode."},
            {"question": "Constraints do what?", "answer": "Reduce ambiguity and unwanted behavior."},
            {"question": "Prompting matters in production because?", "answer": "It directly affects quality, reliability, and workflow fit."},
        ],
        "interview_common_mistakes": [
            "Defining prompt engineering too vaguely.",
            "Not knowing the difference between zero-shot and few-shot prompting.",
            "Ignoring format specification in prompts.",
            "Not being able to explain prompt debugging as an iterative process.",
            "Talking about prompt engineering without connecting it to real AI applications.",
        ],
        "quick_revision_points": [
            "A prompt is the instruction and context given to an LLM.",
            "Prompt engineering is designing inputs to control outputs.",
            "Clear prompts usually outperform vague prompts.",
            "Good prompts often include instruction, context, input, format, and constraints.",
            "Prompt quality strongly affects usefulness, consistency, and hallucination risk.",
            "Zero-shot means direct prompting without examples.",
            "Few-shot means using a few examples to teach the pattern.",
            "Role prompting helps with tone and perspective.",
            "Structured prompting improves clarity and maintainability.",
            "Explicit format requests improve output consistency.",
            "Constraints reduce ambiguity and unwanted behavior.",
            "Prompting is iterative, not one-shot magic.",
            "Prompt debugging starts by identifying the failure mode.",
            "Testing prompts on multiple cases is essential.",
            "Good prompts help reduce hallucination but do not eliminate it.",
            "Prompt templates make production systems easier to manage.",
            "Prompting often works with retrieval, APIs, and validation layers.",
            "Enterprise prompting values predictable output, not just nice wording.",
            "Downstream systems benefit from structured outputs like JSON.",
            "Prompt quality is a product behavior issue, not only a model issue.",
        ],
        "quiz_questions": [
            _q("What is prompt engineering mainly about?", ["Training a GPU", "Designing model inputs to improve outputs", "Building databases", "Compressing models"], 1, "Prompt engineering is about designing instructions and context so the model behaves more usefully."),
            _q("Which is a core part of a strong prompt?", ["Random wording", "Clear output format", "No context at all", "Only emojis"], 1, "Explicit output format often improves consistency and usefulness."),
            _q("What is zero-shot prompting?", ["Prompting with no examples", "Prompting with ten examples", "Fine-tuning the model", "Using no instructions"], 0, "Zero-shot means asking the model to do the task directly without demonstrations."),
            _q("What is few-shot prompting?", ["Prompting with a few examples", "Prompting with no context", "Retraining the tokenizer", "Only using system prompts"], 0, "Few-shot prompting gives example inputs and outputs so the model follows a pattern."),
            _q("A common prompt debugging step is", ["Adding more randomness first", "Making the task clearer and more specific", "Removing all constraints", "Ignoring bad outputs"], 1, "Prompt debugging usually starts by reducing ambiguity and tightening instructions."),
            _q("Why specify output format in a prompt?", ["To make answers longer", "To improve consistency and downstream usability", "To increase randomness", "To avoid all model mistakes"], 1, "Format control helps make responses more predictable and easier to use."),
            _q("Role prompting is mainly useful for", ["Changing tone and perspective", "Compressing the model", "Increasing database speed", "Replacing retrieval"], 0, "Role prompting helps shape tone, audience fit, and perspective."),
            _q("Which statement best describes prompt iteration?", ["Write once and never change", "Improve prompts by testing and refining them across cases", "Replace prompts with training data immediately", "Only change temperature"], 1, "Prompt iteration is the engineering process of testing and improvement."),
        ],
        "resource_sections": {
            "Must watch first": [
                _r("DeepLearning.AI Prompt Engineering for Developers", "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/", "video", "must_watch", "Practical beginner-friendly short course."),
                _r("freeCodeCamp Prompt Engineering Videos", "https://www.youtube.com/@freecodecamp/search?query=prompt%20engineering", "video", "must_watch", "Long-form beginner explainers and walkthroughs."),
            ],
            "Must read first": [
                _r("OpenAI Text Generation Guide", "https://platform.openai.com/docs/guides/text-generation", "article", "must_read", "Official guide with prompt-related generation guidance."),
                _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "One of the most useful prompt pattern references."),
                _r("Anthropic Prompt Engineering Overview", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview", "article", "must_read", "Clear conceptual explanation and technique ideas."),
            ],
            "Practice / explore": [
                _r("OpenAI Cookbook", "https://cookbook.openai.com/", "article", "practice", "Hands-on examples of model-powered workflows."),
                _r("Hugging Face Learn", "https://huggingface.co/learn", "article", "practice", "Broader GenAI and prompting-adjacent learning."),
            ],
            "Optional deep dive": [
                _r("OpenAI Parameter Details", "https://platform.openai.com/docs/guides/text-generation/parameter-details", "article", "optional_deep_dive", "Useful for understanding behavior controls such as parameters."),
                _r("Anthropic Docs", "https://docs.anthropic.com/", "article", "optional_deep_dive", "Additional model-building and prompting documentation."),
            ],
        },
        "resources": [
            _r("OpenAI Text Generation Guide", "https://platform.openai.com/docs/guides/text-generation", "article", "must_read", "Official prompt-related generation guidance."),
            _r("Prompting Guide", "https://www.promptingguide.ai/", "article", "must_read", "Strong practical prompt reference."),
            _r("Anthropic Prompt Engineering Overview", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview", "article", "must_read", "Clear conceptual prompting guide."),
            _r("OpenAI Cookbook", "https://cookbook.openai.com/", "article", "practice", "Hands-on prompt and workflow examples."),
        ],
    }
)
