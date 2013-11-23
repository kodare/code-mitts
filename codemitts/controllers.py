from jinja2 import Environment, PackageLoader

environment = Environment(loader=PackageLoader('codemitts', 'resources/views'))


class Root():
    def index(self):
        template = environment.get_template('index.html')
        return template.render()
    index.exposed = True
