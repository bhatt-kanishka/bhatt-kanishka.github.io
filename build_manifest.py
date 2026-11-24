import os
import json

backend_dir = r'd:\Desktop\Backend_Development'
io_dir = r'd:\Desktop\bhatt-kanishka.github.io'

student_data = {
    'name': 'Kanishka Bhatt',
    'sapId': '590017366',
    'institute': 'University of Petroleum and Energy Studies (UPES)',
    'semester': '5th',
    'subject': 'Backend Development'
}

repo_info = {
    'name': 'EndpointCraft',
    'repoOwner': 'bhatt-kanishka',
    'repoName': 'Backend_Development',
    'githubUrl': 'https://github.com/bhatt-kanishka/Backend_Development',
    'pagesUrl': 'https://bhatt-kanishka.github.io/'
}

labs = [
    {
        'id': 'experiment-1',
        'title': 'Experiment 1: Semantic HTML5 Elements & Web Forms',
        'shortTitle': 'HTML5 Elements',
        'description': 'Semantic page structure, interactive forms, multimedia, canvas rendering.',
        'icon': '🌐',
        'path': 'Lab',
        'readme': 'Lab/Experiment_1_Readme.md',
        'tree': 'Lab/\n├── Experiment-1.html\n└── Experiment_1_Readme.md',
        'files': [
            {'name': 'Experiment-1.html', 'path': 'Lab/Experiment-1.html', 'lang': 'html'}
        ],
        'concepts': ['Semantic HTML5', 'Forms & Validation', 'Canvas 2D', 'Audio/Video', 'Tables'],
        'dependencies': ['None — pure HTML/CSS'],
        'runCommand': 'Open Experiment-1.html in any browser',
        'port': 'Browser'
    },
    {
        'id': 'lab-7-8',
        'title': 'Lab 7 & 8: ES6 To-Do Application',
        'shortTitle': 'ES6 To-Do App',
        'description': 'Client-side To-Do app demonstrating ES6 classes, spread operator, arrow functions, and event delegation.',
        'icon': '✅',
        'path': 'Lab/Lab_7_8',
        'readme': 'Lab/Lab_7_8/Readme.md',
        'tree': 'Lab/Lab_7_8/\n├── app.js\n├── index.html\n└── Readme.md',
        'files': [
            {'name': 'app.js', 'path': 'Lab/Lab_7_8/app.js', 'lang': 'javascript'},
            {'name': 'index.html', 'path': 'Lab/Lab_7_8/index.html', 'lang': 'html'}
        ],
        'concepts': ['ES6 Classes', 'Spread Operator', 'Arrow Functions', 'Event Delegation', 'DOM Manipulation'],
        'dependencies': ['None — pure HTML/JS'],
        'runCommand': 'Open index.html in browser',
        'port': 'Browser'
    },
    {
        'id': 'experiment-12a',
        'title': 'Experiment 12A: Express REST API & EJS SSR',
        'shortTitle': 'Express + EJS',
        'description': 'Express.js REST API with route params, query parsing, body handling, and EJS server-side rendering.',
        'icon': '🚀',
        'path': 'Lab/Experiment_12A',
        'readme': 'Lab/Experiment_12A/Readme.md',
        'tree': 'Lab/Experiment_12A/\n├── Readme.md\n└── nodejs-express-lab/\n    ├── app.js\n    ├── package.json\n    ├── script.js\n    └── views/\n        ├── home.ejs\n        ├── profile.ejs\n        └── users.ejs',
        'files': [
            {'name': 'app.js', 'path': 'Lab/Experiment_12A/nodejs-express-lab/app.js', 'lang': 'javascript'},
            {'name': 'script.js', 'path': 'Lab/Experiment_12A/nodejs-express-lab/script.js', 'lang': 'javascript'},
            {'name': 'package.json', 'path': 'Lab/Experiment_12A/nodejs-express-lab/package.json', 'lang': 'json'},
            {'name': 'home.ejs', 'path': 'Lab/Experiment_12A/nodejs-express-lab/views/home.ejs', 'lang': 'html'},
            {'name': 'users.ejs', 'path': 'Lab/Experiment_12A/nodejs-express-lab/views/users.ejs', 'lang': 'html'},
            {'name': 'profile.ejs', 'path': 'Lab/Experiment_12A/nodejs-express-lab/views/profile.ejs', 'lang': 'html'}
        ],
        'concepts': ['Express.js', 'REST API', 'Route Parameters', 'Query Strings', 'EJS Templating', 'Middleware'],
        'dependencies': ['express', 'ejs'],
        'runCommand': 'cd Lab/Experiment_12A/nodejs-express-lab && npm install && node app.js',
        'port': '3000'
    },
    {
        'id': 'experiment-12b',
        'title': 'Experiment 12B: State Management — Cookies & Sessions',
        'shortTitle': 'Cookies & Sessions',
        'description': 'HTTP state preservation using client-side cookies (cookie-parser) and server-side sessions (express-session).',
        'icon': '🍪',
        'path': 'Lab/Experiment12_B',
        'readme': 'Lab/Experiment12_B/Readme.md',
        'tree': 'Lab/Experiment12_B/\n├── Cookies_example.js\n├── session_example.js\n└── Readme.md',
        'files': [
            {'name': 'Cookies_example.js', 'path': 'Lab/Experiment12_B/Cookies_example.js', 'lang': 'javascript'},
            {'name': 'session_example.js', 'path': 'Lab/Experiment12_B/session_example.js', 'lang': 'javascript'}
        ],
        'concepts': ['Cookies', 'Sessions', 'cookie-parser', 'express-session', 'Stateless HTTP'],
        'dependencies': ['express', 'cookie-parser', 'express-session'],
        'runCommand': 'node Cookies_example.js  OR  node session_example.js',
        'port': '3000'
    },
    {
        'id': 'lecture-15-django',
        'title': 'Lecture 15 Lab: Django To-Do Application',
        'shortTitle': 'Django To-Do',
        'description': 'Full-stack Django To-Do app with ORM, function-based views, templates, and external API integration.',
        'icon': '🐍',
        'path': 'Lab/Lecture 15',
        'readme': 'Lab/Lecture 15/README.md',
        'tree': 'Lab/Lecture 15/\n├── manage.py\n├── pyproject.toml\n├── README.md\n├── todo/\n│   ├── models.py\n│   ├── views.py\n│   ├── urls.py\n│   └── utils.py\n└── todo_project/\n    └── settings.py',
        'files': [
            {'name': 'models.py', 'path': 'Lab/Lecture 15/todo/models.py', 'lang': 'python'},
            {'name': 'views.py', 'path': 'Lab/Lecture 15/todo/views.py', 'lang': 'python'},
            {'name': 'urls.py', 'path': 'Lab/Lecture 15/todo/urls.py', 'lang': 'python'},
            {'name': 'utils.py', 'path': 'Lab/Lecture 15/todo/utils.py', 'lang': 'python'},
            {'name': 'manage.py', 'path': 'Lab/Lecture 15/manage.py', 'lang': 'python'},
            {'name': 'pyproject.toml', 'path': 'Lab/Lecture 15/pyproject.toml', 'lang': 'toml'}
        ],
        'concepts': ['Django ORM', 'Function-Based Views', 'Template Inheritance', 'URL Routing', 'External API', 'Migrations'],
        'dependencies': ['django', 'requests'],
        'runCommand': 'cd "Lab/Lecture 15" && python manage.py migrate && python manage.py runserver',
        'port': '8000'
    },
    {
        'id': 'student-api',
        'title': 'Student Management API — FastAPI + SQLAlchemy',
        'shortTitle': 'Student API',
        'description': 'Production-style REST API with CRUD, pagination, search, Pydantic validation, and dependency injection.',
        'icon': '⚡',
        'path': 'Lab/student_api',
        'readme': 'Lab/student_api/README.md',
        'tree': 'Lab/student_api/\n├── database.py\n├── main.py\n├── models.py\n├── schemas.py\n├── requirements.txt\n├── .env\n└── README.md',
        'files': [
            {'name': 'main.py', 'path': 'Lab/student_api/main.py', 'lang': 'python'},
            {'name': 'database.py', 'path': 'Lab/student_api/database.py', 'lang': 'python'},
            {'name': 'models.py', 'path': 'Lab/student_api/models.py', 'lang': 'python'},
            {'name': 'schemas.py', 'path': 'Lab/student_api/schemas.py', 'lang': 'python'},
            {'name': 'requirements.txt', 'path': 'Lab/student_api/requirements.txt', 'lang': 'text'},
            {'name': '.env', 'path': 'Lab/student_api/.env', 'lang': 'text'}
        ],
        'concepts': ['FastAPI', 'SQLAlchemy ORM', 'Pydantic Validation', 'Dependency Injection', 'Pagination', 'Filtering', 'REST CRUD'],
        'dependencies': ['fastapi', 'uvicorn', 'sqlalchemy', 'python-dotenv', 'pydantic[email]'],
        'runCommand': 'cd Lab/student_api && pip install -r requirements.txt && python main.py',
        'port': '8000'
    },
    {
        'id': 'assessment-b',
        'title': 'Lab Assessment B: Eisenhower Matrix Task Manager',
        'shortTitle': 'Eisenhower Matrix',
        'description': 'Full-stack CRUD app with Express.js, EJS, MongoDB — Eisenhower priority matrix, search, filters, dark mode.',
        'icon': '📋',
        'path': 'Lab/lab_Assessment_B',
        'readme': 'Lab/lab_Assessment_B/Readme.md',
        'tree': 'Lab/lab_Assessment_B/\n├── app.js\n├── package.json\n├── Readme.md\n├── public/\n│   ├── script.js\n│   └── style.css\n└── views/\n    ├── edit-task.ejs\n    ├── index.ejs\n    ├── new-task.ejs\n    └── task-card.ejs',
        'files': [
            {'name': 'app.js', 'path': 'Lab/lab_Assessment_B/app.js', 'lang': 'javascript'},
            {'name': 'package.json', 'path': 'Lab/lab_Assessment_B/package.json', 'lang': 'json'},
            {'name': 'script.js', 'path': 'Lab/lab_Assessment_B/public/script.js', 'lang': 'javascript'},
            {'name': 'style.css', 'path': 'Lab/lab_Assessment_B/public/style.css', 'lang': 'css'},
            {'name': 'index.ejs', 'path': 'Lab/lab_Assessment_B/views/index.ejs', 'lang': 'html'},
            {'name': 'new-task.ejs', 'path': 'Lab/lab_Assessment_B/views/new-task.ejs', 'lang': 'html'},
            {'name': 'edit-task.ejs', 'path': 'Lab/lab_Assessment_B/views/edit-task.ejs', 'lang': 'html'},
            {'name': 'task-card.ejs', 'path': 'Lab/lab_Assessment_B/views/task-card.ejs', 'lang': 'html'}
        ],
        'concepts': ['Express.js', 'EJS', 'MongoDB', 'CRUD', 'Eisenhower Matrix', 'ObjectId', 'Search & Filter', 'Dark Mode'],
        'dependencies': ['express', 'ejs', 'mongodb'],
        'runCommand': 'cd Lab/lab_Assessment_B && npm install && node app.js',
        'port': '3000'
    }
]

