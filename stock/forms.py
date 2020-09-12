# from company.models.employee_model import EmployeeModel
from crispy_forms import bootstrap, layout
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms import layout, bootstrap
from crispy_forms.helper import FormHelper
from django.forms.models import formset_factory
from django import forms
from .models import Stock

# Forms used to enter new Item in the store


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']


class StockCreateForm(forms.ModelForm):
    """
    TODO: Extend CompanyModel into Form
    :returns: TODO
    """

    def __init__(self, *args, **kwargs):
        super(StockCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_action = "company:create-employee"

        self.helper.layout = Layout(
            Div(
                Div('category', css_class="col-sm-2"),
                Div('name', css_class="col-sm-2"),
                Div('quantinty', css_class="col-sm-2"),
                bootstrap.FormActions(
                    layout.Submit('submit', 'Add', css_class='btn btn-primary')),
                css_class='row',
            )
        )

    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']
