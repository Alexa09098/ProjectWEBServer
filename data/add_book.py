from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    genre = StringField('Жанр', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    end_date = StringField('Дата написания', validators=[DataRequired()])
    bought = BooleanField('Работа окончена?')
    author = IntegerField('Автор', validators=[DataRequired()])

    submit = SubmitField('Отправить')
