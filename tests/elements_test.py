from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email,output_cur_addr,output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "Full Name does not match"
            assert email == output_email, "Email does not match"
            assert current_address == output_cur_addr, "Current Address does not match"
            assert permanent_address == output_per_addr, "Permanent Address does not match"
