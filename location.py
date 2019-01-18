import os
from pathlib import Path
import glob
def getLocation():
    if (os.name == "posix"):
        os.environ['DB_PATH'] = glob.glob(str(Path("/home/*/.mozilla/firefox/*/places.sqlite")))[0]
    else:
        os.environ['DB_PATH'] = glob.glob(str(Path(os.getenv('APPDATA')+"\Mozilla\Firefox\Profiles\*\places.sqlite")))[0]