# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:44:49 2021

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
# test  = df['nom_joueurs'] 

df = pd.read_csv('Salaire_joueur_foot_mercato.csv') 

df = df[0:5]


vrai_nom_joueur  = df['nom_joueurs'] 
vrai_salaire_joueur = df['salaires']
#test = df[ df['nom_joueurs'] == 'kylian-mb' ]

#vrai_nom_joueur  = test['nom_joueurs'] 
#vrai_salaire_joueur = test['salaires']

#####################RECUPERER STATS SUR FBREF ##########################

for iro in zip(vrai_nom_joueur, vrai_salaire_joueur):   ### Boucle a 2 arguments
    sleep(2)
    player_name = iro[0]
    salaire_actuel = iro[1]
    #player_name = 'wissam-ben-yedder'
    
    ##### PERMET DE RECUPERER TOUTE LA PAGE HTML DU SITE #######################
    my_url1 = 'https://fbref.com/en/players/8f696594/Memphis-Depay'
    #my_url1 = 'https://www.footmercato.net/france/ligue-1/buteur'
    
    option = Options()
    #option.headless = True
    options=webdriver.ChromeOptions()
        
    chromepath = "C://Users//Slayd//Downloads//chromedriver_win32_new//chromedriver.exe"
    driver = webdriver.Chrome(chromepath, options=option)
    driver.maximize_window()
    driver.set_window_position(-10000,0)
    driver.get(my_url1)
    
    ######### CLICK POUR ACCEPTER LE COOKIE POUR ACCEDER A LA PAGE #######
    elem1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[3]")))
    elem1.click() 
    sleep(3)
    
    try: 
        print('ok search')
        print(player_name)
        ########## ENTRER LE NOM DU JOUEUR SUR LA PAGE
        search_box = driver.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/input[2]')
        search_box.send_keys(player_name)
        search_box.submit()
        #stats = driver.find_element_by_xpath('//*[@id="scout_summary_AM"]/tbody')
        
    except:
        print('error search')
        print(player_name)

        driver.quit()
        errors.append(iro)
        continue
    
    try: 
        
        print(player_name) 
        ######## RECUPERE LE HTML DE LA PAGE !
        dfs = pd.read_html(driver.page_source) #Recupere tous les tableaux de la page
        stats = dfs[10] #selectionne justes le tableau 10 car c'est le tableau des stats importantes
        stats = stats[['Statistic', 'Per 90']]
        driver.quit()
        stats_off = pd.DataFrame(data=stats)
        stats_off.dropna(subset = ["Statistic"], inplace=True)
        
        stats_player = {}
        value_stats = stats_off['Per 90']
        name_colonne = stats_off['Statistic']
        
        for row in zip(value_stats, name_colonne):
            stat = row[1].replace(' ', '_').lower()
            stats_player[stat] = row[0]
        
        # pour verifier au cas ou ya une ligne manquante 
        
        stats_check = ['Non-Penalty Goals', 'npxG', 'Shots Total', 'xA', ' npxG+xA',
                       'Shot-Creating Actions', 'NaN', 'Passes Attempted', 'Pass Completion %', 'Progressive Passes',
                       'Progressive Carries', 'Dribbles Completed', 'Touches (Att Pen)', 'Progressive Passes Rec', 'NaN', 'Pressures', 'Tackles', 'Interceptions', 'Blocks','Clearances', 'Aerials won']
        
        
        for stat in stats_check:
            if stat not in value_stats.keys():
                value_stats[stat] = 0
                
                
        ####
        
        player = [player_name, salaire_actuel,  stats_player['non-penalty_goals'], stats_player['npxg'], stats_player['shots_total'], stats_player['assists'], stats_player['xa'],
                           stats_player['npxg+xa'], stats_player['shot-creating_actions'], stats_player['passes_attempted'], stats_player['pass_completion_%'],
                           stats_player['progressive_passes'], stats_player['progressive_carries'], stats_player['dribbles_completed'],stats_player['touches_(att_pen)'],
                           stats_player['progressive_passes_rec'], stats_player['pressures'], stats_player['tackles'], stats_player['interceptions'],stats_player['blocks'],
                           stats_player['clearances'], stats_player['aerials_won']]    
     
        season.append(player)
        
    except:
        print('error')
        print(player_name)

        
        try : 
            dfs = pd.read_html(driver.page_source)
            stats = dfs[9] #selectionne justes le tableau 10 
            
            stats = stats[['Statistic', 'Per 90']]
            driver.quit()
    
            stats_off = pd.DataFrame(data=stats)
            stats_off.dropna(subset = ["Statistic"], inplace=True)
            
            stats_player = {}
            
            value_stats = stats_off['Per 90']
            name_colonne = stats_off['Statistic']
            
            for row in zip(value_stats, name_colonne):
                stat = row[1].replace(' ', '_').lower()
                stats_player[stat] = row[0]
            
            # pour verifier au cas ou ya une ligne manquante 
            
            stats_check = ['Non-Penalty Goals', 'npxG', 'Shots Total', 'xA', ' npxG+xA',
                           'Shot-Creating Actions', 'NaN', 'Passes Attempted', 'Pass Completion %', 'Progressive Passes',
                           'Progressive Carries', 'Dribbles Completed', 'Touches (Att Pen)', 'Progressive Passes Rec', 'NaN', 'Pressures', 'Tackles', 'Interceptions', 'Blocks','Clearances', 'Aerials won']
            
            
            for stat in stats_check:
                if stat not in value_stats.keys():
                    value_stats[stat] = 0
              
        ####
            player = [player_name, salaire_actuel, stats_player['non-penalty_goals'], stats_player['npxg'], stats_player['shots_total'], stats_player['assists'], stats_player['xa'],
                               stats_player['npxg+xa'], stats_player['shot-creating_actions'], stats_player['passes_attempted'], stats_player['pass_completion_%'],
                               stats_player['progressive_passes'], stats_player['progressive_carries'], stats_player['dribbles_completed'],stats_player['touches_(att_pen)'],
                               stats_player['progressive_passes_rec'], stats_player['pressures'], stats_player['tackles'], stats_player['interceptions'],stats_player['blocks'],
                               stats_player['clearances'], stats_player['aerials_won']]    
         
            season.append(player)
            
        except : 
            
            try : 
                print('error 9')
                elem1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="players"]/div[1]/div[1]/strong/a')))
                elem1.click()
                sleep(3)
                dfs = pd.read_html(driver.page_source) #Recupere tous les tableaux 
    
                stats = dfs[10] #selectionne justes le tableau 10 
                
                #stats = dfs[9]
    
                
                stats = stats[['Statistic', 'Per 90']]
                driver.quit()
        
                stats_off = pd.DataFrame(data=stats)
                stats_off.dropna(subset = ["Statistic"], inplace=True)
                
                stats_player = {}
                
                value_stats = stats_off['Per 90']
                name_colonne = stats_off['Statistic']
                
                for row in zip(value_stats, name_colonne):
                    stat = row[1].replace(' ', '_').lower()
                    stats_player[stat] = row[0]
                
                # pour verifier au cas ou ya une ligne manquante 
                
                stats_check = ['Non-Penalty Goals', 'npxG', 'Shots Total', 'xA', ' npxG+xA',
                               'Shot-Creating Actions', 'NaN', 'Passes Attempted', 'Pass Completion %', 'Progressive Passes',
                               'Progressive Carries', 'Dribbles Completed', 'Touches (Att Pen)', 'Progressive Passes Rec', 'NaN', 'Pressures', 'Tackles', 'Interceptions', 'Blocks','Clearances', 'Aerials won']
                
                
                for stat in stats_check:
                    if stat not in value_stats.keys():
                        value_stats[stat] = 0
                        
                        
                ####
                
                player = [player_name, salaire_actuel, stats_player['non-penalty_goals'], stats_player['npxg'], stats_player['shots_total'], stats_player['assists'], stats_player['xa'],
                                   stats_player['npxg+xa'], stats_player['shot-creating_actions'], stats_player['passes_attempted'], stats_player['pass_completion_%'],
                                   stats_player['progressive_passes'], stats_player['progressive_carries'], stats_player['dribbles_completed'],stats_player['touches_(att_pen)'],
                                   stats_player['progressive_passes_rec'], stats_player['pressures'], stats_player['tackles'], stats_player['interceptions'],stats_player['blocks'],
                                   stats_player['clearances'], stats_player['aerials_won']]    
             
                season.append(player)
                
                
                driver.quit()
                errors.append(iro)
            except : 
                print('error final')
                sleep(3)

                dfs = pd.read_html(driver.page_source)
                #Recupere tous les tableaux 
                stats = dfs[10]
                driver.quit()
                errors.append(iro)
                continue
        
    
        #html_fbref = driver.page_source
        #html_ok = BeautifulSoup(html_fbref, 'html.parser' )
        
        #stats = driver.find_element_by_xpath('//*[@id="scout_summary_AM"]/tbody/tr[1]/td[1]')
    
############# CREATION DE LA BASE DE DONNEE DES JOUEURS ######################     

columns = ['nom_du_joueur', 'salaire', 'non-penalty_goals', 'npxg', 'shots_total', 'assists', 'xa',
                       'npxg+xa', 'shot-creating_actions', 'passes_attempted', 'pass_completion_%',
                       'progressive_passes', 'progressive_carries', 'dribbles_completed','touches_(att_pen)',
                       'progressive_passes_rec', 'pressures', 'tackles', 'interceptions','blocks',
                       'clearances', 'aerials_won']

dataset = pd.DataFrame(season, columns= columns) 
dataset.to_csv('Salaire_joueur_ligue1.csv', index=False)