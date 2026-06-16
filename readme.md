# 🏟️ AI Arena: Multi-LLM Evaluation & Routing Platform

AI Arena is an enterprise-grade multi-model AI evaluation platform built with Streamlit and NVIDIA NIM APIs. The application enables users to compare responses from multiple Large Language Models (LLMs), collect human preference feedback, benchmark model performance, and identify the most effective model for different tasks.

## 🚀 Overview

Choosing the right LLM for a specific task remains a major challenge in Generative AI. Different models excel at different domains such as:

* Coding
* Reasoning
* Mathematics
* Content Generation
* Summarization

AI Arena solves this problem by providing a unified interface where multiple LLMs compete on the same prompt and users evaluate the quality of their responses.

---

## 🎯 Key Features

### Multi-Model Evaluation

Query multiple state-of-the-art LLMs simultaneously:

* Meta Llama 3.3 70B
* DeepSeek R1
* Mixtral 8x7B
* Additional NVIDIA-supported models

---

### Side-by-Side Response Comparison

Compare model outputs in real-time.

```text
User Prompt
      ↓

┌─────────┐ ┌─────────┐ ┌─────────┐
│ Llama   │ │DeepSeek │ │ Mixtral │
└─────────┘ └─────────┘ └─────────┘

      ↓

Human Evaluation
```

---

### Human Preference Collection

Users vote for the best response.

Collected feedback can be used to:

* Rank models
* Build leaderboards
* Train routing systems
* Analyze model strengths

---

### Performance Analytics

Track:

* Win rates
* User preferences
* Model rankings
* Response quality trends

---

### AI Routing Foundation

The platform serves as the foundation for an adaptive AI routing system that automatically selects the best model for a given task category.

---

## 🏗️ System Architecture

```text
                        ┌───────────────┐
                        │   Streamlit   │
                        │      UI       │
                        └───────┬───────┘
                                │
                                ▼

                     ┌──────────────────┐
                     │  Prompt Manager  │
                     └────────┬─────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼

 ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
 │ Llama 3.3    │   │ DeepSeek R1  │   │   Mixtral    │
 └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
        │                  │                  │
        └──────────┬───────┴──────────┬───────┘
                   ▼                  ▼

           ┌──────────────────────┐
           │ Response Comparator  │
           └──────────┬───────────┘
                      │
                      ▼

             ┌────────────────┐
             │ Voting Engine  │
             └───────┬────────┘
                     │
                     ▼

             ┌────────────────┐
             │ Analytics Layer│
             └────────────────┘
```

---

## 🛠️ Technology Stack

### Frontend

* Streamlit

### Backend

* Python 3.12+

### AI Models

* NVIDIA NIM APIs
* Meta Llama
* DeepSeek
* Mixtral

### Data Storage

* CSV-based persistence
* Pandas

### Environment Management

* Python Virtual Environment
* dotenv

---

## 📂 Project Structure

```text
ai-arena/

├── app.py
├── models.py
├── votes.py
├── votes.csv
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-arena.git

cd ai-arena
```

### Create Virtual Environment

```bash
python -m venv venv
```

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
NVIDIA_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will launch at:

```text
http://localhost:8501
```

---

## 📊 Example Workflow

### Step 1

User enters:

```text
Explain reinforcement learning in simple terms.
```

### Step 2

The platform queries multiple LLMs.

### Step 3

Responses are displayed side-by-side.

### Step 4

User votes for the best answer.

### Step 5

Vote is stored and analytics are updated.

---

## 📈 Future Enhancements

### AI Judge

Automated evaluation of responses using an LLM-as-a-Judge framework.

### ELO Ranking System

Model rankings inspired by Chatbot Arena.

### Task Categorization

Automatic classification:

* Coding
* Math
* Reasoning
* Writing

### Intelligent Routing

Automatically route prompts to the highest-performing model.

### Database Integration

Replace CSV storage with:

* PostgreSQL
* SQLite
* MongoDB

### Deployment

* Streamlit Cloud
* Render
* Railway
* AWS

---

## 🔒 Security

* API keys stored in environment variables
* Sensitive credentials excluded from version control
* `.env` included in `.gitignore`

---

## 🎓 Learning Outcomes

This project demonstrates:

* Generative AI Engineering
* Prompt Engineering
* LLM Evaluation
* Multi-Agent Architectures
* Human Feedback Collection
* Model Benchmarking
* Data Analytics
* Streamlit Development
* NVIDIA NIM Integration

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Divyanshu Singh Nathawat**

Aspiring Data Scientist & AI Engineer

Building intelligent systems that evaluate, compare, and optimize Large Language Models.
