from webassets import Environment, Bundle


def compileLess():
    environment = Environment('codemitts/resources/less', 'less')
    less_bundle = Bundle('main.less', filters='less', output='../static/css/main.css')
    environment.register('less_bundle', less_bundle)
    environment['less_bundle'].urls()
