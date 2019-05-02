import os

class Config(object):
	"""docstring for Config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
