from flask import Flask, url_for, request,render_template,redirect
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db=SQLAlchemy(app)



class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    motivation = db.Column(db.String(50), nullable=False)
    in_mars=db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return '<Form %r>' % self.id

@app.route('/')
@app.route('/home')
def root():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/promotion')
def promotion():
    return render_template('promotion.html')


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/astronaut_selection',methods=['POST','GET'])
def astronaut_selection():
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        email = request.form['email']
        profession = request.form['profession']
        gender = request.form['gender']
        motivation = request.form['motivation']
        in_mars = request.form['in_mars']
        
        form=Form(last_name=last_name, first_name=first_name, email=email, profession=profession, gender=gender,motivation=motivation, in_mars=in_mars)
        try:
            db.session.add(form)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении произошла ошибка"
    else:
        return render_template('astronaut_selection.html')
    

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <title>results</title>
</head>
    <body class="d-flex h-100 text-center text-bg-dark">
    
        <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
          <header class="mb-auto">
            <div>
              <h3 class="float-md-start mb-0">Лабораторная №1</h3>
              <nav class="nav nav-masthead justify-content-center float-md-end">
                <a class="nav-link fw-bold py-1 px-0 active" aria-current="page" href="#">Home</a>
                <br><a class="nav-link"></a>
                <a class="nav-link fw-bold py-1 px-0" href="#">Contact</a>
              </nav>
            </div>
          </header>
          
          <main class="px-3">
            <h2> отбор {str(level)} уровня</h2>
            <div>привет {nickname}, твой рейтинг: {str(rating)}</div>
          </main>
        
          <footer class="mt-auto text-white-50">
            <p>Лабораторная <a href="#" class="text-white">Шевелева Кирилла</a>, by <a href=https://github.com/kirill89450" class="text-white">@kirill89450</a>.</p>
          </footer>
        </div>
        
        
            
          
        
        <div class="mallbery-caa" style="z-index: 2147483647 !important; text-transform: none !important; position: fixed;"></div><div class="mallbery-caa" style="z-index: 2147483647 !important; text-transform: none !important; position: fixed;"></div><div class="mallbery-caa" style="z-index: 2147483647 !important; text-transform: none !important; position: fixed;"></div>
    </body>
</html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')