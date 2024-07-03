*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${LOGIN_URL}        https://www.facebook.com/login/
${USERNAME}         User
${PASSWORD}         Password

*** Test Cases ***
Validate Facebook Login
    Open Browser    ${LOGIN_URL}    chrome
    Input Text      id=email        ${USERNAME}
    Input Text      id=pass         ${PASSWORD}
    Click Button    name=login
    Sleep    5
    Close Browser
