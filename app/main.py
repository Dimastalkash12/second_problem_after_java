import os
import json

from flask_login import login_required,LoginManager,login_user,logout_user,current_user
from werkzeug.security import generate_password_hash

from User import User
from db import Leagues
from sqlalchemy import select,desc
import requests
from sqlalchemy.testing.suite.test_reflection import users
from datetime import datetime , timedelta
from Playmaker import playmaker
from db import db
from db import Playmakers
from db import Users
from League import League
from flask import Flask, render_template, redirect, request, jsonify, url_for,flash
from Footballers import Footballers
from forms import LoginForms,RegisterForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

app.config['SECRET_KEY'] = 'top secret'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# connection with authorization
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
api = "330758c4f9d6b00a73af59708b090e4d"
hiders = {"x-apisports-key": api}
response = requests.get("https://v3.football.api-sports.io/leagues", headers=hiders)
league = League(api)
footballers = Footballers(api)
# footballers.getPlayer(hiders, 307, 'Cristiano')
db.init_app(app)
# with app.app_context():
#     leagues=Leagues.query.all()
#     for i in leagues:
#         print(i.country,flush=True)
#     # db.drop_all()
#     # db.create_all()
#     # with open("output.json",'r',encoding='utf-8') as file:
#     #     json1=json.loads(file.read())
#     # for i in json1:
#     #     league2= Leagues(id=i['league']['id'],name=i['league']['name'],country=i['country']['name'])
#     #     db.session.add(league2)
#     #     db.session.commit()


#---------------------------------------------------------------

    # user = Users(login='admin2', password='12345', rights='admin')
    # db.session.add(user)
    # db.session.commit()
    #
    # results = Users.query.all()
    # for i in results:
    #     print(i.login)
    #
    # user=Users.query.filter_by(login='admin1').first()
    # print(user.login)
    #
    # logins=['admin1','admin2']
    # users1=Users.query.filter(Users.login.in_(logins)).all()
    # for i in users1:
    #     print(i.rights)

    # user=Users.query.filter_by(login='admin1').first()
    # user.password='54321'
    # db.session.commit()
    # print(user.password)

    # user = Users.query.filter_by(login='admin1').first()
    # db.session.delete(user)
    # db.session.commit()
# ------------------------------------------------------------
# операции база данных

@app.route('/main')
@app.route('/')
def main():
    return render_template('main.html')

@login_manager.user_loader
def load_user(userId):
    return User.get(userId)


#
#
# @app.route('/about')
# def about():
#     pass

@app.route('/logIn', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('mine'))
    form = LoginForms()
    if form.validate_on_submit():
        user = User.auth(form.login.data, form.password.data)
        if user:
            login_user(user)
            return redirect(url_for('mine'))
    return render_template('Login.html', form=form)


@app.route('/Mine', methods=['POST', 'GET'])
def mine():
    tops = []
    query=(db.session.query(Playmakers).order_by(Playmakers.numOfReq.desc()).limit(10))
    result=query.all()
    return render_template('Mine.html', tops=result)


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    name = data['name']
    league = data['league']
    r = Playmakers.query.filter_by(name=name).first()
    if r and datetime.now()-r.date>timedelta(minutes=10):
        playmaker = footballers.getPlayer(hiders, league, name)
        result = {
            'name': playmaker.name,
            'lastname': playmaker.lastname,
            'age': playmaker.age,
            'birth': playmaker.birth,
            'nationality': playmaker.nationality,
            'height': playmaker.height,
            'weight': playmaker.weight,
            'photo': playmaker.photo,
            'statistics': playmaker.statistics

        }
        r.name=playmaker.name
        r.lastname=playmaker.lastname
        r.data=result
        r.league=league
        r.numOfReq+=1
        r.date=datetime.now()
    elif r:
        r.numOfReq+=1
        result=r.data
    else:
        playmaker = footballers.getPlayer(hiders, league, name)
        result = {
            'name': playmaker.name,
            'lastname': playmaker.lastname,
            'age': playmaker.age,
            'birth': playmaker.birth,
            'nationality': playmaker.nationality,
            'height': playmaker.height,
            'weight': playmaker.weight,
            'photo': playmaker.photo,
            'statistics': playmaker.statistics

        }
        r=Playmakers(name=f'{playmaker.name}',lastname = f'{playmaker.lastname}',league = data['league'],numOfReq=1,data=result,date=datetime.now())
    db.session.add(r)
    db.session.commit()
    return jsonify({'result': result})

@app.route('/api/league')
def searchLeag():
    req=request.args.get('search','')
    league3=Leagues.query.filter(Leagues.name.ilike(f'%{req}%')).limit(10).all()
    return jsonify([
        {
            'id':l.id,
            'name':l.name,
            'country':l.country
        }
        for l in league3
    ])
@app.route('/logOut')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/auth',methods=['POST','GET'])
def auth():
    if current_user.is_authenticated:
        return redirect(url_for('mine'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.get(form.login.data)
        if user is None:
            newUser=Users(login=form.login.data,password=generate_password_hash(form.password.data),rights='user')
            db.session.add(newUser)
            db.session.commit()
            authUser=User.auth(form.login.data,form.password.data)
            login_user(authUser)
            return redirect(url_for('mine'))
        else:
            flash(['this login have already been','red'])
            return render_template('Register.html',form=form)
    return render_template('Register.html', form=form)


# @app.route('/urStory')
# def viewStory():
#

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False, host="0.0.0.0", port=5000)
