# https://www.codewars.com/kata/60e4dfc1dc28e70049e2cb9d

def strings_in_max_depth(s: str):
    stage = 0
    start_index = 0
    result = []
    if '(' not in s:
        result.append(s)
    else:
        current_stage = 0
        for index, symbol in enumerate(s):
            if symbol == '(':
                start_index = index + 1
                current_stage += 1
            elif symbol == ')':
                if current_stage == stage:
                    result.append(s[start_index:index])
                current_stage -= 1
            if current_stage > stage:
                result = []
                stage = current_stage
    return result


print(strings_in_max_depth("AA(XX((YY))(U))"))
print(strings_in_max_depth("((AAX(AB)(UP)F(Z))(HH))"))
print(strings_in_max_depth(
    "FB(TAIHJK(NZZCGDZXKF(SYMBLACQ)SBJMRFM)PRTRX(JCLYCOXIMOKGGIE)MWIOIJDCLXDSQFHK)WLVYSMNNHIGKR(MOIZLOT(RWMAVXSJQROHJ(GZURPPOQJVMYCE(VCPXSHXQ)LETIEWE(CBC)AAHEEO)NZHIGXBSJATXV)BSBYCMKFFAFZIK(KECNRQ)PIIQZGIDMLNQRQS)VGXXBYD"))
print(strings_in_max_depth("AAA"))
print(strings_in_max_depth(""))
