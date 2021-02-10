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

# xxx_CreditDebit = CreditDebit(hash_CreditDebit, regToken_crazy_scientist)
# TokenAsync = xxx_CreditDebit["TokenAsync"]
# print('TokenAsync_CreditDebit = ', TokenAsync)
# time.sleep(1)


""" GetAsyncResponse --------------------------------------------------------------------------- """


# @pytest.mark.parametrize(regToken_crazy_scientist, TokenAsync)
def GetAsyncResponse(regToken, TA):
    hash_GetAsyncResponse = hashlib.md5(('GetAsyncResponse/' + TA + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_GetAsyncResponse = ', hash_GetAsyncResponse)
    params_GetAsyncResponse = {'Hash': hash_GetAsyncResponse, 'Token': regToken_crazy_scientist, 'TokenAsync': TA}

    response_GetAsyncResponse = requests.post(D.DOMAIN + '/games/GetAsyncResponse',
                                              params={'Hash': hash_GetAsyncResponse, 'Token': regToken,
                                                      'TokenAsync': TA}, json=params_GetAsyncResponse)

    response = response_GetAsyncResponse.json()
    # print('url =', response_GetAsyncResponse.url)
    assert response_GetAsyncResponse.status_code == 200
    # GetAsyncResponse_ResultId = response['ResultId']
    return response


""" -------------------------------------------------------------------------------------------- """

xxx_AuthorizationGame = AuthorizationGame(hash_AuthorizationGame, regToken_crazy_scientist)
xxx_GetSlotInfo = GetSlotInfo(hash_GetSlotInfo, regToken_crazy_scientist)
xxx_CreditDebit = CreditDebit(hash_CreditDebit, regToken_crazy_scientist)
TokenAsync = xxx_CreditDebit["TokenAsync"]
print('TokenAsync_CreditDebit = ', TokenAsync)
time.sleep(1)


xxx_GetAsyncResponse = GetAsyncResponse(regToken_crazy_scientist, TokenAsync)
print(xxx_GetAsyncResponse)
GetAsyncResponse_ResultId = xxx_GetAsyncResponse['ResultId']
print('GetAsyncResponse_ResultId = ', GetAsyncResponse_ResultId)

BetSum = 'Bet Sum = ' + str(xxx_GetAsyncResponse["BetSum"])
WinSum = 'Win Sum = ' + str(xxx_GetAsyncResponse["WinInfo"]["WinSum"])
Credit_before_spin = 'CREDIT before spin = ' + str(xxx_GetAsyncResponse["WinInfo"]["Balance"] - xxx_GetAsyncResponse["WinInfo"]["WinSum"] + xxx_GetAsyncResponse["BetSum"])
Credit_after_spin = 'CREDIT after spin  = ' + str(xxx_GetAsyncResponse["WinInfo"]["Balance"])
FreeSpinsCount = 'FreeSpinCount = ' + str(xxx_GetAsyncResponse["FreeSpinsCount"])
CurrentSpinWin = 'CurrentSpinWin = ' + str(xxx_GetAsyncResponse["WinInfo"]["CurrentSpinWin"])
BonusGameId = 'BonusGameId = ' + str(xxx_GetAsyncResponse["SpinResult"]["WinCoins"])
print('\n', BetSum, '\n', WinSum, '\n', Credit_before_spin, '\n', Credit_after_spin, '\n', FreeSpinsCount, '\n', CurrentSpinWin)


if __name__ == "__main__":
    unittest.main()
