"""Entry point for hosting: rebuild the app from base64 text chunks (code_00, code_01, ...), unpack it, serve app.py. Stored databases are unpacked by the app from db<name>_NN chunks."""
import os, sys, zipfile, glob, base64
HERE = os.path.dirname(os.path.abspath(__file__)); APP = os.path.join(HERE, "sacr_app")
if not os.path.isdir(APP):
    data = "".join(open(f).read().strip() for f in sorted(glob.glob(os.path.join(HERE, "code_*"))))
    zp = os.path.join(HERE, "bundle.zip"); open(zp, "wb").write(base64.b64decode(data))
    with zipfile.ZipFile(zp) as z: z.extractall(APP)
sys.path.insert(0, APP); os.chdir(APP)
from app import app  # noqa
