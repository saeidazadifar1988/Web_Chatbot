# Web_Chatbot
A Simple Chatbot with open Source LLMs using Flask and Hugging Face

## Features

- AI-powered conversational chatbot
- Web interface built with HTML, CSS, and JavaScript
- Flask backend for handling requests
- Open-source LLM from Hugging Face
- Conversation history support
- REST API communication between frontend and backend
- Easy to customize and extend

---

## Project Structure

```
Web_Chatbot/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Chatbot web interface
│
├── static/
│   ├── script.js           # Frontend JavaScript
│   ├── style.css           # Stylesheet
│   └── assets/             # Images and other static files
│
└── README.md
```

---

## Technologies Used

- Python 3
- Flask
- Hugging Face Transformers
- PyTorch
- HTML
- CSS
- JavaScript

---

## Model

This project uses the following open-source conversational model:

- **facebook/blenderbot-400M-distill**

The model is automatically downloaded from Hugging Face the first time the application is executed.