#!/usr/bin/python

import os
from Foundation import CFPreferencesCopyAppValue, \
                       CFPreferencesSetAppValue

storefront_canada = "143455-6,13"
apple_id = os.environ['APPLE_USERNAME']
account_info = {
    'bagtype': 1,
    'credit': "",
    'dsid': 10231587043,
    'identifier': apple_id,
    'kind': 0,
    'signedin': False,
    'storefront': storefront_canada,
}

known_accounts = [account_info]
CFPreferencesSetAppValue('KnownAccounts', known_accounts, 'com.apple.commerce')

# We may not need to set this, and we'd probably need to create proper nested NSDictionaries first
# primary_account = {
#     0: {
#         1: account_info,
#     }
# }
#CFPreferencesSetAppValue('PrimaryAccount', primary_account, 'com.apple.commerce')

CFPreferencesSetAppValue('Storefront', storefront_canada, 'com.apple.appstore')
