from .common import *

from .dockerenv import *

SECRET_KEY = '9%pno@m688el28@2+^y4v^&6wluqk-g#j#d7$dsjtht)o30dn1'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://guest:guest@broker/taiga"}

# THROTTLING
#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec"
#}
