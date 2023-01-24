from ._anvil_designer import IdentityTemplate       # Library hanya bisa dijalankan pada environment anvil
from anvil import *
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Identity(IdentityTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def submit_button_click(self, **event_args):
    name = self.name_patient_box.text
    age = self.age_patient_box.text
    gender = self.gender_patient_box.selected_value
    email = self.email_patient_box.text
    anvil.server.call('add_identity',name,age,gender,email)
    self.clear_inputs()
    open_form('Predictive_System')
    
    
  def clear_inputs(self):
    self.name_patient_box.text = ""
    self.age_patient_box.text = ""
    self.gender_patient_box.text = ""
    self.email_patient_box.text = ""

    
  def button_1_click(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    anvil.users.logout()
    open_form('Landing')
    Notification('You have successfully loged out!').show()

    
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Landing')
