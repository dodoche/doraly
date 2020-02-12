#!/usr/bin/python
from flask import Flask
from easy-openshift import openshift as oc
from easy-openshift import openshift_utils

print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))

application = Flask(__name__)

@application.route("/")
def hello():
   return "Jesus lebt!"
if __name__ == "__main__":
    application.run()
