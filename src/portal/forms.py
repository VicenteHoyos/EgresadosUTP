from django import forms

from .models import Registrado,InvitacionAdmin, Contacto #se importa el modelo

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email",]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		if proveeder == "gmail.com":
			raise forms.ValidationError("Por favor utiliza un correo institucional @utp.edu.co")
		else:
			dominio, extension, pais = proveeder.split(".")
			if dominio =="utp":
				if extension == "edu":
					if pais == "co":
						return email
			raise forms.ValidationError("Por favor utiliza un correo institucional @utp.edu.co")

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre

class InvitacionAdminForm(forms.ModelForm):
	class Meta:
		model = InvitacionAdmin
		fields = ["nombre", "email",]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		if proveeder == "gmail.com":
			raise forms.ValidationError("Por favor utiliza un correo institucional @utp.edu.co")
		else:
			dominio, extension, pais = proveeder.split(".")
			if dominio =="utp":
				if extension == "edu":
					if pais == "co":
						return email
			raise forms.ValidationError("Por favor utiliza un correo institucional @utp.edu.co")
		

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre
		
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ["nombre","comentario",]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		if proveeder == "gmail.com":
			raise forms.ValidationError("Por favor utiliza un correo institucional @utp.edu.co")
		else:
			dominio, extension, pais = proveeder.split(".")
			if dominio =="utp":
				if extension == "edu":
					if pais == "co":
						return email
			raise forms.ValidationError("Por favor utiliza un correo institucional @utp.edu.co")
		

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre