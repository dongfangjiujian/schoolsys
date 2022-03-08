from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired,FileAllowed
from wtforms import HiddenField,FloatField,StringField,SubmitField,SelectField,TelField,TextAreaField,DateField,FileField,ValidationError
from wtforms.validators import DataRequired,Regexp,Length,NumberRange
from datetime import date


class Info(FlaskForm):
	"""docstring for Info"""
	def __init__(self, *arg):
		super(Info, self).__init__()
		self.arg = arg
	def id_check(form,field):
		if len(field.data)!=18:
			raise ValidationError('身份证号码错误，请重新输入')
	tb=date.today()
	tianbao=HiddenField(render_kw={'value':tb})
	xueji=StringField('学籍号*',validators=[DataRequired()])
	name=StringField('姓名*',validators=[DataRequired()])
	# sex=SelectField('性别*',choices=['男','女'],validators=[DataRequired()])
	
	# minzu=StringField('民族*',validators=[DataRequired()])
	# shengri=DateField(('出生日期*'),validators=[DataRequired()])
	# ID=StringField('身份证号*',validators=[DataRequired(),Length(min=18,max=18),
	# 	Regexp(r'^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',0,'格式不正确')
	# 	])

	# zhuanye=StringField('报考专业*',validators=[DataRequired()])

		
	# xuexiao=StringField('毕业学校*',validators=[DataRequired()])
	# zhuzhi=StringField('家庭住址*',validators=[DataRequired()])
	# huji=StringField('户籍所在地*',validators=[DataRequired()])
	# shengao=FloatField('身高(米)*',validators=[DataRequired('请输入数字'),NumberRange(min=1.4,max=2.2,message='范围1.40-2.20')])
	# tizhong=FloatField('体重(公斤)*',validators=[DataRequired(),NumberRange(min=35,max=90,message='范围35-90')],render_kw={'test':'neirong'})
	# dianhua1=StringField('电话1*',validators=[
	# 	DataRequired(),
	# 	Length(min=11,max=11),
	# 	Regexp(r'1[3687459]\d{9}',message="手机号码格式不正确")])
	# dianhua2=TelField('电话2')
	# jiangli=TextAreaField('何种奖励*',validators=[DataRequired(message='没有请填无')])
	photo=FileField(label='一寸照片*',validators=[FileRequired(),FileAllowed(['jpg','png'],message='请上传jpg或png格式照片')])


	submit=SubmitField('提交')