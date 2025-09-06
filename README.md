# SahAI – A Compassionate Wellness Buddy 🌱💙

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-orange)](#)
[![Flask](https://img.shields.io/badge/flask-2.x-lightgrey)](#)

---

## 📑 Table of Contents
- [📖 Project Overview](#-project-overview)
- [🛠 Tech Stack](#-tech-stack)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🚀 Usage Guide](#-usage-guide)
- [🌐 API Documentation](#-api-documentation)
- [🖥 Frontend Details](#-frontend-details)
- [📂 Project Structure](#-project-structure)
- [🔐 Authentication / Security](#-authentication--security)
- [⚡ Features Summary](#-features-summary)
- [📝 Examples](#-examples)
- [🤝 Contributing Guide](#-contributing-guide)
- [🧪 Testing Instructions](#-testing-instructions)
- [📜 License](#-license)
- [📌 Future Improvements](#-future-improvements)

---

## 📖 Project Overview
**SahAI** is a self-hosted wellness web application designed to provide young people with a safe, stigma-free, and culturally sensitive space to explore emotions, express gratitude, relax with music, generate art and comics, and engage with AI-driven reflections.  

It uses **Flask + SQLAlchemy** on the backend and integrates **Google Generative AI** for journaling summaries, emotion detection, meditations, stories, and more. The system runs entirely on a local laptop using SQLite, ensuring privacy and control.

---

## 🛠 Tech Stack

| Category        | Technologies / Libraries |
|-----------------|---------------------------|
| **Language**    | Python 3.x, HTML5, CSS, JavaScript |
| **Frameworks**  | Flask, Jinja2, Bootstrap |
| **Database**    | SQLite, SQLAlchemy ORM, Flask-Migrate |
| **Auth**        | Flask-Login, Flask-WTF (CSRF), WTForms |
| **Security**    | Flask-Limiter (rate limiting), Security headers |
| **AI**          | Google Generative AI (Gemini), Pydantic models |
| **Utilities**   | python-dotenv, Werkzeug, Logging module |

📦 **Notable Dependencies**: `flask`, `sqlalchemy`, `flask-login`, `flask-wtf`, `flask-limiter`, `flask-migrate`, `pydantic`, `google-generativeai`.

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/shahram8708/SahAI.git
cd SahAI

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env   # if provided
# Edit .env and add:
# FLASK_ENV=development
# SECRET_KEY=replace-with-random-string
# DATABASE_URL=sqlite:///instance/sahai.db
# GEMINI_API_KEY=your_google_generative_ai_key

# Initialize database
flask db upgrade   # or simply run python app.py on first start

# Run development server
flask run
````

Visit: [http://localhost:5000](http://localhost:5000)

Optional: Seed demo data

```bash
python -m app.services.seed_data
```

---

## 🚀 Usage Guide

Register an account, then explore modules:

### 🔑 Authentication & Profile

* `/register` – Create account
* `/login` – Log in
* `/profile/edit` – Update avatar, bio, language

### 📔 Journals & Emotions

* `/journal/new` – Write private entry (AI summary + mood detection)
* `/dashboard/emotions` – View heatmap & mood analytics

### 🎵 Music

* `/music/recommend` – Mood-based playlists (Spotify/YouTube)

### ❓ Q\&A

* `/questions/ask` – Ask safe questions (English/Hindi, AI-moderated)

### 🧘 Wellness

* `/wellness/meditation` – Generate short meditation
* `/wellness/doodle/new` – Upload doodle for AI interpretation
* `/wellness/story` – Generate 1-min cultural story
* `/wellness/prompts` – Get resilience prompts

### 🌱 Peer & Study Tools

* `/peer` – Post anonymous supportive notes
* `/exam` – Ask exam copilot for study tips

### ✉️ Letters, 🎨 Art & Comics

* `/letters/new` – Write a future letter with unlock date
* `/art/new` – Generate mood-based art prompt (placeholder PNG)
* `/comics/new` – Turn situations into comic scripts

### 🌳 Gratitude

* `/gratitude` – Add daily gratitude leaves & track streaks

### 🎬 Demo

* `/demo/auto` – Auto cycle through app demo slides

---

## 🌐 API Documentation

SahAI is a **web app**, not a public API. Endpoints return HTML pages.
AI tasks internally exchange JSON via **Pydantic models**.

**Example AI journal response:**

```json
{
  "summary": "string",
  "emotions": {"happy": 0.1, "sad": 0.7},
  "keywords": ["reflection", "study"],
  "language": "en"
}
```

A health probe exists at:

```
/_health/ai
```

---

## 🖥 Frontend Details

* Built with **Jinja2 templates** + **Bootstrap**.
* **Reusable partials** for modals & cards.
* **Forms** handled by Flask-WTF with CSRF.
* **Flash messages** for success/error alerts.
* **Static uploads** stored under `static/uploads` with randomized names.

---

## 📂 Project Structure

```
SahAI/
├── app/
│   ├── ai/           # Gemini client, prompts, tasks
│   ├── journal/      # Journals + Emotion Lens
│   ├── music/        # Music recommender
│   ├── questions/    # AI Q&A
│   ├── wellness/     # Meditation, doodles, stories, prompts
│   ├── peer/         # Peer wall
│   ├── exam/         # Exam copilot
│   ├── letters/      # Future letters
│   ├── art/          # Mood-to-Art generator
│   ├── comics/       # Comic generator
│   ├── gratitude/    # Gratitude tree
│   ├── demo/         # Demo pages
│   ├── user/         # Profiles & settings
│   ├── extensions.py # Extensions setup
│   └── models.py     # SQLAlchemy models
├── config.py
├── app.py
├── requirements.txt
└── instance/         # SQLite DB
```

---

## 🔐 Authentication / Security

* **Flask-Login** for user sessions
* **Password hashing** (securely stored)
* **CSRF protection** via Flask-WTF
* **Rate limiting** with Flask-Limiter
* **Security headers** (CSP enforced)
* **Crisis detection**: filters unsafe inputs
* **File uploads** restricted to PNG/JPEG with randomized names
* **Privacy toggles** in `/privacy`

---

## ⚡ Features Summary

* 📔 AI-summarized journaling with mood detection
* 📊 Emotion Lens with visual analytics
* 🎵 Mood-based music recommendations
* ❓ Safe Q\&A in English/Hindi
* 🧘 Meditation & TTS option
* 🎨 Doodle interpretation & mood snapshot
* 📖 Indian folklore cultural story generator
* ✨ Resilience prompts
* 🌱 Peer support wall
* 📚 Exam study copilot
* ✉️ Future letters with unlock date
* 🎨 Abstract art prompts (placeholder)
* 🎭 Comic script generator (placeholder panels)
* 🌳 Gratitude tree with streak tracking
* 👤 User profiles with privacy controls
* 🎬 Auto demo & pitch deck

---

## 📝 Examples

👉 Run locally and try:

* `/demo/auto` – Auto slideshow of features
* `/dashboard/emotions` – Heatmap of your mood history
* `/gratitude` – Track gratitude leaves

*(Insert screenshots or GIFs here when available)*

---

## 🤝 Contributing Guide

1. **Fork & Branch**

   ```bash
   git checkout -b feature/your-feature
   ```
2. Follow **PEP 8** style guidelines
3. Add tests for new functionality (if applicable)
4. Commit & open a **Pull Request** with clear description
5. For security issues → **contact maintainer privately**

---

## 🧪 Testing Instructions

Currently no formal test suite. Manual testing steps:

1. Register & log in.
2. Post a journal entry → check AI summary & emotions.
3. Visit `/dashboard/emotions` → confirm charts.
4. Ask `/questions/ask` → verify safe AI responses.
5. Generate meditations, doodle interpretations, and stories.
6. Test rate-limiting on `/music/recommend`.
7. Upload & delete avatars → check `static/uploads`.

Planned: `pytest` with Flask test client + CI integration.

---

## 📜 License

⚠️ **No license file yet.**
👉 Recommend adding a permissive license (e.g. **MIT** or **Apache 2.0**) to clarify usage rights.

---

## 📌 Future Improvements

* 🖼 Real image generation for art & comics
* 🌍 Multilingual support beyond English/Hindi
* 📱 Mobile/PWA optimization
* ✅ Automated test suite with CI/CD
* 📊 Anonymised analytics for NGOs/educators
* 🔌 Plugin architecture for 3rd-party modules
* 🐳 Docker & deployment scripts (Heroku, Fly.io, etc.)
* ♿ Accessibility audit (WCAG/ARIA compliance)

---

💡 *SahAI is a work in progress — contributions, ideas, and feedback are warmly welcomed!* 🌸
