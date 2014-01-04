from codemitts.models import database_connect
from codemitts.models.User import User
from codemitts.models.Project import Project
from codemitts.models.Quest import Quest
from codemitts.models.Task import Task
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

# Create tasks
task1 = CodeTask(
    name='Create a user',
    description='Create a model for the user.',
    created_by=user1
)

task2 = DocumentationTask(
    name='Document the ODM setup',
    description='We need better documentation of the ODM.',
    created_by=user2
)

# Create project
project = Project(
    name='CodeMitts',
    description=('Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
                 'sed do eiusmod tempor incididunt ut labore et dolore magna '
                 'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                 'ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
    created_by=user1,
    quests = [Quest(
        name='ODM',
        description='Get the document manager up and running.',
        created_by=user2,
        tasks=[task1, task2]
    )]

)

project.save()

project = Project(
    name='Little Red Riding Hood',
    description=('A fairy tale about a young girl and a wolf. Used as an '
                 'example in CodeMitts to test it out. Since the story is '
                 'quite short it will consist of one quest'),
    created_by=user1,
    quests = [Quest(
        name='Write the story',
        description=('Write the whole story about Little Red Riding Hood. '
                     'To make the story safe for kids dont make the wolf die '
                     'in the end. End the story with "... and they lived '
                     'happily ever after. Write in english.'),
        created_by=user1,
        tasks=[
            Task(
                description='Begin with "Once upon a time..."',
                created_by=user1
            )
        ]
    )]

)

project.save()
