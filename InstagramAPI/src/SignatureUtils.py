import hmac
import datetime

from .Constants import Constants
from .Utils import *


class SignatureUtils:
    @staticmethod
    def generateSignature(data):
        hash = hmac.new(Constants.IG_SIG_KEY.encode("utf-8"), data.encode("utf-8"), hashlib.sha256).hexdigest()

        return 'ig_sig_key_version=' + Constants.SIG_KEY_VERSION + \
               '&signed_body=' + hash + '.' + compat_urllib_parse.quote_plus(data)

    @staticmethod
    def generateDeviceId(seed):
        # // Neutralize username/password -> device correlation
        volatile_seed = '%d' % (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()

        return 'android-' + str(hashlib.md5((str(seed) + str(volatile_seed)).encode("utf-8")).hexdigest())[16:]

    @staticmethod
    def generateUUID(type):
        uuid = '%04x%04x-%04x-%04x-%04x-%04x%04x%04x' % (
            mt_rand(0, 0xffff), mt_rand(0, 0xffff),
            mt_rand(0, 0xffff),
            mt_rand(0, 0x0fff) | 0x4000,
            mt_rand(0, 0x3fff) | 0x8000,
            mt_rand(0, 0xffff), mt_rand(0, 0xffff), mt_rand(0, 0xffff)
        )

        return uuid if type else uuid.replace('-', '')
