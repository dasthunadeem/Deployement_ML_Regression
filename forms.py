from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField,TextField
from wtforms.validators import DataRequired

class Input_Form(FlaskForm):
	number = FloatField('Enter your Expirience here:',validators=[DataRequired()])
	submit = SubmitField('Predict')

