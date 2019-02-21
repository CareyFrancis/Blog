
from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('SUBMIT')

class BlogForm(FlaskForm):
    content = TextAreaField('YOUR BLOG')
    submit = SubmitField('Create Blog')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on this blog:', validators=[Required()])
    submit = SubmitField('SUBMIT')

class SubscribeForm(FlaskForm):
    email = StringField("Enter email", validators = [Required()])
    submit = SubmitField("Subscribe")

