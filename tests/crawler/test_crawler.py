import self as self

from tests.mockup.products import retunt_product_kabum
from tests.mockup.not_found import retunt_alredy_existis
from resources.product import Product


def test_product_search():
      return Product.find_product(85197)

def test_answer_get():
    prods = test_product_search()
    assert  prods['codigo'] == retunt_product_kabum()['codigo']

def test_answer_post():
    assert Product.post(self, 1010) == retunt_alredy_existis(1010)