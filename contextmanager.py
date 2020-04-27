"""

Keywords covered:
    * with

Concepts:
    * contextmanager

Resources:
    * https://docs.python.org/3/reference/compound_stmts.html#with
"""

## Beispiel - Daten aus file rauspuhlen
import os
file_name = os.getcwd() + '/workshop5_exceptions_ctxmanager/example.txt'
file = open(file_name, 'r')
for line in file:
    print(line)

same_file = open(file_name, 'r')
for line in same_file:
    print(line)
# ??????????????


# do it again, but this time..
file = open(file_name, 'r')
for line in file:
    print(line)
file.close()  # !

same_file = open(file_name, 'r')
for line in same_file:
    print(line)

# compare this to..
file_name = os.getcwd() + '/workshop5_exceptions_ctxmanager/example.txt'
with open(file_name, 'r') as f:
    for line in f:
        print(line)

with open(file_name, 'r') as f:
    for line in f:
        print(line)


from contextlib import contextmanager
@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

csv = csv_context("file.csv")
webshop = webshop_context("url")


class WebShopResource:

    def __enter__(self):
        print("entering webshop")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting webshop")


with WebShopResource() as shop:
    for item in shop.relevant_items:
        do_sth(item)


