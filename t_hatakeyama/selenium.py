# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep
import traceback
import os, sys, datetime, csv, xlrd, tkinter.messagebox

class Stest:
    def setup(self):
        self.Cdir = os.getcwd()
        print(self.Cdir)


if __name__ == "__main__":
    Action = Stest()
