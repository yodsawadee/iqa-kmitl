# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re









class TestCase2CreateStudyProgram(unittest.TestCase):
    def setUp(self):
        chromedriver = "./chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case2_create_study_program(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("thisispassword")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log in'])[1]/following::input[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::b[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("ENGAGIRCULBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเกษตร")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิศวกรรมศาสตรบัณฑิต (วิศวกรรมเกษตร)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1PTaKWAgUHjjjQM3gMF1SlGoI4l9hjII-")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("ITXINFORMABMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีสารสนเทศ")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิทยาศาสตรบัณฑิต (เทคโนโลยีสารสนเทศ)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1ihUcSgui0nqIp3d6Y7l6hEQzfxLxomQ7")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("AMIMANUFACBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"วิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมระบบการผลิต")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิศวกรรมศาสตรบัณฑิต (วิศวกรรมระบบการผลิต)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1-cjsWRNw7v5GtwaXtPtM7j_Ehi7_VZ8i")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("ICXENGNTECBNI")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการวิศวกรรมและเทคโนโลยี (หลักสูตรนานาชาติ)")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิทยาศาสตรบัณฑิต (การจัดการวิศวกรรมและเทคโนโลยี)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("GOING TO CLOSE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/file/d/1LEFMF3nkPO2lZd0AcNyfaETOusaQlFzI/view?usp=sharing")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("NNTNANOMATBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"วิศวกรรมศาสตรบัณฑิต สาขาวิศวกรรมวัสดุนาโน")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิศวกรรมศาสตรบัณฑิต (วิศวกรรมวัสดุนาโน)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("GOING TO CLOSE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/file/d/1uWaf1Va-AYqkvu-E8RotZfQ3VZmoN_50/view?usp=sharing")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("MSEMUSICENBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมดนตรีและสื่อประสม")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิศวกรรมศาสตรบัณฑิต (วิศวกรรมดนตรีและสื่อประสม)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("GOING TO CLOSE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/file/d/1ipKhqFQHWM9rDMhoL8dOkI3uXQ31CTmT/view?usp=sharing")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("AAILOGIMANBNI")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาการจัดการโลจิสติกส์ (หลักสูตรนานาชาติ)")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิทยาศาสตรบัณฑิต (การจัดการโลจิสติกส์)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("NOT ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/file/d/1pVak2cRqxP2VlxgiYd-NKbvcsFKNS3S2/view?usp=sharing")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("ADMBUSADMIBNI")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรบริหารธุรกิจบัณฑิต (หลักสูตรนานาชาติ)")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"บริหารธุรกิจบัณฑิต")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("NOT ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program supported by other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1KcZP_s_neMPnO0O2DnoJuFcEYH20_lrF")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("IDEAGRIEDUBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรครุศาสตร์อุตสาหกรรมบัณฑิต สาขาวิชาครุศาสตร์เกษตร")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"ครุศาสตร์อุตสาหกรรมบณฑิต (ครุศาสตร์เกษตร)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("NOT ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Collaborated program with other institutes")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=16qO10IRAI_dGCD5ey55TJ6xTgj53xbNc")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("AGTAGRICULDMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชาเกษตรศาสตร์")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"ปรัชญาดุษฎีบัณฑิต (เกษตรศาสตร์)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1FZpWTOjXpnNSHehvnTFG9-NldFVGby89")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("AGIFERMENTBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาเทคโนโลยีการหมัก")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิทยาศาสตรบัณฑิต (เทคโนโลยีการหมัก)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=13dibj_sBWOlnUQM5e0MI7EJQ7bsVTKl9")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("LBATOURHOSBNT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรศิลปศาสตรบัณฑิต สาขาวิชานวัตกรรมการท่องเที่ยวและการบริการ")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"ศิลปศาสตรบัณฑิต (นวัตกรรมการท่องเที่ยวและการบริการ)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1JDyCg0Zd-QvVw8gBEjl-YqFOh2UJtw6j")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("ARC3DBASEDBMT")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรศิลปกรรมศาสตรบัณฑิต สาขาวิชาการออกแบบสนเทศสามมิติ")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"ศิลปกรรมศาสตรบัณฑิต (การออกแบบสนเทศสามมิติ)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/file/d/189JuoD1E8r8FyMmptKybSel_n0mR2cZf/view?usp=sharing")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Export CSV'])[1]/following::button[1]").click()
        driver.find_element_by_id("id_code").click()
        driver.find_element_by_id("id_code").clear()
        driver.find_element_by_id("id_code").send_keys("SCIPETROCHBNI")
        driver.find_element_by_id("id_name").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys(u"หลักสูตรวิทยาศาสตรบัณฑิต สาขาวิชาปิโตรเคมี (หลักสูตรนานาชาติ)")
        driver.find_element_by_id("id_degree_and_major").click()
        driver.find_element_by_id("id_degree_and_major").clear()
        driver.find_element_by_id("id_degree_and_major").send_keys(u"วิทยาศาตรบัณฑิต (ปิโตรเคมี)")
        driver.find_element_by_id("id_program_status").click()
        Select(driver.find_element_by_id("id_program_status")).select_by_visible_text("ACTIVE")
        driver.find_element_by_id("id_program_status").click()
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        Select(driver.find_element_by_id("id_collaboration_with_other_institues")).select_by_visible_text("Program issued specifically by KMITL")
        driver.find_element_by_id("id_collaboration_with_other_institues").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create Study Program'])[1]/following::form[1]").click()
        driver.find_element_by_id("id_pdf_docs_link").click()
        driver.find_element_by_id("id_pdf_docs_link").clear()
        driver.find_element_by_id("id_pdf_docs_link").send_keys("https://drive.google.com/open?id=1EzjUqZU1kCE2Swt2b2eGJZcQsJgkufBK")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Responsible professors'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='admin'])[1]/following::nf[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
