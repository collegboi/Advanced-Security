#!/usr/bin/python

import hashlib
import hmac
from hashlib import md5

key = "FACEBOOK"
plaintext = "AAAABBBBCCCC"
hash = hmac.new(key, plaintext, md5).hexdigest()
# Compare the output of the two hashes.
print hash
print hmac.compare_digest(hmac.new(key, plaintext, md5).hexdigest(), hash)