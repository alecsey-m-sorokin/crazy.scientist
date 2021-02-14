class ErrorCodes:
    error_codes = [10, 11, 13, 49, 50, 51, 64, 100, 101, 102, 105, 108, 109, 110, 113, 114, 115, 116, 150, 151, 152,
                   200,
                   205, 206, 207, 208, 209, 210, 211, 212, 213, 214]
    error_codes_messages = ['HashMismatch', 'RoundNotFound', 'AsyncResponseNotFound', 'GambleInfoNotFound',
                            'GambleCalculationError', 'InternalServiceError', 'MySQLRequestFailed', 'MongoSaveError',
                            'CachePartnerNotFound', 'RequestToPartnerFailed', 'PartnerError', 'WrongParamError',
                            'MongoUserSessionNotFound', 'MySQLRoundCreationError', 'PartnerBlocked', 'UserBlocked',
                            'CacheGameNotFound', 'InsufficientFunds', 'DemoUserNotFound', 'DemoUserCreateError',
                            'DemoUserUpdateError', 'GameBlocked', 'SpinslotInvalidMethod', 'GameEnded',
                            'UnavailableAction', 'JackpotError', 'GameNotFound', 'WrongBetSum',
                            'WrongLogic', 'NoAvailableFreeSpins', 'UserNotFound', 'TokenError']


class DOM:
    DOMAIN_tps = 'https://testpartnerservice.carhenge.space/setup/'
    # DOMAIN = 'https://test-games-api.carhenge.space'
    DOMAIN = 'https://mg-123-games-api.carhenge.space'
    gameURL = 'https://mg-123-games-api.carhenge.space/'
    frontURL = 'https://review-global-mg-cau2g0452.carhenge.space/'
    partnerURL = 'https://mg-123-partners-api.carhenge.space/'
    AuthorizationGame_Url = '/auth/AuthorizationGame'
    GetSlotInfo_Url = '/games/GetSlotInfo'
    CreditDebit_Url = '/games/CreditDebit'
    GetAsyncResponse_Url = '/games/GetAsyncResponse'
    FreeSpin_Url = '/games/FreeSpin'


class APIdata:
    partnerID = '360'
    gameID = '10001'
    # userID = '422021'
    userID = '0'
    currency = 'EUR'
    gameKey = 'TestKey'
    betSum = '1'
    cntLineBet = '25'
    # TokenAsync = ''
    TokenAsync_2 = ''
    CardIndex = '2'
    mobile_platform = '&MobilePlatform=false'
    # query = 'gameURL=' + gameURL + '&frontURL=' + frontURL + '&partnerURL=' + partnerURL + '&partnerId' + partnerID + '&gameID' + gameID + '&userID' + userID + '&currency' + currency
