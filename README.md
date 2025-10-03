# 🪨 📄 ✂️ Rock Paper Scissors (Flask)

A modern, interactive Rock-Paper-Scissors web game built using **Python Flask** with a beautiful, responsive UI and persistent score tracking.

## ✨ Features

- 🎮 **Interactive Gameplay**: Choose between Rock, Paper, or Scissors with visually appealing buttons
- 🎨 **Modern UI**: Beautiful gradient backgrounds, smooth animations, and responsive design
- 📊 **Score Tracking**: Persistent score tracking across browser sessions using Flask sessions
- 🏆 **Game Statistics**: Track wins, losses, and ties with a reset option
- ⚡ **Error Handling**: Proper validation for invalid choices
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- 🔄 **Reset Functionality**: Reset your score anytime with a single click

## 🎯 Game Rules

- **Rock** beats **Scissors**
- **Paper** beats **Rock**
- **Scissors** beats **Paper**
- Same choices result in a **tie**

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors-flask.git
   cd rock-paper-scissors-flask
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:5000` to start playing!

## 🎮 How to Play

1. Click on one of the three choice buttons (Rock 🪨, Paper 📄, or Scissors ✂️)
2. The computer will randomly select its choice
3. View the results in the battle arena with visual feedback
4. Check your persistent score below the results
5. Click "Reset Score" anytime to start fresh
6. Keep playing to improve your statistics!

## 📁 Project Structure

```
rock-paper-scissors/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Game interface template
├── static/
│   └── style.css         # Game styling and animations
└── README.md             # This file
```

## 🔧 Technical Details

- **Framework**: Flask 3.0.0
- **Frontend**: HTML5, CSS3 with modern animations
- **Session Management**: Flask sessions for score persistence
- **Responsive**: Mobile-first design with CSS Grid and Flexbox
- **Error Handling**: Input validation and graceful error messages

## 🚀 Deployment

This application can be deployed to various platforms:

- **Heroku**: Add a `Procfile` and deploy via Git
- **PythonAnywhere**: Upload files and configure WSGI
- **Railway**: Connect your GitHub repository
- **Render**: Deploy directly from Git

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Emoji icons from Unicode Emoji standard
- Gradient backgrounds inspired by modern web design trends

---

**Enjoy the game and may the best player win! 🍀**
