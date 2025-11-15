import streamlit as st
import tempfile
import os
import json
import subprocess
import shutil
import google.generativeai as genai

# ---------------------------------------------------
# CONSTANTS
# ---------------------------------------------------

MODEL_NAME = "models/gemini-2.5-flash"
IGNORE_EXT = [
    ".png", ".jpg", ".jpeg", ".pdf", ".gif", ".ico",
    ".zip", ".exe", ".bin", ".jar"
]
MAX_CHARS_PER_FILE = 20000


# ---------------------------------------------------
# FUNCTION: Clone GitHub repository
# ---------------------------------------------------

def clone_repo(github_url):
    tmp_dir = tempfile.mkdtemp()
    try:
        subprocess.run(["git", "clone", github_url, tmp_dir], check=True)
        return tmp_dir
    except subprocess.CalledProcessError:
        st.error("❌ Failed to clone the repository. Check the URL.")
        return None


# ---------------------------------------------------
# FUNCTION: Scan repository files
# ---------------------------------------------------

def read_repo_files(repo_path):
    repo_data = {}
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file in files:
            if file.startswith("."):
                continue

            ext = os.path.splitext(file)[1]
            if ext in IGNORE_EXT:
                continue

            full_path = os.path.join(root, file)

            try:
                with open(full_path, "r", errors="ignore") as f:
                    content = f.read()[:MAX_CHARS_PER_FILE]

                rel_path = os.path.relpath(full_path, repo_path)
                repo_data[rel_path] = content

            except Exception:
                continue

    return repo_data


# ---------------------------------------------------
# FUNCTION: Generate README using Gemini
# ---------------------------------------------------

def generate_readme(repo_snapshot, api_key):
    genai.configure(api_key=api_key)

    repo_json = json.dumps(repo_snapshot, indent=2)[:200000]

    prompt = f"""
You are an expert software documentation generator.

Below is a snapshot of a repository's structure and content.

Your job:
- Analyze code
- Infer architecture & purpose
- Identify components & technologies
- Produce a polished README.md

README MUST INCLUDE:
- Project Title
- Description
- Features
- Architecture Overview
- Folder Structure
- Installation Steps
- Usage Instructions
- API Documentation (if detected)
- Module Descriptions
- Contributing Guide
- Future Enhancements

Only output valid README.md content.

Repository Snapshot:
{repo_json}
"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)

    return response.text


# ---------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------

st.set_page_config(page_title="README Generator", layout="wide")

st.title("🤖 DocumentDrifter — Auto README Generator")
st.write("Generate a fresh README.md from any GitHub repository using Gemini.")

# ------------------------------------------
# API Key Input Box
# ------------------------------------------

st.subheader("🔐 Enter Your Gemini API Key")
api_key = st.text_input(
    "API Key",
    type="password",
    placeholder="Enter your Gemini API Key here (required)"
)

st.markdown("---")

# ------------------------------------------
# GitHub URL Input
# ------------------------------------------

github_url = st.text_input(
    "Enter GitHub Repository URL (Public Repo):",
    placeholder="https://github.com/user/repo"
)

# ------------------------------------------
# Generate Button
# ------------------------------------------

if st.button("Generate README"):
    if not api_key:
        st.error("❌ Please enter your Gemini API key.")
    elif not github_url.strip():
        st.error("❌ Please enter a GitHub repository URL.")
    else:
        with st.spinner("Cloning repository..."):
            repo_path = clone_repo(github_url)

        if repo_path:
            with st.spinner("Scanning repository..."):
                repo_data = read_repo_files(repo_path)

            with st.spinner("Generating README using Gemini..."):
                try:
                    readme = generate_readme(repo_data, api_key)
                except Exception as e:
                    st.error(f"❌ Gemini API Error: {str(e)}")
                    shutil.rmtree(repo_path)
                    st.stop()

            st.success("🎉 README generated successfully!")

            st.subheader("📄 Generated README.md")
            st.code(readme, language="markdown")

            st.download_button(
                label="📥 Download README.md",
                data=readme,
                file_name="README.md",
                mime="text/markdown"
            )

            shutil.rmtree(repo_path)
