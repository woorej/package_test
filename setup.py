from setuptools import setup, find_packages

setup(
    name='test_package',  # 패키지의 이름
    version='0.1',  # 패키지의 버전
    packages=find_packages(include=['lib', 'lib.*', 'utils', 'utils.*']),  # 포함할 패키지 및 서브 패키지
    install_requires=[],  # 패키지 설치에 필요한 외부 패키지 목록 (예: ['requests'])
    author='Your Name',  # 패키지 작성자의 이름
    author_email='your.email@example.com',  # 작성자의 이메일 주소
    description='A small description about your package',  # 패키지에 대한 간단한 설명
    long_description="hello world",  # README.md 파일에서 긴 설명을 불러옵니다.
    url='https://github.com/woorej/package_test.git',  # 패키지의 소스 코드가 호스팅되는 URL (보통 GitHub 리포지토리)
    scripts=['./bin/client.py'],
    classifiers=[
        # 패키지에 대한 분류자. 전체 리스트는 https://pypi.org/classifiers/ 에서 확인할 수 있습니다.
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # 프로젝트의 라이선스 (이 예시에서는 MIT 라이선스)
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # 프로젝트에 필요한 최소 Python 버전
)

