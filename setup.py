from setuptools import setup, find_packages

setup(
    name='django-security-tools',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A set to security tools for Django.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dreamxinxcode/django-security-tools',
    author='Your Name',
    author_email='brandon@dreamincode.dev',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'django>=3.2',
    ],
    python_requires='>=3.7',
)