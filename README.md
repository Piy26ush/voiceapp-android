# Voice Assistant App (Android + Flask Backend)

This repository contains a complete voice assistant system with:

- **React Native Android App** (`AndroidAssistantApp/`)  
  Handles voice recognition, intent display, and user interaction.

- **Flask Backend** (`assistant-backend/`)  
  Receives transcript text and returns predicted intent.

## 🛠 Structure

```
voiceapp-android/
├── AndroidAssistantApp/   # React Native frontend app
├── assistant-backend/     # Flask backend for intent recognition
├── README.md              # Project overview and instructions
```

## 📦 How to Run

### React Native App

1. Navigate to `AndroidAssistantApp`
2. Install dependencies: `npm install`
3. Run Metro: `npx react-native start`
4. Launch on device: `npx react-native run-android`

### Flask Backend

1. Navigate to `assistant-backend`
2. Install dependencies: `pip install -r requirements.txt`
3. Start server: `flask run --host=0.0.0.0 --port=5001`

## 🌐 Network Communication

The Android app auto-detects local IP and sends POST requests to `/predict` endpoint of the Flask server.

## 👤 Author

[Piyush Waghjale](https://github.com/Piy26ush)

---
