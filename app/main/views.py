from flask import redirect,render_template,url_for,session,request
from datetime import datetime
# from .generate import generate
from . import main
from .forms import Info


@main.route('/',methods=['GET','POST'])
def index():
	infoForm=Info()
	if infoForm.validate_on_submit():
		data=request.form
		return redirect(url_for('.index'))
	return render_template('index.html',infoForm=infoForm)