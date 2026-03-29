"""Structured content for the APIs and Backend topic page."""

from utils.data import TopicContent, _q, _r


APIS_BACKEND_TOPIC = TopicContent(
    key="apis_backend",
    title="APIs and Backend",
    icon="API",
    difficulty="Easy to Medium",
    priority="Very High",
    estimated_time="3 to 4 hours",
    importance_for_movate="Very High",
    why_it_matters=(
        "Backend and API knowledge matters because most AI products need secure services that accept requests, validate users, "
        "call models, connect to databases, integrate with enterprise systems, and return reliable responses. For a Movate AI "
        "Engineer role, backend thinking helps in prompt pipelines, tool integrations, model APIs, automation workflows, "
        "enterprise copilots, and production-ready AI applications."
    ),
    detailed_sections={
        "Backend basics": "Learn what backend means, how it fits with frontend, and why it is the execution layer of applications.",
        "API communication": "Understand requests, responses, HTTP, endpoints, JSON, and status codes in simple language.",
        "REST and CRUD": "Master the most common API design style used in interviews and beginner backend projects.",
        "Authentication and reliability": "Know auth, tokens, validation, error handling, and why backend systems must be safe and stable.",
        "AI app integration": "Connect backend concepts to model APIs, retrieval, tool calling, and enterprise automation workflows.",
    },
    common_mistakes=[
        "Confusing API with database or backend framework.",
        "Explaining backend only as storage and forgetting business logic, auth, and integrations.",
        "Not knowing the difference between GET, POST, PUT, and PATCH.",
        "Mixing up authentication with authorization.",
        "Not being able to explain how an AI app actually uses backend services.",
    ],
    code_examples={
        "Simple JSON": """{
  "name": "Rushikesh",
  "role": "AI Engineer"
}""",
        "Request-response flow": "Client -> HTTP Request -> Backend Route -> Business Logic -> DB/API Call -> Response",
        "AI app flow": "User Query -> Frontend -> Backend -> Retrieval/API/Model -> Post-processing -> Response",
    },
    interview_questions=[
        {"q": "What is backend?", "a": "Backend is the server-side part of an app that handles logic, storage, authentication, and integrations."},
        {"q": "What is an API?", "a": "An API is a communication interface that lets systems exchange requests and responses."},
        {"q": "What is HTTP?", "a": "HTTP is the common protocol used for communication between clients and web servers."},
        {"q": "What is REST?", "a": "REST is a common design style for APIs built around resources and standard HTTP methods."},
        {"q": "Why does an AI app need backend APIs?", "a": "Because the backend safely manages model calls, tools, retrieval, secrets, logging, and business logic."},
    ],
    role_relevance=[
        "AI applications often call APIs instead of talking directly to models or databases from the frontend.",
        "Tools and agent workflows depend on backend services and external integrations.",
        "Backend services connect prompts, business logic, models, databases, and enterprise systems.",
        "Enterprise automation needs reliable request handling, validation, auth, retries, and logging.",
        "Prompt pipelines and AI workflows often use API-based integrations for retrieval, tool calls, and result storage.",
    ],
    learning_objectives=[
        "Understand backend and API fundamentals from scratch in interview-friendly language.",
        "Explain HTTP, JSON, status codes, REST, CRUD, auth, validation, and integrations clearly.",
        "Connect backend ideas to real AI Engineer workflows such as chatbots, RAG, and tool calling.",
        "Revise fast using flow diagrams, rapid-fire answers, and practical examples.",
    ],
    learn_sections=[
        {
            "title": "1. What is Backend",
            "summary": "Backend is the server-side part of an application. It handles logic, data processing, storage, authentication, and integrations that users usually do not see directly.",
            "points": [
                "Users usually interact with the frontend, but the backend does the real work behind the scenes.",
                "It processes user actions such as login, saving data, generating reports, or calling an AI model.",
                "Frontend is like the restaurant menu and table service. Backend is like the kitchen that prepares the result.",
                "Backend also protects secrets, enforces rules, and controls access to data.",
            ],
            "diagram": "Frontend -> Backend -> Database -> Backend -> Frontend",
            "callouts": [{"type": "info", "text": "Interview tip: say backend is the execution and control layer of the app, not just the database."}],
        },
        {
            "title": "2. What is an API",
            "summary": "API stands for Application Programming Interface. In simple words, it is a way for systems to communicate in a structured manner.",
            "points": [
                "A client sends a request and the server sends back a response.",
                "An API exposes data or functionality so another app or system can use it.",
                "Examples: a weather app calling a weather API, a login form calling a backend API, or an AI app calling a model API.",
            ],
            "diagram": "Client -> Request -> API Server -> Response",
        },
        {
            "title": "3. Client-Server Architecture",
            "summary": "Most modern apps use the client-server model. The client asks for something, and the server processes the request and returns a result.",
            "points": [
                "The client can be a browser, mobile app, frontend app, or another service.",
                "The server handles validation, logic, storage, and integrations.",
                "This separation makes systems easier to scale, update, secure, and maintain.",
            ],
            "tables": [
                {
                    "title": "Client vs server responsibilities",
                    "markdown": """| Side | Typical responsibilities |
|---|---|
| Client | UI, user input, rendering, sending requests |
| Server | validation, business logic, storage, auth, integrations |""",
                }
            ],
            "diagram": "Browser/App -> Internet -> Server -> Database",
        },
        {
            "title": "4. HTTP Basics",
            "summary": "HTTP is the protocol most commonly used for web communication between clients and servers.",
            "points": [
                "A request usually has a method, URL, headers, and sometimes a body.",
                "A response usually has a status code, headers, and a body.",
                "A URL is the full address. An endpoint is the specific API path that handles one operation.",
                "Headers carry metadata such as content type or authorization token.",
                "Query parameters are often used for filters such as `?page=2` and path parameters are values inside routes such as `/users/42`.",
            ],
            "diagram": "Client -> HTTP request -> API route -> processing -> HTTP response -> Client",
            "examples": [
                {
                    "label": "Request anatomy",
                    "code": """GET /users/42?include=projects
Headers:
  Authorization: Bearer <token>
  Content-Type: application/json""",
                    "language": "text",
                }
            ],
        },
        {
            "title": "5. HTTP Methods",
            "summary": "HTTP methods tell the backend what kind of action the client wants to perform.",
            "subtopics": [
                {"title": "GET", "content": ["Used to read data.", "Example: `GET /users`", "Interview line: GET usually fetches existing resource data."]},
                {"title": "POST", "content": ["Used to create data or trigger a server-side action.", "Example: `POST /users`", "Interview line: POST usually sends new data to the server."]},
                {"title": "PUT", "content": ["Commonly used for full updates.", "Example: `PUT /users/42`", "Interview line: PUT often replaces the existing representation."]},
                {"title": "PATCH", "content": ["Commonly used for partial updates.", "Example: `PATCH /users/42`", "Interview line: PATCH updates only part of the resource."]},
                {"title": "DELETE", "content": ["Used to remove a resource.", "Example: `DELETE /users/42`", "Interview line: DELETE requests resource removal."]},
            ],
            "tables": [
                {
                    "title": "Method comparison",
                    "markdown": """| Method | Common use | Example |
|---|---|---|
| GET | Read | `GET /tasks` |
| POST | Create | `POST /tasks` |
| PUT | Full update | `PUT /tasks/1` |
| PATCH | Partial update | `PATCH /tasks/1` |
| DELETE | Remove | `DELETE /tasks/1` |""",
                }
            ],
        },
        {
            "title": "6. JSON",
            "summary": "JSON is the most common data format used in APIs. It is lightweight, readable, and easy for systems to exchange.",
            "points": [
                "JSON stores data as key-value pairs.",
                "Request body JSON sends data from client to backend.",
                "Response body JSON sends data from backend to client.",
            ],
            "examples": [
                {
                    "label": "Request body JSON",
                    "code": """{
  "name": "Rushikesh",
  "role": "AI Engineer"
}""",
                    "language": "json",
                },
                {
                    "label": "Response body JSON",
                    "code": """{
  "id": 101,
  "name": "Rushikesh",
  "role": "AI Engineer",
  "status": "created"
}""",
                    "language": "json",
                },
            ],
        },
        {
            "title": "7. Status Codes",
            "summary": "Status codes are numeric signals in HTTP responses that tell the client what happened.",
            "subtopics": [
                {"title": "200 OK", "content": ["The request succeeded.", "Common for successful GET, PUT, or PATCH requests."]},
                {"title": "201 Created", "content": ["A new resource was created successfully.", "Common after successful POST create operations."]},
                {"title": "400 Bad Request", "content": ["The request format or input is invalid.", "Example: required field missing."]},
                {"title": "401 Unauthorized", "content": ["The client is not authenticated properly.", "Example: missing or invalid token."]},
                {"title": "403 Forbidden", "content": ["The client is authenticated but not allowed to do this action.", "Example: regular user trying admin action."]},
                {"title": "404 Not Found", "content": ["The requested route or resource does not exist.", "Example: `GET /users/9999` when that user is missing."]},
                {"title": "500 Internal Server Error", "content": ["Something failed on the server side.", "Example: unexpected exception or broken dependency."]},
            ],
            "tables": [
                {
                    "title": "Status code cheat sheet",
                    "markdown": """| Code | Meaning | Easy memory |
|---|---|---|
| 200 | OK | Request worked |
| 201 | Created | New thing created |
| 400 | Bad Request | Input is wrong |
| 401 | Unauthorized | Not logged in correctly |
| 403 | Forbidden | Logged in, but not allowed |
| 404 | Not Found | Route or item missing |
| 500 | Internal Server Error | Server failed |""",
                }
            ],
        },
        {
            "title": "8. Endpoint Design Basics",
            "summary": "An endpoint is a specific route in an API. Clean endpoints make systems easier to understand, maintain, and scale.",
            "points": [
                "Good endpoint names are resource-oriented, such as `/users`, `/projects`, or `/tasks`.",
                "Versioning is often added like `/api/v1/users` so APIs can evolve safely.",
                "Clean APIs are easier for frontend developers, testers, and other teams to use.",
            ],
            "examples": [{"label": "Good endpoint examples", "code": "GET /users\nGET /users/123\nPOST /projects\nDELETE /tasks/9", "language": "text"}],
        },
        {
            "title": "9. Request and Response Lifecycle",
            "summary": "When a frontend or app calls the backend, several steps happen before the final response is returned.",
            "points": [
                "Client sends the request.",
                "Backend route receives it and validates the input.",
                "Business logic decides what should happen.",
                "Backend may query a database or call another API.",
                "Response is built and returned to the client.",
            ],
            "diagram": "Client -> API Route -> Validation -> Business Logic -> DB/API Call -> Response Builder -> Client",
        },
        {
            "title": "10. CRUD Operations",
            "summary": "CRUD stands for Create, Read, Update, Delete. These are the most common data operations in backend systems.",
            "tables": [
                {
                    "title": "CRUD with tasks resource",
                    "markdown": """| Operation | Meaning | HTTP method | Example endpoint |
|---|---|---|---|
| Create | Add new task | POST | `/tasks` |
| Read | Get tasks | GET | `/tasks` or `/tasks/1` |
| Update | Change task | PUT/PATCH | `/tasks/1` |
| Delete | Remove task | DELETE | `/tasks/1` |""",
                }
            ],
            "diagram": "Create -> POST /tasks\nRead -> GET /tasks\nUpdate -> PATCH /tasks/1\nDelete -> DELETE /tasks/1",
        },
        {
            "title": "11. Authentication and Authorization",
            "summary": "Authentication means who are you. Authorization means what are you allowed to do.",
            "points": [
                "Authentication checks identity, such as login credentials or token validation.",
                "Authorization checks permissions, such as whether the user can access admin data.",
                "Sessions store server-side login state. Token-based auth often sends a token like JWT with requests.",
                "API keys are another simple access method, often used for service-to-service calls.",
                "401 means the user is not authenticated properly. 403 means the user is authenticated but not permitted.",
            ],
            "diagram": "User Login -> Backend verifies -> Token generated -> Client stores token -> Future requests include token",
        },
        {
            "title": "12. Database Interaction from Backend",
            "summary": "Backends usually read and write data through queries or ORM tools. The backend acts as a controlled layer in front of the database.",
            "points": [
                "SQL databases are common for structured relational data and NoSQL databases are common for flexible document-style data depending on the use case.",
                "The backend should validate input before writing to the database.",
                "It should enforce business rules, not let the client directly control the database.",
            ],
            "diagram": "Client -> Backend -> Query/ORM -> Database -> Backend -> Client",
        },
        {
            "title": "13. External API Integrations",
            "summary": "A backend often needs to talk to third-party services such as payment, email, calendar, weather, or AI model APIs.",
            "points": [
                "The backend is the right place to store secrets and call third-party services securely.",
                "It can add retries, timeout handling, validation, and error logging.",
                "This keeps the frontend simpler and safer.",
            ],
            "examples": [{"label": "Common external APIs", "code": "Payment API\nEmail API\nWeather API\nAI model API\nCalendar API", "language": "text"}],
            "diagram": "Client -> Backend -> External API -> Backend -> Client",
        },
        {
            "title": "14. Error Handling in Backend",
            "summary": "Good backend systems do not just work on success cases. They also fail gracefully and safely.",
            "points": [
                "Validation errors happen when input is missing or malformed.",
                "Auth errors happen when the user is not logged in or lacks permission.",
                "Database errors happen when storage operations fail.",
                "Timeout errors and external API failures happen when dependencies are slow or unavailable.",
                "A good backend logs useful details internally but avoids exposing sensitive internals to users.",
            ],
            "diagram": "Request -> Validation/Auth/Dependency checks -> handled error or success -> safe response",
        },
        {
            "title": "15. Backend Frameworks",
            "summary": "Frameworks help developers build backend systems faster by providing routing, validation, middleware, and structure.",
            "subtopics": [
                {"title": "Express.js", "content": ["Popular Node.js backend framework.", "Lightweight and common for building REST APIs."]},
                {"title": "FastAPI", "content": ["Popular Python framework for APIs.", "Very useful for AI apps because Python is common in AI workflows."]},
                {"title": "Flask / Django", "content": ["Flask is lightweight and flexible.", "Django is more full-featured with many built-in tools."]},
            ],
        },
        {
            "title": "16. APIs and Backend for AI Applications",
            "summary": "AI apps need backend systems to manage prompts, model calls, retrieval, tools, validation, and output formatting.",
            "points": [
                "Frontend sends the prompt or user query to the backend.",
                "Backend can construct the final prompt, add user context, or retrieve supporting documents.",
                "Backend calls model inference APIs or internal model services.",
                "It may run tool calls, business rules, post-processing, and logging before returning the response.",
            ],
            "diagram": "User Query -> Frontend -> Backend -> Retrieval/API/Model -> Post-processing -> Response",
        },
    ],
    rest_sections=[
        {
            "title": "1. What is REST",
            "summary": "REST stands for Representational State Transfer. In practice, it means building APIs around resources and standard HTTP behavior.",
            "points": [
                "REST is a design style, not a strict protocol.",
                "It commonly uses resource-based URLs like `/tasks`, `/users`, or `/orders`.",
                "REST is popular because it is simple, understandable, and works well with HTTP.",
            ],
            "diagram": "Client -> REST endpoint -> Resource action -> JSON response",
        },
        {
            "title": "2. REST Principles",
            "summary": "These are the core beginner-friendly principles interviewers expect you to know.",
            "points": [
                "Client-server separation",
                "Stateless requests",
                "Resource-based endpoints",
                "Standard HTTP methods",
            ],
            "table": """| Principle | Simple meaning |
|---|---|
| Client-server separation | UI and backend logic are separate |
| Statelessness | Each request should contain what is needed |
| Resource-based design | URLs represent resources like users or tasks |
| HTTP standards | Methods like GET, POST, PUT, PATCH, DELETE are used consistently |""",
        },
        {
            "title": "3. REST Example with a Resource",
            "summary": "Using one resource such as `tasks` makes REST and CRUD easier to understand and explain.",
            "examples": [
                {"label": "GET /tasks", "code": "Purpose: get all tasks\nResponse: [{\"id\": 1, \"title\": \"Prepare notes\"}]", "language": "text"},
                {"label": "GET /tasks/1", "code": "Purpose: get one task\nResponse: {\"id\": 1, \"title\": \"Prepare notes\"}", "language": "text"},
                {"label": "POST /tasks", "code": "Purpose: create task\nRequest: {\"title\": \"Practice APIs\"}\nResponse: {\"id\": 2, \"title\": \"Practice APIs\"}", "language": "text"},
                {"label": "PUT /tasks/1", "code": "Purpose: full update\nRequest: {\"title\": \"Updated title\"}", "language": "text"},
                {"label": "DELETE /tasks/1", "code": "Purpose: delete task\nResponse: 204 No Content", "language": "text"},
            ],
        },
        {
            "title": "4. CRUD Visual Flow",
            "summary": "CRUD is easier to remember when you map each operation to the resource lifecycle.",
            "diagram": "Client -> POST /tasks -> create\nClient -> GET /tasks -> read\nClient -> PATCH /tasks/1 -> update\nClient -> DELETE /tasks/1 -> delete",
            "points": [
                "Create adds a new resource.",
                "Read fetches one or more resources.",
                "Update changes an existing resource.",
                "Delete removes a resource.",
            ],
        },
        {
            "title": "5. REST vs Action-Heavy Endpoint Design",
            "summary": "Resource-oriented naming is usually cleaner than action-heavy route names.",
            "table": """| Better REST-style | Less ideal action-heavy style |
|---|---|
| `POST /orders` | `/createOrderNow` |
| `GET /tasks/1` | `/fetchTaskById` |
| `DELETE /users/7` | `/removeUserNow` |""",
            "points": [
                "REST-style endpoints are easier to predict and document.",
                "The HTTP method already tells you the action, so the path can focus on the resource.",
            ],
        },
        {
            "title": "6. Idempotency Basics",
            "summary": "Idempotency means repeating the same request produces the same effect after the first successful application.",
            "points": [
                "GET is generally safe for reading and should not change server state.",
                "PUT is often idempotent because sending the same update again should leave the resource in the same state.",
                "POST is usually not idempotent because repeating it may create multiple items.",
            ],
            "diagram": "Repeat same PUT -> same final state\nRepeat same POST -> may create multiple records",
        },
    ],
    ai_integration_examples=[
        {
            "title": "1. Chatbot Backend Flow",
            "business_purpose": "Power a chatbot or help assistant through a secure backend instead of calling the model directly from the frontend.",
            "diagram": "User Message -> Backend -> Prompt Builder -> LLM API -> Response Cleanup -> Client",
            "backend_responsibilities": [
                "Receive the user message and session context.",
                "Add system instructions or prompt templates.",
                "Call the model API securely.",
                "Clean or format the output before returning it.",
                "Log the interaction if needed.",
            ],
            "apis_involved": "Model API, optional moderation API, optional conversation store API.",
            "risks": "Prompt injection, latency, hallucination, and leaking secrets if the model is called directly from the frontend.",
            "why_backend_matters": "The backend keeps model keys private and controls validation, prompting, safety, and logging.",
        },
        {
            "title": "2. RAG-style Backend Flow",
            "business_purpose": "Answer user questions using trusted documents instead of relying only on model memory.",
            "diagram": "User Query -> Backend -> Embed/Retrieve -> Context + Prompt -> LLM -> Answer",
            "backend_responsibilities": [
                "Receive the question.",
                "Run retrieval against a vector store or search layer.",
                "Build a grounded prompt using the retrieved context.",
                "Call the model and return the final answer.",
            ],
            "apis_involved": "Embedding API, vector database or search API, model inference API.",
            "risks": "Poor retrieval quality, outdated documents, token overload, and hallucination if irrelevant context is sent.",
            "why_backend_matters": "The backend orchestrates retrieval, prompt assembly, model calling, and response formatting.",
        },
        {
            "title": "3. Meeting Scheduler Backend Flow",
            "business_purpose": "Turn a natural language scheduling request into calendar-aware actions.",
            "diagram": "User Request -> Backend -> Calendar API -> Conflict Check -> Slot Suggestion -> Response",
            "backend_responsibilities": [
                "Understand the scheduling request.",
                "Check calendar availability.",
                "Apply business rules such as meeting hours or timezone handling.",
                "Suggest or create a slot.",
            ],
            "apis_involved": "Calendar API, user directory API, optional notification API.",
            "risks": "Wrong timezone, double booking, permission issues, and poor handling of ambiguous user requests.",
            "why_backend_matters": "Scheduling needs validation, auth, tool calls, and business logic that should not live in the frontend.",
        },
        {
            "title": "4. Document Analysis Backend Flow",
            "business_purpose": "Process uploaded documents and return summaries, extracted fields, or structured insights.",
            "diagram": "Upload File -> Backend -> Parse Text -> Model/Rules -> Summary -> Store Result -> Return Output",
            "backend_responsibilities": [
                "Handle upload and file validation.",
                "Extract or parse text from the document.",
                "Call AI or rule-based extraction logic.",
                "Store results and return a clean response.",
            ],
            "apis_involved": "File storage API, OCR or parsing service, model API, database.",
            "risks": "Large files, parsing failures, privacy concerns, and poor extraction quality.",
            "why_backend_matters": "The backend manages files safely, coordinates processing, and stores outputs reliably.",
        },
        {
            "title": "5. Agent Tool-Calling Backend Flow",
            "business_purpose": "Support an agent workflow that can use tools, APIs, and business rules to complete a task.",
            "diagram": "User Goal -> Agent Backend -> Tool/API Calls -> Intermediate Results -> Final Output",
            "backend_responsibilities": [
                "Manage the agent loop and available tools.",
                "Validate tool inputs and outputs.",
                "Control retries, step limits, and safety checks.",
                "Format the final answer for the user.",
            ],
            "apis_involved": "Model API, search API, calendar API, database, internal enterprise APIs.",
            "risks": "Wrong tool choice, excessive latency, loops, hallucinated tool arguments, and security risks.",
            "why_backend_matters": "Agentic AI depends on orchestration, guarded tool access, logging, and validation that belong in the backend.",
        },
    ],
    interview_questions_detailed=[
        {"question": "What is backend?", "short_answer": "Backend is the server-side part of an application that handles logic, data, auth, and integrations.", "spoken_answer": "Backend is the part of the system that runs behind the scenes. It receives requests, validates them, applies business logic, talks to databases or external services, and returns responses to the client."},
        {"question": "What is an API?", "short_answer": "An API is a structured way for systems to communicate using requests and responses.", "spoken_answer": "An API exposes data or functionality so another app or service can use it. In practical terms, a client sends a request and the server sends back a response."},
        {"question": "What is the difference between frontend and backend?", "short_answer": "Frontend handles the user-facing interface, while backend handles logic, storage, auth, and integrations.", "spoken_answer": "Frontend is what the user sees and interacts with, such as pages, buttons, or forms. Backend is the server-side layer that processes requests, stores data, enforces rules, and connects to other services."},
        {"question": "What is client-server architecture?", "short_answer": "It is a model where the client sends requests and the server processes them and returns responses.", "spoken_answer": "In client-server architecture, the client is usually the browser, app, or another service, and the server handles logic and data access. This separation makes systems easier to manage and scale."},
        {"question": "What is HTTP?", "short_answer": "HTTP is the common web protocol used for communication between clients and servers.", "spoken_answer": "HTTP is the protocol used for many web requests and responses. It defines how clients send methods, headers, and bodies, and how servers return status codes and content."},
        {"question": "What is a REST API?", "short_answer": "A REST API is an API design style that uses resources, HTTP methods, and stateless requests.", "spoken_answer": "REST is a practical way of designing APIs around resources like users or tasks. It usually uses standard HTTP methods such as GET, POST, PUT, PATCH, and DELETE and treats requests as stateless."},
        {"question": "Difference between GET and POST?", "short_answer": "GET usually reads data, while POST usually creates data or sends input for processing.", "spoken_answer": "GET is mainly used to fetch resource data without changing it. POST is commonly used to create new resources or send input to the server for an action."},
        {"question": "Difference between PUT and PATCH?", "short_answer": "PUT is commonly used for full updates, while PATCH is commonly used for partial updates.", "spoken_answer": "A beginner-friendly explanation is that PUT often replaces the resource representation, while PATCH changes only selected fields."},
        {"question": "What is JSON?", "short_answer": "JSON is a lightweight key-value data format commonly used in APIs.", "spoken_answer": "JSON is a simple text-based format for exchanging structured data. It is popular in APIs because it is readable and easy for systems to parse."},
        {"question": "What is an endpoint?", "short_answer": "An endpoint is a specific API route or URL where a request can be sent.", "spoken_answer": "An endpoint is the address for a specific API operation, such as `GET /users` or `POST /tasks`. It represents where the backend expects a request for one type of work."},
        {"question": "What is CRUD?", "short_answer": "CRUD stands for Create, Read, Update, Delete.", "spoken_answer": "CRUD is a simple way to describe the most common data actions in applications. These actions often map to HTTP methods such as POST, GET, PUT or PATCH, and DELETE."},
        {"question": "What is a status code?", "short_answer": "A status code is a numeric HTTP response code that tells the client what happened.", "spoken_answer": "Status codes help the client understand whether a request succeeded, failed due to client input, failed due to permissions, or failed because of a server-side issue."},
        {"question": "Difference between 401 and 403?", "short_answer": "401 means unauthenticated, while 403 means authenticated but not allowed.", "spoken_answer": "A 401 usually means the user has not provided valid authentication yet, such as a missing or invalid token. A 403 means identity is known but permission is not sufficient for that action."},
        {"question": "What is authentication?", "short_answer": "Authentication is verifying who the user is.", "spoken_answer": "Authentication checks identity. For example, the backend verifies credentials or validates a token to confirm who is making the request."},
        {"question": "What is authorization?", "short_answer": "Authorization is checking what an authenticated user is allowed to do.", "spoken_answer": "After identity is verified, authorization decides whether that user has permission to access the requested resource or action."},
        {"question": "What is JWT at a high level?", "short_answer": "JWT is a token format often used in stateless authentication.", "spoken_answer": "At a high level, JWT is a token the backend can issue after login. The client sends it with later requests, and the backend validates it to identify the user."},
        {"question": "Why do we use APIs?", "short_answer": "APIs let systems communicate in a structured and reusable way.", "spoken_answer": "Modern software systems are made of many parts such as frontends, backends, model services, databases, and third-party tools. APIs provide the standard way for those parts to communicate."},
        {"question": "How does a request-response cycle work?", "short_answer": "The client sends a request, the backend processes it, and then sends a response.", "spoken_answer": "A typical flow is client request to API route, validation, business logic, DB or service calls, response building, and final response back to the client."},
        {"question": "What happens when frontend calls backend?", "short_answer": "The frontend sends a request, the backend validates and processes it, and then returns a response.", "spoken_answer": "The frontend usually sends an HTTP request. The backend receives it, checks it, runs business logic, talks to storage or services if needed, and then returns a response the frontend can display."},
        {"question": "Why should secrets not be stored in frontend?", "short_answer": "Because frontend code is exposed to users, so secrets can be leaked.", "spoken_answer": "Secrets like API keys should stay on the backend because frontend code can be inspected by users. The backend acts as the secure layer for calling external services safely."},
        {"question": "How does backend interact with database?", "short_answer": "The backend reads and writes data through queries or an ORM, usually after validation.", "spoken_answer": "The backend acts as a controlled layer in front of the database. It validates input, applies business rules, and then reads or writes data using queries or ORM tools."},
        {"question": "Why do AI applications need backend APIs?", "short_answer": "AI apps need backend APIs to call models, tools, retrieval systems, and enterprise services safely.", "spoken_answer": "Most AI apps should not directly call everything from the frontend. The backend manages prompt building, retrieval, auth, model calls, secrets, post-processing, and logging."},
        {"question": "What is an external API integration?", "short_answer": "It is when your backend communicates with a third-party service such as payment, email, or model APIs.", "spoken_answer": "External API integration means your backend sends requests to another service outside your own system. This is common for payments, notifications, weather, calendars, and AI model providers."},
        {"question": "How would you design a simple API for tasks?", "short_answer": "Use resource-based endpoints like `GET /tasks`, `GET /tasks/1`, `POST /tasks`, `PATCH /tasks/1`, and `DELETE /tasks/1`.", "spoken_answer": "I would design it around a `tasks` resource. The API would support listing tasks, reading one task, creating tasks, updating tasks, and deleting tasks. I would return JSON and meaningful status codes."},
        {"question": "What happens if an external API fails?", "short_answer": "The backend should handle the failure gracefully, log it, and return a meaningful response.", "spoken_answer": "If an external API fails, the backend should avoid crashing, log the issue, retry when appropriate, and return a safe fallback or error message to the client."},
        {"question": "How do you handle backend errors?", "short_answer": "Validate input, catch expected failures, log errors, and return meaningful but safe responses.", "spoken_answer": "Good backend error handling means identifying validation issues early, handling expected failures carefully, logging what happened for debugging, and avoiding exposure of sensitive internal details."},
        {"question": "Why is validation important?", "short_answer": "Validation protects the backend from bad input and improves data quality and security.", "spoken_answer": "The backend should never blindly trust client input. Validation helps prevent malformed requests, bad data writes, and some security or integrity issues."},
        {"question": "What is statelessness in REST?", "short_answer": "Statelessness means each request carries the information needed for that request instead of relying on hidden server-side conversation state.", "spoken_answer": "At a beginner level, statelessness means the server should be able to understand each request on its own. It should not depend on unseen past request details to know what to do."},
        {"question": "What is idempotency?", "short_answer": "Idempotency means repeating the same request produces the same effect after the first successful application.", "spoken_answer": "A simple explanation is that if you send the same request again, it should not keep causing a new state change each time. PUT is often idempotent, while POST usually is not."},
        {"question": "Explain backend role in an AI chatbot.", "short_answer": "The backend receives user input, builds the model request, calls APIs or retrieval, post-processes output, and returns the response.", "spoken_answer": "In an AI chatbot, the backend is the orchestration layer. It receives the message, manages prompt or context building, calls the model API, may run retrieval or tools, post-processes the answer, logs the interaction, and returns the final response."},
    ],
    interview_scenarios=[
        {
            "question": "Explain how frontend, backend, and database work together.",
            "approach": "Start with the user action, then walk through request, processing, storage, and response.",
            "answer_points": [
                "The user interacts with the frontend, such as a form or button.",
                "The frontend sends a request to the backend.",
                "The backend validates the input and applies business logic.",
                "If needed, the backend reads or writes data in the database.",
                "The backend builds a response and sends it back to the frontend.",
                "The frontend then displays the result to the user.",
            ],
            "diagram": "User -> Frontend -> Backend -> Database -> Backend -> Frontend",
        },
        {
            "question": "Design a simple notes/tasks API.",
            "approach": "Explain the resource, the main CRUD endpoints, JSON responses, and status codes.",
            "answer_points": [
                "Choose a resource like `tasks` or `notes`.",
                "Use `GET /tasks` to list tasks and `GET /tasks/{id}` to fetch one task.",
                "Use `POST /tasks` to create a task with a JSON body.",
                "Use `PATCH /tasks/{id}` or `PUT /tasks/{id}` to update a task.",
                "Use `DELETE /tasks/{id}` to remove a task.",
                "Return JSON responses and meaningful status codes like 200, 201, 400, and 404.",
            ],
            "diagram": "GET /tasks -> list\nGET /tasks/1 -> one\nPOST /tasks -> create\nPATCH /tasks/1 -> update\nDELETE /tasks/1 -> remove",
        },
        {
            "question": "How does an AI app use backend and APIs?",
            "approach": "Explain that the backend is the orchestration layer around model calls and enterprise logic.",
            "answer_points": [
                "The frontend sends the user prompt or query to the backend.",
                "The backend may validate input and add prompt instructions.",
                "It may retrieve context from documents or call tools.",
                "The backend calls the model API.",
                "It post-processes the answer, logs the result, and returns it to the frontend.",
            ],
            "diagram": "User Query -> Frontend -> Backend -> Retrieval / Model API / Tools -> Post-processing -> Response",
        },
        {
            "question": "How would you integrate a third-party API?",
            "approach": "Show security, validation, request handling, error handling, and retries.",
            "answer_points": [
                "Store the API key securely on the backend, not in the frontend.",
                "Validate input before sending it to the third-party service.",
                "Call the external API from the backend.",
                "Handle timeouts, failures, retries, and bad responses carefully.",
                "Log useful details internally and return a safe response to the client.",
            ],
            "diagram": "Client -> Backend -> External API -> Backend formatting and validation -> Client",
        },
    ],
    interview_rapid_fire=[
        {"question": "Backend means?", "answer": "Server-side logic, storage, auth, and integrations."},
        {"question": "API means?", "answer": "A communication interface between systems."},
        {"question": "HTTP means?", "answer": "A common protocol for web communication."},
        {"question": "GET does?", "answer": "Reads data."},
        {"question": "POST does?", "answer": "Creates data or triggers a server-side action."},
        {"question": "JSON is?", "answer": "A lightweight key-value data format."},
        {"question": "401 means?", "answer": "Unauthenticated."},
        {"question": "403 means?", "answer": "Authenticated but not allowed."},
        {"question": "CRUD stands for?", "answer": "Create, Read, Update, Delete."},
        {"question": "REST means?", "answer": "Resource-based API design over HTTP."},
    ],
    interview_common_mistakes=[
        "Confusing API with database or backend framework.",
        "Giving a weak explanation of request and response.",
        "Not knowing common status codes clearly.",
        "Mixing up GET and POST or PUT and PATCH.",
        "Explaining authentication and authorization unclearly.",
        "Failing to connect backend concepts to real AI project workflows.",
    ],
    quick_revision_points=[
        "Backend handles server-side logic and integrations.",
        "Frontend collects input and displays output; backend processes the work.",
        "API is a communication interface between systems.",
        "Client-server architecture separates UI from logic and data access.",
        "HTTP is the common protocol for web communication.",
        "A request can include method, URL, headers, and body.",
        "A response can include status code, headers, and body.",
        "GET usually reads data.",
        "POST usually creates data or sends input for processing.",
        "PUT often means full update.",
        "PATCH often means partial update.",
        "DELETE removes data.",
        "JSON is the most common API data format.",
        "An endpoint is a specific API path.",
        "Query parameters are often used for filtering and paging.",
        "Path parameters identify a specific resource like `/users/42`.",
        "CRUD means Create, Read, Update, Delete.",
        "Create maps to POST.",
        "Read maps to GET.",
        "Update maps to PUT or PATCH.",
        "Delete maps to DELETE.",
        "200 means OK.",
        "201 means Created.",
        "400 means Bad Request.",
        "401 means the user is not authenticated correctly.",
        "403 means the user is authenticated but not allowed.",
        "404 means route or resource not found.",
        "500 means server-side failure.",
        "Authentication means who are you; authorization means what are you allowed to do.",
        "AI apps use backend APIs to call models, tools, retrieval systems, and enterprise services safely.",
    ],
    quiz_questions=[
        _q("What is backend mainly responsible for?", ["Only colors and UI", "Server-side logic, storage, auth, and integrations", "Only internet cables", "Only CSS rendering"], 1, "Backend usually handles business logic, storage, auth, and integrations."),
        _q("Which HTTP method is most commonly used to read data?", ["POST", "GET", "DELETE", "PATCH"], 1, "GET is commonly used for reading or fetching resource data."),
        _q("What is JSON?", ["A frontend framework", "A lightweight key-value data format", "A database engine", "An auth token"], 1, "JSON is a lightweight data format commonly used in APIs."),
        _q("What does 404 usually mean?", ["Created", "Not Found", "Unauthorized", "Server crash only"], 1, "404 means the requested resource or route was not found."),
        _q("What does CRUD stand for?", ["Create, Read, Update, Delete", "Connect, Run, Upload, Deploy", "Create, Remove, Upload, Debug", "Copy, Render, Use, Design"], 0, "CRUD stands for Create, Read, Update, Delete."),
        _q("What is the main difference between 401 and 403?", ["401 is for bad JSON and 403 is for DB failure", "401 means unauthenticated and 403 means authenticated but not allowed", "401 means created and 403 means deleted", "There is no difference"], 1, "401 is about identity not being established correctly, while 403 is about permission."),
        _q("Why should secrets stay on the backend?", ["Because frontend is too fast", "Because frontend code is exposed to users", "Because backend has no logs", "Because APIs only work on servers"], 1, "Frontend code can be inspected, so secrets should stay on the backend."),
        _q("Why do AI apps often need a backend?", ["Only to change button colors", "To securely call model APIs, tools, and external services", "To remove HTTP", "To avoid all databases"], 1, "AI apps often rely on backend orchestration for models, tools, retrieval, auth, and logging."),
    ],
    resources=[
        _r("MDN HTTP Overview", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview", "article", "must_read", "Beginner-friendly HTTP explanation."),
        _r("RESTful API Tutorial", "https://restfulapi.net/", "article", "must_read", "Useful REST reference."),
        _r("FastAPI Docs", "https://fastapi.tiangolo.com/", "article", "must_read", "Python backend and API concepts."),
        _r("Postman Learning Center", "https://learning.postman.com/", "article", "practice", "Helpful for API testing practice."),
    ],
    resource_sections={
        "Must watch first": [
            _r("freeCodeCamp REST API Videos", "https://www.youtube.com/@freecodecamp/search?query=REST%20API", "video", "must_watch", "Beginner-friendly long-form API explainers."),
            _r("freeCodeCamp Backend Videos", "https://www.youtube.com/@freecodecamp/search?query=backend", "video", "must_watch", "Useful backend fundamentals videos."),
            _r("FastAPI Intro Videos", "https://www.youtube.com/results?search_query=FastAPI+beginner", "video", "must_watch", "Good practical introduction for Python backend thinking."),
            _r("IBM Technology API Videos", "https://www.youtube.com/@IBMTechnology/search?query=api", "video", "must_watch", "Short conceptual explainers on backend and APIs."),
        ],
        "Must read first": [
            _r("MDN HTTP Overview", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview", "article", "must_read", "Great beginner-friendly HTTP explanation."),
            _r("RESTful API Tutorial", "https://restfulapi.net/", "article", "must_read", "Simple reference for REST concepts and status codes."),
            _r("FastAPI Docs", "https://fastapi.tiangolo.com/", "article", "must_read", "Useful for Python backend and API ideas."),
            _r("Express Docs", "https://expressjs.com/", "article", "must_read", "Good reference for backend and routing ideas in JavaScript."),
            _r("JSON Introduction", "https://www.json.org/json-en.html", "article", "must_read", "Simple explanation of the JSON format."),
        ],
        "Practice / explore": [
            _r("Postman Learning Center", "https://learning.postman.com/", "article", "practice", "Good for learning how requests and APIs are tested."),
            _r("ReqRes API", "https://reqres.in/", "article", "practice", "Useful simple API for practicing requests and responses."),
            _r("HTTP Status Dogs", "https://httpstatusdogs.com/", "article", "practice", "Fun way to remember common status codes."),
            _r("Hoppscotch", "https://hoppscotch.io/", "article", "practice", "Lightweight tool for trying APIs quickly."),
        ],
        "Optional deep dive": [
            _r("MDN HTTP Messages", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages", "article", "optional_deep_dive", "Detailed request and response message structure."),
            _r("FastAPI Path Params", "https://fastapi.tiangolo.com/tutorial/path-params/", "article", "optional_deep_dive", "Concrete examples of endpoints and params."),
            _r("Express Routing Guide", "https://expressjs.com/en/guide/routing.html", "article", "optional_deep_dive", "Good for understanding route handling."),
            _r("Postman API Fundamentals Student Expert", "https://academy.postman.com/path/postman-api-fundamentals-student-expert", "article", "optional_deep_dive", "Nice guided practice path for API thinking."),
        ],
    },
    flow_diagrams=[
        {"title": "Intro flow", "diagram": "User/App -> Backend/API -> Business Logic -> Database/Model/External Service -> Response"},
        {"title": "REST flow", "diagram": "Client -> HTTP Method + Endpoint -> Backend -> Resource action -> JSON response"},
        {"title": "AI app flow", "diagram": "User Query -> Frontend -> Backend -> Retrieval/API/Model -> Post-processing -> Response"},
    ],
)
