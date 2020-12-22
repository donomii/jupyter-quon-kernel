from setuptools import setup

setup(name='jupyter_quon_kernel',
      version='1.2.1',
      description='Minimalistic quon kernel for Jupyter',
      author='Jeremy Price',
      author_email='donomii@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/brendan-rius/jupyter-quon-kernel/',
      download_url='https://github.com/brendan-rius/jupyter-quon-kernel/tarball/1.2.1',
      packages=['jupyter_quon_kernel'],
      scripts=['jupyter_quon_kernel/install_quon_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'quon'],
      include_package_data=True
      )
