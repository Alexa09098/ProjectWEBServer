from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Название', validators=[DataRequired()])
    team_leader = IntegerField('id капитана', validators=[DataRequired()])
    work_size = StringField('Объем работы', validators=[DataRequired()])
    collaborators = StringField('Сотрудники', validators=[DataRequired()])
    is_finished = BooleanField('Работа окончена?')

    submit = SubmitField('Отправить')
