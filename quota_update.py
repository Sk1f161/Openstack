#!/usr/bin/env python
from novaclient import client
import keystonecli
import psutil
import libvirt


VERSION = '2'
USER = 'admin'
PASSWORD = '######'
TENANT = '######'
AUTH_URL = '#####'

project_list = keystonecli.keystone.projects.list()

mem = psutil.virtual_memory()
mb = 1024 *1024

tenants = []
for projects in project_list:
     # print(projects.id, projects.name)
     if projects.name != 'service':
         tenants.append(projects.name)

for tenant_name in tenants:
    #print(tenant_name)
    nt = client.Client(VERSION, USER, PASSWORD, tenant_name, AUTH_URL)
    quotas = nt.quotas.get(tenant_name)
    limits = nt.limits.get()
    absolute = {l.name: l.value for l in limits.absolute}
    ram = int(mem.available/mb + absolute["totalRAMUsed"])
    print(quotas)
    ### Update tenants quotas
    #nt.quotas.update(tenant_name,ram=ram)
    #print(ram)
