echo sooriyab-23IT155 > sooriya.txt

openssl aes-128-cbc -e -in sooriya.txt -out cipher.bin -k "password" -nosalt

type cipher.bin

openssl enc -aes-128-cbc -d -in cipher.bin -k "password" -nosalt -p

openssl aes-128-cbc -d -in cipher.bin -out pt.txt -k "password" -nosalt

type pt.txt

(echo|set /p=SOORIYA-23IT155) > plain.txt

openssl aes-128-cbc -e -in plain.txt -out cipher2.bin -k "password" -nosalt

fc /b cipher.bin cipher2.bin

openssl genrsa -out pvtkey.pem 2048

openssl rsa -pubout -in pvtkey.pem -out pubkey.pem

openssl rsa -text -in pvtkey.pem

openssl rsautl -encrypt -in plain.txt -pubin -inkey pubkey.pem -out c1.bin

openssl rsautl -decrypt -in c1.bin -inkey pvtkey.pem -out decrypted.txt

openssl rsautl -decrypt -in c1.bin -inkey pvtkey.pem -out decrypted_rsa.txt

type decrypted_rsa.txt

openssl md5 plain.txt

openssl sha256 plain.txt

openssl dgst -sha256 -sign pvtkey.pem -out s.bin plain.txt

openssl dgst -sha256 -verify pubkey.pem -signature s.bin plain.txt