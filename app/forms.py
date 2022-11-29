from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class Client(FlaskForm):
    name = StringField("Nombre:", validators=[DataRequired()])
    document = StringField("Dni:", validators=[DataRequired()])
    address = StringField("Direccion", validators=[DataRequired()])
    phone = StringField("Telefono", validators=[DataRequired()])
    status = BooleanField("Estado")
    submit = SubmitField("Ingresar")