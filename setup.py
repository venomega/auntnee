from distutils.core import setup

setup(
    name='auntnee',
    author="Guillermo Plasencia",
    author_email="guilleps92@nauta.cu",
    version='0.1',
    packages=['auntnee', ],
    requires=["pyotp", "curses", ],
    licence='GPL-3',
    url="https://github.com/venomega/auntnee",
    download_url="https://github.com/venomega/auntnee/archive/0.1.tar.gz",
    description="This is an TOTP Authenticator CLI for the terminal",
    long_description=open("README.md").read(),

)
