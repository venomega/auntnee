from distutils.core import setup

setup(
    name='auntnee',
    author="Guillermo Plasencia",
    author_email="guilleps92@nauta.cu",
    version='0.1',
    packages=['auntnee', 'curses', ],
    requires=["pyotp", ],
    licence='GPL-3',
    description="This is an TOTP Authenticator CLI for the terminal",
    long_description=open("README.md").read(),

)