theory = [
    {
        'id': 'unit-1',
        'title': 'Unit 1: Foundations of Backend Development',
        'shortTitle': 'Foundations',
        'description': 'Client-server architecture, HTTP protocol, status codes, REST constraints.',
        'icon': '📡',
        'path': 'Theory/Unit-1',
        'readme': 'Theory/Unit-1/Readme.md',
        'files': [],
        'concepts': ['Client-Server', 'HTTP Methods', 'Status Codes', 'REST Architecture']
    },
    {
        'id': 'task-2',
        'title': 'Task 2: Flask REST API',
        'shortTitle': 'Flask API',
        'description': 'Python microframework REST API with JSON responses and 404 error handling.',
        'icon': '🧪',
        'path': 'Theory/task-2',
        'readme': 'Theory/task-2/Readme.md',
        'files': [
            {'name': 'app.py', 'path': 'Theory/task-2/app.py', 'lang': 'python'}
        ],
        'concepts': ['Flask', 'REST API', 'JSON Serialization', 'Route Variables', '404 Handling']
    },
    {
        'id': 'task-3',
        'title': 'Task 3: FastAPI REST API',
        'shortTitle': 'FastAPI Hello',
        'description': 'High-performance ASGI REST API with Uvicorn and auto-generated Swagger UI.',
        'icon': '⚡',
        'path': 'Theory/Task_3',
        'readme': 'Theory/Task_3/Readme.md',
        'files': [
            {'name': 'main.py', 'path': 'Theory/Task_3/main.py', 'lang': 'python'}
        ],
        'concepts': ['FastAPI', 'Uvicorn', 'ASGI', 'Swagger UI', 'Hot Reloading']
    },
    {
        'id': 'task-4',
        'title': 'Task 4: Nodemon Developer Workflow',
        'shortTitle': 'Nodemon DX',
        'description': 'File-watcher-based auto-reloading developer workflow.',
        'icon': '🔄',
        'path': 'Theory/Task_4',
        'readme': 'Theory/Task_4/Readme.md',
        'files': [],
        'concepts': ['Nodemon', 'File Watchers', 'Hot Reloading', 'Developer Experience']
    },
    {
        'id': 'task-5',
        'title': 'Task 5: Server-Side Rendering (FastAPI + Jinja2)',
        'shortTitle': 'SSR with Jinja2',
        'description': 'Dynamic server-rendered HTML using FastAPI with Jinja2 templates.',
        'icon': '🎨',
        'path': 'Theory/ssr_demmo_Task_5',
        'readme': 'Theory/ssr_demmo_Task_5/Readme.md',
        'files': [
            {'name': 'main.py', 'path': 'Theory/ssr_demmo_Task_5/main.py', 'lang': 'python'},
            {'name': 'home.html', 'path': 'Theory/ssr_demmo_Task_5/Templates/home.html', 'lang': 'html'},
            {'name': 'students.html', 'path': 'Theory/ssr_demmo_Task_5/Templates/students.html', 'lang': 'html'}
        ],
        'concepts': ['SSR vs CSR', 'Jinja2 Templates', 'Template Inheritance', 'Data Loops']
    },
    {
        'id': 'task-6',
        'title': 'Task 6 / Lecture 7: Web Storage API',
        'shortTitle': 'Web Storage',
        'description': 'localStorage vs sessionStorage comparison in a To-Do list application.',
        'icon': '💾',
        'path': 'Theory/Task-6',
        'readme': 'Theory/Task-6/Readme.md',
        'files': [
            {'name': 'script.js', 'path': 'Theory/Task-6/lecture7/script.js', 'lang': 'javascript'},
            {'name': 'index.html', 'path': 'Theory/Task-6/lecture7/index.html', 'lang': 'html'},
            {'name': 'style.css', 'path': 'Theory/Task-6/lecture7/style.css', 'lang': 'css'}
        ],
        'concepts': ['localStorage', 'sessionStorage', 'JSON Serialization', 'DOM Manipulation']
    },
    {
        'id': 'express-demo',
        'title': 'Express Demo: HTTP Server Basics',
        'shortTitle': 'Express Basics',
        'description': 'Server bootstrapping, HTTP routing, and endpoint design with Express.js.',
        'icon': '🖥️',
        'path': 'Theory/express-demo',
        'readme': 'Theory/express-demo/Readme.md',
        'files': [
            {'name': 'server.js', 'path': 'Theory/express-demo/server.js', 'lang': 'javascript'},
            {'name': 'package.json', 'path': 'Theory/express-demo/package.json', 'lang': 'json'}
        ],
        'concepts': ['Express.js', 'HTTP Routing', 'Handler Callbacks', 'Server Bootstrap']
    },
    {
        'id': 'lecture-15',
        'title': 'Lecture 15: Data Modeling — ORM & ODM',
        'shortTitle': 'Data Modeling',
        'description': 'Conceptual, logical, physical modeling. SQLAlchemy ORM, Mongoose ODM, Pydantic validation, E-Commerce PBL.',
        'icon': '🗄️',
        'path': 'Theory/Lecture_15',
        'readme': 'Theory/Lecture_15/ORM/Readme.md',
        'files': [
            {'name': 'Database.py', 'path': 'Theory/Lecture_15/ORM/Database.py', 'lang': 'python'},
            {'name': 'ecommerce_models.py', 'path': 'Theory/Lecture_15/ORM/ecommerce_models.py', 'lang': 'python'},
            {'name': 'fastapi_pydantic_validation.py', 'path': 'Theory/Lecture_15/ORM/fastapi_pydantic_validation.py', 'lang': 'python'},
            {'name': 'test_fastapi_validation.py', 'path': 'Theory/Lecture_15/ORM/test_fastapi_validation.py', 'lang': 'python'},
            {'name': 'mongoose_models.js', 'path': 'Theory/Lecture_15/ORM/mongoose_models.js', 'lang': 'javascript'},
            {'name': 'ecommerce_mongoose.js', 'path': 'Theory/Lecture_15/ORM/ecommerce_mongoose.js', 'lang': 'javascript'},
            {'name': 'physical_schema.sql', 'path': 'Theory/Lecture_15/ORM/physical_schema.sql', 'lang': 'sql'},
            {'name': 'save_to_mongodb.js', 'path': 'Theory/Lecture_15/ORM/save_to_mongodb.js', 'lang': 'javascript'},
            {'name': 'run_all.py', 'path': 'Theory/Lecture_15/ORM/run_all.py', 'lang': 'python'}
        ],
        'concepts': ['ER Diagrams', 'SQLAlchemy ORM', 'Mongoose ODM', 'Pydantic Validation', 'Cascade Deletion', 'Physical DDL']
    },
    {
        'id': 'lecture-16',
        'title': 'Lecture 16: Database CRUD Operations',
        'shortTitle': 'DB CRUD',
        'description': 'ACID transactions, connection pooling, pagination, SQL vs NoSQL query patterns.',
        'icon': '🔁',
        'path': 'Theory/Lecture_16',
        'readme': 'Theory/Lecture_16/Readme.md',
        'files': [],
        'concepts': ['CRUD Lifecycle', 'ACID Properties', 'Connection Pooling', 'Pagination']
    },
    {
        'id': 'unit-4',
        'title': 'Unit 4: Docker Compose — Multi-Service Stack',
        'shortTitle': 'Docker Compose',
        'description': 'Docker Compose with PostgreSQL, MongoDB, pgAdmin, and Mongo Express.',
        'icon': '🐳',
        'path': 'Theory/unit-4',
        'readme': 'Theory/unit-4/README.md',
        'files': [
            {'name': 'docker-compose.yml', 'path': 'Theory/unit-4/docker/docker-compose/docker-compose.yml', 'lang': 'yaml'}
        ],
        'concepts': ['Docker Compose', 'Container Networking', 'Volumes', 'PostgreSQL', 'MongoDB']
    },
    {
        'id': 'express-docker',
        'title': 'Theory: Express.js in Docker Container',
        'shortTitle': 'Express Docker',
        'description': 'Express.js microservice configured to run inside a Docker container binding to 0.0.0.0.',
        'icon': '📦',
        'path': 'Theory/Express_in_Docker',
        'readme': 'Theory/Express_in_Docker/README.md',
        'files': [
            {'name': 'app.js', 'path': 'Theory/Express_in_Docker/app.js', 'lang': 'javascript'},
            {'name': 'package.json', 'path': 'Theory/Express_in_Docker/package.json', 'lang': 'json'}
        ],
        'concepts': ['Docker Container', 'Host Binding 0.0.0.0', 'Express API', 'Nodemon DX']
    }
]

