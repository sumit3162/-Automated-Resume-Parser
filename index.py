from pathlib import Path

# Create a Jupyter Notebook structure
from nbformat import v4 as nbf

notebook = nbf.new_notebook()

notebook.cells = [

    nbf.new_markdown_cell("### 🧠 **Automated Resume Parser**\n"
                          "**Project Goal:** Automatically extract structured information (name, skills, education, etc.) from resumes (PDF/DOCX) and store it in a PostgreSQL database."),

    nbf.new_markdown_cell("#### 📌 **Technologies Used**\n"
                          "- Python\n"
                          "- spaCy\n"
                          "- PDFPlumber\n"
                          "- python-docx\n"
                          "- Flask (for optional API integration)\n"
                          "- PostgreSQL"),

    nbf.new_code_cell("import spacy\n"
                      "import pdfplumber\n"
                      "import docx\n"
                      "import psycopg2\n"
                      "import re"),

    nbf.new_markdown_cell("### 📄 **Function to Extract Text from PDF**"),
    nbf.new_code_cell("def extract_text_from_pdf(file_path):\n"
                      "    text = \"\"\n"
                      "    with pdfplumber.open(file_path) as pdf:\n"
                      "        for page in pdf.pages:\n"
                      "            text += page.extract_text()\n"
                      "    return text"),

    nbf.new_markdown_cell("### 📄 **Function to Extract Text from DOCX**"),
    nbf.new_code_cell("def extract_text_from_docx(file_path):\n"
                      "    doc = docx.Document(file_path)\n"
                      "    return \"\\n\".join([para.text for para in doc.paragraphs])"),

    nbf.new_markdown_cell("### 🧠 **NLP-Based Info Extraction using spaCy**"),
    nbf.new_code_cell("nlp = spacy.load(\"en_core_web_sm\")\n\n"
                      "def extract_entities(text):\n"
                      "    doc = nlp(text)\n"
                      "    entities = {\"PERSON\": [], \"ORG\": [], \"EDUCATION\": [], \"SKILLS\": []}\n\n"
                      "    for ent in doc.ents:\n"
                      "        if ent.label_ == \"PERSON\":\n"
                      "            entities[\"PERSON\"].append(ent.text)\n"
                      "        elif ent.label_ == \"ORG\":\n"
                      "            entities[\"ORG\"].append(ent.text)\n"
                      "    return entities"),

    nbf.new_markdown_cell("### ⚙️ **Custom Skill Extraction (Regex/Keyword Match)**"),
    nbf.new_code_cell("def extract_skills(text, skill_set):\n"
                      "    skills_found = []\n"
                      "    for skill in skill_set:\n"
                      "        if re.search(rf\"\\b{re.escape(skill)}\\b\", text, re.IGNORECASE):\n"
                      "            skills_found.append(skill)\n"
                      "    return list(set(skills_found))\n\n"
                      "skills_db = ['Python', 'Machine Learning', 'SQL', 'Flask', 'NLP']"),

    nbf.new_markdown_cell("### 🛢️ **Store Extracted Data in PostgreSQL**"),
    nbf.new_code_cell("def store_in_db(data):\n"
                      "    conn = psycopg2.connect(\n"
                      "        dbname=\"resume_db\",\n"
                      "        user=\"postgres\",\n"
                      "        password=\"your_password\",\n"
                      "        host=\"localhost\",\n"
                      "        port=\"5432\"\n"
                      "    )\n"
                      "    cursor = conn.cursor()\n\n"
                      "    insert_query = \"\"\"\n"
                      "    INSERT INTO resumes (name, skills, education, organization)\n"
                      "    VALUES (%s, %s, %s, %s)\n"
                      "    \"\"\"\n"
                      "    cursor.execute(insert_query, (data['PERSON'][0], \n"
                      "                                  \", \".join(data['SKILLS']), \n"
                      "                                  \", \".join(data['EDUCATION']), \n"
                      "                                  \", \".join(data['ORG'])))\n\n"
                      "    conn.commit()\n"
                      "    cursor.close()\n"
                      "    conn.close()"),

    nbf.new_markdown_cell("### ✅ **End-to-End Execution**"),
    nbf.new_code_cell("file_path = \"sample_resume.pdf\"  # or .docx\n"
                      "text = extract_text_from_pdf(file_path)\n"
                      "entities = extract_entities(text)\n"
                      "entities[\"SKILLS\"] = extract_skills(text, skills_db)\n\n"
                      "store_in_db(entities)"),

    nbf.new_markdown_cell("### 🔍 **Output Example**"),
    nbf.new_code_cell("print(entities)")
]

# Save the notebook
output_path = "Automated_Resume_Parser.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    import nbformat
    nbformat.write(notebook, f)

output_path
