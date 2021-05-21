# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:05:41 2021

@author: Slayd
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd
import html5lib

from bs4 import BeautifulSoup
import urllib.request

errors = []
season = []

########## CODE POUR RECUPERER NOM JOUEURS ET SALAIRES SUR FOOTMERCATO #####
my_url1 = 'https://www.footmercato.net/france/ligue-1/joueur'
#my_url1 = 'https://www.footmercato.net/france/ligue-1/buteur'

option = Options()
#option.headless = True
options=webdriver.ChromeOptions()

#chromepath = "C://Users//Slayd//Downloads//chromedriver_win32//chromedriver.exe"

chromepath = "C://Users//Slayd//Downloads//chromedriver_win32_new//chromedriver.exe"
driver = webdriver.Chrome(chromepath, options=option)
driver.maximize_window()
driver.get(my_url1)


elems = driver.find_elements_by_xpath("//a[@href]")

liste_liens_joueurs = []
resultat_joueur = []


for elem in elems:
    liens_nom_joueurs = elem.get_attribute("href")    
    #print( elem.get_attribute("href").strip('/joueur/') )
    liste_liens_joueurs.append(liens_nom_joueurs)
    
    #print(nom_joueurs)
    
#liste_liens_joueurs = liste_liens_joueurs[52:900]
#liste_liens_joueurs = liste_liens_joueurs[52:70]
liste_liens_joueurs_test = liste_liens_joueurs[52:100]
#liste_liens_joueurs = pd.DataFrame(liste_liens_joueurs, columns = ['nom_joueurs'])
#liste_liens_joueurs.to_csv('liste_joueurs_liens.csv', index=False)


for i in liste_liens_joueurs_test:
    
    try:
        my_url1 = i + ('salaire')
        #my_url1 = liste_liens_joueurs_test[3] + ('salaire')
        print(my_url1)
        option = Options()
        dict_joueurs = {}

        #opmepath = tion.headless = True
        
        #chro"C://Users//Slayd//Downloads//chromedriver_win32//chromedriver.exe"
        
        chromepath = "C://Users//Slayd//Downloads//chromedriver_win32_new//chromedriver.exe"
        driver = webdriver.Chrome(chromepath, options=option)
        driver.maximize_window()
        #driver.set_window_position(-10000,0)

        driver.get(my_url1)
        
        html_test = driver.page_source
        html = BeautifulSoup(html_test, 'html.parser' )
        
        salaire = html.find_all(class_= "salary__frequencyValue")
        
        nom_joueur_driver  =driver.find_elements_by_xpath("/html/body/div[3]/p/a[3]")
        chaine_titre_joueur = []
        
        for i in range(len(nom_joueur_driver)):
            titre  = nom_joueur_driver[i].text
            chaine_titre_joueur.append(titre)
        
        salaire_joueur = salaire[3].text.strip()
        #nom_joueurs = liste_liens_joueurs_test[3].strip('https://www.footmercato.net/joueur')
        #nom_joueurs = nom_joueurs.strip('joueur/')
        
        dict_joueurs['nom_joueurs'] = chaine_titre_joueur[0]
        dict_joueurs['salaires'] = salaire_joueur
        
        print(dict_joueurs)
        
        resultat_joueur.append(dict_joueurs)
        
        print(salaire_joueur)
        
        
        driver.quit()
        
    except:
            driver.quit()
            errors.append(i)
            continue


df = pd.DataFrame(resultat_joueur, columns = ['nom_joueurs', 'salaires'])

df.to_csv('Salaire_joueur_foot_mercato.csv', index=False)