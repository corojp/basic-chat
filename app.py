from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        data = request.get_json()
        user_query = data['query']
        
        # Placeholder response
        response_message = f"Response: {user_query}"
        
        return jsonify({"response": response_message})
    
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
