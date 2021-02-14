import hashlib
import time
import unittest

import pytest
import requests

from Locators.Locators import APIdata, DOM

D = DOM
A = APIdata


""" starter testpartnerservice ----------------------------------------------------------------- """
# @pytest.fixture(scope="module")
def partnerservice_starter():
    params = {'gameURL': D.gameURL, 'frontURL': D.frontURL, 'partnerURL': D.partnerURL, 'partnerId': A.partnerID,
              'gameID': A.gameID, 'userID': A.userID, 'currency': A.currency}
    response_testpartnerservice = requests.get(D.DOMAIN_tps, params=params)
    assert response_testpartnerservice.status_code == 200
    regToken_crazy_scientist = response_testpartnerservice.text.split("token=")[1].split("&")[0]
    print('crazy_scientist_IframeUrl = ', response_testpartnerservice.text)
    print('crazy_scientist_regToken = ', regToken_crazy_scientist)
    return regToken_crazy_scientist
""" -------------------------------------------------------------------------------------------- """

RT = partnerservice_starter()

""" AuthorizationGame -------------------------------------------------------------------------- """
@pytest.mark.parametrize(RT)
def hash_AuthorizationGame(rt=RT):
    HASH = hashlib.md5(('AuthorizationGame/' + rt + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_AuthorizationGame = ', HASH)
    return HASH

HAG = hash_AuthorizationGame()

@pytest.mark.parametrize(RT, HAG)
def AuthorizationGame(rt=RT, hag=HAG):
    params_AuthorizationGame = {'Hash': hag, 'Token': rt, 'MobilePlatform': 'false'}
    response_AuthorizationGame = requests.post(D.DOMAIN + '/auth/AuthorizationGame', params={'Hash': hag, 'Token': rt, 'MobilePlatform': 'false'}, json=params_AuthorizationGame)
    response = response_AuthorizationGame.json()
    assert response_AuthorizationGame.status_code == 200
    print(response)
    return response
""" -------------------------------------------------------------------------------------------- """

""" GetSlotInfo -------------------------------------------------------------------------------- """
@pytest.mark.parametrize(RT)
def hash_GetSlotInfo(rt=RT):
    HASH = hashlib.md5(('GetSlotInfo/' + rt + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_GetSlotInfo = ', HASH)
    return HASH

HGSI = hash_GetSlotInfo()

@pytest.mark.parametrize(RT, HAG)
def GetSlotInfo(rt=RT, hgsi=HGSI):
    params_GetSlotInfo = {'Hash': hgsi, 'Token': rt}
    response_GetSlotInfo = requests.post(D.DOMAIN + '/games/GetSlotInfo', params={'Hash': hgsi, 'Token': rt}, json=params_GetSlotInfo)
    response = response_GetSlotInfo.json()
    assert response_GetSlotInfo.status_code == 200
    print(response)
    return response
""" -------------------------------------------------------------------------------------------- """

""" CreditDebit -------------------------------------------------------------------------------- """
@pytest.mark.parametrize(RT)
def hash_CreditDebit(rt=RT):
    HASH = hashlib.md5(('CreditDebit/' + rt + A.betSum + A.cntLineBet + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_CreditDebit = ', HASH)
    return HASH

HCD = hash_CreditDebit()

@pytest.mark.parametrize(RT, HCD)
def CreditDebit(rt=RT, hcd=HCD):
    params_CreditDebit = {'Hash': hcd, 'Token': rt, 'CntLineBet': A.cntLineBet, 'BetSum': A.betSum}
    response_CreditDebit = requests.post(D.DOMAIN + '/games/CreditDebit', params={'Hash': hcd, 'Token': rt, 'CntLineBet': A.cntLineBet, 'BetSum': A.betSum}, json=params_CreditDebit)
    response = response_CreditDebit.json()
    assert response_CreditDebit.status_code == 200
    CreditDebit_TokenAsync = response['TokenAsync']
    print('CreditDebit_TokenAsync =', CreditDebit_TokenAsync)
    print(response)
    return response, CreditDebit_TokenAsync
""" -------------------------------------------------------------------------------------------- """

TA = CreditDebit()[1]


""" GetAsyncResponse --------------------------------------------------------------------------- """
@pytest.mark.parametrize(TA)
def hash_GetAsyncResponse(ta=TA):
    HASH = hashlib.md5(('GetAsyncResponse/' + ta + A.gameKey).encode('utf-8')).hexdigest()
    print('hash_GetAsyncResponse = ', HASH)
    return HASH

HGAR = hash_GetAsyncResponse()

@pytest.mark.parametrize(RT, HGAR, TA)
def GetAsyncResponse(rt=RT, hgar=HGAR, ta=TA):
    params_GetAsyncResponse = {'Hash': hgar, 'Token': rt, 'TokenAsync': ta}
    response_GetAsyncResponse = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': hgar, 'Token': rt, 'TokenAsync': ta}, json=params_GetAsyncResponse)
    response = response_GetAsyncResponse.json()
    assert response_GetAsyncResponse.status_code == 200
    # GetAsyncResponse_ResultId = response['ResultId']
    # print('GetAsyncResponse_ResultId =', GetAsyncResponse_ResultId)
    print(response)
    return response
""" -------------------------------------------------------------------------------------------- """


# GAR = GetAsyncResponse()

# AuthorizationGame()
# GetSlotInfo()
# CreditDebit()
GetAsyncResponse()





if __name__ == "__main__":
    unittest.main()
