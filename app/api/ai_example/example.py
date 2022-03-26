from flask import Blueprint
from flask import jsonify, request
import logging
from app.modules.ai_example.example import example_hello

example_blueprint = Blueprint("example", __name__)
logger = logging.getLogger("ml.log")

@example_blueprint.route("/example/hello_world", methods=["POST"])
def abnormal_detect():
    try:
        postdata = request.get_json()
    except Exception as e:
        logger.error(
            "/example/hello_world error: {}".format(str(e))
        )
        return jsonify({"msg": "example error", "code": 201})
    try:
        process1 = example_hello()
        logger.info(
            "/example/hello_world finish."
        )
        return process1.print_something()
    except Exception as e:
        logger.error(
            "/example/hello_world error: {}".format(str(e))
        )
        return jsonify({"msg": "example error", "code": 201}) 
