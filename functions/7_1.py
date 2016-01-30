def myxml(tagname, content = '', **attributes):
	attrs = ''
	for name, value in attributes.items():
		attrs += ' {}="{}"'.format(name,value)
	return "<{tagname}{attrs}>{content}</{tagname}>".format(tagname = tagname, attrs = attrs, content = content)
	
print myxml('foo')
print myxml('foo', 'bar')
print myxml('p', myxml('i', myxml('b', 'Hello')))
print myxml('foo', 'bar', a = 1, b = 2)