course_plan = {
    'title': 'Course Plan — Backend Development',
    'units': [
        {
            'name': 'Unit 1: Core Architecture & Web Protocols',
            'topics': [
                'Client-Server Architecture & Stateless Design',
                'HTTP Request/Response Lifecycle',
                'HTTP Methods: GET, POST, PUT, DELETE, PATCH',
                'Status Code Classes: 1xx, 2xx, 3xx, 4xx, 5xx',
                'REST Architectural Constraints',
                'Resource-Based URI Design'
            ]
        },
        {
            'name': 'Unit 2: Backend Frameworks & Routing',
            'topics': [
                'Flask Microframework — WSGI routing & JSON responses',
                'FastAPI — ASGI, async, Swagger UI auto-generation',
                'Express.js — Event loop, middleware, route parameters',
                'Nodemon — File-watcher developer experience',
                'Server-Side Rendering with EJS & Jinja2 templates',
                'Client-Side vs Server-Side Rendering comparison'
            ]
        },
        {
            'name': 'Unit 3: State Management & Storage',
            'topics': [
                'HTTP Statelessness and Mitigation Strategies',
                'Client-Side Cookies (cookie-parser)',
                'Server-Side Sessions (express-session)',
                'Web Storage API: localStorage vs sessionStorage',
                'JSON Serialization for Browser Storage'
            ]
        },
        {
            'name': 'Unit 4: Database Management & Data Modeling',
            'topics': [
                'Conceptual, Logical, Physical Data Models',
                'ER Diagram Design and Cardinality',
                'SQLAlchemy ORM — Models, Relationships, Cascades',
                'Mongoose ODM — Schemas, Validators, Subdocuments',
                'Pydantic Data Validation Pipelines',
                'CRUD Operations Lifecycle (Create, Read, Update, Delete)',
                'ACID Transactions & Connection Pooling',
                'Docker Compose for Database Environments',
                'PostgreSQL & MongoDB Administration'
            ]
        },
        {
            'name': 'Unit 5: Full-Stack Integration & Assessment',
            'topics': [
                'Full-Stack CRUD with Express + EJS + MongoDB',
                'Eisenhower Matrix Task Prioritization',
                'Django MVT Pattern — Models, Views, Templates',
                'FastAPI + SQLAlchemy Production API Architecture',
                'Pagination, Search, and Filtering',
                'Dependency Injection Patterns'
            ]
        }
    ]
}

