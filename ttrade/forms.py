from .models import Request, Favor, Tag
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Button, HTML, Div, Field, Row, Fieldset

# class RequestForm(forms.ModelForm):
#     class Meta: 
#         model = Request

class RequestForm(forms.ModelForm):
    class Meta: 
        model = Request
        fields = '__all__'
        exclude = ('user','acceptor','accepted',)
        
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "requestform"
                
        tag = Div('tag', css_class="col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(7) 
        self.helper.layout.insert(8,Fieldset("Select tag",tag, Button("createtagmodal", value="Create New Tag", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        
        self.helper.layout.append(Button('btn_createrequest', 'Create Request', css_class='createrequest', style="margin-top:15px;"))
        self.helper.layout.append(Hidden(name='btn_createrequest', value="btn_createrequest"))
        
    def full_clean(self):
        super(RequestForm, self).full_clean()
        if 'tag' in self._errors:
            self.cleaned_data['tag'] = []
            print("remove tag errors")
            del self._errors['tag']

class FavorForm(forms.ModelForm):
    class Meta: 
        model = Favor
        exclude = ('user',)
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))

# class FavorForm(forms.ModelForm):
#     class Meta: 
#         model = Favor
#         fields = '__all__'
        
#     def __init__(self, *args, **kwargs):
#         super(FavorForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_id = "favorform"
        
#         tag = Div('tag', css_class="col-xs-12", style="padding:0px;") 
#         self.helper.layout.pop(3) 
#         self.helper.layout.insert(3,Fieldset("Select tag",tag, Button("createtagmodal", value="Create New Tag", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        
#         self.helper.layout.append(Button('btn_createfavor', 'Create Favor', css_class='createfavor', style="margin-top:15px;"))
#         self.helper.layout.append(Hidden(name='btn_createfavor', value="btn_createfavor"))
        
#     def full_clean(self):
#         super(RequestForm, self).full_clean()
#         if 'tag' in self._errors:
#             self.cleaned_data['tag'] = []
#             print("remove tag errors")
#             del self._errors['tag']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "tagform"
        self.helper.layout.append(Hidden(name='btn_createtag', value="btn_createtag"))
        self.helper.layout.append(Button('btn_createtag', 'Create Tag', css_class='createtag', data_dismiss="modal"))

class RequestFormUpdate(forms.ModelForm):
    class Meta: 
        model = Request
        fields = '__all__'
        exclude = ('user','acceptor','accepted',)
        
    def __init__(self, *args, **kwargs):
        super(RequestFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "requestformupdate"
        
        self.helper.add_input(Submit('submit', 'Update'))