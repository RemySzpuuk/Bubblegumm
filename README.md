<img align="left" src="bubblegum.gif" style="width:220px;height:220px;">

<br>

# Bubblegum
Bubblegum is a python library used to generate sitemap, reference pages, and page databases.

<br>

### Sitemap generation

The library will scan the project's directory and create a list of all the file directories.
After logging the directories it will scan a nearby config file and remove any html files 
inside there. This allows the user to remove html files if needed.

After the above the library will generate a simple html sitemap which will optermise web crawlers 
trying to read the site.

**Warning this will remove any file named "sitemap.html" in the process**

### Reference pages

A reference page is a list of html/css/js files, the file's directory, and a short description of what the file
does (provided by the user in said file). If a file is not provided with a description, space will be made so 
the user can submit their own description.

### Page database

A page database will contain information on the reference page and additional information not 
presented on the reference pagebut will be in a json format. 
This allows developers to use javascript to scan and display some pages to the user.