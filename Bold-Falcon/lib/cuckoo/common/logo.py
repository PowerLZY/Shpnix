# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# Copyright (C) 2020-2021 PowerLZY.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.



def logo():
    """
    Bold-Falcon asciiarts.

    :return: asciiarts array.
    """
    logos = []

    logos.append("""
     ____        _     _       _____     _                 
    | __ )  ___ | | __| |     |  ___|_ _| | ___ ___  _ __  
    |  _ \ / _ \| |/ _` |_____| |_ / _` | |/ __/ _ \| '_ \ 
    | |_) | (_) | | (_| |_____|  _| (_| | | (_| (_) | | | |
    |____/ \___/|_|\__,_|     |_|  \__,_|_|\___\___/|_| |_|
    """)


    print(color(random.choice(logos), random.randrange(31, 37)))
    print
    print(" Bold-Falcon Sandbox %s" % yellow(CUCKOO_VERSION))
    print(" www.Bold-Falcon.org")
    print(" Copyright (c) 2021-2023")
    print
    sys.stdout.flush()
