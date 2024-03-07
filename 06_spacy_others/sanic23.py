from uuid import UUID
from sanic import Sanic
from sanic.response import json
from sanic.response import text
app = Sanic("app23")

#########################################################
## added middleware --- comment it later
# from package_sanicMiddleware11 import Camelize23
# Camelize23(app)         # some error when sending text responses... so comment it out
#########################################################


@app.post("/post23")
async def post23(request):
    print("payload ====> ", request.json)
    print("manager23 ====> ", request.json['manager'])
    return json({"info": "edo oka response"})

@app.get("/get23")
async def get233(request):
    print("params ===> ", {request.args})
    print("query params ===> ", {request.query_args})
    return json({ "info": "idi query params kosam" })

@app.get("/get24/<param1>/page/<param2>")
async def get244(request, param1, param2):
    print("path param topic/page ===> ", param1, param2)
    return json({ "info": "idi path params kosam" })

#########################################################
@app.route("/update", methods=["POST", "PUT"])
async def handler23(request):
    print(" request method ===> ", request.method)
    return text('OK23')           ### using text from sanic-response


@app.get("/foo11/<foo_id:uuid>")
async def uuid_handler(request, foo_id: UUID):          ### UUID is enforced when matching path
    return text("UUID - {}".format(foo_id))

@app.get("/foo12/<topic23>")
async def uuid_handler_diffName(request, topic23):          ### UUID is enforced when matching path
    print(" request headers ===> ", request.headers)
    print(" request method ===> ", request.method)
    return text("topic23 ===>  {}".format(topic23))
#########################################################
@app.route('/')
async def test(request):
    return json({'hello23': 'world44'})

if __name__ == '__main__':
    # app.run(host="10.0.54.240", port=28080)
    app.run(port=28080)