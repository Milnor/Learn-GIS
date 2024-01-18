# Hints on the **GIS Specialization** from *UC Davis*

Here are my observations on where the directions didn't match reality due to
typos, software updates, etc. For reference, I'm working with **ArcGIS Pro v. 
3.2.1** in January 2024.

On the off chance you are looking for quiz answers or anything else to help you
cheat, you'll need to look elsewhere.

## License

The first challenge I ran into with the course was accessing the license for
ArcGIS Pro. Judging from the course forums, I wasn't the only person confused.

When you register for the GIS Specialization and request a license, you will
(probably) receive an email from a *noreply* address with the subject *License 
Request Received*. One day after that I received a follow up email from 
*notifications@arcgis.com* with the subject *An Invitation to join an ArcGIS 
Online organization, UC Davis Continuing and Professional Education*.

Here's the thing: nothing in that organizational invite suggests that it also 
contains your ArcGIS license, but it does! After emailing 
[coursera@ucdavis.edu](mailto:coursera@ucdavis.edu), the friendly folks at UC 
Davis sent me a PDF with instructions on how to activate the license.

The **TL/DR** is: use the link in the invite email to create an account; then 
navigate to `My settings` > `Licenses` and scroll down to `Download ArcGIS Pro`.
You don't actually enter a license key; that seems to all get handled on the 
back end. You just need to authenticate once when you first load ArcGIS and it 
magically knows you have a license until December 31 of whatever year you 
activated it.
 

## Assignment Issues

### Fundamentals of GIS (1 of 4)
* Assignments 1-3 (ungraded) - smooth sailing, but dull until the last one where 
you learn the fun part of adding a legend, inset map, etc. and exporting the map 
to a PDF.
* Assignment 4 (peer reviewed) - initially the assignment instructions for the 
*Electoral Politics* assignment were wrong, containing something called *Area 
Impacted by Wildfire* instead. 
    - I emailed the UC Davis folks about the problem and though they didn't
reply, three days later I noticed they had fixed it. Thanks, UC Davis! :grin:

### GIS Data Formats, Design and Quality
* Tutorial Assignment 1: Data Structure and File Geodatabase in GIS
    - There was no `Display XY Data` button; instead I had to use `Create Points 
from Table` > `XY Table to Point`
    - There was no `Long Integer` in the drop-down; just use `Long`
    - In Step 4.2 when you create a domain for the *pollutants*, ArcGIS froze 
when I hit `Save`
        * nothing I tried could fix the problem, I think a bug dating back to 
2019 related to domains was never patched correctly; see this [ESRI forum](https://community.esri.com/t5/arcgis-pro-questions/why-does-arcgis-pro-crash-when-setting-domain/td-p/553854) 
* Tutorial Assignment 2: Editing Data - this linked to an official ESRI tutorial
called [Create points on a map](https://pro.arcgis.com/en/pro-app/latest/get-started/create-points-on-a-map.htm).
    - smooth sailing and a useful skill
