# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:47:47 2021

@author: Slayd
"""

class Joueurs: 
    def __init__(self, non_PenaltyGoals, npxG , shots_Total , xA, npxG_xA , passes_Attempted, 
     progressive_Passes, progressive_Carries , dribbles_Completed , touches_Att_Pen , progressive_Passes_Rec ):
        self.non_PenaltyGoals = non_PenaltyGoals
        self.npxG = npxG
        self.Shots_Total = Shots_Total
        self.xA = xA
        self.npxG_xA = npxG_xA
        self.passes_Attempted = passes_Attempted
        self.progressive_Passes = progressive_Passes
        self.progressive_Carries = progressive_Carries
        self.dribbles_Completed = dribbles_Completed
        self.touches_Att_Pen = touches_Att_Pen
        self.progressive_Passes_Rec = progressive_Passes_Rec
        
    def setNon_PenaltyGoals(self, value):
        self.non_PenaltyGoals = value
        
    def setNpxG(self, value):
        self.npxG = value
        
    def setShots_Total(self, value):
        self.shots_Total = value
        
    def setXA(self, value):
        self.xA = value
        
    def setNpxG_xA(self, value):
        self.npxG_xA = value
        
    def setPasses_Attempted(self, value):
        self.passes_Attempted = value
        
    def setProgressive_Passes(self, value):
        self.progressive_Passes = value
        
    def setProgressive_Carries(self, value):
        self.setProgressive_Carries = value
        
    def setDribbles_Completed(self, value):
        self.dribbles_Completed = value
        
    def setTouches_Att_Pen(self, value):
        self.touches_Att_Pen = value
        
    def setProgressive_Passes_Rec(self, value):
        self.progressive_Passes_Rec = value
        
    def getNon_PenaltyGoals(self):
        return self.non_PenaltyGoals
        
    def getNpxG(self):
        return self.npxG
        
    def getShots_Total(self):
        return self.shots_Total
        
    def getXA(self):
        return self.xA
        
    def getNpxG_xA(self):
        return self.npxG_xA
        
    def getPasses_Attempted(self):
        return self.passes_Attempted
        
    def getProgressive_Passes(self):
        return self.progressive_Passes
        
    def getProgressive_Carries(self):
        return self.setProgressive_Carries
        
    def getDribbles_Completed(self):
        return self.dribbles_Completed
        
    def getTouches_Att_Pen(self):
        return self.touches_Att_Pen
        
    def getProgressive_Passes_Rec(self):
        return self.progressive_Passes_Rec
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
Non_Penalty_Goals,_npxG,_Shots_Total,_xA,__npxG_xA,
Shot_Creating_Actions,_NaN,_Passes_Attempted,_Pass_Completion_%,_Progressive_Passes,
Progressive_Carries,_Dribbles_Completed,_Touches_(Att_Pen),_Progressive_Passes_Rec,_NaN,_Pressures,_Tackles,_Interceptions,_Blocks,Clearances,_Aerials_won
'''