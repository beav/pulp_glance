from setuptools import setup, find_packages
# NEED TO VERIFY

setup(
    name='pulp_glance_plugins',
    version='0.1.0',
    packages=find_packages(),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='plugins for glance image support in pulp',
    entry_points={
        'pulp.importers': [
            'importer = pulp_glance.plugins.importers.importer:entry_point',
        ],
        'pulp.distributors': [
            'web_distributor = pulp_glance.plugins.distributors.distributor_web:entry_point',
            'export_distributor = pulp_glance.plugins.distributors.distributor_export:entry_point',
        ]
    }
)
