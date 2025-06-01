# 🧠 Backend – Career Guidance Engine

This is the AI backend for the Hack the Haze – Open Mind Challenge project. Built using **Python**, **FastAPI**, and simple ML/NLP logic, it powers career recommendations tailored for Indian learners based on aptitude, goals, skills, and learning gaps.

---

## 🔧 Tech Stack

- ⚙️ **FastAPI** – high-performance Python API framework
- 🧪 **scikit-learn** – basic aptitude prediction
- 🧠 **Custom NLP/logic** – goal extraction, skill mapping, and recommendations
- 🧰 Python modules – for modular, scalable service design

---

## 📌 Features Implemented

✅ **Aptitude Prediction**  
✅ **Goal Extraction from Text**  
✅ **Skill Mapping with Industry Roles**  
✅ **Career Recommendation Engine**  
✅ **Skill Gap Analysis**  
✅ **Clean Modular Code** (API, services, models, utils, core config)

---

## 🛠️ How to Run Locally

> ⚠️ Ensure Python 3.10+ is installed.

### 1. Create a Virtual Environment

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate   # On macOS/Linux


2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Start the Server
bash
Copy
Edit
uvicorn app.main:app --reload
Server will run at: http://localhost:8000

🔬 API Endpoints

| Endpoint              | Method | Description                           |
| --------------------- | ------ | ------------------------------------- |
| `/`                   | GET    | Root health check                     |
| `/predict-aptitude/`  | POST   | Predict aptitude from scores          |
| `/extract-goals/`     | POST   | Extract goals from user input text    |
| `/map-skills/`        | POST   | Map input skills to suitable careers  |
| `/recommend-careers/` | GET    | Recommend careers from aptitude class |
| `/skill-gap/`         | POST   | Identify missing skills for a path    |



🧠 Example Inputs
POST /predict-aptitude/
Body: [80, 70, 85]

POST /extract-goals/?text=I want to become a civil servant

POST /map-skills/
Body: ["python", "data analysis", "communication"]

POST /skill-gap/
{
  "career_path": "IAS",
  "user_skills": ["communication"]
}


📁 Folder Structure
backend/
├── app/
│   ├── api/            # All API route handlers
│   ├── core/           # Config, constants, logging
│   ├── models/         # ML/NLP model wrappers (mock/dummy)
│   ├── services/       # Logic for aptitude, goals, careers
│   ├── utils/          # NLP/embedding helpers
│   └── main.py         # FastAPI entrypoint
├── requirements.txt
└── README.md           # This file
