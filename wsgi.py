from flask import Flask
import yaml
application = Flask(__name__)

@application.route("/")
def hello():
    
    with open(r'docker-compose.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    documents = yaml.load(file)
    for item, doc in documents.items():
        print(item, ":", doc)

    return "Hello World!"

if __name__ == "__main__":
    application.run()
