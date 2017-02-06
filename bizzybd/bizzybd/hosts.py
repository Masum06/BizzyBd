from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='main'),
    host(r'[\w.]', 'subdomain.urls', name='subdomain'),
    # host(r'[\w.](\w+)', 'subdomain.urls', name='wildcard'),
    # host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
)