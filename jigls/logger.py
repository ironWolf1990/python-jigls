# -*- coding: utf-8 -*-
# https://docs.python.org/3/library/logging.html
# https://towardsdatascience.com/the-reusable-python-logging-template-for-all-your-data-science-apps-551697c8540

import logging
import logging.config

logger = logging.config.fileConfig(fname=r"./config/log.conf")
