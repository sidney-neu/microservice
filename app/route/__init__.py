# register route

def app_route(app):
    from app.api.ai_example.example import example_blueprint
    app.register_blueprint(example_blueprint)
