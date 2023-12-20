"""
stock_view.py
"""
class StockView:
    """
    StockView
    """
    def params(self, model):
        """
        params
        """
        if model.is_bullish():
            sentiment = 'Bullish'
        else:
            sentiment = 'Bearish'
        return {
            'name': model.symbol,
            'price': model.close_price,
            'sentiment': sentiment
        }

    def render(self, model):
        """
        render
        """
        params = self.params(model)
        return '{name}: ${price:0.2f} ({sentiment})'.format_map(params)
