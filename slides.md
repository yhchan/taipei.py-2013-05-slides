# 測試可以簡單一點嗎？

---

# Hubert (@yhchan) <br/> 趨勢科技

---

# 聽過 Travis CI / Codeship 嗎？

---

# 無痛與 Github 整合

---

# 但是其他 Private Repo 呢...

---

# Python CI Services
- [Travis CI](https://travis-ci.org/)
- [CircleCI](https://circleci.com/)
- [Codeship](https://www.codeship.io/)

---

# 還是![Jenkins](http://jenkins-ci.org/sites/default/files/jenkins_logo.png)

---

# 目前我們的狀況

---

# 開發機 ubuntu 12.04.2 LTS<br/>實際上線 CentOS 5.x + Python 2.6

---

# Python 2.6 v.s Python 2.7

---

# Syntax

    !python
    # Python 2.7+ Dictionary Comprehension
    map = {'a': 1, 'b': 2}
    inv_map {v: k for k, v in map.items()}

    # Python 2.7+ with statements
    with open("out.txt","wt"), open("in.txt") as file_out, file_in:
        pass

---

# 寫 Unit Test 也會遇到...

    !python
    # Python 2.7+ contains more assertions
    items1 = {'product': 'Worry-Free'}
    items2 = {'product': 'OfficeScan'}
    self.assertDictEqual(items1, items2)

---

# Python 2 -> Python 3 <br>刺激！

---

# Python 很多版本

---

# 還有 PyPy

---

# 以 Celery 為例

## Celery version 3.0 runs on,

- Python (2.5, 2.6, 2.7, 3.2, 3.3)
- PyPy (1.8, 1.9)
- Jython (2.5, 2.7).

---

# Celery .travis.yml

    !yaml
    language: python
    python:
        - 2.6
        - 2.7
        - 3.2
        - 3.3
    install:
        - pip install --use-mirrors tox
    script: TOXENV=py$(echo $TRAVIS_PYTHON_VERSION | tr -d .) tox -v

---

# 今天的主題 tox

---

# tox 能做什麼

## tox 是基於 virtualenv 的測試工具

- 檢測專案是否正確安裝在不同的 python 環境
- 在不同 python 環境執行單元測試

---

# tox.ini

    !ini
    [tox]
    envlist = py26,py27

    [testenv]
    deps=pytest
    commands=py.test

---

# 感覺跟 Travis CI 類似，但是

---

# setup.py gotcha

## Babel setup.py cmdclass integration

    !python
    from distutils.core import setup
    from babel.messages import frontend as babel

    setup(
        ...
        cmdclass = {'compile_catalog': babel.compile_catalog,
                    'extract_messages': babel.extract_messages,
                    'init_catalog': babel.init_catalog,
                    'update_catalog': babel.update_catalog}
    )

---

# Bang!

    GLOB sdist-make: /Users/hubert/tmp/samplepy/setup.py
    ...
    msg=packaging
    cmdargs=['/Users/hubert/py-envs/py27env/bin/python', 
             local('/Users/hubert/tmp/samplepy/setup.py'), 'sdist', 
             '--formats=zip', '--dist-dir', 
             local('/Users/hubert/tmp/samplepy/.tox/dist')]
    env=None
    Traceback (most recent call last):
      File "setup.py", line 2, in <module>
          from babel.messages import frontend as babel
          ImportError: No module named babel.messages

---

# 就算指定 deps 也沒用

---

# 不能對 virtualenv 客製

---

# 另外一個我們遇到的麻煩

---

# 緣由：Close Source

---

# 不能用 public pypi <br>加上沒有 local pypi server

---

# 之前根本沒人管 depdency ...

---

# install_requires<br>dependency_links

---

# 第一次嘗試

---

# 從 tarball 來

    !python
    from distutils.core import setup
    setup(
        ...
        dependency_links=[
            'http://github.com/celery/celery/tarball/master#egg=celery'
        ]
    )

---

# gitlab 下載 tarball 不能指定 branch

---

# setup.py 一定要在第一層

---

# 喝咖啡 ☕

---

# 第二次嘗試

---

# 從 SCM 來

    !python
    from distutils.core import setup
    setup(
        ...
        dependency_links=[
            'git+https://example.com/spamneggs/foobar.git#egg=foobar-1.2.3'
        ]
    )

---

# setup.py 一定要在第一層...

---

# [Added #subdirectory tag specify a relative subdirectory inside a repo](https://github.com/pypa/pip/pull/526)

---

# 心中下了場雪 ☃

---

# 第三次嘗試<br>git submodules + file:///

---

# git submodules + file:///


    !python
    from distutils.core import setup
    setup(
        ...
        dependency_links=[
            'file:../../../deps/foobar#foobar'
        ]
    )

---

# 裝起來了☺

---

# 但是 tox 炸了 ☹ <br>python setup.py sdist

---

# 老實說：我們的設計不良

---

# tox 還是很好用

---

# Continuous Integration

---

# 測試 + Flake8 + Coverage

    !ini
    [tox]
    envlist = py26, py27

    [testenv]
    commands = nosetests {posargs:--with-cov --cov-report=xml --with-xunit --cov package}
    flake8 --exit-zero package

    deps = nose
    nose-cov
    coverage
    mock
    flake8

    [testenv:py26]
    basepython={homedir}/.pythonbrew/pythons/Python-2.6.8/bin/python

    [testenv:py27]
    basepython={homedir}/.pythonbrew/pythons/Python-2.7.5/bin/python

---

# Jenkins Matrix Project

![Jenkins-Matrix](http://i.imgur.com/LPLHWsP.png)

---

# 我覺得不順手的地方

- deps 有修改就會重建 virtualenv，不能新增就好嗎？
- 沒有 Travis CI 的 install 區塊

---

# tox ☀
