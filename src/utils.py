import pandas as pd
import numpy as np


class Asset(object):
    def __init__(self, ticker, entry_price, quantity, entry_date,
                company_name=None, comment=None):
        self.ticker = ticker
        self.entry_price = entry_price
        self.quantity = quantity
        self.entry_date = entry_date
        self.company_name = company_name
        self.comment = comment

    def update_current_price(current_price):
        self.current_price = current_price

    def update_comment(comment):
        self.comment = comment

    def add_to_comment(comment):
        self.comment += comment

    def set_risk_profile(self, risk_profile):
        self.risk_profile = risk_profile


class Bond(Asset):
    def __init__(self, ticker, entry_price, quantity, entry_date, opening_date,
                 due_date, coupon, company_name=None, comment=None):
        super().__init__(self, ticker, entry_price, quantity, entry_date,
                         company_name, comment)
        self.risk_type = 'risk free'
        self.opening_date = opening_date
        self.due_date = due_date
        self.coupon = coupon


class Stock(Asset):
    def __init__(self, ticker, entry_price, quantity, entry_date,
                 company_name=None, comment=None)
        super().__init__(self, ticker, entry_price, quantity, entry_date,
                         company_name, comment)
        self.risk_type = 'risky'
        self.exit_price = 0.5*self.entry_price


def RiskProfile(object):
    def __init__(self, risk_degree):
        self.risk_degree = risk_degree

    def get_risk_drawdown(self):
        return 0.5 if self.risk_degree == 1 else 0.6 if self.risk_degree == 2 else 0.7

    def get_risk_part(self):
        return 0.5 if self.risk_degree == 1 else 0.6 if self.risk_degree == 2 else 0.7


def Portfolio(object):
    def __init__(self, risk_degree):
        self.assets = {}
        self.risk_profile = risk_profile

    def check_portfolio(self):
        now = pd.Timestamp.now()
        self.current_sum = np.sum([asset.current_price for asset in self.assets.values()])
        self.risk_part = np.sum([asset.current_price for asset in filter(lambda x: x.risk_type == 'risky', self.assets.values())])
        self.risk_free_part = np.sum([asset.current_price for asset in filter(lambda x: x.risk_type == 'risk free', self.assets.values())])
        for date, asset in self.assets:
            if now - data > pd.Timedelta(days=70):
                print('You may want to update this asset')

    def add_asset(self, asset):
        self.assets[asset.entry_date] = asset
