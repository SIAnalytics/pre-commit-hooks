from setuptools import find_packages, setup  # type: ignore


def readme():
    with open('./README.md', encoding='utf-8') as f:
        content = f.read()
    return content


setup(
    name='pre_commit_hooks',
    version='0.1.0',
    description='A pre-commit hook for SI-Analytics',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/SIAnalytics/pre-commit-hooks',
    author='SI-Analytics Authors',
    author_email='hakjinlee@si-analytics.ai',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['PyYAML'],
    entry_points={
        'console_scripts': [
            'say-hello=pre_commit_hooks.say_hello:main',
            'check-copyright=pre_commit_hooks.check_copyright:main',
        ],
    },
)
