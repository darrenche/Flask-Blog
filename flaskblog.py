from flask import Flask, render_template
app = Flask(__name__)

# dummy data for displaying purposes
posts = [
    {
        'author' : 'Darren He',
        'title'  : 'Blog Post 1',
        'content': 'First post content',
        'date_posted' : 'June 26, 2019'
    },
    {
        'author' : 'Doe John',
        'title'  : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted' : 'June 10, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)