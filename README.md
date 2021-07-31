# Auntnee

TODO:
  - support encrypted json (*Aegis* compatible)
  - appimage release
  - design an ui


# About
This program is an TOTP Authenticator for terminal, initialy the json with all 2FA codes is generated from an apk called *Aegis* Authenticator, so this program reads the json file generated with the apk and show you 2FA code from the console.
Now support creation of empty template and is not demanding the *Aegis* json.

# Support

 - creating empty template
 - using existing json from *Aegis* unencrypted
 - add new issuer to the json
 - delete provided issuer from the json
 - change path of json built-in

# Instalation

Just run the following command
```
python3 -m pip install auntnee
```

## Usage

#### First start

When you first run *auntnee* it creates a file in *$HOME/.auntnee.conf* and ask you to specify where are the json file you wana use, if you provide an non-existent file, it will create an empty template ready for add new entries to the json. If you provide an *Aegis* json, it will use that existen json and let you use it.

```
 $> python3 -m auntnee
Failed to solve json file
Please enter the route to json file unencrypted: /tmp/mynewfile.json

 $>
```

After that first run, when you run the command again without any arguments, it will read that json file and start receiving user input
```
 $> python3 -m auntnee
   ┌─<SEARCH>───────────────────┐
   │                            │
   └────────────────────────────┘

   ┌──<Result>──────────────────┐
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   └────────────────────────────┘

```

#### Add new issuer

Of curse, right now if you create an empty json template, there is no entries, lets create one.

```
 $> python3 -m auntnee -a mywebpage.com my_username MY_SITE_KEY_TOTP

 $>

```

And then lets look for it again.

```

   ┌─<SEARCH>───────────────────┐
   │myw                         │
   └────────────────────────────┘

   ┌──<Result>──────────────────┐
   │mywebpage.com 798835        │
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   └────────────────────────────┘
```

As you type in the keyboard, the Result list will update automatically.

#### Delete an issuer

If you want to delete an entry just provide the issuer(or website name like mywebpage.com)

```
 $> python3 -m auntnee -d mywebpage.com
  1 entries removed
 $>
```

And then...

```

   ┌─<SEARCH>───────────────────┐
   │myw                         │
   └────────────────────────────┘

   ┌──<Result>──────────────────┐
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   │                            │
   └────────────────────────────┘
```

The issuer has been removed.

## Help

```
Usage:
 -h | --help	Print this help
 -a | --add	Add a new secrect to de db
 -c | --change	change path of db file
 -d | --del	Delete an entry by issuer (Example: test.com)

Example:
python3 -m auntnee -a mywebpage.com username KEY_TOTP
python3 -m auntnee -c '/path/to/file'
python3 -m auntnee -d mywebpage.com
```


