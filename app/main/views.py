from flask import session,redirect,render_template,url_for,session,request
from datetime import datetime
from .generate import generate
from . import main
from .forms import Info


@main.route('/',methods=['GET','POST'])
def index():
	infoForm=Info()
	if infoForm.validate_on_submit():
		
		data=request.form
		session['name']=infoForm.name.data

		file=infoForm.photo
		print(data)
		print(type(data))
		generate(data,file)
		return redirect(url_for('.success'))
	return render_template('index.html',infoForm=infoForm)
@main.route('/success')
def success():
	return render_template('big_success.html',name=session.get('name'))