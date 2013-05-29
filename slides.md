# 測試可以簡單一點嗎？

---

# Hubert (@yhchan) <br/> 趨勢科技

---

# 寫 code 很開心，but

---

# 人生最<strike>機車</strike>厲害就是這個 BUT！

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

# Python 2 -> Python 3 <br>刺激！

---

# 目前我們的狀況

---

# 開發機 ubuntu 12.04.2 LTS<br/>實際上線 CentOS 5.x + Python 2.6

---

# Python 2.6 v.s Python 2.7

---

# Syntax

## Python 2.6 / 2.7 Syntax

    !python
    # Python 2.7+ Dictionary Comprehension
    map = {'a': 1, 'b': 2}
    inv_map {v: k for k, v in map.items()}

    # Python 2.7+ with statements
    with open("out.txt","wt"), open("in.txt") as file_out, file_in:
        pass

---

# 寫 Unit Test 也會遇到...

## Python 2.6 / 2.7 Syntax

    !python
    # Python 2.7+ contains more assertions
    items1 = {'product': 'Worry-Free'}
    items2 = {'product': 'OfficeScan'}
    self.assertDictEqual(items1, items2)

---

# 跨版本的解決方案

---

# Travis CI / Codeship

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

# 無痛與 Github 整合

---

# 但是其他 Private Repo 呢...

---

# 還是![Jenkins](http://jenkins-ci.org/sites/default/files/jenkins_logo.png)

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

# 之前根本沒人管 dependency ...

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

---

# 換個主題

---

# 測試的起手式

---

# `import unittest`

---

# `assertEqual`

---

# Python 2.6 的世界有點不方便

---

# 即使是簡單比較


## Code
    !python
    def test_simple_dict_compare_1(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        dict2 = {'a': 1, 'b': 1, 'c': 3, 'd': 5}

        self.assertEqual(dict1, dict2)

## Result
    AssertionError: {'a': 1, 'c': 3, 'b': 2, 'd': 4} != 
                    {'a': 1, 'c': 3, 'b': 1, 'd': 5}
---

# Assertion 看不懂也枉然

---

# `import testfixtures`

---

# `compare`

---

# 用 `compare` 好讀多了

## Code
    !python
    def test_simple_dict_compare_2(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        dict2 = {'a': 1, 'b': 1, 'c': 3, 'd': 5}

        compare(dict1, dict2)

## Result
    AssertionError: dict not as expected:

    same:
    ['a', 'c']

    values differ:
    'b': 2 != 1
    'd': 4 != 5

---

# `compare` 遇到 JSON

## Result

    same:
    [u'completed_in', u'max_id_str', u'next_page', u'page']]

    values differ:
    u'max_id': 122078461840982020 != 122078461840982021
    u'results': [{u'created_at': u'Thu, 06 Oct 2011 19:36:17 +0000',
      u'entities': {u'urls': [{u'display_url': u'bit.ly/q9fyz9',
                               u'expanded_url': u'http://bit.ly/q9fyz9',
                               u'indices': [37, 57],
                               u'url': u'http://t.co/L9JXJ2ee'}]},
    ...
    以下三千行

---

# list 只要有一個不一樣就...

---

# Python 2.7 改善很多

## 把差異的部份特別標示出來

                     u'geo': None,
    -                u'id': 122033350327279620,
    ?                                        ^

    +                u'id': 122033350327279621,
    ?

---

# Python 2.6 你可以 <br> `pip install unittest2`

---

# `compare` 還不夠好，但是也還堪用

---

# Mocking

---

# `Replacer`

---

# 以前我們的會這樣寫

    !python
    @patch('hello.yoyo.ClassB')
    @patch('hello.yoyo.ClassA')
    def test_hello(self, MockClassA, MockClassB):
        pass

---

# 但是每 mock 一個就多一個 parameter ...

---

# 後來我們改成這樣

    !python
    def test_mock(self):
        # python 2.6, or using contextlib
        with patch('test_hello.RealClassA') as mock_a:
            with patch('test_hello.RealClassB') as mock_b:
                pass

    def test_mock_27(self):
        # python 2.7+
        with patch('test_hello.RealClassA') as mock_a, \
            with patch('test_hello.RealClassB') as mock_b:

            pass

---

# `Replacer`

    !python
    with Replacer() as r:
        r.replace('test_hello.RealClassA', MagicMock())
        r.replace('test_hello.RealClassB', MagicMock())

        instance_a = RealClassA()
        instance_b = RealClassB()

---

# xUnit with `patch`

    !python
    def setUp(self):
        self.patcher_a = patch('test_hello.RealClassA', spec=True)
        self.patcher_b = patch('test_hello.RealClassB', spec=True)

        self.mock_a = self.patcher_a.start()
        self.mock_b = self.patcher_b.start()

    def tearDown(self):
        self.patcher_a.stop()
        self.patcher_b.stop()

---

# `tearDown` 會不會漏？

---

# xUnit with `Replacer`

    !python
    def setUp(self):
        self.replacer = Replacer()

        self.mock_a = MagicMock()
        self.mock_b = MagicMock()

        self.replacer.replace('test_hello.RealClassA', self.mock_a)
        self.replacer.replace('test_hello.RealClassB', self.mock_b)

    def tearDown(self):
        self.replacer.restore()

---

# `testfixtures` 其他的好東西

---

# `TempDirectory` 超好用

---

# `ShouldRaises` <br> 2.7 之後就還好

---

# [Things to make writing tests easier by Chris Withers](Things to make writing tests easier by Chris Withers/)

---

# 時間有限，想說的很多

---

# 謝謝 ☺

---

# Q & A
