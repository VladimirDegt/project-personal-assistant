from setuptools import setup, find_packages

setup(
    name='my_contacts_book_bot',
    version='0.1',
    description='Contacts book bot for managing contacts',
    url='https://github.com/OksanaDonchuk/goit-pycore-hw-08/blob/main/my_contacts_book/my_contacts_book/main.py',
    author='Oksana Donchuk',
    author_email='ksunya.donchuk@gmail.com',
    packages=find_packages(include=['my_contacts_book', 'my_contacts_book.*']),
    entry_points={'console_scripts': ['my_contacts_book=my_contacts_book.main:main']},
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)