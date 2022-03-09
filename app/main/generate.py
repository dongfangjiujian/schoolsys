from mailmerge import MailMerge
from datetime import time,datetime
from docxtpl import DocxTemplate,InlineImage
from docx import Document
from docx.shared import Cm

template='app/static/template_jinja.docx'


	
def generate(dict,file):

	document=DocxTemplate(template)


	timestamp=datetime.now().strftime(r"%H%M%S")
	filename=dict['name']+timestamp
	finalname="docs/"+filename+'.docx'

	img=InlineImage(document,file.data,width=Cm(2.5),height=Cm(3.5))
	# dict={
	# 'name':'zuoxu',
	# 'xueji':'sdf'
	# }
	context=dict.copy()
	context['img']=img

	
	# document.render({'img':img})
	document.render(context)

	document.save(finalname) 
	return filename
