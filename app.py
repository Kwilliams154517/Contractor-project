from flask import Flask, render_template

app = Flask(__name__)

bang = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

@app.route('/bang')
def bang_index():
    """Show all bang."""
    return render_template('bang_index.html', bang=bang)

@app.route('/')
def home():
	""" Return render home template"""
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)