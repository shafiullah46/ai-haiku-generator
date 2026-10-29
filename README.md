# 🌸 AI Haiku Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

An intelligent, Python-based generative AI microservice that creates expressive short poetry (haikus) based on dynamic user topics while strictly enforcing the traditional 5-7-5 syllable structure using OpenAI's API.

---

## 🚀 Key Highlights

- **Strict Constraint Enforcement:** Uses precision prompt engineering to force models into adhering strictly to the traditional 5-7-5 syllable metric.
- **Deterministic Output:** Configured with `temperature=0.0` for zero-variance, consistent poetic generation.
- **Robust Parsing:** Built-in fallback mechanisms to securely handle standard OpenAI response objects and custom mock environments.
- **Environment-Driven Security:** Loads API credentials and custom base endpoints via system environment variables (`OPENAI_API_KEY`, `OPENAI_API_BASE`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **SDK:** `openai` (Official Python Library)
- **Environment:** Virtualenv (`venv`)

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/shafiullah46/ai-haiku-generator.git](https://github.com/shafiullah46/ai-haiku-generator.git)
cd ai-haiku-generator

2. Virtual Environment Setup
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

3. Install Dependencies
pip install openai

4. Set Environment Variables & Run
# On Windows PowerShell:
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_API_BASE="your_base_url_here"

# Run the generator script
python haiku_generator.py

💻 Sample Output (Topic: 'sky')
Generated Haiku:
Endless blanket blue,
Floating clouds drift high and wide,
Peaceful morning calm.

👨‍💻 Author
Shafiullah Niazi
Deputy Director ML/DevOps | Cloud & AI Infrastructure Specialist
