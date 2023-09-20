#!/bin/bash

pip freeze > .temp
pip uninstall -r .temp -y
rm .temp