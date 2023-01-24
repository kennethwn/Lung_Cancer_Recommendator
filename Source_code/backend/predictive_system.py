from ._anvil_designer import LandingTemplate      # Library hanya bisa dijalankan pada environment anvil
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    if (anvil.users.login_with_form()):
      open_form('Identity')
      

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    if (anvil.users.login_with_form()):
      open_form('Identity')
      

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    
    anvil.server.call('add_feedback',name,email,feedback)
    Notification('Thank you for contact us!').show()
    self.clear_inputs()
    
    
  def clear_inputs(self):
    self.name_box.text = ''
    self.email_box.text = ''
    self.feedback_box.text = ''
    

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Landing')