from flask import Flask, render_template


class FitnessClassApp:
    def __init__(self, debug_mode=True):
        self.app = Flask(__name__)
        self.debug_mode = debug_mode
        self.add_error_handlers()

    def run_server(self):
        self.app.run(debug=self.debug_mode)

    def register_page(self, route, template, view_name): # POLIMORPHYSM
        def view():
            return render_template(template)

        view.__name__ = view_name
        self.app.add_url_rule(route, view_name, view)

    def add_error_handlers(self):
        @self.app.errorhandler(404)
        def page_not_found(error):
            return render_template("404.html"), 404


class BasePageView:
    route = "/"
    template = "index.html"
    view_name = "index"

    def __init__(self, app: FitnessClassApp):
        app.register_page(self.route, self.template, self.view_name)


class IndexPage(BasePageView):
    route = "/"
    template = "index.html"
    view_name = "index"


class AboutPage(BasePageView):
    route = "/about"
    template = "about-us.html"
    view_name = "about"


if __name__ == "__main__":
    app = FitnessClassApp()

    IndexPage(app)
    AboutPage(app)

    app.run_server()
