#!/usr/bin/python
from flask import Flask
import openshift as oc
#from openshift import openshift_utils

print(oc get pods)
#print('OpenShift server version: {}'.format(oc.get_server_version()))

application = Flask(__name__)

@application.route("/")
def hello():
   return "Jesus lebt!"
if __name__ == "__main__":
    application.run()
