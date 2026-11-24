# ⚡ EndpointCraft — Backend Development Documentation

Welcome to **EndpointCraft**, the official interactive documentation and portfolio website for the **Backend Development** coursework completed by **Kanishka Bhatt** at the **University of Petroleum and Energy Studies (UPES)**.

🌐 **Live Website**: [https://bhatt-kanishka.github.io/](https://bhatt-kanishka.github.io/)  
📦 **Source Repository**: [https://github.com/bhatt-kanishka/Backend_Development](https://github.com/bhatt-kanishka/Backend_Development)

---

## 🎓 Student Details

| Attribute | Value |
|:----------|:------|
| **Student Name** | Kanishka Bhatt |
| **SAP ID** | 590017366 |
| **Institute** | University of Petroleum and Energy Studies (UPES), Dehradun |
| **Semester** | 5th Semester |
| **Subject** | Backend Development |

---

## 📖 About EndpointCraft

**EndpointCraft** is a zero-build, static documentation platform designed with a modern "Smartech" pastel mauve theme. It acts as an interactive browser for all backend laboratory experiments, theory modules, practical tasks, course plans, and syllabus matrices.

### Key Capabilities:
- 🎨 **Pastel Mauve Theme**: Soft rounded cards (16–24px radius), subtle shadows, DM Sans typography, and circular progress rings.
- 🧪 **Complete Lab Mapping**: Direct links to all 7 laboratory experiments with dependencies, execution commands, and copy-ready code blocks.
- 📚 **Comprehensive Theory**: 11 academic and practical theory topics spanning REST APIs, ORM/ODM, Pydantic validation, and Docker Compose.
- 🔍 **Live Search**: Instant client-side search across titles, concepts, file paths, and documentation contents.
- 🔗 **Deep-Linkable Routing**: Supports hash routing (`#labs/student-api`, `#theory/lecture-15`) and path-based routing (`#dir=/Lab/Experiment_12A/&file=Readme.md`).
- ⚡ **Offline & Zero-Latency**: Bundled with a comprehensive manifest and embedded cache for instant rendering without API rate limits.
- 📱 **Fully Responsive**: Collapsible sidebar, mobile overlay navigation, and accessible semantic HTML5.

---

## 🗂️ Project & Repository Structure

```text
bhatt-kanishka.github.io/
├── index.html              # Main Single-Page Application (SPA) entry point
├── content.json            # Machine-readable JSON manifest of all labs, theory, and files
├── build_manifest.py       # Build script to regenerate manifest & embedded cache
├── README.md               # Repository documentation and deployment guide
│
├── css/
│   └── style.css           # Pastel mauve design theme, layout, code styles & responsive rules
│
└── js/
    ├── content.js          # JavaScript content manifest and cached documentation
    └── app.js              # Client-side SPA router, search engine, and Markdown renderer
```

---

## 🛠️ Technology Stack

| Technology | Category | Role |
|:-----------|:---------|:-----|
| **HTML5 / Semantic Web** | Structure | Accessible, semantic layout and document structure |
| **CSS3 (Custom Properties)** | Styling | Pastel mauve dashboard theme with CSS grid & flexbox |
| **Vanilla JavaScript (ES6+)** | Logic | Hash router, client-side search, DOM manipulation |
| **Marked.js** | Library | Fast client-side Markdown rendering |
| **Highlight.js** | Library | Code syntax highlighting with Atom One Dark theme |
| **Google Fonts (DM Sans)** | Typography | Clean, modern sans-serif typography |

---

## 🚀 How to Run Locally

Because EndpointCraft uses pure HTML, CSS, and JavaScript with no build step required, you can run it immediately using any local static web server:

### Option 1: Python HTTP Server (Recommended)
```bash
# In the repository root directory
python -m http.server 8000
```
Then open your browser and navigate to:
```text
http://localhost:8000
```

### Option 2: Node.js (npx serve)
```bash
npx serve .
```

### Option 3: VS Code Live Server
Right-click on `index.html` inside VS Code and select **"Open with Live Server"**.

---

## 🌐 GitHub Pages Deployment Guide

EndpointCraft is designed for seamless, one-click hosting on **GitHub Pages**:

### Step-by-Step Deployment:
1. **Push Changes to GitHub**:
   ```bash
   git add .
   git commit -m "Deploy EndpointCraft documentation website"
   git push origin main
   ```

2. **Configure GitHub Pages in Settings**:
   - Navigate to your repository on GitHub: `https://github.com/bhatt-kanishka/bhatt-kanishka.github.io`
   - Click on the **Settings** tab (gear icon at the top).
   - In the left sidebar, click on **Pages** (under the "Code and automation" section).
   - Under **Build and deployment**:
     - **Source**: Select `Deploy from a branch`.
     - **Branch**: Select `main` (or your default branch).
     - **Folder**: Select `/ (root)`.
   - Click **Save**.

3. **Verify Deployment**:
   - Within 1–2 minutes, GitHub Actions will publish your site.
   - Access the live site at: **`https://bhatt-kanishka.github.io/`**

---

## 📋 Coursework Curriculum Overview

### Laboratory Experiments (`Lab/`):
1. **Experiment 1**: Semantic HTML5 Elements, Web Forms, Audio/Video, Canvas 2D
2. **Lab 7 & 8**: ES6 To-Do Application (Classes, Spread Operator, Event Delegation)
3. **Experiment 12A**: Express.js REST API & EJS Server-Side Rendering
4. **Experiment 12B**: State Management (Client Cookies & Server Sessions)
5. **Lecture 15 Lab**: Full-Stack Django To-Do App with External API Integration
6. **Student API**: Production-Grade FastAPI + SQLAlchemy + Pydantic CRUD API
7. **Lab Assessment B**: Eisenhower Decision Matrix Task Management Application (Express + MongoDB)

### Theory Modules (`Theory/`):
1. **Unit 1**: Foundations of Backend Web Development (HTTP Protocols, REST Architecture)
2. **Task 2**: Flask Microframework REST API with JSON Serialization
3. **Task 3**: Asynchronous FastAPI REST API with Automatic Swagger UI
4. **Task 4**: Nodemon Developer Workflow & File System Watchers
5. **Task 5**: Server-Side Rendering (SSR) with FastAPI & Jinja2 Templates
6. **Task 6 / Lecture 7**: Browser Storage Mechanisms (localStorage vs sessionStorage)
7. **Express Demo**: HTTP Server Bootstrapping and Routing Basics
8. **Lecture 15**: Data Modeling Masterclass (Conceptual, Logical, Physical, SQLAlchemy ORM & Mongoose ODM)
9. **Lecture 16**: Database CRUD Lifecycle, ACID Transactions, and Connection Pooling
10. **Unit 4**: Docker Compose Multi-Service Stack (PostgreSQL, MongoDB, pgAdmin, Mongo Express)
11. **Express in Docker**: Containerized Express Server with Host Binding (`0.0.0.0`)

---

## 📄 License & Credits

Created by **Kanishka Bhatt** for the **Backend Development** coursework at **UPES**. All code and documentation are strictly for educational and portfolio presentation purposes.
