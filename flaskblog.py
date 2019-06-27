from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e4a05354109c6bae62b42356949aa62e'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)