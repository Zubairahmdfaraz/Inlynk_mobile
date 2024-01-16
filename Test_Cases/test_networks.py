import sys
import os

from Pages.LoginScreen import LoginScreen

project_root = r'f:\Inlynk_Appium'
sys.path.append(project_root)


import time

from Pages.BasePage import BasePage
from Pages.Networks import Networks


class Test_Networks(BasePage):
    company_name = "ajio"
    relationship_name = "astha"
    company_name_2 = "sowjanya test one"

 

    def test_add_network(self,appium_driver):
        self.nc = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com", "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nc.click_network_icon()
        time.sleep(2)
        self.nc.click_search_icon()
        time.sleep(2)
        self.nc.enter_search_text(self.company_name)
        time.sleep(2)
        self.nc.click_connect_button()
        time.sleep(7)
        self.nc.click_relation_dropdown()
        time.sleep(2)
        self.nc.assign_relationship_dropdown()
        time.sleep(2)
        self.nc.click_assign_relation_manager()
        time.sleep(5)
        self.nc.assign_relation_manager(self.relationship_name)
        time.sleep(5)
        self.nc.select_employee()
        time.sleep(2)
        self.nc.check_box()
        time.sleep(2)
        self.nc.connect_button_2()
        time.sleep(2)
        self.nc.ok_button()
        time.sleep(2)

        #cancelPending

    def test_cancel_pendingrequest(self, appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com" , "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_three_dots_icon()
        time.sleep(2)
        self.nt.click_pending_requests()
        time.sleep(2)
        self.nt.click_cancel_button()
        time.sleep(2)
        self.nt.click_confirm_cancel_yes_button()
        time.sleep(2)
            
     

        #valid company name
            
    def test_valid_company_name(self,appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com" , "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_search_icon()
        time.sleep(2)
        self.nt.enter_search_text(self.company_name_2)
        time.sleep(2)
        self.nt.valid_company_name()
        time.sleep(2)
        
        
        

        #invalid company name
            
    def test_invalid_company_name(self,appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com" , "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_search_icon()
        time.sleep(2)
        self.nt.enter_search_text("jiocdf")
        time.sleep(2)
        self.nt.invalid_company_name()
        time.sleep(2)


        #filter networks relations
        
    def test_filter_networks_relations(self,appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com" , "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_filter_button()
        time.sleep(2)
        self.nt.click_deselect_checkbox()
        time.sleep(2)
        self.nt.select_relation_type()
        time.sleep(2)
        self.nt.apply_filter()
        time.sleep(5)
        self.nt.validate_relationship()
        time.sleep(5)

        #filter followers/following
            
    def test_filter_followers_following(self,appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com" , "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_three_dots_icon()
        time.sleep(2)
        self.nt.following_list()
        time.sleep(2)
        self.nt.follow_filters_button()
        time.sleep(2)
        self.nt.followers_filter_option()
        time.sleep(2)
        self.nt.apply_filter()
        time.sleep(2)
          
        
        #company follow
            
    def test_company_follow(self, appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
            
        self.lp.ValidLogin("csk@yopmail.com", "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_search_icon()
        time.sleep(2)
        self.nt.enter_search_text(self.company_name)
        time.sleep(2)
        self.nt.company_follow_button()
        time.sleep(2)
   

        #company unfollow
        
    def test_unfollow(self, appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)

        self.lp.ValidLogin("csk@yopmail.com" , "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(5)
        self.nt.click_three_dots_icon()
        time.sleep(2)
        self.nt.click_follow_list()
        time.sleep(2)
        self.nt.click_following_button()
        time.sleep(2)
        self.nt.click_unfollow_button()
        time.sleep(2)
       
        
     
  
        #company block
            
    def test_company_block(self, appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
        self.lp.ValidLogin("csk@yopmail.com", "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(2)
        self.nt.click_three_dots_icon()
        time.sleep(2)
        self.nt.following_list()
        time.sleep(2)
        self.nt.company_block_button()
        time.sleep(2)
        self.nt.confirm_block_button()
        time.sleep(2)
        self.nt.back_button()
        time.sleep(2)
        self.nt.click_three_dots_icon()
        time.sleep(2)
        self.nt.block_list_button()
        time.sleep(2)        

        
        
        #company unblock
        
    def test_unblock(self, appium_driver):
        self.nt = Networks(appium_driver)
        self.lp = LoginScreen(appium_driver)
            
        self.lp.ValidLogin("csk@yopmail.com", "Inlink@123")
        self.lp.ClickLogin()
        time.sleep(2)
        self.nt.click_network_icon()
        time.sleep(5)
        self.nt.click_three_dots_icon()
        time.sleep(2)
        self.nt.block_list_button_2()
        time.sleep(2)
        self.nt.unblock_button()
        time.sleep(2)
        self.nt.confirm_unblock_button()
        time.sleep(2)



      


      