syllabus = {
    'title': 'Syllabus — Backend Development',
    'subject': 'Backend Development',
    'code': 'CSXXX',
    'credits': 4,
    'courseOutcomes': [
        'CO1: Understand client-server architecture, HTTP protocols, and REST principles',
        'CO2: Design data models that translate business requirements into database structures',
        'CO3: Implement server-side applications using Node.js/Express, Python/FastAPI, and Python/Flask',
        'CO4: Build and consume RESTful APIs with proper status codes and validation',
        'CO5: Manage application state using cookies, sessions, and browser storage',
        'CO6: Perform CRUD operations using ORM (SQLAlchemy) and ODM (Mongoose) frameworks'
    ],
    'technologies': [
        {'name': 'Node.js', 'category': 'Runtime', 'role': 'Primary JavaScript execution environment', 'version': 'v20+'},
        {'name': 'Express.js', 'category': 'Framework', 'role': 'REST APIs & SSR routing', 'version': '^5.2.1'},
        {'name': 'Python', 'category': 'Runtime', 'role': 'Data modeling & modern backend services', 'version': '3.14'},
        {'name': 'FastAPI', 'category': 'Framework', 'role': 'High-performance ASGI REST APIs', 'version': '0.115+'},
        {'name': 'Flask', 'category': 'Framework', 'role': 'Microframework REST APIs', 'version': '3.x'},
        {'name': 'Django', 'category': 'Framework', 'role': 'Full-stack MVT applications', 'version': '5.x'},
        {'name': 'SQLAlchemy', 'category': 'ORM', 'role': 'Relational database mapping', 'version': '2.0+'},
        {'name': 'Mongoose', 'category': 'ODM', 'role': 'MongoDB document modeling', 'version': '^8.16.1'},
        {'name': 'PostgreSQL', 'category': 'Database', 'role': 'Production relational database', 'version': '16 / latest'},
        {'name': 'MongoDB', 'category': 'Database', 'role': 'NoSQL document database', 'version': '7.0'},
        {'name': 'SQLite', 'category': 'Database', 'role': 'Development & testing database', 'version': 'Built-in'},
        {'name': 'Docker Compose', 'category': 'DevOps', 'role': 'Multi-service containerization', 'version': 'v2+'},
        {'name': 'EJS / Jinja2', 'category': 'Templating', 'role': 'Server-side HTML rendering', 'version': 'Latest'},
        {'name': 'Pydantic', 'category': 'Validation', 'role': 'Request data validation with EmailStr', 'version': 'v2'}
    ]
}

