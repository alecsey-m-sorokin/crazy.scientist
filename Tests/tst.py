import hashlib


def hash_DiceBonusGame(*args):
    gameKey = 'TestKey'
    HASH = hashlib.md5(('DiceBonusGame/' + RT + ResultId + SpinId + BonusGameID + gameKey).encode('utf-8')).hexdigest()
    # var tmp2 = 'DiceBonusGame/' + pm.environment.get("token_crazy") + pm.environment.get("resultId") + pm.environment.get("spinId") + pm.environment.get("BonusGameId") + gameKey
    print('hash_DiceBonusGame = ', HASH)
    return HASH, args

RT = '32432432'
ResultId = '123123123'
SpinId = 'dfdasfdas'
BonusGameID = 'sdfds9de99897a'

xxx = hash_DiceBonusGame(RT, ResultId, SpinId, BonusGameID)
print(xxx)
