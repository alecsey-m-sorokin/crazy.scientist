import hashlib
import time
import unittest

import pytest
import requests

from Locators.Locators import APIdata, DOM

D = DOM
A = APIdata


class API:

    @staticmethod
    def testpartnerservice():
        params = {'gameURL': D.gameURL, 'frontURL': D.frontURL, 'partnerURL': D.partnerURL, 'partnerId': A.partnerID,
                  'gameID': A.gameID, 'userID': A.userID, 'currency': A.currency}
        response = requests.get(D.DOMAIN_tps, params=params)
        assert response.status_code == 200
        regToken_crazy_scientist = response.text.split("token=")[1].split("&")[0]
        print('crazy_scientist_IframeUrl = ', response.text)
        print('crazy_scientist_regToken = ', regToken_crazy_scientist)
        return regToken_crazy_scientist

    @staticmethod
    def AuthorizationGame(RegToken):
        HASH = hashlib.md5(('AuthorizationGame/' + RegToken + A.gameKey).encode('utf-8')).hexdigest()
        params_AuthorizationGame = {'Hash': HASH, 'Token': RegToken, 'MobilePlatform': 'false'}
        response_AuthorizationGame = requests.post(D.DOMAIN + '/auth/AuthorizationGame',
                                                   params={'Hash': HASH, 'Token': RegToken,
                                                           'MobilePlatform': 'false'},
                                                   json=params_AuthorizationGame)
        response = response_AuthorizationGame.json()
        assert response_AuthorizationGame.status_code == 200
        print(response)
        return response

    @staticmethod
    def CreditDebit(RegToken):
        HASH = hashlib.md5(('CreditDebit/' + RegToken + A.betSum + A.cntLineBet + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_CreditDebit = ', HASH)
        params_CreditDebit = {'Hash': HASH, 'Token': RegToken, 'CntLineBet': A.cntLineBet,
                              'BetSum': A.betSum}
        response_CreditDebit = requests.post(D.DOMAIN + '/games/CreditDebit',
                                             params={'Hash': HASH, 'Token': RegToken, 'CntLineBet': A.cntLineBet,
                                                     'BetSum': A.betSum}, json=params_CreditDebit)
        response = response_CreditDebit.json()
        assert response_CreditDebit.status_code == 200
        print('CreditDebit_TokenAsync = ', response['TokenAsync'])
        return response

    @staticmethod
    def GetAsyncResponse(RegToken, TokenAsync):
        HASH = hashlib.md5(('GetAsyncResponse/' + TokenAsync + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_GetAsyncResponse = ', HASH)
        params_GetAsyncResponse = {'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsync}
        response_GetAsyncResponse = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsync}, json=params_GetAsyncResponse)
        response = response_GetAsyncResponse.json()
        assert response_GetAsyncResponse.status_code == 200
        print(response)
        print("ResultId =", response['ResultId'])
        print("SpinId =", response["SpinResult"]["Id"])
        return response


api = API
regToken = api.testpartnerservice()
api.AuthorizationGame(regToken)

i = 1
while i < 50:
    creditDebit = api.CreditDebit(regToken)  # ставка ! CreditDebit # resultId = tokenAsync
    tokenAsync = creditDebit["TokenAsync"]
    time.sleep(1)
    getAsyncResponse = api.GetAsyncResponse(regToken, tokenAsync)  # асинхронный ответ ! GetAsyncResponse
    print(getAsyncResponse)
    resultId = getAsyncResponse['ResultId']
    if getAsyncResponse["SpinResult"]["DiceGame"] is None:
        bonusGameId = "no bonus game"
        print("BonusGameId =", bonusGameId)
        print('i = ', i)
        i = i + 1
    else:
        print('ups ...')
