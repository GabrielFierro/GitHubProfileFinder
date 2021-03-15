import requests


class Consulta():

    def getResponse(user):
        response = requests.get(f'https://api.github.com/users/{user}')
        return response

    def getDatos(respuesta):
        data = [
            respuesta['avatar_url'],
            respuesta['login'],
            respuesta['bio'],
            respuesta['name'],
            respuesta['public_repos']
        ]

        return data
