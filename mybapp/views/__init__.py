from .home import home

from .landing_page.list import ticket_list_s

from .onboardings.list import location_list_on
from .onboardings.form import location_form_on
from .first_rigs.form import rig_form_on
from .first_rigs.list import rig_list_on

from .auth.logout import logout_user

from .tickets.list import ticket_list
from .tickets.form import ticket_form
from .tickets.details import ticket_details
from .tickets.form import ticket_edit_form

from .rigs.list import rig_list
from .rigs.form import rig_form
from .rigs.details import rig_details
from .rigs.form import rig_edit_form

from .locations.list import location_list
from .locations.form import location_form
from .locations.details import location_details
from .locations.form import location_edit_form

from .profiles.list import profile_list
from .profiles.form import profile_form
from .profiles.form import profile_edit_form
from .profiles.details import profile_details

from .miners.list import miner_list
from .auth.register import register