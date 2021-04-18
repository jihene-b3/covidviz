  
from setuptools import setup
from covidmap import __version__ as current_version

setup(
  name='covidmap',
  version=current_version,
  description='Visualization of the Covid-19',
  url='https://github.com/jihene-b3/ProjetCovid/tree/main/covidmap',
  author='Jihène Belgaied  ; Zakaria Laabsi ; Chloé Serre-Combe ; Stephani Ujka',
  author_email='chloe.serre-combe@etu.umontpellier.fr',
  license='MIT',
  packages=['covidmap', 'covidmap.io', 'covidmap.preprocess', 'covidmap.vis'],
  zip_safe=False
)