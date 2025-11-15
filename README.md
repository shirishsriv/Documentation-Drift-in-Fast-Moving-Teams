# 🤖 DocumentDrifter — Auto README Generator

DocumentDrifter is a Streamlit-based application that automatically generates high-quality `README.md` files for any public GitHub repository.
It analyzes repository structure and source code using **Google Gemini**, then produces polished documentation including features, architecture, and usage details.

---

## ⭐ Features

* **🔍 GitHub Repository Parsing**
  Clones any public GitHub repository and scans all non-binary source files.

* **🤖 AI-Generated Documentation**
  Uses **Gemini 2.5 Flash** to infer project purpose, architecture, and components.

* **📂 Smart File Filtering**
  Skips binary and irrelevant files to focus on source code.

* **🧠 Structured Output**
  Automatically produced README includes:

  * Title
  * Description
  * Features
  * Architecture Overview
  * Folder Structure
  * Installation Steps
  * Usage Instructions
  * API / Module Documentation
  * Contributing
  * Future Enhancements

* **💾 Downloadable Output**
  View and download the generated README directly in the UI.

---

## 🏗️ Architecture Overview

```
Streamlit UI ─┐
               │
User Input ----┼--> Repo Cloning → File Scanning → AI Prompt Construction → Gemini → README Output
               │
Gemini API ----┘
```

---

## 📁 Folder Structure

```
.
├── app.py              # Main Streamlit app
├── README.md           # (Generated via the tool)
└── requirements.txt    # Streamlit + Gemini dependencies (recommended)
```

---

## 🚀 Installation

1. **Clone this repository**

   ```
   git clone https://github.com/your/repo.git
   cd repo
   ```

2. **Create a virtual environment (optional but recommended)**

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key**
   You will be prompted for it in the UI.

---

## ▶️ Usage

Run the Streamlit app:

```
streamlit run app.py
```

Then:

1. Enter your **Gemini API Key**
2. Paste a **public GitHub repository URL**
3. Click **Generate README**
4. View or download your new README.md

---

## 🧠 How It Works

### 1. **Repository Cloning**

`clone_repo()` uses `git clone` in a temporary directory.

### 2. **Directory Scanning**

`read_repo_files()`:

* Walks the directory tree
* Skips hidden files/folders
* Ignores binary extensions (`.png`, `.zip`, `.jar`, etc.)
* Reads text files up to 20,000 characters each

### 3. **README Generation**

`generate_readme()`:

* Formats repo snapshot as JSON
* Sends structured prompt to **Gemini 2.5 Flash**
* Receives Markdown README content

### 4. **Streamlit UI**

Provides:

* API key input
* Repo URL input
* Progress spinners
* Final README display
* Download button

---

## 🧩 Modules Summary

| Module              | Purpose                                              |
| ------------------- | ---------------------------------------------------- |
| `clone_repo()`      | Clones GitHub repo into a temp directory             |
| `read_repo_files()` | Recursively scans repo and loads readable text files |
| `generate_readme()` | Sends code snapshot to Gemini and retrieves a README |
| Streamlit UI        | Handles user inputs and displays results             |

---

## 🤝 Contributing

Contributions are welcome!

* Open an issue
* Submit a pull request
* Report bugs or suggest improvements

---

## 🔮 Future Enhancements

* Support for **private GitHub repositories**
* Multi-README generation per folder/module
* Better security for API key handling
* Side-by-side diff with existing README
* Integrating additional LLMs (OpenAI, Claude, Llama)

---

## 📄 License

MIT License (or specify the actual license used).

---

Happy documenting! 🚀
