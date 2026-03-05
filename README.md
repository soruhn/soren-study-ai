# Soren AI Study Helper 📚

An intelligent AI-powered study companion built with Flask and Google Gemini. Get instant explanations for complex problems and generate practice questions to master any subject.

## Features

✨ **Key Features:**
- 🤖 **AI-Powered Explanations** - Get step-by-step breakdowns of any problem
- 📝 **Practice Questions** - Generate custom questions at Easy, Medium, or Hard difficulty
- 💾 **Study Sessions** - Automatically save all your study sessions
- 📋 **Copy to Clipboard** - One-click copying of explanations and answers
- 🎨 **Modern UI** - Beautiful, responsive interface with smooth animations
- ⚡ **Real-time Responses** - Instant feedback powered by Gemini AI

## Installation

### 1. Install Python Dependencies

```bash
pip install flask google-genai
```

### 2. Set Up Your Google Gemini API Key

If requests ran out for the day you can create your own personal key if needed and import it where the key was in line 11,
"os.environ['GEMINI_API_KEY'] = 'AIzaSyAo8qT2pjo9MNyrkx_2BozjYVKw5qFuzHQ'" replace the AIzaSy with your own personal one got from google ai studio.

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

The app will automatically use the API key in the code. You can also set it as an environment variable:

```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Windows CMD
set GEMINI_API_KEY=your-api-key-here
```

### 3. Run the Application

```bash
python "soren test 3 (gemini version).py"
```

The app will start on `http://localhost:5000`

## How to Use

### 📖 Explain Problems Tab

1. Copy or type a problem you need help understanding
2. Paste it in the "Enter Your Problem" text area
3. Click **"Get Explanation"**
4. Wait for the AI to generate a step-by-step explanation
5. Click **"Copy"** to copy the explanation to your clipboard
6. Your session is automatically saved!

**Example problems:**
- "What is photosynthesis and how does it work?"
- "Solve: 2x² + 5x - 3 = 0"
- "Explain the causes of World War II"

### 🎯 Practice Questions Tab

1. Enter a topic you want to practice (e.g., "Calculus", "Spanish Verbs", "Biology")
2. Select a difficulty level:
   - **Easy** - Basic concepts and simple problems
   - **Medium** - Standard problems and mixed topics
   - **Hard** - Advanced problems and complex scenarios
3. Click **"Generate Questions"**
4. Review the 3 practice questions and answers
5. Click **"Copy"** to copy all questions to your clipboard
6. Your practice session is saved automatically!

### 📚 Study Sessions Tab

View all your previous study sessions:
- **See all explanations and practice questions** you've generated
- **View timestamps** for each session
- **Delete sessions** you no longer need
- Sessions are saved in memory while the app runs

**Note:** Sessions are stored in memory. If you restart the app, previous sessions will be cleared. For persistent storage, consider upgrading to a database.

## Project Structure

```
Soren AI Study Helper/
│
├── soren test 3 (gemini version).py  # Flask backend
├── templates/
│   └── index.html                    # Web interface
└── README.md                         # This file
```

## Features in Detail

### Auto-Save Sessions
Every explanation and practice question set is automatically saved to your Study Sessions history. No extra clicks needed!

### Copy Functionality
Click the "Copy" button on any response to instantly copy it to your clipboard. The button shows "✓ Copied!" for 2 seconds to confirm.

### Responsive Design
The app works on desktop, tablet, and mobile browsers with a clean, modern interface.

### Real-time Feedback
Get instant responses using Google's Gemini 2.5 Flash model - one of the fastest and most efficient AI models available.

## Troubleshooting

### "Error: Failed to get explanation"

**Check the Flask terminal for details:**
1. Look at the terminal where you ran the Flask app
2. You should see a detailed error message
3. Common issues:
   - **Invalid API key** - Make sure your GEMINI_API_KEY is correct
   - **Network error** - Check your internet connection
   - **Model unavailable** - The app uses `gemini-2.5-flash` by default

### Port 5000 Already in Use

If you get "Address already in use":
```bash
# Kill the process using port 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or change the port in the code:
# Change: app.run(debug=True)
# To: app.run(debug=True, port=5001)
```

### Sessions Lost After Restart

Sessions are stored in memory. To make them permanent, you'd need to add a database (SQLite, MongoDB, etc.). Currently, the app clears sessions when restarted.

### Button/Styling Issues

Try these steps:
1. **Hard refresh** your browser: `Ctrl+Shift+R`
2. **Clear browser cache** or open in incognito/private mode
3. **Restart Flask** and reload the page

## Advanced Setup (Optional)

### Use a Different AI Model

You can change the model in the Python file:

```python
# Find these lines and change "gemini-2.5-flash" to another model:
response = client.models.generate_content(
    model="gemini-2.5-pro",  # Change here
    contents=prompt
)
```

Available models include:
- `gemini-2.5-flash` (fastest, recommended)
- `gemini-2.5-pro` (more powerful, slower)
- `gemini-3-flash-preview` (latest preview)

### Enable Debug Tips

The app is already in Flask debug mode. To see more detailed error messages, check the terminal output when an error occurs.

## Tips for Best Results

✅ **Write clear problems:** "Explain photosynthesis step-by-step" is better than "photosynthesis"

✅ **Copy answers immediately:** Some browsers may forget clipboard data if you navigate away

✅ **Use appropriate difficulty:** Match the difficulty to your skill level for effective learning

✅ **Review generated answers:** AI is helpful but not always perfect - verify important information

✅ **Use the study sessions:** Review your past sessions to track your learning progress

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** 512MB minimum (1GB+ recommended)
- **Storage:** 100MB for dependencies
- **Internet:** Required for API calls to Google Gemini

## License

Feel free to use and modify this project for your personal or educational use.

## Support

If you encounter issues:

1. Check the **Troubleshooting** section above
2. Review the **Flask terminal output** for error messages
3. Verify your **API key** is valid
4. Ensure your **internet connection** is working

## Future Enhancements

Possible improvements:
- 💾 Database integration for persistent session storage
- 🎓 Subject-specific prompts for better answers
- 📊 Progress tracking and statistics
- 🌙 Dark mode toggle
- 🗣️ Text-to-speech for explanations
- 📱 Mobile app version

---

Happy studying! 🎉
