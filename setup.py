from setuptools import setup
from covidviz import __version__ as current_version

setup(
  name='covidviz',
  version=current_version,
  description='Visualization of the Covid-19',
  url='https://github.com/jihene-b3/ProjetCovid/tree/main/covidmap',
  author='Jihène Belgaied ; Zakaria Laabsi ; Chloé Serre-Combe ; Stephani Ujka',
  author_email='chloe.serre-combe@etu.umontpellier.fr',
  license='MIT',
  packages=['covidviz', 'covidviz.io', 'covidviz.preprocess', 'covidviz.covidmap', 
              'covidviz.icu', 'covidviz.sparse', 'covidviz.covidtime', 'covidviz.demographicfactors'],
  zip_safe=False
)
