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

# Python Version Gotcha

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

# Python 很多版本

---

# 以 Celery 為例

## Celery version 3.0 runs on,

- Python (2.5, 2.6, 2.7, 3.2, 3.3)
- PyPy (1.8, 1.9)
- Jython (2.5, 2.7).

