{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c66df279",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from tqdm import tqdm\n",
    "import time\n",
    "from cachetools import cached, TTLCache\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import numpy as np\n",
    "import datetime as d\n",
    "import selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "74e5a994",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d56fccd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium.webdriver.common.by import By"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "233c9358",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium.webdriver.chrome.service import Service"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "17dfd1de",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support import expected_conditions as EC"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2ba22bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#! pip install chromedriver-autoinstaller"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "99076649",
   "metadata": {},
   "outputs": [],
   "source": [
    "import chromedriver_autoinstaller\n",
    "url = 'https://fr.finance.yahoo.com/'\n",
    "chromedriver_autoinstaller.install()\n",
    "#time.sleep(sleep_time)\n",
    "\n",
    "driver = webdriver.Chrome()\n",
    "\n",
    "# Go to the url page\n",
    "driver.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "51ed6f99",
   "metadata": {},
   "outputs": [
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"xpath\",\"selector\":\"//button[contains(., 'Refuser tout')]\"}\n  (Session info: chrome=107.0.5304.87)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/hy/h5g28d5n337g2cdklvz34njr0000gn/T/ipykernel_73170/1031809778.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Click on button using text on the button\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"//button[contains(., 'Refuser tout')]\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m    974\u001b[0m                 \u001b[0mby\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCSS_SELECTOR\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    975\u001b[0m                 \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'[name=\"%s\"]'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 976\u001b[0;31m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0m\u001b[1;32m    977\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    978\u001b[0m             'value': value})['value']\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"xpath\",\"selector\":\"//button[contains(., 'Refuser tout')]\"}\n  (Session info: chrome=107.0.5304.87)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Click on button using text on the button\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Refuser tout')]\").click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f75752fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Click on button using text on the button\n",
    "input=driver.find_element(By.XPATH, \"//input[contains(@placeholder, 'Rechercher des actualités, des symboles ou des entreprises')]\")\n",
    "input.clear()\n",
    "input.send_keys(\"RNO.PA\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a7960be5",
   "metadata": {},
   "outputs": [
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"[id=\"search-buttons\"]\"}\n  (Session info: chrome=107.0.5304.87)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/hy/h5g28d5n337g2cdklvz34njr0000gn/T/ipykernel_73170/3167692942.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mID\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"search-buttons\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m    974\u001b[0m                 \u001b[0mby\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCSS_SELECTOR\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    975\u001b[0m                 \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'[name=\"%s\"]'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 976\u001b[0;31m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0m\u001b[1;32m    977\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    978\u001b[0m             'value': value})['value']\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"[id=\"search-buttons\"]\"}\n  (Session info: chrome=107.0.5304.87)\n"
     ]
    }
   ],
   "source": [
    "driver.find_element(By.ID,\"search-buttons\").click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c7d2e0d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Downloading: 100%|█████████████████| 8.41M/8.41M [00:04<00:00, 1.90MB/s]\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "__init__() got an unexpected keyword argument 'service'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/hy/h5g28d5n337g2cdklvz34njr0000gn/T/ipykernel_73170/4146855982.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mchrome_options\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd_argument\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"--window-size=1024,768\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;31m# Setup the driver\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m \u001b[0mdriver\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mService\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mChromeDriverManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptions\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mchrome_options\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0;31m# Go to the url page\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: __init__() got an unexpected keyword argument 'service'"
     ]
    }
   ],
   "source": [
    "url = 'https://fr.finance.yahoo.com/'\n",
    "\n",
    "# Define options\n",
    "chrome_options = Options()\n",
    "# Change webdriver shape\n",
    "chrome_options.add_argument(\"--window-size=1024,768\")\n",
    "# Setup the driver\n",
    "driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)\n",
    "# Go to the url page\n",
    "driver.get(url)\n",
    "\n",
    "# Click on button using text on the button\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Refuser tout')]\").click()\n",
    "\n",
    "# Click on span using text on the span\n",
    "driver.find_element(By.XPATH, \"//span[contains(., 'Suivant')]\").click()\n",
    "\n",
    "# Click on li using text on the li\n",
    "driver.find_element(By.XPATH, \"//li[contains(., 'Ajouter Région')]\").click()\n",
    "\n",
    "# Click on label using text on the label\n",
    "driver.find_element(By.XPATH, \"//label[contains(., '%s')]\" % country).click()\n",
    "\n",
    "# Click on button containing 'fermer' on the title\n",
    "driver.find_element(By.XPATH, \"//button[contains(@title, 'Fermer')]\").click()\n",
    "\n",
    "# Find search bar using input tag and placeholder text\n",
    "search_bar = driver.find_element(By.XPATH,\n",
    "                                         \"\"\"//input[contains(@placeholder, 'Filtres de recherche')]\"\"\")\n",
    "\n",
    "#clearing the search bar \n",
    "search_bar.clear()\n",
    "\n",
    "# Send a new text\n",
    "search_bar.send_keys('Rendement de l’action')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "0ecb82fa",
   "metadata": {},
   "outputs": [
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"xpath\",\"selector\":\"//li[contains(., 'Ajouter Région')]\"}\n  (Session info: chrome=104.0.5112.101)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/hy/h5g28d5n337g2cdklvz34njr0000gn/T/ipykernel_48428/3140840269.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;31m# Click on li using text on the li\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"//li[contains(., 'Ajouter Région')]\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m \u001b[0mcountry\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"France\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m \u001b[0;31m# Click on label using text on the label\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m    974\u001b[0m                 \u001b[0mby\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCSS_SELECTOR\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    975\u001b[0m                 \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'[name=\"%s\"]'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 976\u001b[0;31m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0m\u001b[1;32m    977\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    978\u001b[0m             'value': value})['value']\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"xpath\",\"selector\":\"//li[contains(., 'Ajouter Région')]\"}\n  (Session info: chrome=104.0.5112.101)\n"
     ]
    }
   ],
   "source": [
    "url = 'https://fr.finance.yahoo.com/'\n",
    "\n",
    "# Define options\n",
    "chrome_options = Options()\n",
    "# Change webdriver shape\n",
    "chrome_options.add_argument(\"--window-size=1024,768\")\n",
    "# Setup the driver\n",
    "\n",
    "#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)\n",
    "\n",
    "driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)\n",
    "# Go to the url page\n",
    "driver.get(url)\n",
    "\n",
    "# Click on button using text on the button\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Refuser tout')]\").click()\n",
    "\n",
    "# Click on span using text on the span\n",
    "#driver.find_element(By.XPATH, \"//span[contains(., 'Suivant')]\").click()\n",
    "driver.find_element(By.XPATH, \"//body[contains(., 'Mon Portefeuille')]\").click()\n",
    "\n",
    "# Click on li using text on the li\n",
    "driver.find_element(By.XPATH, \"//li[contains(., 'Ajouter Région')]\").click()\n",
    "country=\"France\"\n",
    "# Click on label using text on the label\n",
    "driver.find_element(By.XPATH, \"//label[contains(., '%s')]\" % country).click()\n",
    "\n",
    "# Click on button containing 'fermer' on the title\n",
    "driver.find_element(By.XPATH, \"//button[contains(@title, 'Fermer')]\").click()\n",
    "\n",
    "# Find search bar using input tag and placeholder text\n",
    "search_bar = driver.find_element(By.XPATH,\n",
    "                                         \"\"\"//input[contains(@placeholder, 'Filtres de recherche')]\"\"\")\n",
    "\n",
    "#clearing the search bar \n",
    "search_bar.clear()\n",
    "\n",
    "# Send a new text\n",
    "search_bar.send_keys('Rendement de l’action')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "88036793",
   "metadata": {},
   "outputs": [
    {
     "ename": "NoSuchWindowException",
     "evalue": "Message: no such window: window was already closed\n  (Session info: chrome=104.0.5112.101)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNoSuchWindowException\u001b[0m                     Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/hy/h5g28d5n337g2cdklvz34njr0000gn/T/ipykernel_48428/1509262999.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute_script\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"arguments[0].click();\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mWebDriverWait\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m20\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muntil\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mEC\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0melement_to_be_clickable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"//label[@for='documentType-0']\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/support/wait.py\u001b[0m in \u001b[0;36muntil\u001b[0;34m(self, method, message)\u001b[0m\n\u001b[1;32m     69\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     70\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 71\u001b[0;31m                 \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_driver\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     72\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     73\u001b[0m                     \u001b[0;32mreturn\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/support/expected_conditions.py\u001b[0m in \u001b[0;36m__call__\u001b[0;34m(self, driver)\u001b[0m\n\u001b[1;32m    295\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    296\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__call__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 297\u001b[0;31m         \u001b[0melement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvisibility_of_element_located\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlocator\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    298\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0melement\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0melement\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_enabled\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    299\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0melement\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/support/expected_conditions.py\u001b[0m in \u001b[0;36m__call__\u001b[0;34m(self, driver)\u001b[0m\n\u001b[1;32m    126\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__call__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    127\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 128\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0m_element_if_visible\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_find_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlocator\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    129\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mStaleElementReferenceException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    130\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0;32mFalse\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/support/expected_conditions.py\u001b[0m in \u001b[0;36m_find_element\u001b[0;34m(driver, by)\u001b[0m\n\u001b[1;32m    413\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    414\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mWebDriverException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 415\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    416\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    417\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/support/expected_conditions.py\u001b[0m in \u001b[0;36m_find_element\u001b[0;34m(driver, by)\u001b[0m\n\u001b[1;32m    409\u001b[0m     if thrown.\"\"\"\n\u001b[1;32m    410\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 411\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mby\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    412\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mNoSuchElementException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    413\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m    974\u001b[0m                 \u001b[0mby\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCSS_SELECTOR\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    975\u001b[0m                 \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'[name=\"%s\"]'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 976\u001b[0;31m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0m\u001b[1;32m    977\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    978\u001b[0m             'value': value})['value']\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m~/opt/anaconda3/envs/test/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNoSuchWindowException\u001b[0m: Message: no such window: window was already closed\n  (Session info: chrome=104.0.5112.101)\n"
     ]
    }
   ],
   "source": [
    "driver.execute_script(\"arguments[0].click();\", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, \"//label[@for='documentType-0']\"))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d470c2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "Aller au contenu\n",
    "Choisir la langue\n",
    "Aller à la recherche\n",
    "Vous\n",
    "Faouzi El\n",
    "Session de mentorat\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "0\n",
    "Chat\n",
    "Faouzi El\n",
    "10:34\n",
    "! pip install chromedriver-autoinstaller\n",
    "\n",
    "\n",
    "from selenium import webdriver\n",
    "import chromedriver_autoinstaller\n",
    "from selenium.webdriver.common.by import By\n",
    "from getpass import getpass\n",
    "import time\n",
    "\n",
    "workplace_password = getpass()\n",
    "sleep_time = 5\n",
    "\n",
    "\n",
    "chromedriver_autoinstaller.install()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "driver = webdriver.Chrome()\n",
    "driver.get(\"https://openclassrooms.workplace.com/work/landing/input/?force_password=1\")\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Accept All')]\").click()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "\n",
    "input = driver.find_element(By.XPATH, \"//input[contains(@placeholder, 'Your business email')]\")\n",
    "time.sleep(sleep_time)\n",
    "input.clear()\n",
    "time.sleep(sleep_time)\n",
    "input.send_keys('elmbarkif@gmail.com')\n",
    "time.sleep(sleep_time)\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Continue')]\").click()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "input = driver.find_element(By.ID, \"jsc_c_0\")\n",
    "time.sleep(sleep_time)\n",
    "input.clear()\n",
    "time.sleep(sleep_time)\n",
    "input.send_keys(workplace_password)\n",
    "time.sleep(sleep_time)\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Continue')]\").click()\n",
    "time.sleep(sleep_time)\n",
    "driver.get('https://openclassrooms.workplace.com/groups/108172763225648')\n",
    "\n",
    "\n",
    "driver.close()\n",
    "Votre message\n",
    "\n",
    "Envoyer\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82036a7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "! pip install chromedriver-autoinstaller\n",
    "\n",
    "\n",
    "from selenium import webdriver\n",
    "import chromedriver_autoinstaller\n",
    "from selenium.webdriver.common.by import By\n",
    "from getpass import getpass\n",
    "import time\n",
    "\n",
    "workplace_password = getpass()\n",
    "sleep_time = 5\n",
    "\n",
    "\n",
    "chromedriver_autoinstaller.install()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "driver = webdriver.Chrome()\n",
    "driver.get(\"https://openclassrooms.workplace.com/work/landing/input/?force_password=1\")\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Accept All')]\").click()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "\n",
    "input = driver.find_element(By.XPATH, \"//input[contains(@placeholder, 'Your business email')]\")\n",
    "time.sleep(sleep_time)\n",
    "input.clear()\n",
    "time.sleep(sleep_time)\n",
    "input.send_keys('elmbarkif@gmail.com')\n",
    "time.sleep(sleep_time)\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Continue')]\").click()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "input = driver.find_element(By.ID, \"jsc_c_0\")\n",
    "time.sleep(sleep_time)\n",
    "input.clear()\n",
    "time.sleep(sleep_time)\n",
    "input.send_keys(workplace_password)\n",
    "time.sleep(sleep_time)\n",
    "driver.find_element(By.XPATH, \"//button[contains(., 'Continue')]\").click()\n",
    "time.sleep(sleep_time)\n",
    "driver.get('https://openclassrooms.workplace.com/groups/108172763225648')\n",
    "\n",
    "\n",
    "driver.close()\n",
    "Faouzi El\n",
    "10:39\n",
    "\n",
    "! pip install chromedriver-autoinstaller\n",
    "Faouzi El\n",
    "10:39\n",
    "chromedriver_autoinstaller.install()\n",
    "time.sleep(sleep_time)\n",
    "\n",
    "driver = webdriver.Chrome()\n",
    "Faouzi El\n",
    "10:41\n",
    "import chromedriver_autoinstaller"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
