import hashlib


def hash_DiceBonusGame(RT, ResultId, SpinId, BonusGameID):
    gameKey = 'TestKey'
    HASH = hashlib.md5(('DiceBonusGame/' + RT + ResultId + SpinId + BonusGameID + gameKey).encode('utf-8')).hexdigest()
    # var tmp2 = 'DiceBonusGame/' + pm.environment.get("token_crazy") + pm.environment.get("resultId") + pm.environment.get("spinId") + pm.environment.get("BonusGameId") + gameKey
    print('hash_DiceBonusGame = ', HASH)
    return HASH

xxx = hash_DiceBonusGame('32432432', '123123123', '123123123', '123123123')
print(xxx)
