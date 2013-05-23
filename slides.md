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

# 我所知的 CI Services (for Python)
- [Travis CI](https://travis-ci.org/)
- [CircleCI](https://circleci.com/)
- [Codeship](https://www.codeship.io/)

---

# 還是![Jenkins](http://jenkins-ci.org/sites/default/files/jenkins_logo.png)

---

# 使用情境：<br/>開發機 ubuntu 12.04.2 LTS<br/>實際上線 CentOS 6.4

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

# 以 Celery 為例

## Celery version 3.0 runs on,

- Python (2.5, 2.6, 2.7, 3.2, 3.3)
- PyPy (1.8, 1.9)
- Jython (2.5, 2.7).

---

# Celery 與 Travis CI 

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

# tox.ini

    !ini
    # content of: tox.ini , put in same dir as setup.py
    [tox]
    envlist = py26,py27
    [testenv]
    deps=pytest       # install pytest in the venvs
    commands=py.test  # or 'nosetests' or ...

---

# 感覺跟 Travis CI 類似，但是

---

# setup.py Gotcha

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

# 你會看到

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

# 不能對 virtualenv 客製 <br> 用意：集中到 setup.py

---

# 本地 dependency_links
