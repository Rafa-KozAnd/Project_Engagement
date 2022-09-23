from instapy import InstaPy
from instapy import smart_run

user = ""
senha = ""
path = "C:\geckodriver.exe"

session = InstaPy(username = user, password = senha, geckodriver_path = path)

#with smart_run(session):
#    session.
