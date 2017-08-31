import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(Command):
    command = 'vim +PluginInstall +PluginUpdate +PluginClean +qall'
    assert Command(command).rc == 0
