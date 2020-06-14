from flask import Flask,render_template,url_for,redirect
from forms import Input_Form
import pickle
import numpy as np

app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
model=pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def home():	
	return render_template('home.html',title='Result')


@app.route('/result',methods=['GET','POST'])
def result():
	form=Input_Form()
	if form.validate_on_submit():
		a=form.number.data
		a=model.predict([[a]])
		return render_template('result.html', title='Result',a=' Predicted Salary is ₹ {:.2f}'.format(a[0]),form=form)
	return render_template('result.html', title='Result',form=form)

if __name__ == ('__main__'):
    app.run(debug=True)
    