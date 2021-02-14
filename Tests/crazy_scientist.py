import time
import unittest

import pytest
import requests
import hashlib
from Locators.Locators import APIdata, DOM

D = DOM
A = APIdata

""" starter testpartnerservice ----------------------------------------------------------------- """
params = {'gameURL': D.gameURL, 'frontURL': D.frontURL, 'partnerURL': D.partnerURL, 'partnerId': A.partnerID,
          'gameID': A.gameID, 'userID': A.userID, 'currency': A.currency}
response_testpartnerservice = requests.get(D.DOMAIN_tps, params=params)
print('crazy_scientist_IframeUrl = ', response_testpartnerservice.text)
regToken_crazy_scientist = response_testpartnerservice.text.split("token=")[1].split("&")[0]
print('crazy_scientist_regToken = ', regToken_crazy_scientist)
""" -------------------------------------------------------------------------------------------- """

""" AuthorizationGame -------------------------------------------------------------------------- """
hash_AuthorizationGame = hashlib.md5(
    ('AuthorizationGame/' + regToken_crazy_scientist + A.gameKey).encode('utf-8')).hexdigest()
print('hash_AuthorizationGame = ', hash_AuthorizationGame)
params_AuthorizationGame = {'Hash': hash_AuthorizationGame, 'Token': regToken_crazy_scientist,
                            'MobilePlatform': 'false'}


@pytest.mark.parametrize(hash_AuthorizationGame, regToken_crazy_scientist)
def AuthorizationGame(Hash, regToken):
    response_AuthorizationGame = requests.post(D.DOMAIN + '/auth/AuthorizationGame',
                                               params={'Hash': Hash, 'Token': regToken, 'MobilePlatform': 'false'},
                                               json=params_AuthorizationGame)
    response = response_AuthorizationGame.json()
    url = response_AuthorizationGame.url
    assert response_AuthorizationGame.status_code == 200
    return response
""" -------------------------------------------------------------------------------------------- """

""" GetSlotInfo -------------------------------------------------------------------------------- """
hash_GetSlotInfo = hashlib.md5(('GetSlotInfo/' + regToken_crazy_scientist + A.gameKey).encode('utf-8')).hexdigest()
print('hash_GetSlotInfo = ', hash_GetSlotInfo)
params_GetSlotInfo = {'Hash': hash_GetSlotInfo, 'Token': regToken_crazy_scientist}


@pytest.mark.parametrize(hash_GetSlotInfo, regToken_crazy_scientist)
def GetSlotInfo(Hash, regToken):
    response_GetSlotInfo = requests.post(D.DOMAIN + '/games/GetSlotInfo',
                                         params={'Hash': Hash, 'Token': regToken}, json=params_GetSlotInfo)
    response = response_GetSlotInfo.json()
    assert response_GetSlotInfo.status_code == 200
    return response
""" -------------------------------------------------------------------------------------------- """

""" CreditDebit -------------------------------------------------------------------------------- """
hash_CreditDebit = hashlib.md5(
    ('CreditDebit/' + regToken_crazy_scientist + A.betSum + A.cntLineBet + A.gameKey).encode('utf-8')).hexdigest()
print('hash_CreditDebit = ', hash_CreditDebit)
params_CreditDebit = {'Hash': hash_CreditDebit, 'Token': regToken_crazy_scientist, 'CntLineBet': A.cntLineBet,
                      'BetSum': A.betSum}


@pytest.mark.parametrize(hash_CreditDebit, regToken_crazy_scientist)
def CreditDebit(Hash, regToken):
    response_CreditDebit = requests.post(D.DOMAIN + '/games/CreditDebit',
                                         params={'Hash': Hash, 'Token': regToken, 'CntLineBet': A.cntLineBet,
                                                 'BetSum': A.betSum}, json=params_CreditDebit)
    response = response_CreditDebit.json()
    assert response_CreditDebit.status_code == 200
    # CreditDebit_TokenAsync = response['TokenAsync']
    return response
""" -------------------------------------------------------------------------------------------- """

