"""Entry point for hosting: rebuild bundle.zip from base64 chunks (chunk_00, chunk_01, ...), unpack it, serve app.py."""
import os, sys, zipfile, glob, base64
HERE = os.path.dirname(os.path.abspath(__file__)); APP = os.path.join(HERE, "sacr_app")
if not os.path.isdir(APP):
    data = "".join(open(f).read().strip() for f in sorted(glob.glob(os.path.join(HERE, "chunk_*"))))
    zp = os.path.join(HERE, "bundle.zip"); open(zp, "wb").write(base64.b64decode(data))
    with zipfile.ZipFile(zp) as z: z.extractall(APP)
sys.path.insert(0, APP); os.chdir(APP)
from app import app  # noqa
