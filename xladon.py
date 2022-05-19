import base64
import binascii
import hashlib


def aid_random_md5(buffer):
    return hashlib.md5(buffer).digest()


def ror(x, v):
    a = (x << (64 - v)) | (x >> v)  # x9, ror #61
    return a & 0xffffffffffffffff


def ror_plus(v, shift, x9):
    a = (x9 << (64 - shift)) | (x9 >> shift)
    return (a ^ v) & 0xffffffffffffffff


def validate(num):
    return num & 0xffffffffffffffff


def ladon_calc_1(x8, x9, x22):
    x8 = ror(x8, 0x4)
    x8 = (x8 - x9) ^ x22
    res_1 = x8
    res_2 = ror_plus(x8, 49, x9)
    return res_1, res_2


class XLadon:

    def __init__(self, xk, aid):
        self.make_sig(xk, aid)

    def ladon_2(self, md5_1):
        ror_3d = self.x_2
        x9 = ror(self.r_2, 0x8)
        x8_x9 = ror_3d - x9
        reset_value = x8_x9 ^ md5_1
        for l_value in self.l_value_list:
            ror_x9 = validate(ror(ror_3d, 0x3f))
            ror_3d = validate(reset_value ^ ror_x7)
            x8_ror = validate(ror(reset_value, 0x9))
            and_res = validate(x8_ror + ror_3d)
            reset_value = validate(and_res * l_value)
        x_ladon4 = reset_value
        x_ladon3_ror_3d = validate(ror(ror_3d, 0x3d))
        xladon_3 = validate(x_ladon4 ^ x_ladon3_ror_3d)
        return xladon_3, x_ladon4

    def ladon_1(self, md5_1):
        ror_3d = self.x_1
        x9 = ror(self.r_1, 0x8)  # 08851-25
        x8_x9 = ror_3d + x9
        reset_value = x8_x9 ^ md5_1
        for l_value in self.l_value_list:
            ror_x9 = validate(ror(ror_3d, 0x3f))
            ror_3d = validate(reset_value ^ ror_x9)
            x8_ror = validate(ror(reset_value, 0x4))
            and_res = validate(x8_ror - ror_3d)
            reset_value = validate(and_res ^ l_value)
        x_ladon4 = reset_value
        x_ladon3_ror_3d = validate(ror(ror_3d, 0x3c))
        xladon_3 = validate(x_ladon4 * x_ladon3_ror_3d)
        return xladon_3, x_ladon4
