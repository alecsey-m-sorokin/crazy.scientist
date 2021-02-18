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
    def GetSlotInfo(RegToken):
        HASH = hashlib.md5(('GetSlotInfo/' + RegToken + A.gameKey).encode('utf-8')).hexdigest()
        params_GetSlotInfo = {'Hash': HASH, 'Token': RegToken}
        response_GetSlotInfo = requests.post(D.DOMAIN + '/games/GetSlotInfo',
                                             params={'Hash': HASH, 'Token': RegToken}, json=params_GetSlotInfo)
        response = response_GetSlotInfo.json()
        assert response_GetSlotInfo.status_code == 200
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
        """
        возвращает рараметры: response
        если :
        'BonusGameId' === null, тогда 'BonusGameId' = "no bonus game" : example : ["SpinResult"]["DiceGame"] is None
        иначе :
        'BonusGameId' = jsonData.SpinResult.DiceGame.Id
        'SpinId' = jsonData.SpinResult.Id

        если :
        'ExtraFreeSpins' === null, тогда 'ExtraFreeSpins' = "no ExtraFreeSpins"
        иначе :
        'ExtraFreeSpins' = jsonData.ExtraFreeSpins
         """
        HASH = hashlib.md5(('GetAsyncResponse/' + TokenAsync + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_GetAsyncResponse = ', HASH)
        params_GetAsyncResponse = {'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsync}
        response_GetAsyncResponse = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsync}, json=params_GetAsyncResponse)
        response = response_GetAsyncResponse.json()
        assert response_GetAsyncResponse.status_code == 200
        # print(response)
        print("ResultId =", response['ResultId'])
        print("SpinId =", response["SpinResult"]["Id"])
        return response

    @staticmethod
    def DiceBonusGame(RegToken, ResultId, BonusGameId, SpinId, Info):
        HASH = hashlib.md5(('DiceBonusGame/' + RegToken + ResultId + SpinId + BonusGameId + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_DiceBonusGame = ', HASH)
        params_DiceBonusGame = {"Hash": HASH, "Token": RegToken, "ResultId": ResultId, "BonusGameId": BonusGameId, "SpinId": SpinId, "Info": Info}
        response_DiceBonusGame = requests.post(D.DOMAIN + '/bonus/DiceBonusGame', params={"Hash": HASH, "Token": RegToken, "ResultId": ResultId, "BonusGameId": BonusGameId, "SpinId": SpinId, "Info": Info}, json=params_DiceBonusGame)
        response = response_DiceBonusGame.json()
        assert response_DiceBonusGame.status_code == 200
        url = response_DiceBonusGame.url
        print('DiceBonusGame_TokenAsync = ', response['TokenAsync'])
        return response

    @staticmethod
    def GetAsyncResponse_Dice(RegToken, TokenAsyncDice):
        HASH = hashlib.md5(('GetAsyncResponse/' + TokenAsyncDice + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_GetAsyncResponseDice = ', HASH)
        params_GetAsyncResponse_DiceBonusGame = {'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsyncDice}
        response_GetAsyncResponse_DiceBonusGame = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsyncDice}, json=params_GetAsyncResponse_DiceBonusGame)
        response = response_GetAsyncResponse_DiceBonusGame.json()
        assert response_GetAsyncResponse_DiceBonusGame.status_code == 200
        # GetAsyncResponse_ResultId = response['ResultId']
        return response

    @staticmethod
    def SelectCardBonusGame(RegToken, ResultId, BonusGameId, SpinId, CardIndex, Info):
        HASH = hashlib.md5(('SelectCardBonusGame/' + RegToken + ResultId + SpinId + BonusGameId + A.CardIndex + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_SelectCardBonusGame = ', HASH)
        params_SelectCardBonusGame = {"Hash": HASH, "Token": regToken, "ResultId": ResultId, "BonusGameId": BonusGameId, "SpinId": SpinId, "CardIndex": CardIndex, "Info": Info}
        response_SelectCardBonusGame = requests.post(D.DOMAIN + '/bonus/SelectCardBonusGame', params={"Hash": HASH, "Token": regToken, "ResultId": ResultId, "BonusGameId": BonusGameId, "SpinId": SpinId, "CardIndex": CardIndex, "Info": Info}, json=params_SelectCardBonusGame)
        response = response_SelectCardBonusGame.json()
        assert response_SelectCardBonusGame.status_code == 200
        print('SelectCardBonusGame_TokenAsync = ', response['TokenAsync'])
        return response

    @staticmethod
    def GetAsyncResponse_Card(RegToken, TokenAsyncCard):
        HASH = hashlib.md5(('GetAsyncResponse/' + TokenAsyncCard + A.gameKey).encode('utf-8')).hexdigest()
        print('hash_GetAsyncResponseCard = ', HASH)
        params_GetAsyncResponse_SelectCardBonusGame = {'Hash': HASH, 'Token': RegToken, 'TokenAsync': TokenAsyncCard}
        response_GetAsyncResponse_DiceBonusGame = requests.post(D.DOMAIN + '/games/GetAsyncResponse', params={'Hash': HASH, 'Token': regToken, 'TokenAsync': TokenAsyncCard}, json=params_GetAsyncResponse_SelectCardBonusGame)
        response = response_GetAsyncResponse_DiceBonusGame.json()
        assert response_GetAsyncResponse_DiceBonusGame.status_code == 200
        return response


api = API
regToken = api.testpartnerservice()
api.AuthorizationGame(regToken)

# tokenAsync = api.CreditDebit(regToken)['TokenAsync']  # ставка ! CreditDebit # resultId = tokenAsync
# time.sleep(1)
# resultId = api.GetAsyncResponse(regToken, tokenAsync)['ResultId']


i = 1
while i < 50:
    while True:
        creditDebit = api.CreditDebit(regToken)  # ставка ! CreditDebit # resultId = tokenAsync
        tokenAsync = creditDebit["TokenAsync"]
        time.sleep(1)
        getAsyncResponse = api.GetAsyncResponse(regToken, tokenAsync)  # асинхронный ответ ! GetAsyncResponse
        resultId = getAsyncResponse['ResultId']
        if getAsyncResponse["SpinResult"]["DiceGame"] is None:
            bonusGameId = "no bonus game"
            print("BonusGameId =", bonusGameId)
            print('i = ', i)
            i = i + 1
            continue
        else:
            bonusGameId = getAsyncResponse["SpinResult"]["DiceGame"]["Id"]
            print('\n', "BonusGameId =", bonusGameId, '\n')
            info = 'true'
            spinId = getAsyncResponse["SpinResult"]["Id"]
            diceBonusGame = api.DiceBonusGame(regToken, resultId, bonusGameId, spinId, info)  # кидаем кубик в бонусной игре ! DiceBonusGame
            tokenAsyncDice = diceBonusGame['TokenAsync']
            time.sleep(1)
            getAsyncResponse_Dice = api.GetAsyncResponse_Dice(regToken, tokenAsyncDice)  # асинхронный ответ в бонусной игре ! GetAsyncResponse
            ThrowsLeft = getAsyncResponse_Dice["ThrowsLeft"]
            info = 'false'
            print("ThrowsLeft =", ThrowsLeft)
            while ThrowsLeft > 0:
                diceBonusGame = api.DiceBonusGame(regToken, resultId, bonusGameId, spinId, info)  # кидаем кубик в бонусной игре ! DiceBonusGame
                tokenAsyncDice = diceBonusGame['TokenAsync']
                time.sleep(1)
                getAsyncResponse_Dice = api.GetAsyncResponse_Dice(regToken, tokenAsyncDice)  # асинхронный ответ в бонусной игре ! GetAsyncResponse
                ThrowsLeft = getAsyncResponse_Dice["ThrowsLeft"]
                print("ThrowsLeft =", ThrowsLeft)
                WinType = getAsyncResponse_Dice["SelectedSector"]["WinType"]
                print("WinType =", WinType)
                if WinType == 7:
                    print('! BONUS CARD GAME !')
                    selectCardBonusGame = api.SelectCardBonusGame(regToken, resultId, bonusGameId, spinId, A.CardIndex, info)  # # кидаем кубик в бонусной карточной игре ! SelectCardBonusGame
                    tokenAsyncCard = selectCardBonusGame["TokenAsync"]
                    time.sleep(1)
                    getAsyncResponse_Card = api.GetAsyncResponse_Card(regToken, tokenAsyncCard)  # асинхронный ответ в бонусной карточной игре ! GetAsyncResponse

                    # break
            break


if __name__ == "__main__":
    unittest.main()
