from paver.tasks import task, BuildFailure, needs
from paver.easy import sh


@task
def unit_tests():
    sh('nosetests --with-coverage test/unit')


@task
def lettuce_tests():
    sh('lettuce test/bdd')


@task
def run_pylint():
    try:
        sh('pylint --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" bankapp/ > pylint.txt')
    except BuildFailure:
        pass


@needs('unit_tests', 'lettuce_tests', 'run_pylint')
@task
def default():
    pass
