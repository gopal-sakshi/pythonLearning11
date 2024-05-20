from flask import Blueprint, Response, json, jsonify, request

clubs23_bp = Blueprint('club23', __name__)
@clubs23_bp.route('/getclubs', methods=['GET'])     ## http://localhost:8010/getclubs
def getClubs23():
    jsonResp23 = json.dumps({ "clubs": ["RMA", "Barca", "Atleti"], "status": 200 })
    return jsonResp23

@clubs23_bp.route('/echoPost23', methods=['POST'])
def echoPost24():
    request23 = request.get_json()
    return Response(json.dumps({ "body23":request23,"status":200 }), headers = {'Content-Type': "application/json" })
