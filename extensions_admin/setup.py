from setuptools import setup, find_packages
# NEED TO VERIFY

setup(
    name='pulp_glance_extensions_admin',
    version='0.1.0',
    packages=find_packages(),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='pulp-admin extensions for glance image support',
    entry_points={
        'pulp.extensions.admin': [
            'repo_admin = pulp_glance.extensions.admin.pulp_cli:initialize',
        ]
    }
)
