from setuptools import setup, find_packages

setup(name='KismetCaptureRtl433',
      version='2019.07.0',
      description='Kismet rtl_433 datasource',
      author='Mike Kershaw / Dragorn',
      author_email='dragorn@kismetwireless.net',
      url='https://www.kismetwireless.net/',
      install_requires=['protobuf'],
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'kismet_cap_sdr_rtl433 = KismetCaptureRtl433.kismet_cap_sdr_rtl433:main',
              'kismet_cap_sdr_rtl433_mqtt = KismetCaptureRtl433.kismet_cap_sdr_rtl433_mqtt:main',
              ],
          },
     )


