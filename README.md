# nephelaiio.vim

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-vim.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-vim)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/vim/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/vim) to install and configure vim

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

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role from sources using the command line by calling molecule directly ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
