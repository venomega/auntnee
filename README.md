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

### Fisrt start

When you first run *auntnee*
