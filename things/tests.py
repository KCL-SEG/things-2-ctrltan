from django.test import TestCase
from django import forms 
from .models import Thing
from .forms import ThingForm
# Create your tests here.

class ThingFormTestCase(TestCase):

    def setUp(self):
        self.test_thing = {
             'name': 'Stephanie Lawal',
             'description': 'My lengthy description that is not lengthy',
             'quantity': 5
        }

    def test_thing_is_valid(self):
        form = ThingForm(data=self.test_thing)
        self.assertTrue(form.is_valid())

    #Test name
    def test_name_less_than_max_length(self):
        self.test_thing['name'] = 'Stephanie Lawal Lawal Lawal Lawal'
        form = ThingForm(data=self.test_thing)
        self.assertTrue(form.is_valid())

    def test_name_longer_than_max(self):
        self.test_thing['name'] = 'Stephanie Lawal Lawal Lawal Lawal Lawal'
        form = ThingForm(data=self.test_thing)
        self.assertFalse(form.is_valid())

    #Test description
    def test_description_can_be_blank(self):
        self.test_thing['description'] = ''
        form = ThingForm(data=self.test_thing)
        self.assertTrue(form.is_valid())

    def test_description_more_than_max_length(self):
        self.test_thing['description'] = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis nato'
        form = ThingForm(data=self.test_thing)
        self.assertFalse(form.is_valid())

    def test_description_less_than_max(self):
        self.test_thing['description'] = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis na'
        form = ThingForm(data=self.test_thing)
        self.assertTrue(form.is_valid())

    #Test quantity
    def test_quantity_minimum(self):
        self.test_thing['quantity'] = 0
        form = ThingForm(data=self.test_thing)
        self.assertTrue(form.is_valid())

    def test_quantity_maximum(self):
        self.test_thing['quantity'] = 50
        form = ThingForm(data=self.test_thing)
        self.assertTrue(form.is_valid())

    def test_quantity_above_maximum(self):
        self.test_thing['quantity'] = 51
        form = ThingForm(data=self.test_thing)
        self.assertFalse(form.is_valid())

    def test_quantity_below_minimum(self):
        self.test_thing['quantity'] = -1
        form = ThingForm(data=self.test_thing)
        self.assertFalse(form.is_valid())

    #Test all
    def test_thing_has_necessar_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertTrue(isinstance(form.fields['description'].widget, forms.Textarea))
        self.assertIn('quantity', form.fields)
        self.assertTrue(isinstance(form.fields['quantity'].widget, forms.NumberInput))
        self.assertNotIn('created_at', form.fields)
