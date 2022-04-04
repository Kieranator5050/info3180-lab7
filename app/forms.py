# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import InputRequired, DataRequired

extensions = ['jpg','png','apng','avif','webp',
'gif','jpeg','jfif','pjpeg','pjp','svg']

class UploadForm(FlaskForm):
    description = TextAreaField('Description',
                                    validators=[
                                        InputRequired(), 
                                        DataRequired()
                                        ])
                                        
    photo = FileField('img_file', 
                            validators=[
                                FileRequired(), 
                                FileAllowed(extensions, "Only Images!" )
                                ])