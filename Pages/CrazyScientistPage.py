import hashlib
import unittest

import pytest
import requests

from Locators.Locators import APIdata, DOM

D = DOM
A = APIdata


@pytest.fixture(scope="module")
def test_partnerservice_starter():
    params = {'gameURL': D.gameURL, 'frontURL': D.frontURL, 'partnerURL': D.partnerURL, 'partnerId': A.partnerID,
              'gameID': A.gameID, 'userID': A.userID, 'currency': A.currency}
    response_testpartnerservice = requests.get(D.DOMAIN_tps, params=params)
    assert response_testpartnerservice.status_code == 200
    print('crazy_scientist_IframeUrl = ', response_testpartnerservice.text)
    regToken_crazy_scientist = response_testpartnerservice.text.split("token=")[1].split("&")[0]
    print('crazy_scientist_regToken = ', regToken_crazy_scientist)
    return regToken_crazy_scientist


""" AuthorizationGame -------------------------------------------------------------------------- """


@pytest.mark.usefixtures('test_partnerservice_starter')
@pytest.fixture(scope="module")
def hash_AuthorizationGame():
    HASH = hashlib.md5(
        ('AuthorizationGame/' + str(test_partnerservice_starter) + A.gameKey).encode('utf-8')).hexdigest()

    print('hash_AuthorizationGame = ', HASH)
    return HASH


@pytest.mark.usefixtures('hash_AuthorizationGame', 'test_partnerservice_starter')
def AuthorizationGame():
    params_AuthorizationGame = {'Hash': str(hash_AuthorizationGame), 'Token': str(test_partnerservice_starter),
                                'MobilePlatform': 'false'}
    response_AuthorizationGame = requests.post(D.DOMAIN + '/auth/AuthorizationGame',
                                               params={'Hash': str(hash_AuthorizationGame),
                                                       'Token': str(test_partnerservice_starter),
                                                       'MobilePlatform': 'false'},
                                               json=params_AuthorizationGame)
    response = response_AuthorizationGame.json()
    assert response_AuthorizationGame.status_code == 200

    print(str(test_partnerservice_starter))

    return response


AuthorizationGame()


if __name__ == "__main__":
    unittest.main()

