def help():
    print ("Usage:\n -h | --help\tPrint this help\n -a | --add\tAdd a new secrect to de db\n -c | --change\tchange path of db file\n -d | --del\tDelete an entry by issuer (Example: test.com)\n\nExample:\npython3 -m auntnee -a mywebpage.com username KEY_TOTP\npython3 -m auntnee -c '/path/to/file'\npython3 -m auntnee -d mywebpage.com\n")
