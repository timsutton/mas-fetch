#!/bin/sh

brew install argon/mas/mas
mas signin $APPLE_USER $APPLE_PASSWORD

# El Capitan: 1018109117
mas install 1018109117
