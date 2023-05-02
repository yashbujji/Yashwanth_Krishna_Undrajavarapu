# from setuptools import setup, find_packages

# setup(
#     name='ark-biotech-dashboard',
#     version='0.1',
#     packages=find_packages(),
#     install_requires=[
#         'flask',
#         'psycopg2-binary',
#         'plotly',
#         'pandas'
#     ],
#     entry_points={
#         'console_scripts': [
#             'run-app=ark_biotech_dashboard.app:main'
#         ]
#     },
#     author='Your Name',
#     author_email='yourname@email.com',
#     description='A web-based dashboard to visualize real-time process data originating from one of Ark Biotech\'s bioreactors',
#     license='Proprietary & Confidential',
#     keywords='dashboard biotech bioreactor real-time data visualization'
# )

from setuptools import setup, find_packages

setup(
    name='dashboard',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'psycopg2-binary',
        'pandas',
        'numpy',
        'matplotlib',
        'plotly',
        'flask-cors',
        # 'psycopg2==2.9.1',
    ],
    entry_points={
        'console_scripts': [
            'dashboard=dashboard:main'
        ]
    },
)
