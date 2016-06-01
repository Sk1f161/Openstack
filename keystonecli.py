#!/usr/bin/env python
from keystoneclient.v3 import client

keystone = client.Client(auth_url = '######',
                   username = 'admin',
                   password = '######',
                   tenant_name = 'admin')


# project_list = keystone.projects.list()
# for projects in project_list:
#     print(projects.id, projects.name)
