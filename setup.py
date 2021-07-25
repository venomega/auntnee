from distutils.core import setup

setup(
    name='auntnee',
    author="venomega",
    author_email="usercryptonumberzero@gmail.com",
    version='0.2',
    packages=['auntnee', ],
    requires=["pyotp", "curses", ],
    licence='GPL-3',
    url="https://github.com/venomega/auntnee",
    download_url="https://github.com/venomega/auntnee/archive/0.2.tar.gz",
    description="This is an TOTP Authenticator CLI for the terminal",
    long_description=open("README.md").read(),

)
