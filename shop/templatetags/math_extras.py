from django import template

register = template.Library()

def mult(value, arg):
	"""
		Multiplies the values
	"""
	return int(value) * int(arg)

register.filter('mult', mult)