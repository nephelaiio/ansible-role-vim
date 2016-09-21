Role Name
=========

An ansible role to install and configure vim

Requirements
------------

Please make sure your environment has [docker](https://www.docker.com) and [vagrant](https://www.vagrantup.com) installed in order to run role validation tests

Role Variables
--------------

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.
An additional list of reserved parameters is [available](/defaults/reserved.yml); overriding these is strongly discouraged.

Dependencies
------------

By default this role does not depend on any external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: vim vim_packages: vim }


Testing
-------

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial (ubuntu:xenial)
  * CentOS 7 (centos:7)
  * Debian Jessie (debian:jessie)
  * Arch Linux (pritunl/archlinux:latest)

You can test the role from sources using the command line using molecule directly
```
molecule test
```
Please review the [documentation](http://docs.ansible.com/ansible/galaxy.html#setup-travis-integrations) in case you wish to add continuous integration for the role using [Travis CI](https://travis-ci.org)

License
-------

This project is licensed under the terms of the [MIT License](/LICENSE)
