import allure
from selene import browser, be, have, command
import os


def test_fill_authorization_form():
    with allure.step("Open registrations form"):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    with allure.step("Fill form"):
        browser.element("#firstName").click().type('Yana')
        browser.element("#lastName").type('Surname')
        browser.element("#userEmail").type('test@ya.com')
        browser.element("label[for='gender-radio-2']").click()
        browser.element("#userNumber").type('89771452365')
        browser.element("#dateOfBirthInput").click()

        browser.element(".react-datepicker__year-select").type('1997').click()
        browser.element('.react-datepicker__month-select').type('January').click()
        browser.element('[class="react-datepicker__day react-datepicker__day--006"]').click()

        browser.element('#subjectsInput').type('English').press_enter()
        browser.element("label[for='hobbies-checkbox-3']").click()
        browser.element('#uploadPicture')
        browser.element('#currentAddress').type('Smolnaya street')
        browser.element('#state').click()
        browser.element('//input[@id="react-select-3-input"]').type('Uttar Pradesh').press_enter()
        browser.element('//input[@id="react-select-4-input"]').type('Agra').press_enter()

    with allure.step('Submit form'):
        browser.element('#submit').should(be.clickable).click()

    with allure.step("Check form results"):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text(
            'Thanks for submitting the form'))
        browser.all('.table-responsive .table td:nth-child(2)').should(have.exact_texts(
            'Yana Surname', 'test@ya.com', 'Female', '8977145236', '06 January,1997', 'English', 'Music',
            '', 'Smolnaya street', 'Uttar Pradesh Agra'))





