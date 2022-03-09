from mailmerge import MailMerge
from datetime import time,datetime

template='static/template.docx'

document=MailMerge(template)
	
def generate(**dict):

	# for field in document.get_merge_fields() :
		
	# 	for k,v in dict.items():
	# 		if k in field :



	# 			new_dict[k]=v
	# 			print(new_dict)
				
	# document.merge(new_dict)
	# document.write('zuoxu.docx') 

	timestamp=datetime.now().strftime(r"%H%M%S")
	filename=dict['name']+timestamp
	finalname="docs/"+filename+'.docx'
	document.merge(**dict)

	document.write(finalname) 
	return filename