# Cache all files
cache = {}
all_paths = set()
for lab in labs:
    if lab.get('readme'):
        all_paths.add(lab['readme'])
    for f in lab.get('files', []):
        all_paths.add(f['path'])

for th in theory:
    if th.get('readme'):
        all_paths.add(th['readme'])
    for f in th.get('files', []):
        all_paths.add(f['path'])

for p in all_paths:
    fp = os.path.join(backend_dir, p.replace('/', os.sep))
    if os.path.isfile(fp):
        with open(fp, 'r', encoding='utf-8', errors='replace') as f:
            cache[p] = f.read()

manifest = {
    'student': student_data,
    'repo': repo_info,
    'labs': labs,
    'theory': theory,
    'coursePlan': course_plan,
    'syllabus': syllabus,
    'cache': cache
}

# Write content.json in bhatt-kanishka.github.io
json_path_io = os.path.join(io_dir, 'content.json')
with open(json_path_io, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print('Wrote:', json_path_io)

# Write content.json in Backend_Development
json_path_bd = os.path.join(backend_dir, 'content.json')
with open(json_path_bd, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print('Wrote:', json_path_bd)

# Write js/content.js in bhatt-kanishka.github.io
raw_base_str = "https://raw.githubusercontent.com/" + repo_info['repoOwner'] + "/" + repo_info['repoName'] + "/main"
github_base_str = "https://github.com/" + repo_info['repoOwner'] + "/" + repo_info['repoName']

js_content = f"""// EndpointCraft Content Manifest & Embedded Cache
const REPO_OWNER = {json.dumps(repo_info['repoOwner'])};
const REPO_NAME = {json.dumps(repo_info['repoName'])};
const RAW_BASE = "{raw_base_str}";
const GITHUB_BASE = "{github_base_str}";

const STUDENT = {json.dumps(student_data, indent=2, ensure_ascii=False)};
const LABS = {json.dumps(labs, indent=2, ensure_ascii=False)};
const THEORY = {json.dumps(theory, indent=2, ensure_ascii=False)};
const COURSE_PLAN = {json.dumps(course_plan, indent=2, ensure_ascii=False)};
const SYLLABUS = {json.dumps(syllabus, indent=2, ensure_ascii=False)};
const EMBEDDED_CACHE = {json.dumps(cache, indent=2, ensure_ascii=False)};
"""

js_path_io = os.path.join(io_dir, 'js', 'content.js')
with open(js_path_io, 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Wrote:', js_path_io)

# Write js/content.js in Backend_Development
os.makedirs(os.path.join(backend_dir, 'js'), exist_ok=True)
js_path_bd = os.path.join(backend_dir, 'js', 'content.js')
with open(js_path_bd, 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Wrote:', js_path_bd)

print('Manifest generation complete!')
