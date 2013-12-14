from webassets import Environment, Bundle


def compileLess():
    environment = Environment('codemitts/resources/less', 'less')
    output = '../static/css/main.css'
    less_bundle = Bundle('main.less', filters='less', output=output)
    environment.register('less_bundle', less_bundle)
    environment['less_bundle'].urls()


def compileJavascript():
    environment = Environment('vendor/bootstrap/js/', 'javascript')
    output = '../../../codemitts/resources/static/javascript/bootstrap.js'
    bootstrap_javascript_bundle = Bundle('*', output=output)
    environment.register('bootstrap_javascript_bundle',
                         bootstrap_javascript_bundle)
    environment['bootstrap_javascript_bundle'].urls()
