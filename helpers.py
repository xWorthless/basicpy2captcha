def get_sitekey(driver):
    return driver.find_element_by_class_name("g-recaptcha").get_attribute(
        "data-sitekey"
    )