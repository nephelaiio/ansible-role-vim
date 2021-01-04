# nephelaiio.vim

[![Build Status](https://github.com/nephelaiio/ansible-role-vim/workflows/CI/badge.svg)](https://github.com/nephelaiio/ansible-role-vim/actions)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.vim-blue.svg)](https://galaxy.ansible.com/nephelaiio/vim/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/vim) to install and configure vim

## Local install

Execute the following from the command line shell

```
curl -s https://raw.githubusercontent.com/nephelaiio/ansible-role-vim/master/install.sh | bash
```

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: servers
      roles:
         - role: vim
           vim_packages: neovim
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

This role is tested against the following distributions (docker images):

  * Ubuntu Focal
  * Ubuntu Bionic
  * Debian Buster

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
