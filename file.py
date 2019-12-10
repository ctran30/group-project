import os
print('__file__',__file__) #print the string of file variable
print('dirname', os.path.dirname(__file__))
print('abspath', os.path.abspath(os.path.dirname(__file__)))

basedir = os.path.abspath(os.path.dirname(__name__))
print(os.path.join(basedir, 'app.db'))