""" GetAsyncResponse --------------------------------------------------------------------------- """
# @pytest.mark.parametrize(regToken_crazy_scientist, TokenAsync)
def GetAsyncResponse(regToken, TA):
    hash_GetAsyncResponse = hashlib.md5(('GetAsyncResponse/' + TA + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_GetAsyncResponse = ', hash_GetAsyncResponse)
    params_GetAsyncResponse = {'Hash': hash_GetAsyncResponse, 'Token': regToken_crazy_scientist, 'TokenAsync': TA}
    response_GetAsyncResponse = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': hash_GetAsyncResponse, 'Token': regToken, 'TokenAsync': TA}, json=params_GetAsyncResponse)
    response = response_GetAsyncResponse.json()
    # print('url =', response_GetAsyncResponse.url)
    url = response_GetAsyncResponse.url
    assert response_GetAsyncResponse.status_code == 200
    # GetAsyncResponse_ResultId = response['ResultId']
    return response
""" -------------------------------------------------------------------------------------------- """

""" DiceBonusGame ------------------------------------------------------------------------------ """
def hash_DiceBonusGame(RT, ResultId, SpinId, BonusGameID):
    HASH = hashlib.md5(('DiceBonusGame/' + RT + ResultId + SpinId + BonusGameID + A.gameKey).encode('utf-8')).hexdigest()
    # var tmp2 = 'DiceBonusGame/' + pm.environment.get("token_crazy") + pm.environment.get("resultId") + pm.environment.get("spinId") + pm.environment.get("BonusGameId") + gameKey
    print('hash_DiceBonusGame = ', HASH)
    return HASH


# @pytest.mark.parametrize(hash_DiceBonusGame, regToken_crazy_scientist, resultId, BonusGameId, SpinId, Info)
def DiceBonusGame(Hash, regToken, rId, bgId, sId, info):
    params_DiceBonusGame = {"Hash": Hash, "Token": regToken, "ResultId": rId, "BonusGameId": bgId, "SpinId": sId, "Info": info}
    response_DiceBonusGame = requests.post(D.DOMAIN + '/bonus/DiceBonusGame', params={"Hash": Hash, "Token": regToken, "ResultId": rId, "BonusGameId": bgId, "SpinId": sId, "Info": info}, json=params_DiceBonusGame)
    response = response_DiceBonusGame.json()
    assert response_DiceBonusGame.status_code == 200
    url = response_DiceBonusGame.url
    print(url)
    # DiceBonusGame_TokenAsync = response['TokenAsync']
    return response
""" -------------------------------------------------------------------------------------------- """

""" GetAsyncResponse_DiceBonusGame ------------------------------------------------------------- """
# @pytest.mark.parametrize(regToken_crazy_scientist, TokenAsync)
def GetAsyncResponse_DiceBonusGame(regToken, TokenAsyncDice):
    hash_GetAsyncResponse_DiceBonusGame = hashlib.md5(('GetAsyncResponse/' + TokenAsyncDice + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_GetAsyncResponseDice = ', hash_GetAsyncResponse_DiceBonusGame)
    params_GetAsyncResponse_DiceBonusGame = {'Hash': hash_GetAsyncResponse_DiceBonusGame, 'Token': regToken_crazy_scientist, 'TokenAsync': TokenAsyncDice}
    response_GetAsyncResponse_DiceBonusGame = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': hash_GetAsyncResponse_DiceBonusGame, 'Token': regToken, 'TokenAsync': TokenAsyncDice}, json=params_GetAsyncResponse_DiceBonusGame)
    response = response_GetAsyncResponse_DiceBonusGame.json()
    assert response_GetAsyncResponse_DiceBonusGame.status_code == 200
    # GetAsyncResponse_ResultId = response['ResultId']
    return response
""" -------------------------------------------------------------------------------------------- """

""" SelectCardBonusGame ------------------------------------------------------------------------ """
def hash_SelectCardBonusGame(RT, ResultId, SpinId, BonusGameID):
    HASH = hashlib.md5(('SelectCardBonusGame/' + RT + ResultId + SpinId + BonusGameID + A.CardIndex + A.gameKey).encode('utf-8')).hexdigest()
    # var tmp2 = 'SelectCardBonusGame/' + pm.environment.get("token_crazy") + pm.environment.get("resultId") + pm.environment.get("spinId") + pm.environment.get("BonusGameId") + CardIndex.toString() + gameKey
    print('hash_SelectCardBonusGame = ', HASH)
    return HASH


# @pytest.mark.parametrize(hash_DiceBonusGame, regToken_crazy_scientist, resultId, BonusGameId, SpinId, Info)
def SelectCardBonusGame(Hash, regToken, rId, bgId, sId, cIndex, info):
    params_SelectCardBonusGame = {"Hash": Hash, "Token": regToken, "ResultId": rId, "BonusGameId": bgId, "SpinId": sId, "CardIndex": cIndex, "Info": info}
    response_SelectCardBonusGame = requests.post(D.DOMAIN + '/bonus/SelectCardBonusGame', params={"Hash": Hash, "Token": regToken, "ResultId": rId, "BonusGameId": bgId, "SpinId": sId, "CardIndex": cIndex, "Info": info}, json=params_SelectCardBonusGame)
    # //{"Hash":"{{hash_crazy_SelectCardBonusGame}}","Token":"{{token_crazy}}","ResultId":"{{TokenAsync}}","BonusGameId":"{{BonusGameId}}","SpinId":"{{spinId}}","CardIndex":2,"Info":false}
    response = response_SelectCardBonusGame.json()
    assert response_SelectCardBonusGame.status_code == 200
    url = response_SelectCardBonusGame.url
    print(url)
    # SelectCardBonusGame_TokenAsync = response['TokenAsync']
    return response
""" -------------------------------------------------------------------------------------------- """

""" GetAsyncResponse_SelectCardBonusGame ------------------------------------------------------------- """
# @pytest.mark.parametrize(regToken_crazy_scientist, TokenAsync)
def GetAsyncResponse_SelectCardBonusGame(regToken, TokenAsyncCard):
    hash_GetAsyncResponse_SelectCardBonusGame = hashlib.md5(('GetAsyncResponse/' + TokenAsyncCard + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_GetAsyncResponseCard = ', hash_GetAsyncResponse_SelectCardBonusGame)
    params_GetAsyncResponse_SelectCardBonusGame = {'Hash': hash_GetAsyncResponse_SelectCardBonusGame, 'Token': regToken_crazy_scientist, 'TokenAsync': TokenAsyncCard}
    response_GetAsyncResponse_DiceBonusGame = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': hash_GetAsyncResponse_SelectCardBonusGame, 'Token': regToken, 'TokenAsync': TokenAsyncCard}, json=params_GetAsyncResponse_SelectCardBonusGame)
    response = response_GetAsyncResponse_DiceBonusGame.json()
    assert response_GetAsyncResponse_DiceBonusGame.status_code == 200
    # GetAsyncResponse_ResultId = response['ResultId']
    return response
""" -------------------------------------------------------------------------------------------- """


xxx_AuthorizationGame = AuthorizationGame(hash_AuthorizationGame, regToken_crazy_scientist)  # авторизация в игре по токену ! AuthorizationGame
xxx_GetSlotInfo = GetSlotInfo(hash_GetSlotInfo, regToken_crazy_scientist)  # получение информации о игре ! GetSlotInfo

i = 1
while i < 50:
    while True:
        xxx_CreditDebit = CreditDebit(hash_CreditDebit, regToken_crazy_scientist)  # ставка ! CreditDebit
        TokenAsync = xxx_CreditDebit["TokenAsync"]
        print('TokenAsync_CreditDebit = ', TokenAsync)
        time.sleep(1)

        xxx_GetAsyncResponse = GetAsyncResponse(regToken_crazy_scientist, TokenAsync)  # асинхронный ответ ! GetAsyncResponse
        GetAsyncResponse_ResultId = xxx_GetAsyncResponse['ResultId']
        print('GetAsyncResponse_ResultId = ', GetAsyncResponse_ResultId)
        if xxx_GetAsyncResponse["SpinResult"]["DiceGame"] is None:
            BonusGameId = "no bonus game"
            print("BonusGameId =", BonusGameId)
            continue
        else:
            BonusGameId = xxx_GetAsyncResponse["SpinResult"]["DiceGame"]["Id"]
            print("BonusGameId =", BonusGameId)
            Info = 'true'
            spinId = xxx_GetAsyncResponse["SpinResult"]["Id"]
            print("SpinId =", spinId)
            xxx_hash_DiceBonusGame = hash_DiceBonusGame(regToken_crazy_scientist, GetAsyncResponse_ResultId, spinId, BonusGameId)
            xxx_DiceBonusGame = DiceBonusGame(xxx_hash_DiceBonusGame, regToken_crazy_scientist, GetAsyncResponse_ResultId, BonusGameId, spinId, Info)  # # кидаем кубик в бонусной игре ! DiceBonusGame
            DiceBonusGame_TokenAsync = xxx_DiceBonusGame["TokenAsync"]
            print('TokenAsync_DiceBonusGame = ', DiceBonusGame_TokenAsync)
            time.sleep(1)

            xxx_GetAsyncResponse_DiceBonusGame = GetAsyncResponse_DiceBonusGame(regToken_crazy_scientist, DiceBonusGame_TokenAsync)  # асинхронный ответ в бонусной игре ! GetAsyncResponse
            Info = 'false'
            ThrowsLeft = xxx_GetAsyncResponse_DiceBonusGame["ThrowsLeft"]
            print("ThrowsLeft =", ThrowsLeft)
            print(xxx_GetAsyncResponse_DiceBonusGame)
            while ThrowsLeft > 0:
                xxx_DiceBonusGame = DiceBonusGame(xxx_hash_DiceBonusGame, regToken_crazy_scientist, GetAsyncResponse_ResultId, BonusGameId, spinId, Info)  # # кидаем кубик в бонусной игре ! DiceBonusGame
                DiceBonusGame_TokenAsync = xxx_DiceBonusGame["TokenAsync"]
                time.sleep(1)
                xxx_GetAsyncResponse_DiceBonusGame = GetAsyncResponse_DiceBonusGame(regToken_crazy_scientist, DiceBonusGame_TokenAsync)  # асинхронный ответ в бонусной игре ! GetAsyncResponse
                ThrowsLeft = xxx_GetAsyncResponse_DiceBonusGame["ThrowsLeft"]
                print("ThrowsLeft =", ThrowsLeft)
                print(xxx_GetAsyncResponse_DiceBonusGame)
                WinType = xxx_GetAsyncResponse_DiceBonusGame["SelectedSector"]["WinType"]
                print("WinType =", WinType)
                if WinType == 7:
                    print('! BONUS CARD GAME !')
                    xxx_hash_SelectCardBonusGame = hash_SelectCardBonusGame(regToken_crazy_scientist, GetAsyncResponse_ResultId, spinId, BonusGameId)
                    xxx_CardBonusGame = SelectCardBonusGame(xxx_hash_SelectCardBonusGame, regToken_crazy_scientist, GetAsyncResponse_ResultId, BonusGameId, spinId, A.CardIndex, Info)  # # кидаем кубик в бонусной карточной игре ! SelectCardBonusGame
                    CardBonusGame_TokenAsync = xxx_CardBonusGame["TokenAsync"]
                    time.sleep(1)
                    xxx_GetAsyncResponse_CardBonusGame = GetAsyncResponse_SelectCardBonusGame(regToken_crazy_scientist, CardBonusGame_TokenAsync)  # асинхронный ответ в бонусной карточной игре ! GetAsyncResponse

                    # break
            break
    print('i = ', i)
    i = i + 1






    # BetSum = 'Bet Sum = ' + str(xxx_GetAsyncResponse["BetSum"])
    # WinSum = 'Win Sum = ' + str(xxx_GetAsyncResponse["WinInfo"]["WinSum"])
    # Credit_before_spin = 'CREDIT before spin = ' + str(xxx_GetAsyncResponse["WinInfo"]["Balance"] - xxx_GetAsyncResponse["WinInfo"]["WinSum"] + xxx_GetAsyncResponse["BetSum"])
    # Credit_after_spin = 'CREDIT after spin  = ' + str(xxx_GetAsyncResponse["WinInfo"]["Balance"])
    # FreeSpinsCount = 'FreeSpinCount = ' + str(xxx_GetAsyncResponse["FreeSpinsCount"])
    # CurrentSpinWin = 'CurrentSpinWin = ' + str(xxx_GetAsyncResponse["WinInfo"]["CurrentSpinWin"])
    # BonusGameId = 'BonusGameId = ' + str(xxx_GetAsyncResponse["SpinResult"]["DiceGame"])
    # if xxx_GetAsyncResponse["SpinResult"]["DiceGame"] is None:

    #     BonusGameId = "no bonus game"
    #     print("BonusGameId =", BonusGameId)
    # else:
    #     BonusGameId = xxx_GetAsyncResponse["SpinResult"]["DiceGame"]["Id"]
    #     print("BonusGameId =", BonusGameId)
    #     Info = 'true'
    #     spinId = xxx_GetAsyncResponse["SpinResult"]["Id"]
    #     print("SpinId =", spinId)
    #
    # print('\n', BetSum, '\n', WinSum, '\n', Credit_before_spin, '\n', Credit_after_spin, '\n', FreeSpinsCount, '\n',
    #       CurrentSpinWin, '\n', BonusGameId)

if __name__ == "__main__":
    unittest.main()
