from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    name = StringField('Enter search value', validators=[DataRequired(), Length(min=1)])
    search = SubmitField(label='Search!')
