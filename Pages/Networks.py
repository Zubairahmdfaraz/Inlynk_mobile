from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class Networks:
    def __init__(self, driver):
        self.driver = driver
        self.network_icon_XPATH = '//android.widget.FrameLayout[@content-desc="Networks"]'
        self.search_icon_id = "com.peoplelink.inlink:id/menu_action_search"
        self.search_textbox_id = "com.peoplelink.inlink:id/search_src_text"
        self.connect_button_xpath = '//android.widget.Button[@resource-id="com.peoplelink.inlink:id/connect"]'
        self.click_relation_dropdown_id = "com.peoplelink.inlink:id/text_input_end_icon"
        self.assign_relationship_dropdown_XPATH = '//android.widget.TextView[@text="Assign relation Manager"]'
        self.assign_relation_manager_id = "com.peoplelink.inlink:id/searchEmployee"
        self.select_employeename = "com.peoplelink.inlink:id/relationName"
        self.check_box_id = "com.peoplelink.inlink:id/terms_conditions"
        self.connect_button_id_2 = "com.peoplelink.inlink:id/connectBtn"
        self.ok_button_id = "com.peoplelink.inlink:id/ok"
        self.back_button_xpath = '//android.widget.ImageButton[@content-desc="Collapse"]'

        #
        
        self.three_dots_icon = "com.peoplelink.inlink:id/ivDotsMenu"
        self.pending_requests_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/title" and @text="Pending requests"]'
        self.cancel_button = '(//android.widget.Button[@resource-id="com.peoplelink.inlink:id/cancelBtn"])[1]'
        self.confirm_cancel_yes_button = "com.peoplelink.inlink:id/tvYes"
        
        #
        
        self.validcompanyname_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/companyName"]'
        
        #
        
        self.no_company_exists_text = 'com.peoplelink.inlink:id/noDataContent_company'
        self.invite_company_button = 'com.peoplelink.inlink:id/invite'
        
        #
        
        self.filter_button = 'com.peoplelink.inlink:id/filter'
        self.deselect_checkbox = '(//android.widget.ImageView[@resource-id="com.peoplelink.inlink:id/checkBox"])[1]'
        self.apply_filter_button_id = 'com.peoplelink.inlink:id/apply_filter'
        self.select_relation_type_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/itemName" and @text="Distributor"]'
        self.relationship_validation = 'com.peoplelink.inlink:id/relationShip'
        
        #
        
        self.follow_filters = '//android.widget.LinearLayout[@resource-id="com.peoplelink.inlink:id/filterLayout"]/android.widget.ImageView'
        self.followers_filter = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/itemName" and @text="Followers"]'
        self.following_filter = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/itemName" and @text="Following"]'
        
        #
        
        self.follow_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/title" and @text="Follow"]'        
        self.follow_button = 'com.peoplelink.inlink:id/followBtn'

        #
        
        self.follow_list_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/title" and @text="Follow"]'
        self.following_button =  '(//android.widget.Button[@resource-id="com.peoplelink.inlink:id/followBtn"])[1]'
        self.unfollow_button_id = "com.peoplelink.inlink:id/tv_delete"

        #
        
        self.block_button = 'com.peoplelink.inlink:id/block'
        self.confirm_block_button_id = 'com.peoplelink.inlink:id/tv_delete'
        self.back_button_xpath = '//android.widget.ImageView[@resource-id="com.peoplelink.inlink:id/backButton"]'
        self.block_list_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/title" and @text="Blocklist"]'
        self.company_name = 'com.peoplelink.inlink:id/companyName'
        
        #
        
        self.block_list_xpath = '//android.widget.TextView[@resource-id="com.peoplelink.inlink:id/title" and @text="Blocklist"]'
        self.unblock_button_id = "com.peoplelink.inlink:id/unblock"
        self.confirm_unblock_button_id = "com.peoplelink.inlink:id/tv_delete"
    
    
    
    
    #company add network
    
    def click_network_icon(self):
        self.driver.find_element(AppiumBy.XPATH, self.network_icon_XPATH).click()

    def click_search_icon(self):
        self.driver.find_element(AppiumBy.ID, self.search_icon_id).click()

    def enter_search_text(self, company_name):
        self.driver.find_element(AppiumBy.ID, self.search_textbox_id).send_keys(company_name)

    def click_connect_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.connect_button_xpath).click()


    def click_relation_dropdown(self):
            self.driver.find_element(AppiumBy.ID, self.click_relation_dropdown_id).click()

    def assign_relationship_dropdown(self):
            self.driver.find_element(AppiumBy.XPATH, self.assign_relationship_dropdown_XPATH).click()
          
    def click_assign_relation_manager(self):
            self.driver.find_element(AppiumBy.ID, self.assign_relation_manager_id).click()

    def assign_relation_manager(self, relationship_name):
            self.driver.find_element(AppiumBy.ID, self.assign_relation_manager_id).send_keys(relationship_name)

            self.driver.hide_keyboard()

    def select_employee(self):
            self.driver.find_element(AppiumBy.ID, self.select_employeename).click()

    def check_box(self):
            self.driver.find_element(AppiumBy.ID, self.check_box_id).click()

    def connect_button_2(self):
            self.driver.find_element(AppiumBy.ID, self.connect_button_id_2).click()

    def ok_button(self):
            self.driver.find_element(AppiumBy.ID, self.ok_button_id).click()

    def back_button(self):
            self.driver.find_element(AppiumBy.ID, self.back_button_xpath).click()



    #cancelPending
    
    def click_three_dots_icon(self):
        self.driver.find_element(AppiumBy.ID, self.three_dots_icon).click()

    def click_pending_requests(self):
        self.driver.find_element(AppiumBy.XPATH, self.pending_requests_xpath).click()

    def click_cancel_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.cancel_button).click()

    def click_confirm_cancel_yes_button(self):
        self.driver.find_element(AppiumBy.ID, self.confirm_cancel_yes_button).click()



    #valid company name
    
    def valid_company_name(self):
        valid_companyname = self.driver.find_element(AppiumBy.XPATH, self.validcompanyname_xpath).text
        if valid_companyname == "company_name_2":
            return "Successfully Found"
        else:
              return "Not Found"
    
    
    
    #invalid company name
    
    def invalid_company_name(self):
        self.driver.hide_keyboard()
        no_company_exists_text = self.driver.find_element(AppiumBy.ID, self.no_company_exists_text).text
        invite_button = self.driver.find_element(AppiumBy.ID, self.invite_company_button).text
        if no_company_exists_text == "No companies has been found by this search result." and invite_button == "Invite Company":
            return "No company exists"
        else:
            return "Company exists"
             
             
    #filter relations 
            
    def click_filter_button(self):
        self.driver.find_element(AppiumBy.ID, self.filter_button).click()

    def click_deselect_checkbox(self):
        self.driver.find_element(AppiumBy.XPATH, self.deselect_checkbox).click()

    def select_relation_type(self):
        self.driver.find_element(AppiumBy.XPATH, self.select_relation_type_xpath).click()
    
    def apply_filter(self):
        self.driver.find_element(AppiumBy.ID, self.apply_filter_button_id).click()

    def validate_relationship(self):
        relationship_validation = self.driver.find_element(AppiumBy.ID, self.relationship_validation).text
        if relationship_validation == "Distributor":
            return "Successfully filtered"
        else:
            return "Failed to filter"
        
    #filter followers and following
    
    def follow_filters_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.follow_filters).click()
    
    def followers_filter_option(self):
        self.driver.find_element(AppiumBy.XPATH, self.followers_filter).click()
    
    def following_filter_option(self):
        self.driver.find_element(AppiumBy.XPATH, self.following_filter).click()



    #company follow
    
    def company_follow_button(self):
        follow_button_text = self.driver.find_element(AppiumBy.ID, self.follow_button).text
        self.driver.find_element(AppiumBy.ID, self.follow_button).click()
        Following_button_text = self.driver.find_element(AppiumBy.ID, self.follow_button).text
        if follow_button_text == "Follow" and Following_button_text == "Following":
            return "Successfully followed"
        else:
            return "Failed to follow"
        
    def following_list(self):
        self.driver.find_element(AppiumBy.XPATH, self.follow_xpath).click()
  
    
    #company unfollow
    
    def click_three_dots_icon(self):
        self.driver.find_element(AppiumBy.ID, self.three_dots_icon).click()
    
    def click_follow_list(self):
        self.driver.find_element(AppiumBy.XPATH, self.follow_list_xpath).click()

    def click_following_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.following_button).click()

    def click_unfollow_button(self):
        self.driver.find_element(AppiumBy.ID, self.unfollow_button_id).click()

    
    
    #company block
    
    def company_block_button(self):
        self.driver.find_element(AppiumBy.ID, self.block_button).click()
        
    def confirm_block_button(self):
        self.driver.find_element(AppiumBy.ID, self.confirm_block_button_id).click()

    def back_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.back_button_xpath).click()

    def block_list_button(self):
        self.driver.find_element(AppiumBy.XPATH, self.block_list_xpath).click()

        companyname_blocklist = self.driver.find_element(AppiumBy.ID, self.company_name).text

        if companyname_blocklist == "Company Name":
            return "Successfully blocked"
        else:
            return "Failed to block"
        
    
    
    #company unblock
    
    def block_list_button_2(self):
        self.driver.find_element(AppiumBy.XPATH, self.block_list_xpath).click()
    
    def unblock_button(self):
        self.driver.find_element(AppiumBy.ID, self.unblock_button_id).click()
    
    def confirm_unblock_button(self):
        self.driver.find_element(AppiumBy.ID, self.confirm_unblock_button_id).click()

