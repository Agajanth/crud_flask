from flask import Flask

app = Flask(__name__)


from app import rout
from app import database
