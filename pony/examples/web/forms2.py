from datetime import datetime

from pony.main import *

use_autoreload()

@http('/')
@printhtml
def index():
    f = Form()
    f.first_name = Text(required=True)
    f.last_name = Text()
    f.birth_date = Composite(required=True)
    f.birth_date.year = Text(size=4)
    f.birth_date.month = Text(size=4)
    f.birth_date.day = Text(size=2)

    if f.birth_date.is_valid:
        year, month, day = f.birth_date.value
        try: birth_date = datetime(int(year), int(month), int(day))
        except ValueError: f.birth_date.error_text = 'Incorrect date'

    if f.is_valid:
        print '<h1>Hello, %s!</h1>' % f.first_name.value
    else:
        print '<h1>Please fill the form:</h1>'
        print f

start_http_server()
