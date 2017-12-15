#!/usr/bin/python

import os
import sys


def apply_to_prod():
    print("Copying")
    os.system("cp -r development/models/default/nlu_model/ development/models/")
    os.system("cp -r development/models/nlu_model/  app/models/")
    os.system("cp -r development/models/rasa_core_model/  app/models/")
    os.system("cp -r development/data app")


def train():
    os.system("python development/train_nlu.py")
    os.system("sleep 5")
    os.system("python development/train_dm.py")
    os.system("sleep 5")


def test():
    os.system('python development/check_dm.py')


def main(todo=None):
    if (todo == 't'):
        train()
        apply_to_prod()
    elif (todo == 'd'):
        apply_to_prod()
    elif (todo == 'tt'):
        train()
        apply_to_prod()
        test()
    elif (todo == 'test'):
        test()


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except Exception as e:
        print(
            """Usage: {} <options>\n\toptions
            -\n\t\tt\ttrain\n\t\ttt\ttrain and
            test\n\t\td\tdeploy""".format(sys.argv[0]))
