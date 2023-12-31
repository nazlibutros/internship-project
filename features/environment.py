from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context,scenario_name):
    """
    :param scenario_name: 
    :param context: Behave context
    """
    # ### CHROME ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # ### MOBILE ####
    mobile_emulation = {"deviceName": "iPhone 14 Pro Max"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=20)
    context.app = Application(context.driver)

    # service = Service(
    #     executable_path='C:\Users\rtbut\OneDrive\Desktop\internship\chromedriver.exe')
    #
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # ### FIREFOX ####
    # service = Service(executable_path='/Users/rtbut/OneDrive/Desktop/internship/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    # ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # context.driver.maximize_window()

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'ali_59vutx'
    # bs_key = '6qH4Am5Hk9nsG7qU9PCv'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # # kevincribman_n1FUEc
    # # fyKSJSXt7QN13oznAzWz
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name
    #     # 'os': 'OS X',
    #     # 'osVersion': 'Big Sur',  # Adjust to the macOS version you are using
    #     # 'browserName': 'Chrome',
    #     # 'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    ## use it with reely firefox test, maximize window not working ##
    # context.driver.set_window_size(1280, 720)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
