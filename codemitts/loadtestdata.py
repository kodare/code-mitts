from codemitts.models import database_connect
from codemitts.models.User import User
from codemitts.models.Project import Project
from codemitts.models.Feature import Feature
from codemitts.models.CodeTask import CodeTask
from codemitts.models.DocumentationTask import DocumentationTask

database_connect('codemitts')

# Create user
user1 = User(
    first_name='Lisa',
    last_name='Andersson',
    email='lisa.andersson@example.org',
    username='Lisa'
)

user1.save()

user2 = User(
    first_name='Per',
    last_name='Nilsson',
    email='per.nilsson@example.org',
    username='Per'
)

user2.save()


# Create project
project = Project(
    name='CodeMitts',
    description=('Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
                 'sed do eiusmod tempor incididunt ut labore et dolore magna '
                 'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                 'ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
    created_by=user1
)

project.save()


# Create feature
feature = Feature(
    name='ODM',
    description='Get the document manager up and running.',
    project=project,
    created_by=user2
)

feature.save()


# Create tasks
task1 = CodeTask(
    name='Create a user',
    description='Create a model for the user.',
    feature=feature,
    created_by=user1
)

task1.save()

task2 = DocumentationTask(
    name='Document the ODM setup',
    description='We need better documentation of the ODM.',
    feature=feature,
    created_by=user2
)

task2.save()
