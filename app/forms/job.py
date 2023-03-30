from flask_wtf import FlaskForm
from wtforms import (
        PasswordField,
        SubmitField,
        BooleanField,
        StringField,
    )


# Добавление работы (модель)
class AddJobForm(FlaskForm):
    team_leader = StringField("Team Leader id")
    job_title = StringField('Job Title')
    work_size = StringField("Work Size")
    collaborators = StringField("Collaborators")
    is_finished = BooleanField("job is finished?")

    submit = SubmitField('Submit')
