PyFreeBilling : open source voip wholesale billing platform
===========================================================

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/mwolff44/pyfreebilling/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/mwolff44/pyfreebilling/?branch=master) [![Documentation Status](https://readthedocs.org/projects/pyfreebilling/badge/?version=latest)](https://readthedocs.org/projects/pyfreebilling/?badge=latest)

# Table of content


* About pyfreebilling
* License
* Features
* Prerequisites
* Installation
* Contact information


# What is pyfreebilling

pyfreebilling is an open source wholesale billing platform for FreeSWITCH. 

pyfreebilling is developed under python, LUA and PostgreSQL as the database layer.


# Documentation

Please visit : [http://pyfreebilling.readthedocs.org/](http://pyfreebilling.readthedocs.org/)


# License

pyfreebilling is under GPLv3 license. You can read it in COPYING file.


# Features

There are a some features supported. Most of them are configurable via the web
interface. A few of them are:

- Customer add/modify/delete
   - IP termination
   - SIP authentication
   - Prepaid and/or postpaid
   - Realtime billing
   - Block calls on negative balance (prepaid) or balance under credit limit (postpaid)
   - Block / allow negative margin calls
   - Email alerts
   - Daily balance email to customer
   - Limit the maximum number of calls per customer and/or per gateway
   - Multiple contexts
   - Tons of media handling options
   - Powerfull ratecard engine

- Provider add/modify/delete
   - Powerful LCR engine
   - Routing based on area code
   - Routing decision based on quality, reliability, cost or load balancing (equal)
   - Limit max channels by each provider gateway

- Extensive call and financial reporting screens (TBD)

- CDR export to CSV

- Design for scalability

... and much more :)


# Prerequisites

In order to run pyfreebilling, you need the following configured, secured  and 
working Basic Operating System (Linux or BSD, but also windows).

The project uses freeswitch, PostgreSQL and Django.


# Contact Information

Name: Mathias WOLFF

Email: website contact form


Website: [http://www.pyfreebilling.com](http://www.pyfreebilling.com)


# Requirements status

Stable version
[![Requirements Status](https://requires.io/bitbucket/mwolff/pyfreebilling/requirements.png?branch=master)](https://requires.io/bitbucket/mwolff/pyfreebilling/requirements/?branch=master)

Dev version
[![Requirements Status](https://requires.io/bitbucket/mwolff/pyfreebilling/requirements.png?branch=develop)](https://requires.io/bitbucket/mwolff/pyfreebilling/requirements/?branch=develop)
