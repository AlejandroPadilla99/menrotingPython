from re import I
from tests.selenium_tests.factoryn_design_pattern import finder_element

find_the_enter_store_button = {
    'Fin the enter element',
    finder_element,
    {
        'by':'xpath',
        'key':'/html/body/div[1]/p[1]/a',
        'action':True,
        'type':'click'
    }

}

click_on_sing_in_button = {
    'Click on sing in button',
    finder_element,
    {
        'by':'xpath',
        'key':'/html/body/div[1]/div[2]/div/a[2]',
        'action':True,
        'type':'click'
    }
}

fill_the_username_textbox = {

}




login.flows.enroll(
    'Fill the username textbox', finder_element,
    {
        'by':'id',
        'key':'stripes--94156071',
        'action':True,
        'type':'send_keys',
        'value': 'Alejandro'
    }
)