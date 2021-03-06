#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) 2020, Evgeni Golov <evgeni@golov.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: foreman_model
short_description: Manage Foreman hardware models
description:
    - Manage Foreman hardware models
author:
    - "Evgeni Golov (@evgeni)"
options:
  name:
    description:
      - Name of the Foreman hardware model
    required: true
    type: str
  info:
    description:
      - General description of the hardware model
    type: str
  vendor_class:
    description:
      - The class of the machine as reported by the OpenBoot PROM.
      - This is primarily used by Solaris SPARC builds and can be left blank for other architectures.
    type: str
  hardware_model:
    description:
      - The class of CPU supplied in this machine.
      - This is primarily used by Sparc Solaris builds and can be left blank for other architectures.
    type: str
extends_documentation_fragment:
  - foreman
  - foreman.entity_state
'''

EXAMPLES = '''
- name: "Create ACME Laptop model"
  foreman_model:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "acme laptop"
    info: "this is the acme laptop"
    state: present
'''

RETURN = ''' # '''


from ansible.module_utils.foreman_helper import ForemanEntityAnsibleModule


class ForemanModelModule(ForemanEntityAnsibleModule):
    pass


def main():
    module = ForemanModelModule(
        foreman_spec=dict(
            name=dict(required=True),
            info=dict(),
            vendor_class=dict(),
            hardware_model=dict(),
        ),
    )

    with module.api_connection():
        module.run()


if __name__ == '__main__':
    main()
