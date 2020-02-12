from flask import Flask
import openshift as oc
application = Flask(__name__)

@application.route("/")
def hello():
print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))
   return "Jesus lebt!"
if __name__ == "__main__":
    application.run()
