#!/usr/bin/env python
import os

def get_credentials():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tanant_name'] = os.environ['OS_TENANT_NAME']
    d['project_name'] = os.environ['OS_PROJECT_NAME']
    d['identity_api'] = os.environ['OS_IDENTITY_API_VERSION']
    d['image_api'] = os.environ['OS_IMAGE_API_VERSION']
    return d

def get_nova_credentials_v2():
    d = {}
    d['version'] = '2'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

print(get_credentials())