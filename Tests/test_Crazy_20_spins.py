import datetime
import time
import unittest

import pytest
from parameterized import parameterized
from Locators.Locators import APIdata, DOM, bets
from Pages.CrazyScientistPage import API

D = DOM
A = APIdata
api = API
regToken = api.testpartnerservice()
api.AuthorizationGame(regToken)
i = 0
# @parameterized.expand([('1', '25'), ('2', '25'), ('3', '25'), ('4', '25'), ('5', '25')])


@parameterized.expand(bets)
def test_01_crazy_20_spins(betSum, cntLineBet):
    creditDebit = api.CreditDebit(regToken, betSum, cntLineBet)  # ставка ! CreditDebit # resultId = tokenAsync
    tokenAsync = creditDebit["TokenAsync"]
    # time.sleep(1)
    getAsyncResponse = api.GetAsyncResponse(regToken, tokenAsync)  # асинхронный ответ ! GetAsyncResponse
    resultId = getAsyncResponse['ResultId']
    if getAsyncResponse["SpinResult"]["DiceGame"] is None:
        bonusGameId = "no bonus game"
        print("BonusGameId =", bonusGameId)
        print('betSum = %s , cntLineBet = %s' % (betSum, cntLineBet))
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
            elif WinType == 6:
                print('! Loose All !')
            elif WinType == 1:
                print('! Coins !')

    # print('finished after %s times' % i)


if __name__ == "__main__":
    unittest.main()
