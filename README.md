# Affordable

An abstraction layer to facilitate RL environment developing.

Concepts
---------------

* Game
* World
* Agent
  * Affordable
    * Action
    * State
* Embedding


How to release
---------------

```bash
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*

git tag va.b.c master
git push origin va.b.c
```

