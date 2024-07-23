from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random


class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    base_number = random.randint(1, 100)
    app_tables.square_numbers.add_row(base_number=base_number, squared=base_number**2)

    for row in app_tables.square_numbers.search():
      print("%s squared is %s" % (row['base_number'], row['squared']))
#       A change 17
