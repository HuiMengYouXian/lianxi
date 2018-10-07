#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
一摞有序的纸牌
Card 卡片
'''
import collections	#集合模块，提供了许多有用的集合类

Card=collections.namedtuple('Card',['rank','suit'])	#命名数组 构建只有少数属性没有方法的对象

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='黑桃 红桃 梅花 方片'.split()
	
    def __init__(self):
	    self._cards=[Card(rank,suit) for suit in self.suits 
		                             for rank in self.ranks]
    def __len__(self):
	    return len(self._cards)
    def __getitem__(self,position):
	    return self._cards[position]
suit_values=dict(黑桃=3,红桃=2,梅花=1,方片=0)
def spades_high(card):
	rank_value=FrenchDeck.ranks.index(card.rank)
	return rank_value*len(suit_values)+suit_values[card.suit]