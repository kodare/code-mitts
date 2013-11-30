from jinja2 import Environment, PackageLoader
from codemitts.models.Project import Project

environment = Environment(loader=PackageLoader('codemitts', 'resources/views'))


class Root():
    def index(self):
        template = environment.get_template('index.html')
        # TODO: Implement inverse lookup of all model reference fields http://stackoverflow.com/questions/14470565/bi-directional-relationship-in-mongoengine
        return template.render(projects = Project.objects)
    index.exposed = True
