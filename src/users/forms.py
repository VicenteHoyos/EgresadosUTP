from django import forms

from .models import User
from posts.models import Interes


class userForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={"imagen_Perfil",
        "username",
        "first_name",
        "last_name",
        "email", 
         "website",
         "telefono",
         "ciudad", 
         "dni_administrador",
         "fecha_Nacimiento",
         "genero",
         "Confirmacion_manejo_datos_sensibles",
         "biografia"
        }

class userEgresadoForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={"imagen_Perfil",
        "username",
        "first_name",
        "last_name",
        "email", 
         "website",
         "telefono",
         "ciudad", 
         "dni_administrador",
         "fecha_Nacimiento",
         "genero",
         "Confirmacion_manejo_datos_sensibles",
         "biografia",
         'categorias'
        }
        widgets = {
         'categorias': forms.CheckboxSelectMultiple(),
        }
    # categorias = forms.ModelMultipleChoiceField(queryset=Interes.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['categorias'] = [t.pk for t in 
                kwargs['instance'].categorias.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.categorias.clear()
            for interes in self.cleaned_data['categorias']:
                instance.categorias.add(interes)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        #if commit:
        instance.save()
        self.save_m2m()

        return instance

class userAgregarInteresForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
          'categorias'
        }
        widgets = {
         'categorias': forms.CheckboxSelectMultiple(),
        }
    # categorias = forms.ModelMultipleChoiceField(queryset=Interes.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['categorias'] = [t.pk for t in 
                kwargs['instance'].categorias.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.categorias.clear()
            for interes in self.cleaned_data['categorias']:
                instance.categorias.add(interes)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        #if commit:
        instance.save()
        self.save_m2m()

        return instance

class userEnableForm(forms.ModelForm):
    class Meta:
        model = User
        fields ={
        # "username",
        # "email", 
        "Administrador", 
        }

class userEnableEgresadoForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        # "username",
        # "email", 
        "Egresado", 
        }

class userDisableForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        # "username",
        # "email",
        "Administrador", 
        }
class userDisableEgresadoForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        # "username",
        # "email",
        "Egresado", 
        }

class userAdminUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        "username",
        "first_name",
        "last_name",
        "email", 
         "website",
         "telefono",
         "ciudad", 
         "genero",
         "biografia"
        }

class userEgresadoUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields ={
        "username",
        "first_name",
        "last_name", 
         "website",
         "telefono",
         "ciudad",
         "biografia",
        }
    # class Meta:
    #     model = Post
    #     fields = ('titulo', 'imagen', "contenido", "publish")    
    #     # widgets = {
    #     #      'categorias': forms.CheckboxSelectMultiple(),
    #     #  }