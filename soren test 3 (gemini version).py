from flask import Flask, render_template, request, jsonify, session
from google import genai
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure Gemini API
os.environ['GEMINI_API_KEY'] = 'AIzaSyCGxOPhegyT_SMQcOF6lkK1kla5BQdMJLY'
client = genai.Client()

# List available models
print("Available models:")
for model in client.models.list():
    print(f"  - {model.name}")

# In-memory storage for study sessions
study_sessions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/explain', methods=['POST'])
def explain_problem():
    data = request.json
    problem = data.get('problem', '')
    
    if not problem:
        return jsonify({'error': 'No problem provided'}), 400
    
    try:
        prompt = f"You are a helpful tutor. Explain this problem step-by-step:\n\n{problem}\n\nProvide a clear, educational explanation."
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({'explanation': response.text})
    except Exception as e:
        print(f"ERROR in explain_problem: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/api/practice', methods=['POST'])
def generate_practice():
    data = request.json
    topic = data.get('topic', '')
    difficulty = data.get('difficulty', 'medium')
    
    if not topic:
        return jsonify({'error': 'No topic provided'}), 400
    
    try:
        prompt = f"Generate 3 practice questions about {topic} at {difficulty} difficulty level. Format as numbered list with answers below."
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({'questions': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/save-session', methods=['POST'])
def save_session():
    data = request.json
    session_data = {
        'id': len(study_sessions) + 1,
        'timestamp': datetime.now().isoformat(),
        'topic': data.get('topic', 'Untitled'),
        'content': data.get('content', ''),
        'notes': data.get('notes', '')
    }
    study_sessions.append(session_data)
    return jsonify({'success': True, 'session_id': session_data['id']})

@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    return jsonify(study_sessions)

@app.route('/api/sessions/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    global study_sessions
    study_sessions = [s for s in study_sessions if s.get('id') != session_id]
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)