import random, string
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shortlink.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(20), unique=True, nullable=False)




def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_url = request.form['full_url']
        short_code = generate_short_code()
        new_url = URL(full_url=full_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()
        return render_template('short_url.html', short_code=short_code)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    print(short_code)
    if url_entry:
        return redirect(url_entry.full_url)
    return "URL Not Found!", 404


@app.route('/links')
def links():
    urls=URL.query.all()
    return render_template('all_links.html',urls=urls)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()

    app.run(debug=True)
