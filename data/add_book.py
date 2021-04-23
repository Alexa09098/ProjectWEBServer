from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddBookForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    genre = StringField('Жанр', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    end_date = StringField('Дата написания', validators=[DataRequired()])
    is_bought = BooleanField('Книга куплена?')
    author = IntegerField('Автор', validators=[DataRequired()])

    submit = SubmitField('Отправить')
