# ShadowHash

## Introduction :

As we know on Linux operating systems password are generally stored in "/etc/shadow/" file in specific format and there are some formats.
Each row in "/etc/shadow" file is a string with 9 fields separated by ':'.

Little example below :
gituser:$6$kURThR6P$YUPkU29r1k2x2zXRU5R6eNYg6/qZv5aIcZreV21Fkgco0Kc609DiWBPlhObrKKqbO9dsU.MrqgpvP0WGU63IV1:17354:0:99999:7:::

The nine different fields are :

1. The local username
2. Password hash
3. Number of days since the start of unix time (01/01/1970) that the password was last changed
4. Minimum number of days before the password can be changed
5. Maximum number of days before the password must be changed. 99999 means that the user will not be forced to change their password
6. Number of days before forcing the password change that the user will be warned.
7. The number of days after expiration that the account will be disabled
8. Days since the start of unix time that the account has been disabled
9. Reserved for future use

The majority of these fields are usually not used by Linux distributions. The most important fields are the user name and hash. The hash field consists of three separate fields. They are separated by"$" and represent :

1. Some of these characters represent the cryptographic hash mechanism used to generate the actual hash.
2. A randomly generated salt to protect against rainbow table attacks.
3. hash is the result of associating the user's password with the previously stored salt.


- Hash accepted :
-----------------

1. $1$ : md5
2. $2a$ : Blowfish
3. $2y$ : Blowfish, with correct handling of 8 bit characters
4. $5$ : sha256
5. $6$ : sha512


- Simple example with mkpasswd command :
----------------------------------------

mkpasswd --method=sha512 --salt=kURThR6P doit0002

- Command line :
----------------

python -c "import crypt; print crypt.crypt('doit0002', '\$6\$kURThR6P')"


- Test :
--------

[gituser@localhost ~]$ sudo cat /etc/shadow | grep gituser
gituser:$6$kURThR6P$YUPkU29r1k2x2zXRU5R6eNYg6/qZv5aIcZreV21Fkgco0Kc609DiWBPlhObrKKqbO9dsU.MrqgpvP0WGU63IV1:17354:0:99999:7:::

[gituser@localhost ~]$ python -c "import crypt; print crypt.crypt('doit0002', '\$6\$kURThR6P')"
$6$kURThR6P$YUPkU29r1k2x2zXRU5R6eNYg6/qZv5aIcZreV21Fkgco0Kc609DiWBPlhObrKKqbO9dsU.MrqgpvP0WGU63IV1

PS : Special thanks to Hansel
https://www.aychedee.com/2012/03/14/etc_shadow-password-hash-formats/
