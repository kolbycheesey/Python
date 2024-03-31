# import system


# def setup_function():
#     system.bootstrap()  # create vanilla installation.

# def teardown_function():
#     system.reset()  # reset installation.

# def test01():
#     # <-- expects setup()
#     system.create_user('bob')
#     assert 'bob' in system.directory
#     # <-- expects teardown() even when the assertion fails.

# def test02():
#     # <-- expects setup()
#     system.create_user('jane')
#     assert 'jane' in system.directory
#     # <-- expects teardown() even when the assertion fails.
