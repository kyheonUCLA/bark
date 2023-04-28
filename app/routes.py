from flask import render_template, request, jsonify, send_from_directory
from app import app
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/themes', methods=['POST', 'GET'])
def themes():
    if request.method == 'POST':
        data = request.get_json()
        if data.get('theme'):
            theme_name = data.get('theme')
            message = f'Hello from server! You selected the {theme_name} theme.'
            return jsonify({'success': True, 'message': message, 'data': data})
        else:
            return jsonify({'success': False, 'message': 'Missing theme parameter'})
    else:
        titles=['Fantasy', 'Pixar', 'Western', 'Goofy', 'Sci-FI', 'SpongeBob']
        images = ['fantasy1.jpeg', 'pixar4.jpeg', 'western1.webp', 'western3.jpeg', 'sci-fi1.webp', 'fantasy1.jpeg']
        return render_template('themes.html', images=images, titles=titles)

@app.route('/build', methods=['POST', 'GET'])
def build():
    return render_template('build.html')

@app.route('/test2', methods=['POST', 'GET'])
def test2():
    titles=['Fantasy', 'Pixar', 'Western', 'Goofy', 'Sci-FI', 'SpongeBob']
    images = ['fantasy1.jpeg', 'pixar4.jpeg', 'western1.webp', 'western3.jpeg', 'sci-fi1.webp', 'fantasy1.jpeg']
    if request.method == "POST":
        return request.get_json()
    else:
        return render_template('test2.html', images=images, titles=titles)