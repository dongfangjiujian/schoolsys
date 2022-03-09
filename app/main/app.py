from flask import Flask 
from flask import request
from flask import make_response
from flask import redirect,session,url_for,flash
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import Form,StringField,SubmitField,ValidationError
from wtforms.validators import DataRequired
from datetime import datetime
from form import Info
from generate import generate
from pathlib import Path
from flask_script import Manager,Command

from add_pic import addPic

app = Flask(__name__)
app.config['SECRET_KEY']='dongfangjiujian111'
bootstrap=Bootstrap(app)
moment=Moment(app)
manager=Manager(app)

class NameForm(FlaskForm):
	"""docstring for NameForm"""

	name=StringField('你的名字',validators=[DataRequired()])
	submit= SubmitField('提交')


@app.route('/',methods=['GET','POST'])
def index():
	user_agent=request.headers.get('User_Agent') 
	# return '<h1>Hello</h1><p>'+user_agent+'</p>'
	# return '<h1>%s</h1>' % user_agent ,400
	response=make_response('<h1>cookie</h1>')
	response.set_cookie('name','zuoxu')
	name=None
	formData=None
	form=NameForm()
	infoForm=Info()
	# if form.validate_on_submit():
	# 	old_name=session.get('name')
	# 	if old_name is not None and old_name !=form.name.data:
	# 		flash('换名字了吗？')
	# 	session['name']=form.name.data
	# 	form.name.data=''
	# 	return redirect(url_for('index'))
	if infoForm.validate_on_submit():
		formData=request.form
		fn=generate(**formData)
		file=infoForm.photo.data
		pic_name=fn+Path(file.filename).suffix
		doc_name=fn+".docx"
		file.save('docs/'+pic_name)
		
		addPic(doc_name,pic_name)
		
		session['name']=infoForm.name.data
		return redirect(url_for('success'))
	return render_template('index.html',current_time=datetime.utcnow(),infoForm=infoForm,name=session.get('name'))
@app.route('/success')
def success():
	return render_template('success.html',name=session.get('name'))
@app.route('/user/<name>')
def user(name):
	 
	return render_template('user.html',name=name)
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')


if __name__ == '__main__':
	# app.run(debug=True)
	manager.run()