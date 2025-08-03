Web Scraping Learning 
==============================

This repository documents my journey of learning web scraping using Python. It includes exercises and real-world projects, progressing from basic static page scraping to handling dynamic, JavaScript-heavy websites and automation.

Technologies & Libraries Used
-----------------------------
- Requests: For making HTTP requests to fetch web content.
- BeautifulSoup: For parsing and navigating HTML/XML content.
- Scrapy: A powerful framework for large-scale and scalable crawling.
- Selenium: For automating interactions with dynamic websites.
- Pandas: For structuring, cleaning, and analyzing scraped data.

Project Structure & Key Learnings
---------------------------------

1. BeautifulSoup/ – Static Website Scraping
   - Goal: Practice data extraction from simple HTML pages.
   - Highlights:
     • Making GET requests and parsing HTML.
     • Navigating DOM elements via tags, classes, and IDs.
     • Extracting tables, text, and links.
     • Saving output to Excel files.

2. scrapy_project/ – Advanced Scraping with Scrapy
   - Goal: Learn scalable scraping using the Scrapy framework.
   - Highlights:
     • Building and running spiders.
     • Using Items and Pipelines to clean and store data (CSV, JSON).
     • Managing settings, middlewares, and pagination.
     • Simulating login to scrape protected pages.

3. Selenium/ – Web Automation & Dynamic Scraping
   - Goal: Handle JavaScript-rendered websites using browser automation.
   - Highlights:
     • Automating browser actions like clicking, typing, and navigating.
     • Using waits to handle dynamic content loading.
     • Working with iframes, alerts, and multiple tabs.
     • Applying the Page Object Model (POM) for code organization.

4. Projects/ – End-to-End Projects
   - Goal: Combine skills into full real-world scraping applications.
   - Highlights:
     • Building full-stack scraping pipelines (scrape → clean → report).
     • Exporting data to Excel and Word formats.
     • Creating distributable `.exe` applications for easy usage.

Usage
-----
These projects are for educational purposes. Make sure to follow the terms of service and robots.txt policies of the websites you scrape.

Author
------
Rohan Prabhakar

