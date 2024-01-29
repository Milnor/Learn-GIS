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
* Assignments 1-3 (ungraded) - smooth sailing, but dull until the last one where you learn the fun part of adding a legend, inset map, etc. and exporting the map to a PDF.
* Assignment 4 (peer reviewed) - **California Wildfires**
    - An earlier version of the class had a different assignment called **Electoral Politics**; it has been replaced with the Wildfires assignment though they haven't caught all the bugs in the courseware:
        * The instructions mention a quiz you can use to confirm the correctness of your answers; as of Jan. 27, 2024 it has not been implemented
        * Step 3 refers to the "image below," which is missing
        * The discussion prompt after the assignment asks questions about the earlier Electoral Politics assignment
    - This assignment is less complex than assignments 1-3, but is ultimately more difficult because you don't get the step-by-step walkthrough in the instructions
    - GUI Hints
        * You can find the following Geoprocessing tools by hitting the "Geoprocessing" button under the "View" menu and then searching for them by name in the "Find Tools" search box:
            - Dissolve
            - Intersect
            - Calculate Geometry
                * **Don't** use the "Calculate" button from the attribute table if asked to use "Calculate Geometry"
            - Summary Statistics
                * This tool will create a table under "Standalone Tables" in the Contents Pane; you can "Open" it, but it has no attribute table
    - Step 2(f) is easy to mess up, but there is a great discussion in the [course forums](https://www.coursera.org/learn/gis/discussions/forums/PIke4O-YEe2SiAqrlB2yZw/threads/R1W5jLr4Ee6bbwo1s9RgVw) on this part!
    - I believe (though I'm not certain because the quiz to confirm has not been implemented) that before Step 2(i) they left out something imporant: add another new field to the `Counties` attribute table called `Area_Acres` where you use the "Calculate Geometry" tool again to calculate the total area of each county in *US Survey Acres*. Otherwise, I think you'll get meaningless units for your percentages.
    - The PDF instructions from Assignment 3 make Steps 4-6 easy; the map is different, but the procedures are the same
        * The metadata for the `Counties` and `Wildfires` layers will tell you what data sources to credit in Step 4


### GIS Data Formats, Design and Quality (2 of 4)
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
 * Tutorial Assignment 3: A Suitability Analysis
   - This gives you a **lot** of practice with the **Raster Calculator**
   - p. 7 "Esri Extensions" is now "ArcGIS Pro Extensions"
   - p. 8 `nav_dem_10m` wasn't selectable by itself; I had to select `Band_1` inside of it to continue with the directions
       * later you'll see `nav_dem_10m_Band1` in the Contents pane rather than just `nav_dem_10m`
   - p. 15 The "Processing Extent" dropdown wasn't obvious like in the screenshot; it was hidden under the "Extent of a Layer" button
