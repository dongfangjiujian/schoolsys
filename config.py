import os
basedir=os.path.abspath(os.path.dirname(__file__))
print(basedir)
print(os.path.dirname(__file__))

class Config:
	"""docstring for Config"""
	def __init__(self, arg):
		super(Config, self).__init__()
		self.arg = arg

	SECRET_KEY=os.environ.get('SECRET_KEY') or "dongfangjiujian111"
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	"""docstring for DevelopmentConfig"""
	def __init__(self, arg):
		super(DevelopmentConfig, self).__init__()
		self.arg = arg
	DEBUG=True
		
config ={
	'development':DevelopmentConfig,
	'default':DevelopmentConfig
}		