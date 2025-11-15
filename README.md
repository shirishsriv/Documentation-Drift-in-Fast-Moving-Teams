# 🤖 DocumentDrifter — Auto README Generator

DocumentDrifter is a Streamlit-powered application that automatically generates polished, production-ready `README.md` files for any **public GitHub repository**.
It analyzes repository structure and source code using **Google Gemini** and produces documentation including architecture, modules, features, folder structures, and more.

---

## ✨ Key Features

### 🔍 Intelligent Repository Scanning

* Clones a public GitHub repository into a temporary workspace
* Recursively scans all readable text-based source files
* Automatically ignores binary and irrelevant file types:
  `.png`, `.jpg`, `.jpeg`, `.pdf`, `.gif`, `.ico`, `.zip`, `.exe`, `.bin`, `.jar`, etc.

### 🤖 AI-Generated Documentation

* Uses **Gemini 2.5 Flash** (`models/gemini-2.5-flash`)
* Summarizes repository contents into a detailed `README.md`
* Identifies code structure, API components, modules, and potential architecture
* Produces consistent, clean Markdown output

### 🚀 Streamlined User Experience

* Simple Streamlit UI
* Password-style API key entry
* GitHub URL input
* Spinners for cloning, scanning, and generation steps
* In-browser README preview
* One-click download button

---

## 🏗️ Application Architecture

```
╭───────────────────────────────────────────────────────────────╮
│                           Streamlit UI                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ • API key input                                           │ │
│  │ • GitHub repo URL input                                   │ │
│  │ • Generate README button                                  │ │
│  └──────────────────────────────────────────────────────────┘  │
╰───────────────────────────────────────────────────────────────╯

                │ User Trigger
                ▼

      ┌───────────────────────┐
      │  clone_repo()         │
      │  - git clone into tmp │
      └───────────────────────┘

                ▼

      ┌────────────────────────────┐
      │  read_repo_files()         │
      │  - walk directory tree     │
      │  - ignore hidden/binary    │
      │  - load readable content   │
      └────────────────────────────┘

                ▼

      ┌──────────────────────────────┐
      │ generate_readme()            │
      │ - snapshot → JSON            │
      │ - Gemini prompt              │
      │ - returns README.md text     │
      └──────────────────────────────┘

                ▼

      ┌────────────────────────────┐
      │ Streamlit Output           │
      │ • Markdown preview         │
      │ • Download button          │
      └────────────────────────────┘
```

---

## 📁 Repository Structure

```
.
├── app.py               # Main Streamlit application
├── db.py                # (New) database or storage utilities (*open file for full integration*)
├── README.md            # Auto-generated documentation (this file)
└── requirements.txt     # Recommended dependencies (Streamlit, Gemini SDK)
```

---

## ⚙️ Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/shirishsriv/Documentation-Drift-in-Fast-Moving-Teams
   cd Documentation-Drift-in-Fast-Moving-Teams
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App

Launch Streamlit:

```bash
streamlit run app.py
```

Then:

1. Enter your **Gemini API Key**
2. Paste a **GitHub repository URL**
3. Click **Generate README**
4. View or download your generated README.md

---

## 🧠 How It Works Internally

### `clone_repo(url)`

* Clones a GitHub repository to a secure temporary directory
* Displays error in UI if cloning fails

### `read_repo_files(path)`

* Recursively walks repository
* Skips hidden files and binary extensions
* Reads up to **20,000 characters** per file
* Returns `{ relative_path: content }` dictionary snapshot

### `generate_readme(snapshot, api_key)`

* Converts snapshot to JSON
* Builds structured prompt with documentation requirements
* Uses Gemini to generate full Markdown README
* Returns cleaned Markdown text

---

## 🧩 Modules Summary

| Module                | Purpose                                                            |
| --------------------- | ------------------------------------------------------------------ |
| **app.py**            | Main application, UI logic, repo scanning, Gemini integration      |
| **clone_repo()**      | Clones GitHub repo to a temporary directory                        |
| **read_repo_files()** | Loads repository contents while filtering                          |
| **generate_readme()** | Constructs prompt + generates README from Gemini                   |
| **db.py**             | *(Not fully analyzed — open file to include accurate description)* |

---

## 🤝 Contributing

Contributions are welcome!
You can improve documentation, add features, optimize scanning, or enhance AI prompt structure.

1. Fork the repo
2. Create a branch
3. Commit your changes
4. Submit a pull request

---

## 🔮 Future Roadmap

* Support for **private repositories**
* README diffs vs existing file
* Multi-file documentation generation
* Integration with OpenAI, Claude, Llama models
* Rich previews + architecture diagrams
* Improved security for API key handling
* Repo insights dashboard

---

## 📄 License

MIT License
Feel free to use, modify, and distribute.

---

Happy documenting! 🚀
DocumentDrifter saves developers from documentation drift — one repo at a time.
