from setuptools import setup, find_packages  # or find_namespace_packages


with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    
setup(
    
    name="image_processing",
    version='0.0.1',
    author='Matheus Cruz',
    description='Um pacote de processamento de imagens',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/matheus3santos/image-processing-package.git',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
    
)