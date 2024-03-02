from json import loads, dumps
from humps import camelize, decamelize      # python3 -m pip install pyhumps (camelize = transform to camel case)


class Camelize23:
    def __init__(self, app):
        @app.middleware("request")
        async def request_to_snake_case(request):

            if request.body:
                request.body = bytes(dumps(decamelize(loads(request.body))), "utf-8")

        @app.middleware("response")
        async def response_to_camel(request, response):

            if response.body:
                response.body = bytes(dumps(camelize(loads(response.body))), "utf-8")