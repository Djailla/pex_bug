I have an issue with pip-tools and PEX

Here is a dummy example

In `requirements.in` is a single package as a dependency

To have pinned requirements, I use `pip-tools` with this command :

`pip-compile requirements.in --upgrade --index-url=https://pypi.org/pypi/ --no-emit-trusted-host --no-emit-index-url -q`

The ouput is in `requirements.txt`

Then I try to build a PEX file using either

`pex .`

or

`tox -e bundle`

But both fails with :

```Failed to resolve compatible distributions:
1: pex-test==0.1 requires jaraco-functools==3.5.0 but jaraco.functools 3.5.0 was resolved
2: pex-test==0.1 requires jaraco-text==3.7.0 but jaraco.text 3.7.0 was resolved
3: pex-test==0.1 requires jaraco-context==4.1.1 but jaraco.context 4.1.1 was resolved
4: pex-test==0.1 requires jaraco-classes==3.2.1 but jaraco.classes 3.2.1 was resolved
5: pex-test==0.1 requires jaraco-collections==3.5.1 but jaraco.collections 3.5.1 was resolved
6: pex-test==0.1 requires zc-lockfile==2.0 but zc.lockfile 2.0 was resolved```

Issue being wiht `.` or `-` not matching :(
