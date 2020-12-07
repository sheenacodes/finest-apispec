#!/usr/bin/env python3

import connexion

from swagger_server import encoder


#def main():
app = connexion.App(__name__, specification_dir='./swagger/')
application = app.app
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'finest-platform-services'})
#app.run(port=8080)




if __name__ == '__main__':
    #main()
    pass
